#metodos auxiliares
import numpy as np

#encuentra el nombre en el archivo de turnos
def name_index(nombres,nombre):
    try:
        index=nombres.index(nombre)
        return index
    except:
        return -1

def day_index(columns,day):
    try:
        index=columns.index(int(day))
        return index
    except:
        return -1

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
