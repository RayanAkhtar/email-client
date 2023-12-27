import unittest

import helpers as h


receiver_email = ["arjenahmed123@gmail.com"]
username = "rayanakhtar12032003@gmail.com"
password = "jpgy cdaw owvc lpyj"


class MyTestCase(unittest.TestCase):
    def test_opens_server_correctly(self):
        # Checks that we are able to setup the server properly
        server = h.Email(username, password)
        server.logout()

    def test_send_email_once(self):
        # Sends a single email_helpers
        server = h.Email(username, password)

        message = "Hello World!"
        server.send_email(receiver_email, message)

        server.logout()

    def test_send_email_three_times(self):
        # Sends 3 emails with different messages
        server = h.Email(username, password)

        for i in range(1, 4):
            server.send_email(receiver_email, f"Hello World {i}")

        server.logout()

    def test_send_email_different_accounts(self):
        # Sends the same email_helpers to different accounts
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
