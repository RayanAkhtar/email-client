import os

template_extensions = ['txt', 'pdf', 'docx']        # Supported template file extensions
spreadsheet_extensions = ['xlsx', 'csv']            # Supported spreadsheet extensions


def get_user_input(lower_bound, upper_bound):
    while True:
        choice = input(f"Please enter a number between {lower_bound} and {upper_bound}: ")
        if choice.isnumeric() and lower_bound <= int(choice) <= upper_bound:
            return int(choice)
        else:
            print("Please enter a valid integer within the correct range: ")


def get_yes_or_no():
    while True:
        choice = input("Please enter [Y]es or [N]o").lower().strip()
        if choice.startswith('y'):
            return 'y'
        elif choice.startswith('n'):
            return 'n'
        print("Please enter an appropriate value")


def get_option_from_list(data):
    while True:
        choice = input("Please enter either the file name or its corresponding number: ")
        if choice.isnumeric() and 1 <= int(choice) <= len(data):
            return data[int(choice) - 1]
        else:
            if choice in data:
                return choice


def get_extension(message):
    while True:
        extension = input(message)
        if extension in template_extensions:
            return extension
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

    for i in range(0, len(files)):
        print(f"File {i+1} - {files[i]}")

    return files


def display_message(message):
    print("This is what the email body will look like: ")
    print(message)  # Todo later in gui, make it possible for the user to edit these messages instead
