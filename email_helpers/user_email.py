import os
import text_menu.user_io as io
import email_helpers.helpers


extensions = [".txt", ".pdf", ".docx"]


def mail(spreadsheet, column_name, is_auto):
    prompt_for_subject = True

    if is_auto:
        print("Would you like to set email subjects if they are not already set in the spreadsheet?")
        prompt_for_subject = io.get_yes_or_no() == 'y'

    user_email = helpers.Email()
    for record in spreadsheet.records:

        subject = helpers.get_subject(record, (not is_auto) or prompt_for_subject)

        receivers_email = helpers.get_email(record, column_name)
        if receivers_email is None:
            continue

        template = helpers.get_template_file(record, column_name)
        if template is None or receivers_email is None:
            print(f"No template found to send to {receivers_email}")
            print("Email will not be sent\n")
            continue

        template_path = "output/" + template

        message = helpers.get_message(record, column_name)
        if message is None:
            print(f"No file found under name {record[column_name]}")
            print("File will not be sent\n")
            continue

        if not is_auto:
            io.display_message(message)
            print("Would you like to send this message?")

            response = io.get_yes_or_no()
            if response == 'n':
                print(f"File {template} not send to {receivers_email}")
                os.remove(template_path)
                continue

        print(f"Sending file {template} to {receivers_email}")
        files = helpers.get_file_attachments(record)

        user_email.send_email([receivers_email], message, subject, files)
        os.remove(template_path)
        print(f"File {template} sent successfully to {receivers_email}\n")

    user_email.close()

