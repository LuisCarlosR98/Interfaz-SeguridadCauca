import pandas as pd
from openpyxl import *
from views import errors as err

#Descriptor [wb].[values]=>matriz de [fila][columna]
def read_file(path,sheetname):
    try:
        wb = pd.read_excel(path,sheetname)
        return wb
    except Exception as e:
        err.load_error(str(e)+"read file")
        return None

def write_file_dataframe(path,sheetname,dataframe):
    try:
        dataframe.to_csv (path+'.csv', index = False)
        return True
    except Exception as e:
        err.load_error(str(e)+"write files")
        return False

def set_file_extension(path,oldExtension,newExtension):
    if oldExtension in path:
        newPath = path.replace(oldExtension,newExtension)
        return newPath
    else:
        return None

def write_dataframe(path,wb,columns,rows,values):
    try:
        index=0
        for value in values:
            wb.values[rows[index]][columns[index]]=value
            index=index+1
        #Cambio de ruta
        newPath = set_file_extension(path,"xlsx","csv")
        wb.to_csv(newPath,index=False)
        return True
    except Exception as e:
        err.load_error(str(e)+"write data files")
        return False


def create_dataFrame(data):
    try:
        return pd.DataFrame(data)
    except Exception as e:
        err.load_error(str(e)+"create data files")
        return None
