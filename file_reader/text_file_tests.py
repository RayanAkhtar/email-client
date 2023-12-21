import unittest
import text_file_reader as tfr

test_file_single = "text_files/word_test_file"
test_file_multiple = "text_files/word_test_multiple"
test_file_multiple_space = "text_files/word_test_multiple_space"
test_file_large = "text_files/word_test_file_large"

class MyTestCase(unittest.TestCase):

    ######################################   .TXT TEST CASES   ######################################
    def test_read_txt_single_line(self):
        text = tfr.read_txt_file(test_file_single + ".txt")
        result = "Hello, my name is [name]. I am [age] years old and I am currently doing a project in [project]"
        self.assertEqual(result, text)

    def test_read_txt_multiple_lines(self):
        text = tfr.read_txt_file(test_file_multiple + ".txt")
        result = """Hello, my name is [name]
I am [age] years old
I am doing a project in [project]"""
        self.assertEqual(result, text)

    def test_read_txt_multiple_lines_with_space(self):
        text = tfr.read_txt_file(test_file_multiple_space + ".txt")
        result = """Hello, my name is [name].

I am [age] years old.


I am currently doing a project in [project]."""
        self.assertEqual(result, text)

    def test_read_txt_large(self):
        text = tfr.read_txt_file(test_file_large + ".txt")
        result = "reached the end properly" in text
        self.assertEqual(True, result)

        ######################################   .PDF TEST CASES   ######################################

    def test_read_pdf_single_line(self):
        text = tfr.read_pdf_file(test_file_single + ".pdf").strip()
        result = "Hello, my name is [name]. I am [age] years old and I am currently doing a project in [project]"
        self.assertEqual(result, text)

    def test_read_pdf_multiple_lines(self):
        text = tfr.read_pdf_file(test_file_multiple + ".pdf").strip()
        result = "Hello, my name is [name]  \nI am [age] years old  \nI am doing a project in [project]"
        self.assertEqual(text, result)

    def test_read_pdf_multiple_lines_with_space(self):
        text = tfr.read_pdf_file(test_file_multiple_space + ".pdf").strip()
        result = "Hello, my name is [name].  \n \nI am [age] years old.  \n \n \nI am currently doing a project in [project]."
        self.assertEqual(result, text)

    def test_read_pdf_large(self):
        text = tfr.read_pdf_file(test_file_large + ".pdf")
        result = "reached the end properly" in text
        self.assertEqual(True, result)



                ######################################   .DOCX TEST CASES   ######################################

    def test_read_docx_single_line(self):
        text = tfr.read_docx_file(test_file_single + ".docx").strip()
        result = "Hello, my name is [name]. I am [age] years old and I am currently doing a project in [project]"
        self.assertEqual(result, text)

    def test_read_docx_multiple_lines(self):
        text = tfr.read_docx_file(test_file_multiple + ".docx").strip()
        result = "Hello, my name is [name]  \nI am [age] years old  \nI am doing a project in [project]"
        self.assertEqual(text, result)

    def test_read_docx_multiple_lines_with_space(self):
        text = tfr.read_docx_file(test_file_multiple_space + ".docx").strip()
        result = "Hello, my name is [name].  \n \nI am [age] years old.  \n \n \nI am currently doing a project in [project]."
        self.assertEqual(result, text)

    def test_read_docx_large(self):
        text = tfr.read_docx_file(test_file_large + ".docx")
        result = "reached the end properly" in text
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
