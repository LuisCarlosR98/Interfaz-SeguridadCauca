#importar la libreria de lectura de archivos xlsx
import xlrd
#importar la libreria de vectores
import numpy as np

class reader:
    #leer una columna del archivo: parametros(numero de columna,ruta del archivo, nombre de la hoja)
    def read_column(num_column,file_path,sheet_name):
        #Abrir el archivo
        openFile = xlrd.open_workbook(file_path)
        #Abrir la hoja
        sheet = openFile.sheet_by_name(sheet_name)
        #vector de elementos
        elements=[]
        for i in range(sheet.nrows):
            elements.append(sheet.cell_value(num_column,i))

        data=np.array(elements)
        return data

    #leer una fila
    def read_row(num_row,file_path,sheet_name):
        #Abrir el archivo
        openFile = xlrd.open_workbook(file_path)
        #Abrir la hoja
        sheet = openFile.sheet_by_name(sheet_name)
        #vector de elementos
        elements=[]
        for i in range(sheet.ncolumns):
            elements.append(sheet.cell_value(i,num_row))

        data=np.array(elements)
        return data
