import text_menu.user_io as io
import email_helpers.user_email as email
import text_menu.templates as templates
import file_reader.file_reader as fr


def menu():

    spreadsheet = fr.read_file(templates.get_spreadsheet_choice())
    column_name = templates.get_column_name(spreadsheet, "Please enter the column that contains the names of the template files")

    print("Would you like to verify emails?")
    is_auto = io.get_yes_or_no() != 'y'

    email.mail(spreadsheet, column_name, is_auto)

    print("No more emails to send")
    input("Press enter to return to main menu: ")

