from files import file as fl
from model import aux_methods as aux_m
from model import novelty
from model import wr_methods as wr
import numpy as np

#clase modelo principal
class MODEL:
    #constructor clase modelo
    #atributos:(ruta de archivo1, ruta de archivo2)
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2
        self.novelties = list()

    #metodo de lectura archivo de novedades
    #atributos:(nombre de la hoja)
    def ReadVisitrack(self,sheetName):
        #Cargar informacion relevante del archivo novedades de Visitack
        wb = fl.read_file(self.path1,sheetName)

        i=0
        while i < len(wb.values):
            obj_nov = novelty.Novelty(wb.get("Guard_Causa").tolist()[i],wb.get("Guard_Cubre").tolist()[i],aux_m.rls_novelty(wb.get("Novedad").tolist()[i]),float(wb.get("Variación del turno").tolist()[i]),wb.get("Creado en").tolist()[i])
            self.novelties.append(obj_nov)
            i+=1

    #metodo de lectura del archivo de turnos
    #parametros:(nombre de la hoja)
    def WriteTurns(self,sheetName):
        #Cargar la informacion del archivo turnos
        wb = fl.read_file(self.path2,sheetName)
        #listas de datos
        ls_columns = list()
        ls_rows = list()
        ls_data = list()
        #modificar el data frame
        i=0
        while i < len(self.novelties):
            nam_index = aux_m.name_index(wb,self.novelties[i].GuardCausa)
            day_index = aux_m.day_index(wb,self.novelties[i].getDia())
            if(nam_index or day_index) >= 0:
                ls_rows.append(nam_index)
                ls_columns.append(day_index)
                ls_data.append(self.novelties[i].getNov_str())

            i+=1
            
        fl.write_cell(self.path2,sheetName,ls_columns,ls_rows,ls_data)

        #retornar la respuesta

    #Metodo que llena el archivo con las horas extras
    def WriteHours(self,path):
        #Generar el dataframe para las horas extras
        wb = fl.create_DataFrame(('Nombre','H DIU','H NOC','FES DIU','FES NOC'))
        #Generar el archivo excel a partir del dataframe
        fl.write_file_dataframe(path+".xlsx","HORAS_NOVEDADES",wb)
        wb = fl.read_file(path+".xlsx","HORAS_NOVEDADES")
        values_act = wr.generateElements(self.novelties)


    #metodo de escritura sobre el archivo de resultados
    #parametos:(hoja archivo1, hoja archivo2)
    def WriteSolution(self,sheetName1,sheetName2,path):
        #leer el archivo de Visitrac
        self.ReadVisitrack(sheetName1)
        #escribir las novedades en el archivo de turnos
        self.WriteTurns(sheetName2)
        #generar el nuevo data frame de calculo de horas
        #self.WriteHours(path)
        #retornar true si la operacion fue exitosa y false si no lo fue
        return True
