
class TextFormatter:

    def __init__(self, input_text, files, dictionary):
        self.input_text = input_text
        self.files = files
        self.output_text = []
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
                    self.output_text.append(self.square_format(text))
                elif char == '{':
                    text = self.get_until("}")
                    self.output_text.append(self.curly_format(text))
                elif char == '?':
                    text = self.get_until("?")
                    self.output_text.append(self.optional_format(text))
                else:
                    print("Invalid character in delimiter set")
                    exit(-1)
            else:
                self.output_text.append(char)

    def get_until(self, delims):  # Pointer goes past delimiter
        text = ""
        while self.input_text[self.pos] not in delims:
            text += self.input_text[self.pos]
            self.pos += 1
            if self.pos == len(self.input_text):
                print(f"No delimiter found: {delims}")
                exit(-1)
        self.pos += 1
        return text

    def square_format(self, text):
        if '.' in text:
            file_data = ""  # todo waiting on completion of file_reader to read file text
            return file_data

        default = "ERROR"
        key = text

        if ":" in text:
            pos_to_split = text.index(":")
            key = text[:pos_to_split]
            default = text[pos_to_split + 1:]

        result = self.dictionary[key]
        if result is None:
            return default
        return result

    def curly_format(self, text):
        # todo later in ai-text part
        return

    def optional_format(self, text):
        formatted = OptionalFormatter(text)

        option = self.dictionary[formatted.title]

        if option in formatted.options:
            return formatted.options[option]

        return formatted.default


class OptionalFormatter:
    def __init__(self, text):
        self.title = ""
        self.options = []
        self.default = ""

        self.pos = 0
        self.text = text.strip()  # to remove leading/trailing whitespace
        self.init_title()
        self.init_options()
        self.init_default()

    def init_title(self):
        self.title = self.get_until("?#~").split()

    def init_options(self):
        while self.text[self.pos:] != "~":
            text = self.get_until("?#~")
            self.options += text.split()

    def init_default(self):
        if "~" in self.text:
            default = self.get_until("~")
            self.default = default.split()

    def get_until(self, delims):  # Pointer stays on delimiter
        text = ""
        while self.text[self.pos] not in delims:
            text += self.text[self.pos]
            self.pos += 1
            if self.pos == len(self.text):
                print(f"No delimiter found: {delims}")
                exit(-1)
        return text
