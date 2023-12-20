

delimiters = "{}[]?"


class TextFormatter:

    def __init__(self, input_text, files, dictionary):
        self.input_text = input_text
        self.files = files
        self.output_text = []
        self.pos = 0
        self.dictionary = dictionary

    def format_text(self):
        while self.pos < len(self.input_text):
            char = self.input_text[self.pos]
            self.pos += 1
            if char in delimiters:
                if char == '[':
                    text = self.get_until(']')
                    self.output_text.append(self.square_format(text))
                elif char == '{':
                    text = self.get_until('}')
                    self.output_text.append(self.curly_format(text))
                elif char == '?':
                    text = self.get_until('?')
                    self.output_text.append(self.optional_format(text))
                else:
                    print("Invalid character in delimiter set")
                    exit(-1)
            else:
                self.output_text.append(char)

    def get_until(self, delimiter):
        text = ""
        while self.input_text[self.pos] != delimiter:
            text += self.input_text[self.pos]
            self.pos += 1
            if self.pos == len(self.input_text):
                print(f"No delimiter found: {delimiter}")
                exit(-1)
        return text

    def square_format(self, text):
        if '.' in text:
            #todo get file data
            return
        if ':' in text:
            pos_to_split = text.index(":")
            key = text[:pos_to_split]
            default = text[pos_to_split + 1:]
            if self.dictionary[key] is not None:
                return self.dictionary[key]
            else:
                return default
        else:
            if (self.dictionary[text]) is not None:
                return self.dictionary[text]
            else:
                return "ERROR"

    def curly_format(self, text):
        #todo
        return

    def optional_format(self, text):
        #todo
        return
