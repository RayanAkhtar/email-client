from email_helpers.helpers import Email
import file_reader.file_reader as fr
import os
import text_menu.user_io as io

extensions = [".txt", ".pdf", ".docx"]


def mail(spreadsheet, column_name): # For now it is duplicated, but will have different behaviour later

    user_email = Email()
    for record in spreadsheet.records:
        if "subject" in record.keys():
            subject = record["subject"]
        else:
            print("No subject header was identified for this email")
            subject = input("Enter a subject, or leave blank to ignore: ")

        if "email" in record.keys():
            receivers_email = record["email"]
        else:
            print(f"No email associated with template file {record[column_name]}")
            print("This file will not be sent\n")
            continue

        if receivers_email is None:
            print(f"No email associated with template file {record[column_name]}")
            print("This file will not be sent\n")
            continue

        found_message = False
        for extension in extensions:
            template = record[column_name] + extension
            message = fr.read_file(template)
            if message is not None:
                found_message = True
                break

        if not found_message:
            print(f"No file found under file name {record[column_name]}")
            print("File will not be sent\n")
            continue

        message = fr.read_file(template)

        io.display_message(message)

        print("Would you like to send this message?")
        response = io.get_yes_or_no()

        if response == 'n':
            os.remove("output/" + template)
            continue

        files = [] # todo later, incorporate into email_helpers sending

        user_email.send_email([receivers_email], message, subject)
        os.remove("output/" + template)
        print(f"File {template} sent successfully to {receivers_email}\n")

    user_email.logout()