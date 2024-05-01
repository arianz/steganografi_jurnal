import PyPDF2

def edit_pdf_metadata(input_pdf, output_pdf, new_metadata):
    # Open the input PDF file in read-binary mode
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # Copy pages and metadata from the input PDF to the output PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Update metadata
        pdf_writer.add_metadata(new_metadata)

        # Write the updated metadata to the output PDF file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

input_pdf = 'output/input.pdf'
output_pdf = 'output/output.pdf'
new_metadata = {'/Title': 'Sejarah Digital Forensik', '/Author': 'Tejo', '/Subject': 'New Subject'}

edit_pdf_metadata(input_pdf, output_pdf, new_metadata)

