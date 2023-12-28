# email-client
A python-based project to support automation of emails with text reformatting including the use of AI-Generated prompts


# Prerequisites
In order to use the email client, you will need to have a gmail account.
Then, click on your profile and go to 'Manage your google account', from here, go to 'security', turn on 'two step verification' and head into that section,
After this, go to 'App passwords' and type in any name for this. Keep track of the password as you will need to use this when logging in.
When it comes to typing in your password, you will use this instead of your gmail password.
<br>
It is important to note that it is essential to keep this password safe and secure as other people will be able to access your account using this password too.
<br><br>
Before running the program, you should create a spreadsheet file and a template file, putting them in the `spreadsheets` and `templates` folders respectively.
More detail on the format of templates and spreadsheets will be provided below.

# How to use

## Running the program
When running the program, you will be given options to format templates or to send emails.
<br>
If you choose to format templates, you will need to provide a spreadsheet.
You are also given an option to use a single template or multiple templates.
In the single template option, you must provide the template file in the program.
On the other hand, if you choose not to use a single template, you must provide the full file name of the template as a field in the spreadsheet file.


## Formatting the template
In order to make use of the program, you will want a template. Ideally, this should be a plain .txt file, however, it can also accept .pdf and .docx files too.
It is heavily recommended to avoid creating pdf files as this is a lengthy process, as opposed to the creation of docx and txt files.
There are different types of ways you can reformat a template:

### 1. Strict Text Replacement '[s]'
With Strict Text Replacement, you are able to replace text with data held in the column of a csv table. For example, suppose you have a column called ```name``` in the csv file, then if you have ```[name]``` at any point in your template, the program will replace the text with that held in the table. Please note that you will need to provide a default value if you leave an entry empty in the spreadsheet file, otherwise your template will contain ```ERROR``` at the selected point, this will help highlight if you are missing any details in your spreadsheet file, or if you were supposed to have a default value there.
<br>
In order to have a default value in your text replacement, you can use the ```:``` sign to indicate a default value. For example, if you were to have ```[Name:Tom]``` in your file, then the program will check the record in the spreadsheet file for column ```Name```, and if there is no value, it will be replaced with ```Tom```.
<br>
In order to get all data held within another `.pdf`, `.txt` or `.docx` file, you will need to include the file name as well as its extension. For example: `[cv.pdf]`.
The main reasoning behind this functionality is to make templates look cleaner, as well as providing the generative ai model some more data to aid text generation.

### 2. Optional and Default Paragraph Replacement
Suppose you are formatting cover letters, you may wish to tailor your application to a specific field such as AI, Machine Learning, or Software Engineering, but reformatting paragraphs each time can be monotonous, thats where optional and default paragraph replacement comes in to play.
In order to start a section of paragraph replacement, use the ```? field``` character to signal the beginning of a section. Within this section, you can use the ```#``` character to define an optional paragraph. To do this, start the line with ```#name``` where name is the name of the column to check against in the spreadsheet.
<br>
For example, consider you have a column called `field` in your program, with possible values of `computer_science`, `programming` and `artificial_intelligence`, then you would have up to 3 `#` sections such as `#programming` followed by paragraph text. This section will run until it hits the next `#`, `~` or `?` character.
<br>
Now, what if you wish to have a default paragraph, for example, if the field is in `software_engineering`. Then you could either ignore the section as a whole, or instead have a default paragraph. To have this default paragraph, you would need to use the `~` operator, this is similar to the `#` operator, except that you do not need to provide any values on it.

### 3. Generative AI replacement
Now, suppose you wish to tailor your email to a specific case. Lets refer back to the cover letter example in this case. In this case, you could ask AI to generate a few reasons why you are a good fit for the company, or how your projects allign with the firm's objective. To do this, you would need to copy/paste for every email/cover letter you wish to send.
<br>
Instead, you can use AI text replacement to do the job on your behalf. To do this, you will need to enclose your prompt in `{}`. For example, you could do `{tell me about company x}` to get a response from an AI text generator and use this to tailor your text replacement.
<br>
Now this is fine, but the problem lies in the fact that text generation can be quite length and irrelevant at times, or not tailored to your text replacement, so there are a few other things you can do to make this more tailored to your needs.
<br>
Firstly, you can chain commands together, this can be done using the `;` operator within the `{}` operator. An example of this is as follows `{Tell me what you know about company x; now use this data to write a few sentances about y}`.
<br>
Another thing that you can do is provide more template files to pass to the AI text replacement tool, you are even able to pass the current state of text replacement to get it to finish sentences for you.
<br>
To pass a file, you will need to enclose the file name in the ai prompt using `[]`. 
For example, you can do `{prompt_1 [file_name_here]; prompt_2; prompt_3}`to pass a file for reference alongside a prompt and then chain it to another prompt. 
In order to pass the current state of the text replacement, you can use `[self]` to pass itself for a reference.
<br>
Here is an example command `{Tell me about company x; use the following text to show why I am a good fit for the company [cv.pdf]; now use this data to finish off the following paragraph, only write a few sentances: [self]}`.


## Formatting the spreadsheet file
It is optional to provide a spreadsheet file to the program, it must be in either `.csv` or `.xls` format in order to be processed correctly. Along with this, if you wish to use strict and optional text replacements, the column name must match the keyword held within `[]` and `#`. The column names will be converted to lowercase before use in both the template and the spreadsheet file, please keep this in mind. Also, it is best to use `_` or `-` to space words as opposed to a normal space character.
In the spreadsheet file, there are a few keywords that should be provided if you wish to send emails to users, they can also be used in the text replacement program if you wish:
<br>
1. `email_address` - This field **must** be filled in to send an email to the company of your choosing.
2. `subject` - This field can be included to provide a subject to the email. By default, AI will be used, in order to keep it blank, create a `subject` row and leave blank with an empty default value.
3. `file_n` - You can send multiple files using the email client at the end of an email, to do this, you will need columns such as `file_1`, `file_2`, and so on.


## Example Template and CSV file
In this case, I will provide an abstract email for a job application:
<br>
<br>
```
Dear [hiring_manager_name:Hiring Manager],

I hope this email finds you in good health. I am a student at university x, hoping to seek an internship in [field name] at [company name]. I would like to apply here as {what do you know about company x; here is a copy of my cv, use it to point out why I am a fit for [company name] [cv.pdf]; now use this data to finish off the paragraph: [self]}.

? field name
#computer_science 
Paragraph here containing text about your experience in computer_science 

#software_development 
Same but for software development

#artificial_intellgence 
Same but for artificial intelligence

~ 
A default paragraph if you want

?

More email content.

I hope to hear from you soon,

Kindest Regards,
Name
```

Now suppose in the spreadsheet, we have company_name = company x, field_name = computer science and no hiring manager name, then we could end up with the following:

```
Dear Hiring Manager,

I hope this email finds you in good health. I am a student at university x, hoping to seek an internship in Computer Science at company x. I would like to apply here as I am interested in your innovations in ....

Paragraph here containing text about your experience in computer_science 

More email content.

I hope to hear from you soon,

Kindest Regards,
Name
```