import unittest

from text_formatter.text_formatting import TextFormatter


class MyTestCase(unittest.TestCase):

    ########################            TESTING STRICT TEXT FORMATTING            ########################
    def test_simple_square(self):
        dummy_text = "Hello [Greeting]"
        formatter = TextFormatter(dummy_text, [], {"Greeting": "World"})
        formatter.format_text()
        self.assertEqual("Hello World", formatter.output_text)

    def test_simple_square_multiple_formats(self):
        dummy_text = "[Greeting 1] [Greeting 2]"
        dictionary = {
            "Greeting 1": "Hello",
            "Greeting 2": "World"
        }

        formatter = TextFormatter(dummy_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("Hello World", formatter.output_text)

    def test_multiple_square_lines(self):
        dummy_text = """[Greeting]
            My name is [Name]
            This is my [Project Name] project"""
        dictionary = {
            "Greeting": "Hello World",
            "Name": "Rayan",
            "Project Name": "text formatting"
        }

        formatter = TextFormatter(dummy_text, [], dictionary)
        formatter.format_text()

        self.assertEqual(
            """Hello World
            My name is Rayan
            This is my text formatting project""",
            formatter.output_text
        )

    def test_square_default_values(self):
        dummy_text = "The next word should be Blank: [Word:Blank]"
        dictionary = {}
        formatter = TextFormatter(dummy_text, [], dictionary)
        formatter.format_text()
        self.assertEqual("The next word should be Blank: Blank", formatter.output_text)

    def test_square_no_default_available(self):
        dummy_text = "The next word should be ERROR: [Word]"
        dictionary = {}
        formatter = TextFormatter(dummy_text, [], dictionary)
        formatter.format_text()
        self.assertEqual("The next word should be ERROR: ERROR: NO OPTION MATCH AND NO DEFAULT VALUE", formatter.output_text)

    def test_file(self):
        return  # todo waiting on file reading

    def test_multiple_files(self):
        return  # todo waiting on file reading

    def test_different_types_files(self):
        return  # todo waiting on file reading

    ########################            TESTING OPTIONAL TEXT FORMATTING            ########################

    def test_no_options(self):
        input_text = """? no options to search

        ?"""

        formatter = TextFormatter(input_text, [], {})
        formatter.format_text()

        self.assertEqual("", formatter.output_text)

    def test_only_default(self):
        input_text = """? no options to search
        ~This is the default
        ?"""

        formatter = TextFormatter(input_text, [], {})
        formatter.format_text()

        self.assertEqual("This is the default", formatter.output_text)

    def test_single_option_wo_default_success(self):
        input_text = """? 1 option to search
        #SUCCESS
        This should be the answer
        ~This is the default
        ?"""

        dictionary = {"1 option to search":"SUCCESS"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("This should be the answer", formatter.output_text)

    def test_single_option_wo_default_fail(self):
        input_text = """? 1 option to search
        #SUCCESS
        This should not be the answer and should instead print "ERROR: NO OPTION MATCH AND NO DEFAULT VALUE"
        ?"""

        dictionary = {"1 option to search":"FAIL"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("ERROR: NO OPTION MATCH AND NO DEFAULT VALUE", formatter.output_text)

    def test_single_option_with_default(self):
        input_text = """? 1 option to search
        #SUCCESS
        This should not be the answer
        ~This is the default and should be the answer
        ?"""

        dictionary = {"1 option to search":"FAIL"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("This is the default and should be the answer", formatter.output_text)

    def test_multiple_options_with_default_opt_1(self):
        input_text = """? 3 options to search
        #SUCCESS 1
        This should be the answer
        #SUCCESS 2
        This should not be the answer
        #SUCCESS 3
        This should not be the answer
        ~This is the default and should not be the answer
        ?"""

        dictionary = {"3 options to search":"SUCCESS 1"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("This should be the answer", formatter.output_text)

    def test_multiple_options_with_default_opt_2(self):
        input_text = """? 3 options to search
        #SUCCESS 1
        This should not be the answer
        #SUCCESS 2
        This should be the answer
        #SUCCESS 3
        This should not be the answer
        ~This is the default and should not be the answer
        ?"""

        dictionary = {"3 options to search":"SUCCESS 2"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("This should be the answer", formatter.output_text)

    def test_multiple_options_with_default_opt_3(self):
        input_text = """? 3 options to search
        #SUCCESS 1
        This should not be the answer
        #SUCCESS 2
        This should not be the answer
        #SUCCESS 3
        This should be the answer
        ~This is the default and should not be the answer
        ?"""

        dictionary = {"3 options to search":"SUCCESS 3"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("This should be the answer", formatter.output_text)

    def test_multiple_options_with_default_fail(self):
        input_text = """? 3 options to search
        #SUCCESS 1
        This should not be the answer
        #SUCCESS 2
        This should not be the answer
        #SUCCESS 3
        This should not be the answer
        ~This is the default and should be the answer
        ?"""

        dictionary = {"3 options to search":"SUCCESS 4"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("This is the default and should be the answer", formatter.output_text)


    def test_multiple_options_wo_default_opt_1(self):
        input_text = """? 3 options to search
        #SUCCESS 1
        This should be the answer
        #SUCCESS 2
        This should not be the answer
        #SUCCESS 3
        This should not be the answer
        ?"""

        dictionary = {"3 options to search":"SUCCESS 1"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("This should be the answer", formatter.output_text)

    def test_multiple_options_wo_default_opt_2(self):
        input_text = """? 3 options to search
        #SUCCESS 1
        This should not be the answer
        #SUCCESS 2
        This should be the answer
        #SUCCESS 3
        This should not be the answer
        ?"""

        dictionary = {"3 options to search":"SUCCESS 2"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("This should be the answer", formatter.output_text)

    def test_multiple_options_wo_default_opt_3(self):
        input_text = """? 3 options to search
        #SUCCESS 1
        This should not be the answer
        #SUCCESS 2
        This should not be the answer
        #SUCCESS 3
        This should be the answer
        ?"""

        dictionary = {"3 options to search":"SUCCESS 3"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("This should be the answer", formatter.output_text)

    def test_multiple_options_wo_default_fail(self):
        input_text = """? 3 options to search
        #SUCCESS 1
        This should not be the answer
        #SUCCESS 2
        This should not be the answer
        #SUCCESS 3
        This should not be the answer
        ?"""

        dictionary = {"3 options to search":"SUCCESS 4"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("ERROR: NO OPTION MATCH AND NO DEFAULT VALUE", formatter.output_text)

    def test_multiple_defaults_no_options(self):
        input_text = """? 3 options to search
        ~ This would have been just fine
        ~ But having this means that the test should fail
        ~ There should not be multiple defaults
        ?"""

        dictionary = {"3 options to search":"SUCCESS 1"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("ERROR: MULTIPLE DEFAULTS", formatter.output_text)

    def test_multiple_defaults_single_options(self):
        input_text = """? 3 options to search
        #SUCCESS 1
        This should not be the answer
        ~ This would have been just fine
        ~ But having this means that the test should fail
        ~ There should not be multiple defaults
        ?"""

        dictionary = {"3 options to search":"SUCCESS 1"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("ERROR: MULTIPLE DEFAULTS", formatter.output_text)

    def test_multiple_defaults_multiple_options(self):
        input_text = """? 3 options to search
        #SUCCESS 1
        This should not be the answer
        #SUCCESS 2
        This should not be the answer
        #SUCCESS 3
        This should not be the answer
        ~ This would have been just fine
        ~ But having this means that the test should fail
        ~ There should not be multiple defaults
        ?"""

        dictionary = {"3 options to search":"SUCCESS 1"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("ERROR: MULTIPLE DEFAULTS", formatter.output_text)




    ########################            TESTING NON-AI MIXED TEXT FORMATTING            ########################


    def test_multiple_options_with_squares(self):
        dummy_text = """Hello [planet]
        ? paragraph to choose 
        #p1
        This should output my name: [name]
        #p2
        This should output my project: [project]
        ~This should contain none of my data
        ?"""

        dictionary = {"planet": "World", "paragraph to choose": "p1", "name":"Rayan"}

        formatter = TextFormatter(dummy_text, [], dictionary)
        formatter.format_text()

        result = """Hello World
        This should output my name: Rayan"""

        self.assertEqual(result, formatter.output_text)




    def test_multiple_options_with_squares_multi_line(self):
        dummy_text = """Hello [planet]
        ? paragraph to choose 
        #p1
        This should output my name: [name]
        This should then output my project: [project]
        #p2
        This should output my project: [project]
        ~This should contain none of my data
        ?"""

        dictionary = {"planet": "World", "paragraph to choose": "p1", "name":"Rayan", "project":"email client"}

        formatter = TextFormatter(dummy_text, [], dictionary)
        formatter.format_text()

        result = """Hello World
        This should output my name: Rayan
        This should then output my project: email client"""

        self.assertEqual(result, formatter.output_text)


    ########################            TESTING AI-GENERATED TEXT FORMATTING            ########################

    # todo: Will implement tests upon completion of the ai part





if __name__ == '__main__':
    unittest.main()
