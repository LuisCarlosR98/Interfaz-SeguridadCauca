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
    novelty = novelty.lower()
    if(novelty=="ausencia"):
        return [1,"AU"]
    if(novelty=="tiempo extra"):
        return [0,"TE"]
    if(novelty=="incapacidad"):
        return [1,"IC"]
    if(novelty=="salida antes"):
        return [1,"SA"]

def is_diurnal(hour):
    if hour >= "06:00" and hour < "21:00":
        return True
    return False
