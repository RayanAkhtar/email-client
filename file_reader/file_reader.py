import file_reader.text_file_reader as tfr
import file_reader.spreadsheet_file_reader as sfr


def read_file(file):
    extension = file.split('.')[-1]
    if extension == 'txt':
        return tfr.read_txt_file(file)
    elif extension == 'pdf':
        return tfr.read_pdf_file(file)
    elif extension == 'docx':
        return tfr.read_docx_file(file)
    elif extension == 'csv':
        return sfr.read_csv_file(file)
    elif extension == 'xlsx':
        return sfr.read_xlsx_file(file)
    else:
        print("Invalid file extension")
