import text_menu.user_io as io
import email_helpers.auto_email as auto
import email_helpers.verify_email as verify
import text_menu.templates as templates


def menu():

    spreadsheet = templates.get_spreadsheet_choice()
    column_name = templates.get_column_name(spreadsheet, "Please enter the column that contains the names of the template files")

    print("Would you like to verify emails?")
    option = io.get_yes_or_no()
    if option == "y":
        verify.mail(spreadsheet, column_name)
    else:
        auto.mail(spreadsheet, column_name)

    print("No more emails to send")
    input("Press enter to return to main menu: ")

