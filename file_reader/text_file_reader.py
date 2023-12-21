import PyPDF2
import docx


def read_txt_file(file):
    # Reads a text file and outputs the entire contents of that file
    file = open(file, 'r')
    text = file.readlines()
    file.close()
    return "".join(text)


def read_pdf_file(file):
    # Reads the text from a pdf file and outputs it as a single string
    text = ""
    file = PyPDF2.PdfReader(file)
    num_pages = len(file.pages)
    for i in range(num_pages):
        text += file.pages[i].extract_text()
    return text


def read_docx_file(file):
    # Reads the text from a docx file and outputs it as a single string
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:

        # To be in our desired format, we must do this
        if para.text != "":
            text += para.text + " "
        text += " \n"

    return text

