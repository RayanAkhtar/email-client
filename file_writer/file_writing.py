import os
from docx2pdf import convert
from docx import Document


def save_formatted_file(text_to_write, filename, extension, output_path="output/"):
    # Writes text to a txt/pdf/docx file
    write_dict = {
        'txt': write_to_txt,
        'pdf': write_to_pdf,
        'docx': write_to_docx
    }

    write_dict[extension](text_to_write, filename, output_path)


def write_to_txt(text_to_write, filename, output_path):
    # Writes text to a text file and saves it in output_path/name
    file = open(output_path + filename + ".txt", 'w')
    file.write(text_to_write)
    file.close()


def write_to_pdf(text_to_write, filename, output_path):
    # Writes text to a pdf file and saves it
    docx_path = write_to_docx(text_to_write, filename, output_path)
    convert(docx_path, output_path + filename + ".pdf")
    os.remove(docx_path)


def write_to_docx(text_to_write, filename, output_path):
    # Writes test to a docx file and saves it
    doc = Document()
    doc.add_paragraph(text_to_write)
    docx_path = output_path + filename + ".docx"
    doc.save(docx_path)
    return docx_path
