from email_helpers.helpers import Email
import file_reader.file_reader as fr
import os
import text_menu.user_io as io


def mail(spreadsheet, column_name): # For now it is duplicated, but will have different behaviour later

    email = Email()
    for record in spreadsheet.records():
        subject = record["subject"]
        receivers_email = record["email_helpers"]
        template = record[column_name]
        message = fr.read_file(template)
        files = []  # todo later, incorporate into email_helpers sending

        # todo later: add a way or the user to edit emails and then submit that
        #   The part below is a simple template that to either send or skip an email_helpers
        #   The plan is to allow the user to then edit the email_helpers in some console or text editor

        print("Would you like to send this email_helpers: ")
        response = io.get_yes_or_no()
        if response == 'y':
            email.send_email([receivers_email], message, subject)
        os.remove("template/" + template)

    email.logout()