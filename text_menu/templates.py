import text_menu.io as io
import file_reader.file_reader as fr
import text_formatter.text_formatting as tf
import file_writer.file_writing as fw


def menu():

    print("Would you like to use a single template only")
    choice = io.get_yes_or_no()

    spreadsheet = fr.read_file(get_spreadsheet_choice())

    if choice:  # Single file
        template = fr.read_file(get_template_choice())
    else:  # Multi file
        template_column = get_column_name(spreadsheet, "Please enter the name of the template file header")

    name_column = get_column_name(spreadsheet, "Enter the column name for the file name: ")
    extension = io.get_extension("Please enter the file extension: ")

    if choice:
        create_templates(template, spreadsheet, name_column, extension)
    else :
        create_multiple_templates(template_column, spreadsheet, name_column, extension)


def get_template_choice():
    files = io.list_files("templates")
    file = io.get_option_from_list(files)  # In this case, file should be the path
    return file


def get_spreadsheet_choice():
    files = io.list_files("spreadsheets")
    file = io.get_option_from_list(files)
    return file


def get_column_name(spreadsheet, message):
    print(message)
    column_name = io.get_option_from_list(spreadsheet.headers)
    return column_name


def create_templates(template, spreadsheet, name_column, extension):
    for row in spreadsheet.records:
        formatter = tf.TextFormatter(template, row)
        formatter.format_text()
        fw.save_formatted_file(formatter.output_text, row[name_column], extension) # todo: needs implementing


def create_multiple_templates(template_column, spreadsheet, name_column, extension):

    loaded_templates = {}
    for row in spreadsheet.records:
        if row[template_column] not in loaded_templates.keys():
            loaded_templates[template_column] = fr.read_file(row[template_column])

        formatter = tf.TextFormatter(loaded_templates[template_column], row)
        formatter.format_text()
        fw.save_formatted_file(formatter.output_text, row[name_column], extension)


