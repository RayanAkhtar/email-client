import csv
import pandas as pd


class SpreadsheetFile:
    def __init__(self):
        self.headers = []
        self.records = []                   # A list of records to loop through
        self.curr_row = 0                   # Keeping track of the users current row


def read_csv_file(filename):
    # Reads a csv file and returns a SpreadsheetFile
    spreadsheet_file = SpreadsheetFile()
    with open(filename, 'r') as file:
        for row in csv.reader(file):
            if spreadsheet_file.curr_row == 0:
                spreadsheet_file.headers = row
                spreadsheet_file.curr_row += 1
                continue

            record = {}
            headers = spreadsheet_file.headers

            for i in range(len(headers)):
                if headers[i] == '':
                    continue
                if row[i] == '':
                    record[headers[i]] = None
                else:
                    record[headers[i]] = row[i]

            spreadsheet_file.records.append(record)
            spreadsheet_file.curr_row += 1
    return spreadsheet_file


def read_xlsx_file(file):

    # Reads an xlsx file and returns a SpreadsheetFile
    spreadsheet_file = SpreadsheetFile()
    df = pd.read_excel(file)

    records = df.values
    spreadsheet_file.headers = df.keys().values
    headers = spreadsheet_file.headers

    diff_format = all_nans(headers)  # If the user does not start at A1 in the spreadsheet

    if diff_format:
        records = remove_fake_nans(records)
        headers = records[0]

    for row in records:

        record = {}
        for i in range(len(headers)):
            val = row[i]
            if pd.isna(val):
                record[headers[i]] = None
            else:
                if isinstance(val, float):
                    val = int(val)
                record[headers[i]] = str(val)

        spreadsheet_file.records.append(record)
    if diff_format:
        spreadsheet_file.records = spreadsheet_file.records[1:]
    return spreadsheet_file


def remove_fake_nans(records):
    # Removes rows and columns that are all NaN
    fixed_records_rows = []
    # first remove redundant rows
    for record in records:
        for val in record:
            if not pd.isna(val):
                fixed_records_rows.append(record)
                break

    # Then remove redundant columns
    headers = []
    for val in fixed_records_rows[0]:
        headers.append(not pd.isna(val))  # contains true if not NaN

    fixed_records = []
    for row in fixed_records_rows:
        record = []
        i = 0
        for val in row:
            if headers[i]:
                record.append(val)
            i += 1
        fixed_records.append(record)

    return fixed_records


def all_nans(record):
    # Returns true if there are no undefined values in the record provided
    for val in record:
        if 'Unnamed:' in val: # This appears when reading xlsx files as opposed to nothing in a csv file
            return True
    return False
