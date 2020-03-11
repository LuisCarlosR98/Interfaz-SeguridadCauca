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

def write_cell(path,sheetName,row,col,value):
    wb = load_workbook(path)
    sheet = wb[sheetName]
    sheet.cell(row = row,column = col, value = value)
    wb.save(filename=path)

def create_DataFrame(columns):
    return pd.DataFrame(columns=columns)
