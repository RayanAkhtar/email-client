import os
import text_formatter.text_formatting as tf
from colorama import Fore, Style

template_extensions = ['txt', 'pdf', 'docx']        # Supported template file extensions
spreadsheet_extensions = ['xlsx', 'csv']            # Supported spreadsheet extensions
delim_start = "{[?"
delim_end = "}]?"

def get_user_input(message, lower_bound, upper_bound):
    print(message)
    while True:
        choice = input(f"Please enter a number between {lower_bound} and {upper_bound}: ")
        if choice.isnumeric() and lower_bound <= int(choice) <= upper_bound:
            clear_screen()
            return int(choice)

        clear_screen()
        print(message)
        print(f"Incorrect input, please try again")


def get_yes_or_no(message, use_colour=False):
    if use_colour:
        colour_print(message)
    else:
        print(message)
    while True:
        choice = input("Please enter [Y]es or [N]o: ").lower().strip()
        if choice.startswith('y'):
            clear_screen()
            return 'y'
        elif choice.startswith('n'):
            clear_screen()
            return 'n'
        clear_screen()
        if use_colour:
            colour_print(message)
        else:
            print(message)
        print("Input not recognised, please try again")


def get_option_from_list(data, message):
    print(message)
    while True:
        choice = input("Please enter either the file name or its corresponding number: ")
        if choice.isnumeric() and 1 <= int(choice) <= len(data):
            clear_screen()
            return data[int(choice) - 1]
        else:
            if choice in data:
                clear_screen()
                return choice
        clear_screen()
        print(message)
        print("Input not recognised, please try again")


def get_extension(message):
    message = "You can currently save the file as a 'txt', 'pdf' or 'docx' file"
    print(message)
    while True:
        extension = input("Enter a file type: ")
        if extension in template_extensions:
            clear_screen()
            return extension
        clear_screen()
        print(message)
        print("Please enter a valid template extension (txt, pdf, docx)")


def get_all_files_in_directory(path, extensions):
    files = os.listdir(path)
    valid_files = []
    for file in files:
        if file.split(".")[-1] in extensions:
            valid_files.append(file)

    return valid_files


def list_files(option):
    if option == "templates":
        files = get_all_files_in_directory("templates/", template_extensions)
    else:
        files = get_all_files_in_directory("spreadsheets/", spreadsheet_extensions)

    return files


def get_files_as_string(files):
    message = ""
    for i in range(0, len(files)):
        message += f"File {i+1} - {files[i]}\n"
    return message


def get_message_to_display(message):
    return "This is what the email body will look like:\n\n" + message + "\n\n"


def colour_print(message):
    char_ptr = 0
    red_colour = False
    while char_ptr < len(message):
        char = message[char_ptr]
        char_ptr += 1

        if char in delim_start:
            red_colour = True
        elif char in delim_end:
            red_colour = False
        else:
            print_colour(char, red_colour)


def print_colour(char, red_colour):
    if red_colour:
        print(Fore.RED + char + Style.RESET_ALL, end='')
    else:
        print(char, end='')


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print()
