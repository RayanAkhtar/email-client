import dotenv
import text_menu.user_io as io


def menu():
    menu_funcs = {
        1: change_email,
        2: change_api_Key,
        3: skip
    }

    menu_string = """\
    Change User Data:
        1. Change email address and password
        2. Change OpenAI API Key
        3. Go back
    """

    io.clear_screen()
    choice = io.get_user_input(menu_string, 1, 3)
    io.clear_screen()

    menu_funcs[choice]()


def change_email():
    io.print_current_email_data()
    input("Press enter to continue: ")
    io.clear_screen()

    response = io.get_yes_or_no("Would you like to change your email and app key?")
    io.clear_screen()
    if response != 'y':
        return

    email = input("Please enter your new email address: ")
    dotenv.set_key(".env", "GMAIL_EMAIL", email)
    dotenv.load_dotenv()

    password = input("Please enter your new email app key: ")
    dotenv.set_key(".env", "GMAIL_PASSWORD", password)
    dotenv.load_dotenv()

    print("Data saved successfully")
    input("Press enter to return to menu: ")


def change_api_Key():
    io.print_current_api_key()
    input("Press enter to continue: ")
    io.clear_screen()

    response = io.get_yes_or_no("Would you like to change your API key?")
    io.clear_screen()
    if response != "y":
        return

    api_key = input("Please enter your new API Key: ")
    dotenv.set_key(".env", "OPENAI_API_KEY", api_key)
    dotenv.load_dotenv()

    print("API key saved successfully")
    input("Press enter to return to menu: ")

def skip():
    pass