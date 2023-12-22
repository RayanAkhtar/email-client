import aspose.words as aw
import aspose.pdf as ap


output_path = "../output"


def save_formatted_file(text_to_write, filename, extension):
    if extension == 'txt':
        write_to_txt(text_to_write, filename)
    elif extension == 'pdf':
        write_to_pdf(text_to_write, filename)
    elif extension == 'docx':
        write_to_docx(text_to_write, filename)
    else:
        print(f'Unsupported file: {extension}')
        exit(-1)


def write_to_txt(text_to_write, filename):
    file = open(output_path + filename + ".txt", 'w')
    file.write(text_to_write)
    file.close()


def write_to_pdf(text_to_write, filename):
    file = ap.Document()
    page = file.pages.add()
    text = ap.text.TextFragment(text_to_write)
    page.paragraphs.add(text)
    file.save(output_path + filename + ".pdf")


def write_to_docx(text_to_write, filename):
    file = aw.Document()
    builder = aw.DocumentBuilder(file)
    builder.write(text_to_write)
    file.save(output_path + filename + ".docx")
