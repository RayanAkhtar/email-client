import file_reader.file_reader as fr
import ai_text_generator.generator as generator

text_file_extensions = ["txt", "pdf", "docx"]


class TextFormatter:

    def __init__(self, input_text, dictionary):
        self.input_text = input_text                # The text to reformat
        self.output_text = ""                       # The output text to return once the text is formatted correctly
        self.pos = 0                                # A position to keep track of the current formatting state
        self.dictionary = dictionary                # A record from a csv file, should be passed in as a mapping
        self.delimiters = "{[?"                     # Delimiters to trigger a string format

    def format_text_helper(self, end_char, func):
        if end_char not in self.input_text[self.pos:]:
            self.output_text += self.input_text[self.pos - 1:]
            self.pos = len(self.output_text)
            return ""

        text = self.get_until(end_char)
        return_val = func(text)
        if return_val is None:
            return None
        self.output_text += func(text)
        return ""

    def format_text(self):

        format_text_funcs = {
            '[': [self.square_format, ']'],
            '{': [self.curly_format, '}'],
            '?': [self.optional_format, '?']
        }

        # Runs over the input text and formats where necessary
        while self.pos < len(self.input_text):
            char = self.input_text[self.pos]
            self.pos += 1
            if char in self.delimiters:
                format_func = format_text_funcs[char][0]
                char_end = format_text_funcs[char][1]
                result = self.format_text_helper(char_end, format_func)
                if result is None:
                    self.output_text = None
                    return
            else:
                self.output_text += char

    def get_until(self, delims):
        # Gets the characters in a string until reaching a character in delims
        # Pointer goes past delimiter in this version
        text = ""
        while self.input_text[self.pos] not in delims:
            text += self.input_text[self.pos]
            self.pos += 1
        self.pos += 1
        return text

    def square_format(self, text):
        # Strict formatting is done here
        if '.' in text:
            extension = text.split('.')[-1]
            assert extension in text_file_extensions
            file_data = fr.read_file(text)
            if file_data is None:
                return "Error: NO FILE DATA"
            return file_data

        if text == "self":
            return self.output_text

        default = "ERROR: NO DEFAULT VALUE FOUND"
        key = text

        if ":" in text:
            pos_to_split = text.index(":")
            key = text[:pos_to_split]
            default = text[pos_to_split + 1:]

        if key not in self.dictionary.keys():
            return default
        result = self.dictionary[key]
        if result is None:
            return f"ERROR: NO VALUE IN SPREADSHEET FOR {key}"
        return result

    def curly_format(self, text):
        formatted_text = self.recurse(text)
        if formatted_text is None:
            self.output_text = None
            return None
        return generator.generate_text_chained(formatted_text)


    def optional_format(self, text):
        # Optional formatting is done here
        if text.count("~") > 1:
            return "ERROR: MULTIPLE DEFAULTS"

        formatted = OptionalFormatter(text)

        if formatted.options == {} or formatted.title not in self.dictionary.keys():
            return self.recurse(formatted.default)

        option = self.dictionary[formatted.title]
        if option in formatted.options:
            return self.recurse(formatted.options[option])

        if formatted.default == "":
            return "ERROR: NO DEFAULT VALUE FOUND"
        return self.recurse(formatted.default)

    def recurse(self, text):
        # To recurse over formatted text, e.g: squares nested within an optional
        # Note that nesting one optional block inside another is not implemented
        formatter = TextFormatter(text, self.dictionary)
        formatter.format_text()
        return formatter.output_text


class OptionalFormatter:
    def __init__(self, text):
        self.title = ""                     # In a csv file, this will be the column name
        self.options = {}                   # In the csv file, this should be the possible values under 'title'
        self.default = ""                   # When we cannot find an optional value to return

        self.pos = 0                        # Initial position
        self.text = text.strip()            # To remove leading/trailing whitespace from the input text
        self.init_title()                   # Gets the column name to search the record for
        self.init_options()                 # Gets the list of possible options from 'text'
        self.init_default()                 # Gets the default value if present

    def init_title(self):
        # Gets the column name to search the record for
        if "#" in self.text or "~" in self.text:
            self.title = self.get_until("?#~").strip()
            return
        self.title = ""  # There shouldn't be a title if there are no options and defaults

    def init_options(self):
        # Gets the possible options from the text provided
        if "#" not in self.text:
            self.options = {}
            return
        while "#" in self.text[self.pos:]:
            self.pos += 1
            text = self.get_until("?#~").split("\n")
            key = text[0] # value after the '#' part
            values = "\n".join(text[1:])    # Any data following the #
            self.options[key] = values.strip()

        self.pos -= 1  # Does this to get the '~' if there is a default

    def init_default(self):
        # Gets the default value from the input text if it is present
        if "~" in self.text:  # There may not always be a default
            self.pos += 1
            if "~" in self.text[self.pos]:
                self.pos += 1
            self.default = self.text[self.pos:]

    def get_until(self, delims):
        # Gets the text until it hits one of the characters in delims
        # Pointer stays on delimiter in this version
        text = ""

        while self.pos < len(self.text) and self.text[self.pos] not in delims:
            text += self.text[self.pos]
            self.pos += 1

        return text
