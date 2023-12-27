from email_helpers.helpers import Email
import file_reader.file_reader as fr
import os


def mail(spreadsheet, column_name):

    user_email = Email()
    for record in spreadsheet.records():
        if "subject" in record.keys():
            subject = record["subject"]
        else:
            print("No subject header was identified for this email_helpers")
            subject = input("Enter a subject, or leave blank to ignore: ")

        if "email_helpers" in record.keys():
            receivers_email = record["email_helpers"]
        else:
            print(f"No email_helpers associated with template file {record[column_name]}")
            print("This file will not be sent\n")
            continue
        template = record[column_name]
        message = fr.read_file(template)

        files = [] # todo later, incorporate into email_helpers sending

        user_email.send_email([receivers_email], message, subject)
        os.remove("template/" + template)
        print(f"File {template} sent successfully to {receivers_email}\n")

    user_email.logout()

