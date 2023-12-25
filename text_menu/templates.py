import text_menu.user_io as io
import file_reader.file_reader as fr
import text_formatter.text_formatting as tf
import file_writer.file_writing as fw


def menu():

    print("\nWould you like to use a single template only")
    choice = io.get_yes_or_no()

    spreadsheet = fr.read_file(get_spreadsheet_choice())

    if choice:  # Single file
        template = fr.read_file(get_template_choice())
    else:  # Multi file
        template_column = get_column_name(spreadsheet, "\nPlease enter the name of the template file header")

    name_column = get_column_name(spreadsheet, "\nEnter the column name for the file name: ")
    extension = io.get_extension("\nPlease enter the file extension: ")

    if choice:
        create_templates(template, spreadsheet, name_column, extension)
    else:
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
    for i in range(len(spreadsheet.headers)):
        print(f"Header {i + 1}: {spreadsheet.headers[i]}")
    print("")
    column_name = io.get_option_from_list(spreadsheet.headers)
    return column_name


def create_templates(template, spreadsheet, name_column, extension):
    for row in spreadsheet.records:
        formatter = tf.TextFormatter(template, row)
        formatter.format_text()
        fw.save_formatted_file(formatter.output_text, row[name_column], extension, "output/")


def create_multiple_templates(template_column, spreadsheet, name_column, extension):
    all_templates = io.get_all_files_in_directory("templates/", ["txt", "pdf", "docx"])
    loaded_templates = {}
    failed_templates = []

    for row in spreadsheet.records:
        if row[template_column] not in all_templates:
            print(f"ERROR IN {row[name_column]}: {row[template_column]} not found in templates folder")
            failed_templates.append(row[name_column])
            continue

        if row[template_column] not in loaded_templates.keys():
            loaded_templates[template_column] = fr.read_file(row[template_column])

        formatter = tf.TextFormatter(loaded_templates[template_column], row)
        formatter.format_text()
        fw.save_formatted_file(formatter.output_text, row[name_column], extension)

    print("\nFinished template creation")
    if len(failed_templates) > 0:
        print("Failed templates:")
        for template in failed_templates:
            print("\t" + template)
        print("The rest of the files have been successfully created\n")
    else:
        print("All templates were successfully created\n")




