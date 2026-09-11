# Proyecto Autos (Alerce) — contexto inicial

Notas trasladadas desde una conversación previa (24 de agosto de 2026) para arrancar este proyecto sin perder contexto. Nace igual que [Radar Comercial](https://github.com/agenciaaimpacto-cyber/radar-comercial) y [Danny Mera Seguros](https://github.com/agenciaaimpacto-cyber/dannymeraseguros): un frente de negocio nuevo, separado intencionalmente en su propia carpeta.

**Estado: recién empieza.** Danny no tiene experiencia previa en venta de autos — la oportunidad se presentó el 24 de agosto de 2026 y quiere partir rápido (dijo textualmente "no sé nada, porque recién pasó hoy, pero quiero hacerlo y vender mucho").

**Ruta local:** `/Users/danny/negocio autos` (carpeta creada por Danny directamente fuera de `~/Documents` — ya sigue la regla aprendida en Radar Comercial de no ubicar proyectos con automatización dentro de Documentos/Escritorio/Descargas, ver nota técnica en el CLAUDE.md de Danny Mera Seguros si en algún momento se necesita algo corriendo en local vía `launchd`).

## El negocio: agente libre en consignación de autos

Danny se suma como agente libre (freelance) de una automotora en el sector de Alerce (Puerto Montt, Región de Los Lagos). No es dueño de la automotora ni tiene relación de dependencia — es un vendedor externo que capta autos y clientes, y la automotora pone el trato, la logística de venta y se queda con un porcentaje.

**Estructura de comisiones ofrecida por la automotora:**
- Venta de auto al contado: **$100.000** de comisión por auto vendido.
- Venta de auto con crédito: **$150.000** de comisión por auto vendido.
- **Consignación (el modelo con más potencial):** si Danny consigue que un dueño le entregue su auto en consignación (el dueño quiere vender con la automotora), Danny pacta un precio con ese dueño. Si el auto se termina vendiendo a un comprador por un precio mayor al pactado, la automotora se queda con el **2% del precio de venta final**, y **la diferencia entre el precio pactado con el dueño y el precio de venta final (menos ese 2%) es la ganancia de quien consiguió la consignación** — en este caso, Danny.

**Ejemplo trabajado (para tener la mecánica clara, no es un caso real de cliente):**
- Precio pactado con el dueño del auto: $5.000.000
- Precio de venta final a un comprador: $6.000.000
- Comisión de la automotora (2% de $6.000.000): $120.000
- Diferencia entre pactado y venta final: $1.000.000
- Ganancia de Danny: $1.000.000 − $120.000 = **$880.000**

**Por qué este modelo y no comprar-arreglar-vender (el modelo "Kia" que Danny ya probó una vez):**
- Consignación: $0 de capital invertido, $0 de riesgo financiero, el trabajo es 100% gestión digital (conseguir el auto + conseguir el comprador). Se pueden tener varios autos en proceso a la vez sin necesitar más capital.
- Comprar-arreglar-vender: inmoviliza capital (ej. ~$2.000.000 por auto) durante semanas, riesgo de que el arreglo salga más caro, depende de mecánico/repuestos/tiempo físico. No es el perfil de Danny (su patrón ya confirmado en otros negocios: todo lo que hace funciona desde el computador, sin capital en riesgo, escalable a otras ciudades sin depender de su presencia física).

## Plan de expansión
- **Alerce (Puerto Montt):** primer frente, con la automotora que hizo la oferta. Meta: operativo desde el jueves siguiente a esta conversación (27 de agosto de 2026).
- **Punta Arenas:** mismo modelo, replicado con el hermano de Danny. Es el paso lógico siguiente, pero **después** de que Alerce esté funcionando — no arrancar los dos frentes a la vez (más [Danny Mera Seguros](../DannyMeraSeguros) sigue activo en paralelo, con agosto 2026 recién cerrando). El orden importa: no sobrecargar el sistema.

## Número de WhatsApp
Decisión tomada en la conversación previa: usar el mismo número que ya usa para campañas (+56 9 5793 8503, el mismo que aparece en Danny Mera Seguros), pero separando las conversaciones con una etiqueta/carpeta específica en WhatsApp Business (ej. "Autos Alerce") para no mezclar leads de seguros con leads de autos en el mismo hilo. No se justifica un número nuevo hasta validar que el modelo funciona con el primer cierre real.

Razonamiento sobre por qué esto no genera bloqueo de Meta: los leads inician el contacto (por anuncio), Danny responde — es el flujo más seguro para WhatsApp Business. Lo que sí genera bloqueos es mensajería masiva no solicitada, algo que este flujo no hace.

## Sitio / landing (este proyecto)
Igual que con Seguros, la idea es que un sitio simple sea la capa de confianza para quien llega desde WhatsApp o desde un anuncio — no un catálogo de autos ni una tienda transaccional todavía, solo lo suficiente para que el lead confíe y siga la conversación.

**Decisiones tomadas para la primera versión (24 de agosto de 2026, sin más información disponible — ajustar cuando Danny tenga más detalles):**
- **Nombre/marca: confirmado como "AutoDirecto"** (26 de agosto de 2026, aplicado en el sitio el 10 de septiembre de 2026 — ver sección "Vitrina de autos" más abajo). Ya no se usa "Danny Mera Autos".
- **Automotora de Alerce:** se mantiene genérica en el sitio ("una automotora establecida en Alerce"), sin nombrarla — mismo criterio que en Seguros con los bancos/casas comerciales, para no dar detalles de un tercero sin su autorización explícita.
- **Público del sitio:** dos audiencias en una sola landing —
  1. Dueños de auto que quieren venderlo (consignación) — mensaje: gestión completa, sin costo para vender, sin las vueltas de venderlo por cuenta propia.
  2. Compradores de auto (contado o crédito).
- **No se exponen los números internos de comisión** (100k/150k/2%) en el sitio público — esa es información del negocio de Danny con la automotora, no algo que el cliente necesite ver.
- **Sin casos reales todavía** (recién parte) — la landing es de captación/validación, no de prueba social. Agregar casos reales cuando existan los primeros cierres.

## Regla de contenido importante (corregida el 26 de agosto de 2026)
Al armar la primera versión del sitio se colaron dos afirmaciones que no son precisas y que se corrigieron después de que Danny las revisara:
- **El precio no lo pone el dueño del auto unilateralmente — se negocia.** Nunca escribir "tú pones/decides el precio". Usar "conversamos el precio" o "negociamos juntos el precio".
- **El proceso no es 100% online ni "sin oficina".** El contacto y seguimiento son por WhatsApp, pero la parte final — ver o mostrar el vehículo, y cerrar la venta/compra — siempre se hace en persona, en la automotora. Nunca decir "100% por WhatsApp", "sin oficina de por medio" ni "sin que muevas un dedo". En vez de esconder este paso, se enmarca como algo positivo: la visita presencial es **por seguridad de ambas partes** (comprador y vendedor), no una molestia ni una limitación.
- **No nombrar una ciudad específica de automotora al describir el mecanismo general** (ej. evitar "el cierre se hace en la automotora en Alerce" en textos como la descripción de la fanpage de Facebook, que debe servir igual si más adelante se suma Punta Arenas u otra ciudad). Mencionar Alerce está bien cuando se habla de dónde opera Danny hoy (ej. el eyebrow del sitio, el footer), pero no al explicar la mecánica de "cómo funciona" de forma que quede atada a una sola ciudad/automotora.

Aplica el mismo espíritu que la regla ya existente en Danny Mera Seguros de no prometer algo que después no se cumple tal cual (ahí es con plazos de devolución, acá es con el precio y con el proceso 100% remoto).

## Vitrina de autos disponibles (agregada el 10 de septiembre de 2026)

Además de la landing de captación (`index.html`), el sitio tiene una página `autos.html` que muestra el inventario real de autos disponibles — portada por auto + galería de fotos al hacer clic (lightbox con miniaturas, año/km/precio/descripción y botón directo a WhatsApp mencionando el auto). Se actualiza a pedido de Danny, no automáticamente.

**Identidad visual (confirmada el 10 de septiembre de 2026):** Danny pasó un logo ya diseñado (círculo navy con anillo naranja, auto estilizado, texto "AUTO" en blanco + "DIRECTO" en naranja). Se adoptó esa paleta para todo el sitio (`index.html` y `autos.html`), reemplazando el verde azulado/dorado que se había usado por defecto al inicio:
- `--navy-dark: #04152A`, `--navy: #0B2038`, `--navy-light: #E7ECF1` (fondos oscuros / header / footer)
- `--orange: #F35501`, `--orange-deep: #C74506` (acento de marca — precios, hovers, detalles)
- El logo original está en `assets/logo-autodirecto.png`, con copias redimensionadas `assets/logo-autodirecto-120.png` (header/favicon) y `-300.png` (usos más grandes) generadas con Pillow para no servir el archivo de 1.6MB completo en el sitio.

**Filtro por ciudad (agregado el 10 de septiembre de 2026):** la vitrina tiene pestañas "Todas / Puerto Montt / Punta Arenas" (con el conteo de autos de cada una) sobre la grilla, en JS puro sin dependencias — filtra client-side, no recarga la página. Las pestañas aparecen solo si hay 2+ ciudades con autos; con una sola ciudad se ocultan solas. La ciudad de cada auto se muestra también como etiqueta en la tarjeta y en el detalle del lightbox.

**Flujo de trabajo (carpeta madre → sitio):**
- La estructura es de **dos niveles: `vehiculos/<Ciudad>/<Auto>/`** — primero una carpeta por ciudad (hoy: "Puerto Montt" y "Punta Arenas", nombres exactos para que se vean bien en los filtros), y dentro de cada ciudad, una subcarpeta por auto (nombre de la carpeta = nombre del auto tal como se muestra en el sitio) con las fotos del auto y un `datos.txt` (`precio`, `km`, `anio`, `descripcion` en formato `clave: valor`; si no hay km, se puede escribir `km: Consultar por WhatsApp` y se muestra tal cual). Instrucciones completas, incluidas en el propio proyecto para que Danny las tenga a mano, en [`vehiculos/_LEEME.txt`](vehiculos/_LEEME.txt).
- Portada: si hay una foto que empieza con "portada" en el nombre, esa se usa; si no, se usa la primera foto en orden alfabético — ojo, esto a veces elige una foto de interior en vez de una del exterior del auto (pasó con Suzuki Alto 800 y Mazda CX-3 al cargar el inventario inicial); conviene revisar visualmente después de generar y renombrar la foto correcta como "portada.jpg" si hace falta.
- Carpetas/archivos que empiezan con "." o "_" se ignoran (sirven para notas sin que aparezcan como auto), tanto a nivel de ciudad como de auto.
- **`vehiculos/` es local, no se sube al repo** (está en `.gitignore`) — igual que "Contenido Carrusel" en el proyecto de Seguros. Ahí quedan las fotos originales sin comprimir; el sitio no las usa directamente.
- Cuando Danny avisa ("actualiza la vitrina de autos" o similar), se corre `python3 scripts/generar_vitrina.py` desde la raíz del proyecto. El script:
  1. Lee todas las subcarpetas de `vehiculos/` (ignorando `.`/`_`).
  2. Por cada auto, redimensiona sus fotos a máx. 1600px y las guarda como JPG optimizado en `assets/autos/<slug-del-auto>/01.jpg, 02.jpg, ...` (la portada siempre queda como `01.jpg`).
  3. Regenera `autos.html` completo a partir de la plantilla `scripts/autos_template.html`, insertando los datos de todos los autos como JSON embebido (no hay build step para el usuario final — sigue siendo HTML estático, la "compilación" la hace este script bajo pedido).
  4. Es una reconstrucción completa cada vez: si una carpeta de auto se eliminó de `vehiculos/`, desaparece sola del sitio sin pasos adicionales.
- Después de correr el script, el flujo normal de siempre: revisar que `autos.html` y `assets/autos/` quedaron bien, `git add`, commit, push a `main` — Netlify despliega solo.
- **No es una automatización programada** (no usa `launchd` ni una rutina en la nube) — es a demanda, dentro de una sesión de Claude Code en esta carpeta, cuando Danny lo pide explícitamente. Si en algún momento se quiere automatizar la publicación (ej. que Danny solo deje fotos en Finder y el sitio se actualice solo), aplica la misma nota técnica de `launchd` + carpetas fuera de Documentos ya documentada en el CLAUDE.md de Danny Mera Seguros — pero `vehiculos/` ya vive fuera de `~/Documents` (dentro de `~/negocio autos`), así que esa parte ya está resuelta si se llega a necesitar.
- Verificado end-to-end el 10 de septiembre de 2026 con un auto de prueba (3 fotos placeholder, borrado después de confirmar): grid, portada, click para abrir galería, navegación prev/next, miniaturas, y formato de precio/km funcionan correctamente.

**Carga del inventario inicial (10 de septiembre de 2026):** Danny ya tenía una carpeta `Autodirecto/` con 12 autos organizados por ciudad (`Alerce` = Puerto Montt, `PUQ` = Punta Arenas), con fotos y — para 8 de los 12 — un flyer PNG ya diseñado (mismo estilo "disponible para entrega inmediata" que el logo) con año, motor, transmisión, km y valor. Se leyó cada flyer para extraer esos datos y se armó `vehiculos/<Ciudad>/<Auto>/` a partir de eso — quedaron **8 autos publicados**:
  - Puerto Montt: Kia Sportage 2020 LX ($16.990.000), Suzuki Alto 800 2019 ($4.500.000), Volkswagen Amarok Highline 4x4 2019 ($17.990.000).
  - Punta Arenas: Chevrolet Trax (Tracker) 2014 ($7.800.000, conversable), Hyundai Porter 2010 ($8.200.000, conversable), Mazda Axela Sport 2016 ($7.800.000, conversable), Mazda CX-3 2017 ($8.900.000), Mazda Demio 2017 ($6.900.000, conversable).
  - Nombres de carpeta corregidos respecto al original al copiar (typos o datos que el flyer contradecía): "Sanyong rexton" no se tocó porque no tenía flyer; "Chevrolet Track 2014" → "Chevrolet Trax (Tracker) 2014" (el flyer dice Trax/Tracker, no Track); "Volswagen" → "Volkswagen"; "Mazda CX3" → "Mazda CX-3 2017" (el flyer trae el año, la carpeta original no); "Kia Sportage 2010" → "Kia Sportage 2020 LX" (**el flyer dice año 2020**, no 2010 — se le creyó al flyer, que es el material que Danny mismo diseñó con los datos reales, sobre el nombre de la carpeta).
  - Ojo con los montos grandes en los flyers: el número que aparece más grande no siempre es el precio de venta — varios flyers destacan "PIE DESDE $X" (el pie mínimo para financiar), que es distinto del "VALOR $Y" (el precio total del auto). El campo `precio` de cada `datos.txt` se llenó con el VALOR, nunca con el pie.
  - **4 autos quedaron sin publicar por falta de datos** (tienen fotos en `vehiculos/` pero no `datos.txt` porque esas carpetas no traían flyer con precio/km): Ssangyong Rexton 2016 (Puerto Montt), Kia Sorento 2010, Nissan 2015 burdeo y Nissan Note gris (Punta Arenas). Quedó anotado en [`vehiculos/_LEEME.txt`](vehiculos/_LEEME.txt) — en cuanto Danny dé precio (y km si lo tiene) para alguno, se le agrega `datos.txt` y aparece en la próxima regeneración.
  - La carpeta original `Autodirecto/` (y su copia idéntica en `~/Documents/Autodirecto`, probablemente un duplicado accidental de iCloud/Finder) se dejó intacta sin tocar — ya cumplió su función como fuente de datos y fotos, y quedó agregada a `.gitignore` para que no se suba pesada al repo. Vale la pena que Danny la revise en algún momento y decida si borrar alguna de las dos copias.

## Cómo seguir
Al abrir una sesión de Claude Code en esta carpeta, este archivo da el contexto — se puede pedir directamente "seguimos con el proyecto de autos" y continuar desde acá. Si Danny confirma nombre de marca, si quiere nombrar la automotora, o si el número de WhatsApp cambia, actualizar este archivo.

Si más adelante se decide replicar el patrón técnico completo de Radar Comercial / Danny Mera Seguros (repo en GitHub, deploy automático en Netlify, posible automatización de contenido), seguir la misma guía documentada en el `CLAUDE.md` de Danny Mera Seguros, sección "Cómo se configuró Radar Comercial (guía técnica reutilizable)" — aplica igual acá.
