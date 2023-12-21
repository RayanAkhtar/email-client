import PyPDF2
import docx


def read_txt_file(file):
    file = open(file, 'r')
    text = file.readlines()
    file.close()
    return "".join(text)


def read_pdf_file(file):
    txt_to_return = ""
    file = PyPDF2.PdfReader(file)
    num_pages = len(file.pages)
    for i in range(num_pages):
        txt_to_return += file.pages[i].extract_text()
    return txt_to_return


def read_docx_file(file):
    doc = docx.Document(file)
    txt_tp_return = ""
    for para in doc.paragraphs:

        # To be an exact replica of a .docx file, we must do this
        if para.text == "":
            txt_tp_return += " \n"
        else:
            txt_tp_return += para.text + "  " + "\n"

    return txt_tp_return

