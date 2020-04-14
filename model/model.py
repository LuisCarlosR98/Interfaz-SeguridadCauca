from files import file as fl
from model import aux_methods as aux_m
from model import novelty
from model import wr_methods as wr
import numpy as np
from views import errors as err

#clase modelo principal
class Model:
    #constructor clase modelo
    #atributos:(ruta de archivo1, ruta de archivo2)
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2
        self.novelties = list()

    #metodo de lectura archivo de novedades
    #atributos:(nombre de la hoja)
    def read_visitrack(self,sheetName):
        try:
            #Cargar informacion relevante del archivo novedades de Visitack
            wb = fl.read_file(self.path1,sheetName)
            i=0
            while i < len(wb.values):
                obj_nov = novelty.Novelty(wb.get("Guard_Causa").tolist()[i],wb.get("Guard_Cubre").tolist()[i],aux_m.rls_novelty(wb.get("Novedad").tolist()[i]),float(wb.get("Tiempo").tolist()[i]),wb.get("F&H_Inicio_Novedad").tolist()[i],wb.get("F&H_Fin_Novedad").tolist()[i])
                self.novelties.append(obj_nov)
                i+=1
            return True
        except Exception as e:
            err.load_error(str(e)+"modelo: Read VISITRACK")
            return False


    #metodo de lectura del archivo de turnos
    def read_turns(self,sheetName):
        try:
            wb = fl.read_file(self.path2,sheetName)
            return wb
        except Exception as e:
            err.load_error(str(e)+"modelos write TURNS: metodo[read_turns]")
            return False

    #parametros:(nombre de la hoja)
    def write_turns(self,sheetName):
        """try:"""
        #Cargar la informacion del archivo turnos
        dataframe = self.read_turns(sheetName)
        #diccionario con los datos y las posiciones de las horas_novedades
        dic = wr.generate_file_turns(dataframe,self.novelties)
        columns = dic['columns']
        rows = dic['rows']
        data = dic['data']
        fl.write_dataframe(self.path2,dataframe,columns,rows,data)
        #retornar la respuesta
        return True
        """except Exception as e:
            err.load_error(str(e)+" _En la clase modelo write TURNS: metodo[write_turns]")
            return False"""

    #Metodo que llena el archivo con las horas extras
    def write_hours(self,path):
        try:
            #crear diccionario de datos
            data = {'Nombre':[],'H DIU':[],'H NOC':[],'FES DIU':[],'FES NOC':[]}
            #crear lista de objetos persona
            persons = wr.generate_hours(self.novelties)
            #cargar el diccionario con la informacion recibida
            for person in persons:
                data["Nombre"].append(person.name)
                data["H DIU"].append(person.h_diurns)
                data["H NOC"].append(person.h_nocturns)
                data["FES DIU"].append(person.h_Fdiurns)
                data["FES NOC"].append(person.h_Fnocturns)
            #Generar el dataframe para las horas extras
            wb = fl.create_dataFrame(data)
            data2 = wr.final_data(wb)
            wb2 = fl.create_dataFrame(data2)
            #guarda el dataframe en formato excel
            return fl.write_file_dataframe(path,"horas_novedades",wb2)

        except Exception as e:
            err.load_error(str(e)+"modelos: write Hours")
            return None


    #metodo de escritura sobre el archivo de resultados
    #parametos:(hoja archivo1, hoja archivo2)
    def write_solution(self,sheetName1,sheetName2,path):
        #leer el archivo de Visitrac
        res = self.read_visitrack(sheetName1)
        if res:
            #escribir las novedades en el archivo de turnos
            res = self.write_turns(sheetName2)
            if res:
                #generar el nuevo data frame de calculo de horas
                res = self.write_hours(path)
                #retornar true si la operacion fue exitosa y false si no lo fue
                return res
            return res
        return res
