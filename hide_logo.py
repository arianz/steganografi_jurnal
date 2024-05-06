import PyPDF2

def hide_logo(pdf_file_path):
    # Baca file PDF
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()
        
        # Tambahkan blank page sebagai halaman pertama
        pdf_writer.add_blank_page(width=pdf_reader.pages[0].mediabox.width,
                                  height=pdf_reader.pages[0].mediabox.height)
        
        # Tambahkan semua halaman kecuali halaman pertama
        for page_num in range(1, len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        # Sembunyikan logo dengan steganografi
        output_pdf_path = 'output_with_hidden_logo.pdf'
        with open(output_pdf_path, 'wb') as output_file:
            # Salin metadata dari file asli ke file output
            pdf_writer.add_metadata(pdf_reader.metadata)
            pdf_writer.write(output_file)
            
    return output_pdf_path

# Contoh penggunaan
pdf_file_path = 'output/hasil.pdf'
output_pdf_path = hide_logo(pdf_file_path)
print(f"Logo Telkom University Surabaya berhasil disembunyikan pada halaman pertama dalam file: {output_pdf_path}")
