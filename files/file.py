import pandas as pd
from openpyxl import *
from tkinter import *
from tkinter import filedialog

#Descriptor [wb].[values]=>matriz de [fila][columna]
def read_file(path,sheetname):
    wb = pd.read_excel(path,sheetname)
    return wb

def write_file_dataframe(path,sheetname,dataframe):
    dataframe.to_excel(path,sheetname,columns=None,index=False,engine='openpyxl')

def write_cell(path,sheetName,columns,rows,values):
    wb = load_workbook(path)
    sheet = wb[sheetName]
    i=0
    for element in values:
        sheet.cell(row = rows[i],column = columns[i]). value = element
        i=+1
    wb.save(path)

def create_DataFrame(columns):
    return pd.DataFrame(columns=columns)
