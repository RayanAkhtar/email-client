import text_menu.help as help
import text_menu.emails as emails
import text_menu.templates as templates
import text_menu.user_io as io


def menu():
    print("""Welcome to the AI Email Client:
    1. Create templates
    2. Send emails
    3. Help
    4. Quit
    """)

    choice = io.get_user_input(1, 4)
    if choice == 1:
        templates.menu()
    elif choice == 2:
        emails.menu()
    elif choice == 3:
        help.menu()
    else:
        print("Exiting Program")
        exit(0)

