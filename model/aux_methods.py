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
        return [2,"TE"]
    if(novelty=="Permiso"):
        return [3,"PE"]
    if(novelty=="Salida antes"):
        return [4,"SA"]
