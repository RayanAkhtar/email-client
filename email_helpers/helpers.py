import smtplib
from email.mime.text import MIMEText
import ssl

port = 465


class Email:
    def __init__(self, sender_email=None, password=None):
        self.msg = None                         # The message to send to the recipient
        self.sender_email = sender_email        # The sender's email_helpers
        self.password = password                # The sender's password
        self.server = None                      # The server to send the email_helpers on
        self.login()                            # Sets up most of the user's data

    def login(self):
        # Sets up user data and logs in
        if self.sender_email is None:
            self.sender_email = input("Please enter your email_helpers address and press enter: ")

        if self.password is None:
            self.password = input("Please type in your password and press enter: ")

        context = ssl.create_default_context()

        self.server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
        self.server.login(self.sender_email, self.password)

    def logout(self):
        self.server.close()

    def send_email(self, recipients, message, subject=""):
        # Send an email_helpers to the recipient with a given message
        self.msg = MIMEText(message)
        self.msg["Subject"] = subject
        self.msg["From"] = self.sender_email
        self.msg["To"] = ', '.join(recipients)
        self.server.sendmail(self.sender_email, recipients, self.msg.as_string())

