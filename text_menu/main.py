import text_menu.help as help
import text_menu.emails as emails
import text_menu.templates as templates


def menu():
    print("""Welcome to the AI Email Client:
    1. Create a templates               # Not implemented
    2. Send emails                      # Not implemented
    3. Help                             # Not implemented
    4. Quit""")

    choice = get_user_input(1, 4)
    if choice == 1:
        templates.menu()
    elif choice == 2:
        emails.menu()
    elif choice == 3:
        help.menu()
    else:
        print("Exiting Program")
        exit(0)


def get_user_input(lower_bound, upper_bound):
    valid = False
    while not valid:
        choice = input(f"Please enter a number between {lower_bound} and {upper_bound}: ")
        if choice.isnumeric() and lower_bound <= int(choice) <= upper_bound:
            return int(choice)
        else:
            print("Please enter a valid integer within the correct range: ")


