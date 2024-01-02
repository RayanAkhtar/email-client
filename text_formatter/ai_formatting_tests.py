import unittest

from win32com.servers import dictionary

from text_formatter.text_formatting import TextFormatter


class MyTestCase(unittest.TestCase):
    ########################            TESTING AI-GENERATED TEXT FORMATTING            ########################

    def test_ai_simple(self):
        # Tests that the AI-Text generator actually works
        print("Testing ai simple:")
        dummy_text = "{Tell me a fun fact about programming}"
        dictionary = {}
        formatter = TextFormatter(dummy_text, dictionary)
        formatter.format_text()
        print(formatter.output_text)
        print()

    def test_ai_chained(self):
        # Tests that output is chained properly
        # This should not show the original text, only the reversed to be correct
        print("Testing ai chained")
        dummy_test = "{Tell me a fun fact about programming; reverse the text}"
        dictionary = {}
        formatter = TextFormatter(dummy_test, dictionary)
        formatter.format_text()
        print(formatter.output_text)
        self.assertNotIn("Fun Fact", formatter.output_text)
        print()


    def test_ai_with_file(self):
        # This test checks to see that the file is actually provided into the ai prompt
        print("Testing ai with file")
        dummy_text = "{Print out the following test: [hw.txt]}"
        dictionary = {}
        formatter = TextFormatter(dummy_text, dictionary)
        formatter.format_text()
        print(formatter.output_text)
        self.assertIn("Hello World", formatter.output_text)
        print()

    def test_multiple_ai_in_file(self):
        # This test checks to see that we can run multiple prompts in a single string
        print("Testing multiple ai in file")
        dummy_text = "{Tell me a fun fact about the python programming language}\n"
        dummy_text += "{Tell my a fun fact about the java programming language}\n"
        dummy_text += "{Now return the value 'hello world'}"

        formatter = TextFormatter(dummy_text, dictionary)
        formatter.format_text()
        print(formatter.output_text)
        print()


if __name__ == '__main__':
    unittest.main()
