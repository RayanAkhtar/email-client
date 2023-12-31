import text_menu.user_io as io
import file_reader.file_reader as fr
import text_formatter.text_formatting as tf
import file_writer.file_writing as fw
import os

def menu():

    no_spreadsheets = len(io.list_files("spreadsheets")) <= 0
    no_templates = len(io.list_files("templates")) <= 0
    if no_spreadsheets or no_templates:
        if no_spreadsheets:
            print("No spreadsheets found, please ensure that they are in spreadsheets/")
        if no_templates:
            print("No templates found, please ensure that they are in templates/")
        input("Please press enter to return to main menu")
        return

    message = "Would you like to use a single template only? "
    choice = io.get_yes_or_no(message)
    io.clear_screen()

    spreadsheet = fr.read_file(get_spreadsheet_choice())

    if choice == 'y':  # Single file
        template = fr.read_file(get_template_choice())
    else:  # Multi file
        template_column = get_column_name(spreadsheet, "Please enter the name of the template file header")

    name_column = get_column_name(spreadsheet, "Enter the column name for the file name: ")
    extension = io.get_extension("Please enter the file extension: ")

    if choice == 'y':
        create_templates(template, spreadsheet, name_column, extension)
    else:
        create_multiple_templates(template_column, spreadsheet, name_column, extension)

    print("Files have been created")
    input("Press 'enter' to continue...")


def get_template_choice():
    files = io.list_files("templates")
    message = io.get_files_as_string(files)
    file = io.get_option_from_list(files, message)  # In this case, file should be the path
    io.clear_screen()
    return file


def get_spreadsheet_choice():
    files = io.list_files("spreadsheets")
    message = io.get_files_as_string(files)
    file = io.get_option_from_list(files, message)
    io.clear_screen()
    return file


def get_column_name(spreadsheet, message):
    for i in range(len(spreadsheet.headers)):
        message += f"\nHeader {i + 1}: {spreadsheet.headers[i]}"
    message += "\n"

    column_name = io.get_option_from_list(spreadsheet.headers, message)
    io.clear_screen()
    return column_name


def create_templates(template, spreadsheet, name_column, extension):
    for row in spreadsheet.records:
        if file_exists(name_column, row, extension):
            continue
        formatter = tf.TextFormatter(template, row)
        formatter.format_text()
        if formatter.output_text is None:
            return
        else:
            fw.save_formatted_file(formatter.output_text, row[name_column], extension, "output/")


def create_multiple_templates(template_column, spreadsheet, name_column, extension):
    all_templates = io.get_all_files_in_directory("templates/", ["txt", "pdf", "docx"])
    loaded_templates = {}
    failed_templates = []
    failed = False

    for row in spreadsheet.records:

        if failed:
            failed_templates.append(row[name_column])
            continue

        if file_exists(name_column, row, extension):
            continue

        if row[template_column] not in all_templates:
            print(f"ERROR IN {row[name_column]}: {row[template_column]} not found in templates folder")
            failed_templates.append(row[name_column])
            continue

        if row[template_column] not in loaded_templates.keys():
            loaded_templates[template_column] = fr.read_file(row[template_column])

        formatter = tf.TextFormatter(loaded_templates[template_column], row)
        formatter.format_text()
        if formatter.output_text is not None and "{FAILED}" not in formatter.output_text:
            fw.save_formatted_file(formatter.output_text, row[name_column], extension)
        else:
            failed_templates.append(row[name_column])
            failed = True

    io.clear_screen()
    print("Finished template creation")
    if len(failed_templates) > 0:
        print("Failed templates:")
        for template in failed_templates:
            print("\t" + template + "." + extension)
        print("The rest of the files have been successfully created\n")
    else:
        print("All templates were successfully created\n")
    input("Press enter to return to the main menu: ")


def file_exists(name_column, record, extension):
    file_path = "output/" + record[name_column] + "." + extension
    io.clear_screen()
    if os.path.exists(file_path):
        print(f"File {file_path} currently exists, this record will not be reformatted")
        input("Press enter to continue onto the next email: ")
        return True
    return False

