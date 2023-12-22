

def save_formatted_file(text_to_write, filename, extension, output_path="../output"):
    if extension == 'txt':
        write_to_txt(text_to_write, filename, output_path)
    elif extension == 'pdf':
        write_to_pdf(text_to_write, filename, output_path)
    elif extension == 'docx':
        write_to_docx(text_to_write, filename, output_path)
    else:
        print(f'Unsupported file: {extension}')
        exit(-1)


def write_to_txt(text_to_write, filename, output_path):
    file = open(output_path + filename + ".txt", 'w')
    file.write(text_to_write)
    file.close()


def write_to_pdf(text_to_write, filename, output_path):
    pass


def write_to_docx(text_to_write, filename, output_path):
    pass
