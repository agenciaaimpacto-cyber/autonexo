#!/usr/bin/env python3
"""
Genera checklist-consignacion.pdf a partir del contenido fijo abajo.
Uso: python3 scripts/generar_checklist_pdf.py
"""
from pathlib import Path
from fpdf import FPDF, XPos, YPos

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "assets" / "logo-autonexo-300.png"
OUTPUT = ROOT / "checklist-consignacion.pdf"

NAVY = (4, 21, 42)
ORANGE = (243, 85, 1)
ORANGE_DEEP = (199, 69, 6)
INK = (20, 32, 46)
INK_DIM = (91, 102, 112)
LINE = (221, 227, 232)

SECTIONS = [
    ("DATOS BÁSICOS DEL AUTO", [
        "Marca, modelo y versión (ej: \"Kia Sportage LX 2.0\", no solo \"Kia Sportage\")",
        "Año",
        "Color",
        "Kilometraje actual",
        "Motor (cilindrada) y combustible (bencina, diésel, híbrido)",
        "Transmisión (manual o automática)",
        "Tracción (4x2 o 4x4, si aplica)",
    ]),
    ("ESTADO Y USO", [
        "¿Cuántos dueños ha tenido? (único dueño pesa mucho en el precio)",
        "¿Mantenciones al día? ¿Servicio de marca o mecánico particular?",
        "¿Algún detalle estético o mecánico pendiente? (mejor saberlo ahora)",
        "¿Cuántas llaves tiene?",
        "¿Todo funcionando? (aire acondicionado, alza vidrios, radio, etc.)",
    ]),
    ("DOCUMENTACIÓN  -  filtra problemas legales antes de avanzar", [
        "¿Revisión técnica y permiso de circulación al día?",
        "¿Tiene multas o deudas pendientes asociadas a la patente?",
        "¿Está con prenda, leasing o crédito vigente sobre el auto?",
        "Patente (para verificar antecedentes si hace falta)",
    ]),
    ("PRECIO", [
        "¿Cuánto espera recibir el dueño por el auto?",
        "¿Está dispuesto a conversar el precio, o es un mínimo fijo?",
    ]),
    ("FOTOS QUE NECESITAMOS PARA PUBLICAR  -  mínimo 6 a 8", [
        "Frontal 3/4 (la más importante - suele ser la portada)",
        "Trasera 3/4",
        "Lateral completo",
        "Interior (asientos delanteros y volante)",
        "Tablero (mostrando el kilometraje)",
        "Motor",
        "Cualquier detalle o daño que tenga (mejor mostrarlo que ocultarlo)",
    ]),
    ("CONTACTO DEL DUEÑO", [
        "Nombre y teléfono (para coordinar visita y cierre - no se publica)",
        "Ciudad (Puerto Montt o Punta Arenas)",
    ]),
]


class ChecklistPDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*INK_DIM)
        self.cell(0, 10, "AutoNexo - Tu próximo auto, más cerca", align="C")


def main():
    pdf = ChecklistPDF(format="A4", unit="mm")
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.add_page()
    pdf.set_margins(16, 14, 16)

    # Top navy band with logo
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, 210, 26, style="F")
    if LOGO.exists():
        pdf.image(str(LOGO), x=15, y=3, h=20)
    pdf.set_xy(38, 6)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 7, "Checklist de consignación", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_x(38)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(240, 200, 180)
    pdf.cell(0, 5.5, "Qué preguntarle al dueño antes de publicar el auto", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_y(32)

    for titulo, items in SECTIONS:
        # Section header
        pdf.set_font("Helvetica", "B", 10.5)
        pdf.set_text_color(*ORANGE_DEEP)
        pdf.cell(0, 5.5, titulo, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_draw_color(*ORANGE)
        pdf.set_line_width(0.5)
        y = pdf.get_y()
        pdf.line(16, y, 194, y)
        pdf.ln(2)

        pdf.set_font("Helvetica", "", 9.5)
        pdf.set_text_color(*INK)
        for item in items:
            x0 = pdf.get_x()
            y0 = pdf.get_y()
            # checkbox
            pdf.set_draw_color(*INK_DIM)
            pdf.rect(x0, y0 + 0.7, 3.5, 3.5)
            pdf.set_x(x0 + 6)
            pdf.multi_cell(194 - 16 - 6, 4.6, item, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2.5)

    pdf.set_font("Helvetica", "I", 9.5)
    pdf.set_text_color(*INK_DIM)
    pdf.set_draw_color(*LINE)
    y = pdf.get_y()
    pdf.line(16, y, 194, y)
    pdf.ln(3)
    pdf.multi_cell(0, 5.5, "Con todo esto completo, se arma la ficha del auto y la recomendación de precio de oferta al dueño.")

    pdf.output(str(OUTPUT))
    print(f"Listo: {OUTPUT}")


if __name__ == "__main__":
    main()
