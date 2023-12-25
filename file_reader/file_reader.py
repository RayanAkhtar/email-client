import file_reader.text_file_reader as tfr
import file_reader.spreadsheet_file_reader as sfr


def read_file(file):
    extension = file.split('.')[-1]
    if extension == 'txt':
        return tfr.read_txt_file("templates/" + file)
    elif extension == 'pdf':
        return tfr.read_pdf_file("templates/" + file)
    elif extension == 'docx':
        return tfr.read_docx_file("templates/" + file)
    elif extension == 'csv':
        return sfr.read_csv_file("spreadsheets/" + file)
    elif extension == 'xlsx':
        return sfr.read_xlsx_file("spreadsheets/" + file)
    else:
        print("Invalid file extension")
