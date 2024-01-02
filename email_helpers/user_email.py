import os
import text_menu.user_io as io
import email_helpers.helpers as helpers


extensions = [".txt", ".pdf", ".docx"]


def mail(spreadsheet, column_name, is_auto):
    prompt_for_subject = True

    if is_auto:
        message = "Would you like to set email subjects if they are not already set in the spreadsheet?"
        prompt_for_subject = io.get_yes_or_no(message) == 'y'

    user_email = helpers.Email()

    if not user_email.success:
        return

    for record in spreadsheet.records:
        io.clear_screen()

        receivers_email = helpers.get_email(record, column_name)
        if receivers_email is None:
            continue

        template = helpers.get_template_file(record, column_name)
        if template is None or receivers_email is None:
            print(f"No template found to send to {receivers_email}")
            print("Email will not be sent")
            input("Press Enter to continue onto the next email: ")
            continue

        template_path = "output/" + template

        message_to_send = helpers.get_message(record, column_name)
        if message_to_send is None:
            print(f"No file found under name {record[column_name]}")
            print("File will not be sent")
            input("Press Enter to continue onto the next email: ")
            continue

        prompt_for_subject = prompt_for_subject or not is_auto
        subject = helpers.get_subject(record, prompt_for_subject, message_to_send, receivers_email)

        used_ai = "{" in message_to_send
        contains_error = "ERROR" in message_to_send

        should_verify = (not is_auto) or used_ai or contains_error
        if should_verify:
            display_message = ("Coloured text will be used to highlight ai and errors.\n"
                               "The email will not contain this coloured text.\n")
            display_message += io.get_message_to_display(message_to_send)
            display_message += "Would you like to send this message?\n"

            response = io.get_yes_or_no(display_message, True)
            if response == 'n':
                print(f"File {template} not sent to {receivers_email}")
                input("Press Enter to continue onto the next email: ")
                continue

        print(f"Sending file {template} to {receivers_email}")
        files = helpers.get_file_attachments(record)

        user_email.send_email([receivers_email], message_to_send, subject, files)
        os.remove(template_path)
        if not is_auto:
            print(f"File {template} sent successfully to {receivers_email}")
            input("Press Enter to continue onto the next email: ")
        io.clear_screen()

    user_email.close()

    io.clear_screen()
    print("No more emails to send")
    input("Press enter to return to main menu: ")

