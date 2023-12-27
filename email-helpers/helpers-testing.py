import unittest

import helpers as h

# TODO
#       Tell the user to go to gmail
#           Set up 2fa
#           Set up a passkey
#           Use that passkey when they want to login
#           Let them know that this may not be too secure, so don't use this for their main email

receiver_email = ["rayanakhtar200330@gmail.com", "ra1422@ic.ac.uk"]
username = "rayanakhtar12032003@gmail.com"
password = "jpgy cdaw owvc lpyj"


class MyTestCase(unittest.TestCase):
    def test_opens_server_correctly(self):
        server = h.Email(username, password)
        server.logout()

    def test_send_email_once(self):
        server = h.Email(username, password)

        message = "Hello World!"
        server.send_email(receiver_email, message)

        server.logout()

    def test_send_email_three_times(self):
        server = h.Email(username, password)

        for i in range(1, 4):
            server.send_email(receiver_email, f"Hello World {i}")

        server.logout()

    def test_send_email_different_accounts(self):
        oth_acc_1 = ["rayan.akhtar.computing@gmail.com"]
        oth_acc_2 = ["rayan.akhtar.testing@gmail.com"]
        message = "Hello World"

        server = h.Email(username, password)

        server.send_email(receiver_email, message)
        server.send_email(oth_acc_1, message)
        server.send_email(oth_acc_2, message)

        server.logout()


if __name__ == '__main__':
    unittest.main()
