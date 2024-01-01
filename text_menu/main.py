import text_menu.help as help
import text_menu.emails as emails
import text_menu.templates as templates
import text_menu.user_io as io


def menu():
    menu_funcs = {
        1: templates.menu,
        2: emails.menu,
        3: help.menu,
        4: exit
    }

    menu_string = """\
Welcome to the AI Email Client:
    1. Create templates
    2. Send emails
    3. Help
    4. Quit
"""

    io.clear_screen()
    choice = io.get_user_input(menu_string, 1, 4)
    io.clear_screen()

    menu_funcs[choice]()

