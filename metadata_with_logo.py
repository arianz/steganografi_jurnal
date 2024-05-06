import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def add_cover_page(input_pdf, output_pdf, new_metadata, logo_path):
    # Create a new PDF with a cover page
    with open(output_pdf, 'wb') as output_file:
        # Create a canvas
        c = canvas.Canvas(output_file, pagesize=letter)

        # Add the logo
        c.drawImage(logo_path, 0, 0, width=letter[0], height=letter[1])

        # Save the canvas as the first page
        c.showPage()
        c.save()

    # Open the original PDF and the new PDF
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # Add the cover page to the beginning of the PDF
        pdf_writer.add_page(PyPDF2.PdfReader(output_pdf).pages[0])

        # Copy pages and metadata from the input PDF to the output PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Update metadata
        pdf_writer.add_metadata(new_metadata)

        # Write the updated PDF to the output file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

input_pdf = 'output/jurnal.pdf'
output_pdf = 'output/hasil.pdf'
new_metadata = {
    '/Title': 'Model of Business Process Improvement in Organizations Based on the Business Process Improvement Approach', 
    '/Author': 'Yoppy Mirza Maulana', 
    '/Subject': 'Business Process',
    '/Creator': 'Yoppy Mirza Maulana',
    '/Producer': 'PyPDF2',
    '/Creation Date': '',
    '/Modification Date': '',
    '/Keywords': 'business process, business process analysis and modeling, business process improvement'
    }
logo_path = 'output/logo-tus.png'

add_cover_page(input_pdf, output_pdf, new_metadata, logo_path)
