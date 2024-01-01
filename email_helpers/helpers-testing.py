import unittest
import email_helpers.test_data as data
import email_helpers.helpers as h


class MyTestCase(unittest.TestCase):
    def test_opens_server_correctly(self):
        # Checks that we are able to setup the server properly
        server = h.Email(data.username, data.password)
        server.close()

    def test_send_email_once(self):
        # Sends a single email_helpers
        server = h.Email(data.username, data.password)

        message = "Hello World!"
        server.send_email(data.receiver_email, message)

        server.close()

    def test_send_email_three_times(self):
        # Sends 3 emails with different messages
        server = h.Email(data.username, data.password)

        for i in range(1, 4):
            server.send_email(data.receiver_email, f"Hello World {i}")

        server.close()

    def test_send_email_different_accounts(self):
        # Sends the same email_helpers to different accounts
        message = "Hello World"

        server = h.Email(data.username, data.password)

        server.send_email(data.receiver_email, message)
        server.send_email(data.oth_acc_1, message)
        server.send_email(data.oth_acc_2, message)

        server.close()


if __name__ == '__main__':
    unittest.main()
