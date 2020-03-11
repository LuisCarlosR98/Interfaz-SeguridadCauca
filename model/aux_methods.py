#metodos auxiliares
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
    array = np.array(dataframe.columns.tolist())
    try:
        index = array.tolist().index(day)
    except:
        index = -1

    return index+1

def rls_novelty(novelty):
    if(novelty=="Ausencia"):
        return [1,"AU"]
    if(novelty=="Tiempo Extra"):
        return [2,"TE"]
    if(novelty=="Permiso"):
        return [3,"PE"]
    if(novelty=="Salida antes"):
        return [4,"SA"]

def rls_hours(day,hour,cod_nov):
    hours=['0','0','0','0']
    if(hour[0:2]<"18" and cod_nov==1):
        print("diurnas y ausencia")
    if(hour[0:2]<"18" and cod_nov==2):
        print("diurnas y tiempo extra")
    if(hour[0:2]<"18" and cod_nov==3):
        print("diurnas y Permiso pri")
    if(hour[0:2]<"18" and cod_nov==4):
        print("diurnas y Salida antes")

    if(hour[0:2]>"18"):
        print("nocturnas")
    return hours

hr = rls_hours('18','17:30',3)
print (hr)
