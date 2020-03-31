#metodos auxiliares
import numpy as np
#encuentra el nombre en el archivo de turnos
def name_index(dataframe,nombre):
    index=0
    for element in dataframe.values:
        if(element[0]==nombre):
            break
        index+=1

    if index>=len(dataframe.values):
        index = -1

    return index+2

def day_index(dataframe,day):
    v_array = np.array(dataframe.columns.tolist())
    try:
        index = v_array.tolist().index(day)
        return index+1
    except:
        index = -1
        return index

def rls_novelty(novelty):
    if(novelty=="Ausencia"):
        return [1,"AU"]
    if(novelty=="Tiempo Extra"):
        return [0,"TE"]
    if(novelty=="Incapacidad"):
        return [1,"IC"]
    if(novelty=="Salida antes"):
        return [1,"SA"]

def is_diurnal(hour):
    if hour >= "06:00" and hour < "21:00":
        return True
    return False
