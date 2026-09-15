#!/usr/bin/env python3
"""
Genera index.html (el home, que incluye la vitrina de vehículos) a partir de
las carpetas en vehiculos/.

La estructura es vehiculos/<Ciudad>/<Auto>/ (dos niveles: primero la ciudad,
después una subcarpeta por auto — el nombre de esa subcarpeta es el nombre
del auto que se muestra en el sitio). Adentro de cada auto:
  - datos.txt con líneas "clave: valor" (precio, km, anio, descripcion)
  - fotos (jpg/jpeg/png/webp) — la que se llame "portada.*" es la foto de
    portada; si no hay ninguna así, se usa la primera en orden alfabético.

Carpetas que empiezan con "." o "_" se ignoran (sirven para notas/plantillas),
tanto a nivel de ciudad como de auto.

Este script hace una reconstrucción completa cada vez: borra y regenera
assets/autos/ e index.html a partir de lo que hay en vehiculos/ en este
momento. Así, si se elimina una carpeta de auto, automáticamente desaparece
del sitio — no hace falta "avisarle" al script qué cambió.

index.html se genera completo desde scripts/index_template.html (que trae
el resto del contenido del home — hero, sección de venta, footer — con un
placeholder __AUTOS_JSON__ donde se inyectan los datos). Para cambiar textos
o diseño del home fuera del catálogo de autos, edita index_template.html,
no index.html directamente (se sobreescribe en cada corrida).

Uso: python3 scripts/generar_vitrina.py
"""
import json
import re
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
VEHICULOS_DIR = ROOT / "vehiculos"
ASSETS_AUTOS_DIR = ROOT / "assets" / "autos"
TEMPLATE_PATH = ROOT / "scripts" / "index_template.html"
OUTPUT_PATH = ROOT / "index.html"

FOTO_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
MAX_DIMENSION = 1600
JPEG_QUALITY = 82

WHATSAPP_POR_CIUDAD = {
    "Puerto Montt": "56940130088",
    "Punta Arenas": "56986912463",
}
WHATSAPP_DEFAULT = "56957938503"

CAMPOS_REQUERIDOS = ["precio", "km", "anio", "descripcion"]
ALIAS_CLAVES = {
    "año": "anio",
    "anio": "anio",
    "precio": "precio",
    "km": "km",
    "kilometraje": "km",
    "descripcion": "descripcion",
    "descripción": "descripcion",
}


def slugify(nombre: str) -> str:
    s = nombre.strip().lower()
    s = (
        s.replace("á", "a").replace("é", "e").replace("í", "i")
        .replace("ó", "o").replace("ú", "u").replace("ñ", "n")
    )
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "auto"


def parsear_datos(datos_path: Path) -> dict:
    datos = {}
    for linea in datos_path.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea or ":" not in linea:
            continue
        clave, valor = linea.split(":", 1)
        clave = ALIAS_CLAVES.get(clave.strip().lower(), clave.strip().lower())
        datos[clave] = valor.strip()
    return datos


def formatear_precio(valor: str) -> str:
    digitos = re.sub(r"[^\d]", "", valor)
    if not digitos:
        return valor
    n = int(digitos)
    return "$" + f"{n:,}".replace(",", ".")


def formatear_km(valor: str) -> str:
    digitos = re.sub(r"[^\d]", "", valor)
    if not digitos:
        return valor
    n = int(digitos)
    return f"{n:,}".replace(",", ".") + " km"


def procesar_foto(origen: Path, destino: Path):
    with Image.open(origen) as img:
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")
        img.thumbnail((MAX_DIMENSION, MAX_DIMENSION), Image.LANCZOS)
        img.save(destino, "JPEG", quality=JPEG_QUALITY, optimize=True)


def procesar_auto(carpeta: Path, ciudad: str):
    nombre = carpeta.name
    datos_path = carpeta / "datos.txt"
    if not datos_path.exists():
        print(f"  [SALTADO] '{ciudad}/{nombre}': falta datos.txt")
        return None

    datos = parsear_datos(datos_path)
    faltantes = [c for c in CAMPOS_REQUERIDOS if c not in datos or not datos[c]]
    if faltantes:
        print(f"  [SALTADO] '{ciudad}/{nombre}': faltan datos {faltantes} en datos.txt")
        return None

    fotos_origen = sorted(
        [f for f in carpeta.iterdir() if f.suffix.lower() in FOTO_EXTS],
        key=lambda f: f.stem.lower(),
    )
    if not fotos_origen:
        print(f"  [SALTADO] '{ciudad}/{nombre}': no tiene fotos")
        return None

    portada_idx = next(
        (i for i, f in enumerate(fotos_origen) if f.stem.lower().startswith("portada")),
        0,
    )
    fotos_origen.insert(0, fotos_origen.pop(portada_idx))

    slug = slugify(f"{ciudad}-{nombre}")
    destino_dir = ASSETS_AUTOS_DIR / slug
    destino_dir.mkdir(parents=True, exist_ok=True)

    fotos_web = []
    for i, foto in enumerate(fotos_origen, start=1):
        destino = destino_dir / f"{i:02d}.jpg"
        try:
            procesar_foto(foto, destino)
            fotos_web.append(f"assets/autos/{slug}/{i:02d}.jpg")
        except Exception as e:
            print(f"  [AVISO] '{nombre}': no se pudo procesar foto '{foto.name}' ({e})")

    if not fotos_web:
        print(f"  [SALTADO] '{ciudad}/{nombre}': ninguna foto se pudo procesar")
        shutil.rmtree(destino_dir, ignore_errors=True)
        return None

    return {
        "slug": slug,
        "nombre": nombre,
        "ciudad": ciudad,
        "anio": datos["anio"],
        "km_raw": datos["km"],
        "km": formatear_km(datos["km"]),
        "precio_raw": datos["precio"],
        "precio": formatear_precio(datos["precio"]),
        "descripcion": datos["descripcion"],
        "whatsapp": WHATSAPP_POR_CIUDAD.get(ciudad, WHATSAPP_DEFAULT),
        "portada": fotos_web[0],
        "fotos": fotos_web,
        "orden": carpeta.stat().st_mtime,
    }


def main():
    if not VEHICULOS_DIR.exists():
        print(f"No existe la carpeta {VEHICULOS_DIR}")
        sys.exit(1)

    if ASSETS_AUTOS_DIR.exists():
        shutil.rmtree(ASSETS_AUTOS_DIR)
    ASSETS_AUTOS_DIR.mkdir(parents=True)

    ciudades = sorted(
        [
            d for d in VEHICULOS_DIR.iterdir()
            if d.is_dir() and not d.name.startswith((".", "_"))
        ]
    )

    carpetas = [
        (ciudad.name, carpeta)
        for ciudad in ciudades
        for carpeta in sorted(ciudad.iterdir())
        if carpeta.is_dir() and not carpeta.name.startswith((".", "_"))
    ]

    print(f"Revisando {len(carpetas)} carpeta(s) de auto en {len(ciudades)} ciudad(es)...")
    autos = []
    for ciudad_nombre, carpeta in carpetas:
        auto = procesar_auto(carpeta, ciudad_nombre)
        if auto:
            autos.append(auto)
            print(f"  [OK] '{ciudad_nombre}/{auto['nombre']}' — {len(auto['fotos'])} foto(s)")

    autos.sort(key=lambda a: a["orden"], reverse=True)
    for auto in autos:
        del auto["orden"]

    if not TEMPLATE_PATH.exists():
        print(f"Falta la plantilla {TEMPLATE_PATH}")
        sys.exit(1)

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    autos_json = json.dumps(autos, ensure_ascii=False, indent=2)
    salida = template.replace("__AUTOS_JSON__", autos_json)
    OUTPUT_PATH.write_text(salida, encoding="utf-8")

    print(f"\nListo: {len(autos)} auto(s) publicado(s) en {OUTPUT_PATH.name}")


if __name__ == "__main__":
    main()
