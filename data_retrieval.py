import pandas as pd
import xlrd
import csv
from datetime import datetime
from data_cleaner import clean_csv


"""
\\\\\\
Purpose: To extract data from excel file into csv format.
Return:  CSV file name that contains the excel data. 
\\\\\\
"""
def csv_from_excel(file):
    file_name = file[:file.__len__()-5]
    #wb = xlrd.open_workbook('112320Discourse_Analysis_TSA_Manuscript.xlsx')
    wb = xlrd.open_workbook(file)
    #sh = wb.sheet_by_name('1')
    #your_csv_file = open(file_csv , 'w')
    #wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    data_files = []
    for sheet in wb.sheets():
        now = datetime.now()
        timestamp = "{0}-{1}-{2} {3}".format(now.year, now.month, now.day, now.strftime("%H:%M:%S"))
        file_csv = file_name + '_Sheet_{0}_{1}'.format(sheet.name, timestamp) + '.csv'
        your_csv_file = open(file_csv, 'w')
        data_files.append(file_csv)
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
        for rownum in range(sheet.nrows):
            wr.writerow(sheet.row_values(rownum))
        your_csv_file.close()

    return data_files

def dataframe_from_csv(files):
    frames = []
    for file in files[1:]: # first sheet contains no data
        squeaky_clean = clean_csv(file)
        frames.append(squeaky_clean)
    return frames

def retrieve_df_list(file):
    input_file = '112320Discourse_Analysis_TSA_Manuscript.xlsx'
    if file == "default":
        file = input_file
    data_file = csv_from_excel(file)
    df_list = dataframe_from_csv(data_file)

    return df_list

# runs the csv_from_excel function:
if __name__ == '__main__':
    file = '112320Discourse_Analysis_TSA_Manuscript.xlsx'

    data_file = csv_from_excel(file)
    df_list = dataframe_from_csv(data_file)
    print("done")