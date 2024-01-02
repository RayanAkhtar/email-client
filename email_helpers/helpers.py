import os.path
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import file_reader.file_reader as fr

port = 465


class Email:
    def __init__(self, sender_email=None, password=None):
        self.msg = MIMEMultipart()              # The message to send to the recipient
        self.sender_email = sender_email        # The sender's email
        self.password = password                # The sender's password
        self.server = None                      # The server to send the email on
        self.success = self.login()             # Sets up most of the user's data

    def login(self):
        while True:
            # Sets up user data and logs in
            if self.sender_email is None:
                self.sender_email = input("Please enter your email address and press enter: ")

            if self.password is None:
                self.password = input("Please type in your password and press enter: ")

            context = ssl.create_default_context()

            self.server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
            try:
                self.server.login(self.sender_email, self.password)
                return True
            except smtplib.SMTPAuthenticationError:
                print("\nLogin failed, Incorrect email or password")
                print("Do not use your email password, refer to the 'help' section for more details")
                input("Returning to the Main menu, press 'enter' to continue")
                return False

    def close(self):
        self.server.close()

    def send_email(self, recipients, message, subject="", files=None):
        # Send an email to each recipient with the given message
        for recipient in recipients:
            self.msg = MIMEMultipart()

            self.msg["Subject"] = subject
            self.msg["From"] = self.sender_email
            self.msg["To"] = recipient

            message = strip_brackets(message)
            self.msg.attach(MIMEText(message, "plain"))
            self.attach_files(files)

            self.server.sendmail(self.sender_email, recipient, self.msg.as_string())

    def attach_files(self, files, directory="output/"):
        if files is None:
            files = []

        for path in files:
            if path is None:
                continue
            file_path = os.path.join(directory, path)
            if os.path.exists(file_path):
                attachment = MIMEBase('application', 'octet-stream')
                with open(file_path, 'rb') as file:
                    attachment.set_payload(file.read())
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
                self.msg.attach(attachment)
            else:
                print(f"File not found: {file_path}")


def get_subject(record, prompt_if_none, message_to_send, receivers_email):
    subject = ""
    if "subject" in record.keys():
        subject = record["subject"]

    if prompt_if_none and subject is None:
        print("No subject header was identified for this email")

        print(f"The message is {message_to_send}")
        print(f"The email is to {receivers_email}")

        subject = input("Enter a subject, or leave blank to ignore: ")

    return subject


def get_email(record, column_name):
    receivers_email = None
    if "email" in record.keys():
        receivers_email = record["email"]

    if receivers_email is None:
        print(f"No email associated with template file {record[column_name]}")
        print("This file will not be sent\n")

    return receivers_email


def get_message(record, column_name):
    template_file = get_template_file(record, column_name)
    if template_file is None:
        return None

    return fr.read_file(template_file)


def get_template_file(record, column_name):
    extensions = [".txt", ".pdf", ".docx"]

    for extension in extensions:
        filename = record[column_name] + extension
        if os.path.exists("output/" + filename):
            return filename

    return None


def get_file_attachments(record):
    files = []
    file = "file_"
    i = 1

    while (file + str(i)) in record.keys():
        files.append(record[file + str(i)])
        i += 1

    return files


def strip_brackets(message):
    to_remove = "{}[]?"
    translation_table = str.maketrans("", "", to_remove)
    stripped_message = message.translate(translation_table)
    return stripped_message


