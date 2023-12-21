import unittest
import spreadsheet_file_reader as sfr

spreadsheet_1 = "spreadsheet_files/excel_test_workbook"


class MyTestCase(unittest.TestCase):

    def test_correct_csv(self):
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

    def test_correct_xlsx(self):
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


if __name__ == '__main__':
    unittest.main()
