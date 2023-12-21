import unittest

from text_formatter.text_formatting import TextFormatter


class MyTestCase(unittest.TestCase):

    ########################            TESTING STRICT TEXT FORMATTING            ########################

    def test_simple_square(self):
        # A single check to see that strict replacement is working correctly
        dummy_text = "Hello [Greeting]"
        formatter = TextFormatter(dummy_text, [], {"Greeting": "World"})
        formatter.format_text()
        self.assertEqual("Hello World", formatter.output_text)

    def test_simple_square_multiple_formats(self):
        # A check to see that you can have multiple strict replacements
        dummy_text = "[Greeting 1] [Greeting 2]"
        dictionary = {
            "Greeting 1": "Hello",
            "Greeting 2": "World"
        }

        formatter = TextFormatter(dummy_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("Hello World", formatter.output_text)

    def test_multiple_square_lines(self):
        # A check to see that strict replacement can happen across all multiple lines
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
        # A check to see that you can have default values in strict replacement
        dummy_text = "The next word should be Blank: [Word:Blank]"
        dictionary = {}
        formatter = TextFormatter(dummy_text, [], dictionary)
        formatter.format_text()
        self.assertEqual("The next word should be Blank: Blank", formatter.output_text)

    def test_square_no_default_available(self):
        # A check to see that ERROR will be returned when formatting without a key and default value
        dummy_text = "The next word should be ERROR: [Word]"
        dictionary = {}
        formatter = TextFormatter(dummy_text, [], dictionary)
        formatter.format_text()
        result = "The next word should be ERROR: ERROR: NO OPTION MATCH AND NO DEFAULT VALUE"
        self.assertEqual(result, formatter.output_text)

    def test_file(self):
        return  # todo waiting on file reading

    def test_multiple_files(self):
        return  # todo waiting on file reading

    def test_different_types_files(self):
        return  # todo waiting on file reading

    ########################            TESTING OPTIONAL TEXT FORMATTING            ########################

    def test_no_options(self):
        # A check to skip any option sets that do not have options and defaults
        input_text = """? no options to search

        ?"""

        formatter = TextFormatter(input_text, [], {})
        formatter.format_text()

        self.assertEqual("", formatter.output_text)

    def test_only_default(self):
        # A check to see that default is returned when there are no options
        input_text = """? no options to search
        ~This is the default
        ?"""

        formatter = TextFormatter(input_text, [], {})
        formatter.format_text()

        self.assertEqual("This is the default", formatter.output_text)

    def test_single_option_wo_default_success(self):
        # A cehck to see that options are being selected properly
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
        # A check to see a fail as there is no default in the event of no options being available
        input_text = """? 1 option to search
        #SUCCESS
        This should not be the answer and should instead print "ERROR: NO OPTION MATCH AND NO DEFAULT VALUE"
        ?"""

        dictionary = {"1 option to search":"FAIL"}

        formatter = TextFormatter(input_text, [], dictionary)
        formatter.format_text()

        self.assertEqual("ERROR: NO OPTION MATCH AND NO DEFAULT VALUE", formatter.output_text)

    def test_single_option_with_default(self):
        # A check to see that the default will be selected when no options can be selected
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
        # Checks to see that option 1 is output correctly when in a multi-line block of options with a default
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
        # Checks to see that option 2 is output correctly when in a multi-line block of options with a default
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
        # Checks to see that option 3 is output correctly when in a multi-line block of options with a default
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
        # Checks to see that the default is output correctly when in a multi-line block of options with a default
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
        # Checks to see that option 1 is output correctly when in a multi-line block of options without a default
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
        # Checks to see that option 2 is output correctly when in a multi-line block of options without a default
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
        # Checks to see that option 3 is output correctly when in a multi-line block of options without a default
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
        # Checks to see that an error is output when in a multi-line block of options without a default and where
        # there are no options selected
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
        # A test that should return an error since you shouldn't have multiple defaults
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
        # Same as above, a value shouldn't be selected if there are multiple defaults
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
        # Same as above, except with multiple options
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
        # Tests to see that both strict and optional replacement work correctly together
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
        # Tests to see that optional and strict formatting work across multiple lines
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
