import file_reader.text_file_reader as tfr
import file_reader.spreadsheet_file_reader as sfr
import os

possible_paths = ["templates/", "spreadsheets/", "output/"]


def read_file(file):

    selected_path = None
    for path in possible_paths:
        if os.path.exists(path + file):
            selected_path = path + file
            break

    if selected_path is None:
        return None

    extension = file.split('.')[-1]
    if extension == 'txt':
        return tfr.read_txt_file(selected_path)
    elif extension == 'pdf':
        return tfr.read_pdf_file(selected_path)
    elif extension == 'docx':
        return tfr.read_docx_file(selected_path)
    elif extension == 'csv':
        return sfr.read_csv_file(selected_path)
    elif extension == 'xlsx':
        return sfr.read_xlsx_file(selected_path)
    else:
        print("Invalid file extension")
