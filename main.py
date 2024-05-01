import PyPDF2
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io


def create_blank_page(page_size=letter):
    # Membuat PDF baru dengan satu halaman kosong
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=page_size)
    
    # Menggambar kotak putih untuk menutupi seluruh halaman
    can.setFillColorRGB(1, 1, 1)  # Warna putih
    can.rect(0, 0, page_size[0], page_size[1], fill=1, stroke=0)
    
    can.showPage()
    can.save()

    packet.seek(0)  # Kembali ke awal data
    new_pdf = PyPDF2.PdfReader(packet)
    
    return new_pdf.pages[0]

"""
def edit_pdf_with_blank_first_page(input_pdf, output_pdf, new_metadata):
    # Membaca PDF asli
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # Buat halaman kosong
        blank_page = create_blank_page()

        # Tambahkan halaman kosong di awal
        pdf_writer.add_page(blank_page)

        # Tambahkan semua halaman dari input PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Tambahkan metadata baru
        pdf_writer.add_metadata(new_metadata)

        # Tulis ke file output
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

def encode_metadata(metadata):
    # Encode metadata dengan Base64
    encoded_metadata = {}
    for key, value in metadata.items():
        encoded_str = base64.b64encode(value.encode()).decode()  # Encode base64
        # Apply simple string replacement, e.g., replacing 'O' with '='
        modified_str = encoded_str.replace("O", "=")
        encoded_metadata[key] = modified_str
    return encoded_metadata
"""

def caesar_cipher(text, shift):
    # Ubah teks berdasarkan pergeseran tertentu (Caesar cipher)
    result = []
    for char in text:
        if char.isalpha():  # Hanya ubah karakter alfabet
            # Menentukan apakah karakter besar atau kecil
            start = ord('A') if char.isupper() else ord('a')
            # Pergeseran dengan wrap-around (mod 26)
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result.append(new_char)
        else:
            result.append(char)  # Karakter non-alfabet tetap sama
    return ''.join(result)

"""
def edit_pdf_with_modifications(input_pdf, output_pdf, new_metadata):
    # Membaca PDF asli
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # Buat halaman kosong untuk akhir dokumen
        blank_page = create_blank_page()

        # Tambahkan semua halaman dari input PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Tambahkan halaman kosong di akhir
        pdf_writer.add_page(blank_page)

        # Kosongkan metadata lama dan tambahkan metadata baru yang sudah dienkode
        encoded_metadata = encode_metadata(new_metadata)

        pdf_writer.add_metadata(encoded_metadata)

        # Tulis ke file output
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)
"""
def edit_pdf_with_modifications(input_pdf, output_pdf, new_metadata):
    # Membaca PDF asli
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # Buat halaman kosong untuk akhir dokumen
        blank_page = create_blank_page()

        # Tambahkan semua halaman dari input PDF
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Tambahkan halaman kosong di akhir
        pdf_writer.add_page(blank_page)

        # Terapkan Caesar cipher dengan pergeseran 4
        encrypted_metadata = {}
        for key, value in new_metadata.items():
            encrypted_metadata[key] = caesar_cipher(value, 4)

        # Tambahkan metadata yang sudah dienkripsi
        pdf_writer.add_metadata(encrypted_metadata)

        # Tulis ke file output
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)


# Contoh penggunaan
input_pdf = 'output/output_blank_first_page.pdf'
output_pdf = 'output/output_with_blank_and_caesar_metadata.pdf'
new_metadata = {'/Title': 'Model of Business Process Improvement in Organizations Based on the Business Process Improvement Approach', 
                '/Author': 'Yoppy Mirza Maulana', 
                '/Subject': 'Business Process',
                '/Creator': 'Yoppy Mirza Maulana',
                '/Producer': 'PyPDF2',
                '/Creation Date': '',
                '/Modification Date': '',
                '/Keywords': 'business process, business process analysis and modeling, business process improvement'
                }

#edit_pdf_with_blank_first_page(input_pdf, output_pdf, new_metadata)
edit_pdf_with_modifications(input_pdf, output_pdf, new_metadata)