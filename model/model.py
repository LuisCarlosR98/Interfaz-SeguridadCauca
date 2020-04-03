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
                obj_nov = novelty.Novelty(wb.get("Guard_Causa").tolist()[i],wb.get("Guard_Cubre").tolist()[i],aux_m.rls_novelty(wb.get("Novedad").tolist()[i]),float(wb.get("Tiempo").tolist()[i]),wb.get("F&H_Inicio_Novedad").tolist()[i])
                self.novelties.append(obj_nov)
                i+=1
            return True
        except Exception as e:
            err.load_error(str(e)+"modelo: Read VISITRACK")
            return False


    #metodo de lectura del archivo de turnos
    #parametros:(nombre de la hoja)
    def write_turns(self,sheetName):
        try:
            #Cargar la informacion del archivo turnos
            wb = fl.read_file(self.path2,sheetName)
            #listas de datos
            ls_columns = list()
            ls_rows = list()
            ls_data = list()
            #modificar el data frame
            i=0
            while i < len(self.novelties):
                nam_index = aux_m.name_index(wb.get("ADMINISTRATIVOS").tolist(),self.novelties[i].GuardCausa)
                day_index = aux_m.day_index(wb.columns.tolist(),self.novelties[i].getDia())
                if(nam_index >= 0 and day_index >= 0):
                    ls_rows.append(nam_index)
                    ls_columns.append(day_index)
                    ls_data.append(self.novelties[i].getNov_str())

                i+=1
            fl.write_dataframe(self.path2,wb,ls_columns,ls_rows,ls_data)
            #retornar la respuesta
            return True
        except Exception as e:
            err.load_error(str(e)+"modelos write TURNS")
            return False

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
                data["H DIU"].append(str(person.h_diurns).replace(".",":"))
                data["H NOC"].append(str(person.h_nocturns).replace(".",":"))
                data["FES DIU"].append(str(person.h_Fdiurns).replace(".",":"))
                data["FES NOC"].append(str(person.h_Fnocturns).replace(".",":"))
            #Generar el dataframe para las horas extras
            wb = fl.create_dataFrame(data)
            #guarda el dataframe en formato excel
            return fl.write_file_dataframe(path,"horas_novedades",wb)

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
