import pandas as pd
from openpyxl import *

#Descriptor [wb].[values]=>matriz de [fila][columna]
def read_file(path,sheetname):
    try:
        wb = pd.read_excel(path,sheetname)
        return wb
    except Exception as e:
        return "Error: "+str(e)

def write_file_dataframe(path,sheetname,dataframe):
    try:
        print(path)
        dataframe.to_csv (path+'.csv', index = False)
        return True
    except Exception as e:
        return "Error: "+str(e)

def write_cell(path,sheetName,columns,rows,values):
    try:
        wb = load_workbook(path)
        sheet = wb[sheetName]
        i=0
        for element in values:
            sheet.cell(row = rows[i],column = columns[i]). value = element
            i=+1
        wb.save(path)
        return True
    except Exception as e:
        return "Error: "+str(e)

def create_dataFrame(data):
    try:
        return pd.DataFrame(data)
    except Exception as e:
        return "Error: "+str(e)
