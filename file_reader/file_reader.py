import file_reader.text_file_reader as tfr
import file_reader.spreadsheet_file_reader as sfr
import os

possible_paths = ["templates/", "spreadsheets/", "output/"]
func_dict = {
    'txt': tfr.read_txt_file,
    'pdf': tfr.read_pdf_file,
    'docx': tfr.read_docx_file,
    'csv': sfr.read_csv_file,
    'xlsx': sfr.read_xlsx_file
}


def read_file(file):

    selected_path = None
    for path in possible_paths:
        if os.path.exists(path + file):
            selected_path = path + file
            break

    if selected_path is None:
        return None

    extension = file.split('.')[-1]
    return func_dict[extension](selected_path)
