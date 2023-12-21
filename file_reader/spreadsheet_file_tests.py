import unittest
import spreadsheet_file_reader as sfr

spreadsheet_1 = "spreadsheet_files/excel_test_workbook"
spreadsheet_2 = "spreadsheet_files/excel_test_workbook_2"
spreadsheet_3 = "spreadsheet_files/excel_test_workbook_3"


class MyTestCase(unittest.TestCase):

    # A nicely formatted file is one where columns are contiguous, meaning there are no blank columns between data

    def test_correct_csv(self):
        # Tests a nicely formatted csv file, starting at A0
        spreadsheet_data = sfr.read_csv_file(spreadsheet_1 + ".csv")
        records = [
            {
                "name": "Rayan",
                "age": "19",
                "project": "Email Client"
            },
            {
                "name": "Joe",
                "age": "20",
                "project": "Project A"
            },
            {
                "name": "Smith",
                "age": None,
                "project": "Project B"
            }
        ]
        self.assertEqual(records, spreadsheet_data.records)

    def test_diff_format_csv(self):
        # Tests a nicely formatted csv file that begins at a place other than (A,0)
        spreadsheet_data = sfr.read_csv_file(spreadsheet_2 + ".csv")
        records = [
            {
                "name": "Rayan",
                "age": "19",
                "project": "Email Client"
            },
            {
                "name": "Joe",
                "age": "20",
                "project": "Project A"
            },
            {
                "name": "Smith",
                "age": None,
                "project": "Project B"
            }
        ]
        self.assertEqual(records, spreadsheet_data.records)

    def test_weird_format_csv(self):
        # Tests a csv file that is not nicely formatted, starting at a value other than A0
        spreadsheet_data = sfr.read_csv_file(spreadsheet_3 + ".csv")
        records = [
            {
                "name": "Rayan",
                "age": "19",
                "project": "Email Client"
            },
            {
                "name": "Joe",
                "age": "20",
                "project": "Project A"
            },
            {
                "name": "Smith",
                "age": None,
                "project": "Project B"
            }
        ]

        self.assertEqual(records, spreadsheet_data.records)

    def test_correct_xlsx(self):
        # Tests a nicely formatted xlsx file that starts at A0
        spreadsheet_data = sfr.read_xlsx_file(spreadsheet_1 + ".xlsx")
        records = [
            {
                "name": "Rayan",
                "age": "19",
                "project": "Email Client"
            },
            {
                "name": "Joe",
                "age": "20",
                "project": "Project A"
            },
            {
                "name": "Smith",
                "age": None,
                "project": "Project B"
            }
        ]
        self.assertEqual(records, spreadsheet_data.records)

    def test_diff_format_xlsx(self):
        # Tests a nicely formatted xlsx file that starts somewhere other than A0
        spreadsheet_data = sfr.read_xlsx_file(spreadsheet_2 + ".xlsx")
        records = [
            {
                "name": "Rayan",
                "age": "19",
                "project": "Email Client"
            },
            {
                "name": "Joe",
                "age": "20",
                "project": "Project A"
            },
            {
                "name": "Smith",
                "age": None,
                "project": "Project B"
            }
        ]
        self.assertEqual(records, spreadsheet_data.records)

    def test_weird_format_xlsx(self):
        # Tests an xslx file that is not nicely formatted, starting at a position other than A0.
        spreadsheet_data = sfr.read_xlsx_file(spreadsheet_3 + ".xlsx")
        records = [
            {
                "name": "Rayan",
                "age": "19",
                "project": "Email Client"
            },
            {
                "name": "Joe",
                "age": "20",
                "project": "Project A"
            },
            {
                "name": "Smith",
                "age": None,
                "project": "Project B"
            }
        ]
        self.assertEqual(records, spreadsheet_data.records)


if __name__ == '__main__':
    unittest.main()
