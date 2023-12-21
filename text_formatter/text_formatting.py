class TextFormatter:

    def __init__(self, input_text, files, dictionary):
        self.input_text = input_text
        self.files = files
        self.output_text = ""
        self.pos = 0
        self.dictionary = dictionary  # A record to pass into the formatter
        self.delimiters = "{}[]?"

    def format_text(self):
        while self.pos < len(self.input_text):
            char = self.input_text[self.pos]
            self.pos += 1
            if char in self.delimiters:
                if char == '[':
                    text = self.get_until("]")
                    self.output_text += (self.square_format(text))
                elif char == '{':
                    text = self.get_until("}")
                    self.output_text += (self.curly_format(text))
                elif char == '?':
                    text = self.get_until("?")
                    self.output_text += (self.optional_format(text))
                else:
                    print("Invalid character in delimiter set")
                    exit(-1)
            else:
                self.output_text += char

    def get_until(self, delims):  # Pointer goes past delimiter in this version
        text = ""
        while self.input_text[self.pos] not in delims:
            text += self.input_text[self.pos]
            self.pos += 1
            if self.pos >= len(self.input_text):
                print(f"No delimiter found: {delims}")
                exit(-1)
        self.pos += 1
        return text

    def square_format(self, text):
        if '.' in text:
            file_data = ""  # todo waiting on completion of file_reader to read file text
            return file_data

        default = "ERROR: NO OPTION MATCH AND NO DEFAULT VALUE"
        key = text

        if ":" in text:
            pos_to_split = text.index(":")
            key = text[:pos_to_split]
            default = text[pos_to_split + 1:]

        if key not in self.dictionary.keys():
            return default
        result = self.dictionary[key]
        return result

    def curly_format(self, text):
        # todo later in ai-text part
        return

    def optional_format(self, text):
        if text.count("~") > 1:
            return "ERROR: MULTIPLE DEFAULTS"

        formatted = OptionalFormatter(text)

        if formatted.options == {} or formatted.title not in self.dictionary.keys():
            return self.recurse(formatted.default)

        option = self.dictionary[formatted.title]
        if option in formatted.options:
            return self.recurse(formatted.options[option])

        if formatted.default == "":
            return "ERROR: NO OPTION MATCH AND NO DEFAULT VALUE"
        return self.recurse(formatted.default)


    def recurse(self, text):
        formatter = TextFormatter(text, self.files, self.dictionary)
        formatter.format_text()
        return formatter.output_text


class OptionalFormatter:
    def __init__(self, text):
        self.title = ""
        self.options = {}
        self.default = ""

        self.pos = 0
        self.text = text.strip()  # to remove leading/trailing whitespace
        self.init_title()
        self.init_options()
        self.init_default()

    def init_title(self):
        if "#" in self.text or "~" in self.text:
            self.title = self.get_until("?#~").strip()
            return
        self.title = ""

    def init_options(self):
        if "#" not in self.text:
            self.options = {}
            return
        while "#" in self.text[self.pos:]:
            self.pos += 1
            text = self.get_until("?#~").split("\n")
            key = text[0]
            values = "\n".join(text[1:])
            self.options[key] = values.strip()

        self.pos -= 1  # Does this to get the '~' if there is a default

    def init_default(self):
        if "~" in self.text:  # There may not always be a default
            self.pos += 1
            if "~" in self.text[self.pos]:
                self.pos += 1
            self.default = self.text[self.pos:]

    def get_until(self, delims):  # Pointer stays on delimiter in this version
        text = ""

        while self.pos < len(self.text) and self.text[self.pos] not in delims:
            text += self.text[self.pos]
            self.pos += 1

        return text
