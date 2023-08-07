import PyPDF2
from translate import Translator
from reportlab.pdfgen import canvas

def traducir_pdf(input_path, output_path, idioma_destino):
    # Leer el contenido del PDF original
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages

        # Crear un objeto Translator para el idioma de destino
        translator = Translator(to_lang=idioma_destino)

        # Crear un nuevo PDF con el texto traducido
        c = canvas.Canvas(output_path)
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()

            # Traducir el texto de la página actual
            traduccion = translator.translate(text)

            # Agregar el texto traducido al nuevo PDF
            c.drawString(100, 100, traduccion)

            # Agregar un salto de página después de cada página traducida
            c.showPage()

        # Guardar el nuevo PDF
        c.save()

if __name__ == "__main__":
    input_path = 'pdf.pdf'
    output_path = 'libro.pdf'
    idioma_destino = 'es'

    traducir_pdf(input_path, output_path, idioma_destino)
