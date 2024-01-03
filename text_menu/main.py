import os

import dotenv

import text_menu.help as help
import text_menu.emails as emails
import text_menu.templates as templates
import text_menu.user_io as io
import text_menu.account as account


def menu():
    if "GMAIL_EMAIL" in os.environ:
        del os.environ["GMAIL_EMAIL"]
    if "GMAIL_PASSWORD" in os.environ:
        del os.environ["GMAIL_PASSWORD"]
    if "OPENAI_API_KEY" in os.environ:
        del os.environ["OPENAI_API_KEY"]
    dotenv.load_dotenv()

    menu_funcs = {
        1: templates.menu,
        2: emails.menu,
        3: account.menu,
        4: help.menu,
        5: exit
    }

    menu_string = """\
Welcome to the AI Email Client:
    1. Create templates
    2. Send emails
    3. Change emails and passwords
    4. Help
    5. Quit
"""

    io.clear_screen()
    choice = io.get_user_input(menu_string, 1, 5)
    io.clear_screen()

    menu_funcs[choice]()

