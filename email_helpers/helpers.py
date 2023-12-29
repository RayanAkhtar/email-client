import os.path
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465


class Email:
    def __init__(self, sender_email=None, password=None):
        self.msg = MIMEMultipart()              # The message to send to the recipient
        self.sender_email = sender_email        # The sender's email
        self.password = password                # The sender's password
        self.server = None                      # The server to send the email on
        self.login()                            # Sets up most of the user's data

    def login(self):
        # Sets up user data and logs in
        if self.sender_email is None:
            self.sender_email = input("Please enter your email address and press enter: ")

        if self.password is None:
            self.password = input("Please type in your password and press enter: ")

        context = ssl.create_default_context()

        self.server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
        self.server.login(self.sender_email, self.password)

    def logout(self):
        self.server.close()

    def send_email(self, recipients, message, subject="", files=None):
        # Send an email to each recipient with the given message
        for recipient in recipients:
            self.msg = MIMEMultipart()

            self.msg["Subject"] = subject
            self.msg["From"] = self.sender_email
            self.msg["To"] = recipient

            self.attach_files(files)
            self.msg.attach(MIMEText(message, "plain"))

            self.server.sendmail(self.sender_email, recipient, self.msg.as_string())

    def attach_files(self, files, directory="output/"):
        if files is None:
            return
        for path in files:
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