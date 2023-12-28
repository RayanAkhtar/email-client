from email_helpers.helpers import Email
import file_reader.file_reader as fr
import os
import text_menu.user_io as io

extensions = [".txt", ".pdf", ".docx"]


def mail(spreadsheet, column_name):
    # Automatically sends bulk email to the recipients

    print("Would you like to set email subjects if they are not already set in the spreadsheet?")
    response = io.get_yes_or_no()
    if response == 'y':
        skip_subject = False
    else:
        skip_subject = True

    user_email = Email()
    for record in spreadsheet.records:

        if "subject" in record.keys():
            subject = record["subject"]
        elif not skip_subject:
            print("No subject header was identified for this email")
            subject = input("Enter a subject, or leave blank to ignore: ")
        else:
            subject = None

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
            if (message != None):
                found_message = True
                break

        if not found_message:
            print(f"No file found under file name {record[column_name]}")
            print("File will not be sent\n")
            continue

        message = fr.read_file(template)

        files = [] # todo later, incorporate into email_helpers sending

        user_email.send_email([receivers_email], message, subject)
        os.remove("output/" + template)
        print(f"File {template} sent successfully to {receivers_email}\n")

    user_email.logout()

