from files import file as fl
import aux_methods as aux_m
import numpy as np

#clase modelo principal
class MODEL:
    #constructor clase modelo
    #atributos:(ruta de archivo1, ruta de archivo2)
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2

    #metodo de lectura archivo de novedades
    #atributos:(nombre de la hoja)
    def ReadVisitrack(self,sheetName):
        #Cargar informacion relevante del archivo novedades de Visitack
        wb = fl.read_file(self.path1,sheetName)
        data = [wb.get("Guard_Causa"),wb.get("Guard_Cubre"),wb.get("Novedad"),wb.get("Variación del turno"),wb.get("Creado en")]
        #retorna una matriz
        return data

    #metodo de lectura del archivo de turnos
    #parametros:(nombre de la hoja)
    def WriteTurns(self,sheetName,elements):
        #Cargar la informacion del archivo turnos
        wb = fl.read_file(self.path2,sheetName)
        #modificar el data frame
        i=0
        while i < len(elements[0].tolist()):
            nam_index = aux_m.name_index(wb,elements[0][i])
            day_index = aux_m.day_index(wb,elements[4][i][8:10])
            if(nam_index or day_index)>=0):
                #registro de novedades en turnos
                fl.write_cell(self.path2,sheetName,nam_index,day_index,aux_m.rls_novelty(elements[2][i])[1])
            i+=1
        #retornar la respuesta
        return True

    #Metodo que llena el archivo con las horas extras
    def WriteHours(self,path):
        #Generar el dataframe para las horas extras
        wb = fl.create_DataFrame(('Nombre','H DIU','H NOC','FES DIU','FES NOC'))
        fl.write_file_dataframe(path+".xlsx","HORAS",wb)


    #metodo de escritura sobre el archivo de resultados
    #parametos:(hoja archivo1, hoja archivo2)
    def WriteSolution(self,sheetName1,sheetName2,path):
        #leer el archivo de Visitrac
        elements = self.ReadVisitrack(sheetName1)
        print(elements)
        #escribir las novedades en el archivo de turnos
        self.WriteTurns(sheetName2,elements)
        #generar el nuevo data frame de calculo de horas
        self.WriteHours(path)
        #retornar true si la operacion fue exitosa y false si no lo fue
        return True
