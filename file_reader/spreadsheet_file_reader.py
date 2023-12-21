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
                spreadsheet_file.curr_row += 1
                continue
            record = {}
            for i in range(len(headers)):
                if row[i] == '':
                    record[headers[i]] = None
                else:
                    record[headers[i]] = row[i]
            spreadsheet_file.records.append(record)
            spreadsheet_file.curr_row += 1
    return spreadsheet_file

def read_xlsx_file(file):
    spreadsheet_file = SpreadsheetFile()
    df = pd.read_excel(file)
    headers = df.keys().values
    records = df.values

    for row in records:
        record = {}
        for i in range(len(headers)):
            val = row[i]
            if pd.isna(val):
                record[headers[i]] = None
            else:
                if isinstance(val, float):
                    val = str(int(val))
                record[headers[i]] = val

        spreadsheet_file.records.append(record)
    return spreadsheet_file
