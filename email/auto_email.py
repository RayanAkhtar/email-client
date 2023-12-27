from helpers import Email
import file_reader.file_reader as fr
import os


def mail(spreadsheet, column_name):

    email = Email()
    for record in spreadsheet.records():
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
        template = record[column_name]
        message = fr.read_file(template)

        files = [] # todo later, incorporate into email sending

        email.send_email([receivers_email], message, subject)
        os.remove("template/" + template)
        print(f"File {template} sent successfully to {receivers_email}\n")

    email.logout()

