import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl

port = 465

# todo remove before committing:
#       email: rayanakhtar2003.testing@gmail.com
#       https://www.google.com/settings/security/lesssecureapps
#       app password: jpgy cdaw owvc lpyj


class Email:
    def __init__(self, sender_email=None, password=None):
        self.msg = None
        self.sender_email = sender_email
        self.password = password
        self.server = None
        self.login()

    def login(self):
        if self.sender_email is None:
            self.sender_email = input("Please enter your email address and press enter: ")

        if self.password is None:
            self.password = input("Please type in your password and press enter: ")

        context = ssl.create_default_context()

        self.server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
        self.server.login(self.sender_email, self.password)

    def logout(self):
        self.server.close()

    def send_email(self, recipients, message, subject=""):
        self.msg = MIMEText(message)
        self.msg["Subject"] = subject
        self.msg["From"] = self.sender_email
        self.msg["To"] = ', '.join(recipients)
        self.server.sendmail(self.sender_email, recipients, self.msg.as_string())

