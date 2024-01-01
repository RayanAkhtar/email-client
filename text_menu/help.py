import text_menu.user_io as io


def menu():

    menu_dict = {
        1: template_help,
        2: spreadsheet_help,
        3: email_help
    }

    message = """\
    1. Help on formatting templates
    2. Help on formatting spreadsheets
    3. Help on emailing
    4. Go back
"""

    response = io.get_user_input(message, 1, 4)

    menu_dict[response]()

    io.clear_screen()


def template_help():

    intro = """\
In this program, we will format a template file specific to each record in the provided spreadsheet.
By doing this, we can then bulk create files which we will then send in the email part of this program.
    
When creating template files, you can either create a docx file (a word document), a pdf file, or a txt file.
Images, along with other forms of data such as tables and charts are not currently supported.
The program will only format text, altering the text that contains the symbols described below.

In this example, we will use the following record: {a:10, b:20, c:None, d:Category A}
We will now go over the following types of text formatting

Press enter to continue: """

    io.clear_screen()
    input(intro)

    strict_formatting_help = """\
Strict Text Formatting:
    [a] - No default value
        With this type of text formatting, we find the value under header 'a' in the current record, in this case it is 10.
        So this means that if we have '[a]' in our file, it will be replaced with '10'.
        If there was no value for 'a', then '[a]' would be replaced with 'ERROR' in the file.
        
    [a:b] - Default value
        In this case, we have provided a default value 'b'.
        So if the value of 'a' is not defined, then '[a]' return 'b' instead.
    
    [filename.ext] - Files
        In this case, we will instead be replacing '[filename.ext]' with the text held within the file filename.ext, but it is essential
        to note that ext must be a txt, pdf or docx file. Also, the file must be held in the 'templates/' folder
    
    [self] - Current state of the template file
        This will replace '[self]' with all of the text held in the template so far. The main use for this can be shown
        in the AI-formatting, when you wish to chain prompts, but this will be explained shortly.
        
Press enter to continue: """

    io.clear_screen()
    input(strict_formatting_help)

    optional_formatting_help = """\
Optional Text Formatting:
    This is what an example for optional text formatting would look like:
    
        ? Column name                                       <- The column name to check values for
        # Category A                                        <- If the value held at 'Column name' is 'Category A'
        Paragraph A                                         <- The text to keep in the template
        # Category B
        Paragraph B
        ~                                                   <- To signal an optional default paragraph
        Default paragraph here                              <- The default paragraph
        ?                                                   <- Must start and end all optional paragraphs with this
        
    This type of formatting would be used when you want to have different paragraphs depending on the value of a record
    in a spreadsheet.
    If you do not have a paragraph for a value held, then the default will be returned in that section. If you do not
    provide a default in this specific case, then 'ERROR' would be returned in that section instead. 
    
Press enter to continue: """

    io.clear_screen()
    input(optional_formatting_help)

    ai_generation_help = """\
AI-Generated Formatting.
    There are a few different things that we can do with AI-Generation in this template.
    
        {a} - Single prompt
            This will pass the prompt 'a' to the AI Model
        
        {a;b} - Chained prompts 
            This will pass the prompt 'a' to the AI Model, which will return 'a2'. 
            Then it will provide both 'a2' and 'b' to the model in the same prompt.
        
        {a [b.ext]} - File prompts
            This will pass both 'a' as well as the text in 'b.ext' to the AI Model.
            'b.ext' must follow the conventions mentioned previously in strict text formatting.

Press enter to continue: """

    io.clear_screen()
    input(ai_generation_help)

    advice_help = """\
When formatting text, you may receive 'ERROR' in different sections, this will be included so that you can see where
the error occurs. If you wish to bulk send emails without verification, we will skip over any files that contain 'ERROR'
and also point out that there is an error in the file so that you can verify data.

Press enter to continue: """

    io.clear_screen()
    input(advice_help)
    io.clear_screen()


def spreadsheet_help():
    io.clear_screen()

    intro = """\
Spreadsheets are a key aspect of this program, this is required in order to format a template.
Spreadsheet files must either be a '.csv' file or a '.xlsx' file.

When creating a spreadsheet, your first row of values will be headers. These headers will need to be included in the 
template when you wish to do strict and optional text formatting. After this point, every other row will be considered a 
record. For each record we will create a template. You will need to specify the column which will be used to name the file.

Press enter to continue: """

    input(intro)
    io.clear_screen()

    example_spreadsheet = """\
An example spreadsheet will be shown below:
    
    | Name  | Age |   Company   |  
    | John  |  24 |   Company A |
    | Smith |  45 |   Company B |

In this example, we will be creating 2 formatted templates, one for 'John' and another for 'Smith'. In the program, we 
would also be asked to choose a column name to name the file, in this case, we will use 'Name' as the column to name the
file.

Press enter to continue: """

    input(example_spreadsheet)
    io.clear_screen()

    explaination = """\
Suppose we have the template:
    [Name] is [Age] and works for [Company]
    ? Company
    # Company A
    Some paragraph about company A here
    # Company B
    Some paragraph about company B here
    ~
    Some default paragraph here
    ?

Then we would have the following files in 'output/':

    1. John.ext (The user can choose it to be either a txt, docx, or pdf)
        John is 24 and works for Company A
        Some paragraph about company A here
    
    2. Smith.ext
        Smith is 45 and works for Company B
        Some paragraph about company B here
        
Press enter to continue: """

    input(explaination)
    io.clear_screen()

    extra_data = """\
In the spreadsheet, if you choose to leave a value blank, you must provide a default value in the template, this way,
you can prevent any erroneous output. Note that in this example, we provided a default value for optional text replacement
but we have not done this for strict text replacement.

Press enter to return to the main menu: """

    input(extra_data)
    io.clear_screen()


def email_help():
    email_help_section = """\
When it comes to sending emails, you must use a gmail account for now.
To allow this program to send emails, you will also be required to enable 2 Factor Authentication and generate an App
Password Key. This will be what you will enter instead of your gmail's password for this app. Please note that emails
that are sent in this program will not be recorded under your gmail.

In this program, you will be asked to select a spreadsheet, this spreadsheet must contain a column header called 'email'.
This will contain the recipient's email address. You will be asked to provide the column name for the file names that 
will be present in 'output/'. Note that files must be created before bulk sending emails. If you include a 'subject'
header in your file, then this will be included as the email's subject, otherwise you will be prompted to provide one yourself.

If any of the formatted templates contain 'ERROR', the user will be notified of this and the email will not be sent.    

Press enter to continue: """

    io.clear_screen()
    input(email_help_section)
    io.clear_screen()

