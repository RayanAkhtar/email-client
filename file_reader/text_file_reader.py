import PyPDF2
import docx


#   TODO:
#       txt file reading
#       pdf file reading
#       docx file reading


def read_txt_file(file):
    file = open(file, 'r')
    text = file.readlines()
    file.close()
    return text


def read_pdf_file(file):
    txt_to_return = ""
    file = PyPDF2.PdfReader(file)
    num_pages = file.getNumPages()
    for i in range(num_pages):
        txt_to_return += file.getPage(i).extractText()
    return txt_to_return


def read_docx_file(file):
    doc = docx.Document(file)
    txt_tp_return = ""
    for para in doc.paragraphs:
        txt_tp_return += para.text
    return txt_tp_return

