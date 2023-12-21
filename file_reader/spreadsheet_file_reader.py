import csv
import pandas as pd

# Might need to refer to this later
# Installing collected packages: pytz, tzdata, six, numpy, python-dateutil, pandas
#  WARNING: The script f2py.exe is installed in 'C:\Users\rayan\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts' which is not on PATH.
#  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
#


# TODO:
#       csv file reading
#       xlsx file reading

class SpreadsheetFile:
    def __init__(self):
        self.records = []                   # A list of records to loop through
        self.curr_row = 0                   # Keeping track of the users current row


def read_csv_file(filename):
    spreadsheet_file = SpreadsheetFile()
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if spreadsheet_file.curr_row == 0:
                headers = row
                continue
            record = {}
            for i in range(len(headers)):
                record[headers[i]] = row[i]
            spreadsheet_file.records.append(record)
    return spreadsheet_file

def read_xlsx_file(file):
    df = pd.read_excel(file)
    print(df)