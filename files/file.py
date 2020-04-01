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
        dataframe.to_csv (path+'.csv', index = False)
        return True
    except Exception as e:
        return "Error: "+str(e)

def set_file_extension(path,oldExtension,newExtension):
    if oldExtension in path:
        newPath = path.replace(oldExtension,newExtension)
        return newPath
    else:
        return False

def write_dataframe(path,wb,columns,rows,values):
    try:
        index=0
        for value in values:
            wb.values[rows[index]][columns[index]]=value
            index=index+1
        print(wb.values)
        #Cambio de ruta
        newPath = set_file_extension(path,"xlsx","csv")
        wb.to_csv(newPath,index=False)
        return True
    except Exception as e:
        #print(str(e))
        return "Error: "+str(e)


def create_dataFrame(data):
    try:
        return pd.DataFrame(data)
    except Exception as e:
        return "Error: "+str(e)
