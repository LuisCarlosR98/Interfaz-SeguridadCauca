from model import calendar_methods as cl


def value_diurnal(hour):
    if(hour>"21" or hour<"06"):
        return 0
    return 1

def index_name(name,collection):
  try:
    i=0
    for element in collection:
        if(element[0]==name):
            return i
        i=+1
    return -1
  except:
    return -1

def index_type_hour(hour_date,day_date):
    val_diurnal = value_diurnal(hour_date)
    val_holiday = cl.value_holiday(day_date)
    if(value_diurnal == 0 and value_holiday == 0):
        return 2
    if(value_diurnal == 0 and value_holiday == 1):
        return 4
    if(value_diurnal == 1 and value_holiday == 0):
        return 1
    if(value_diurnal == 1 and value_holiday == 1):
        return 3

def dif_hora(hour_date):
    if (value_diurnal(hour_date)==1):
        return 21 - hour_date
    if (value_diurnal(hour_date)==0):
        if hour_date==24:
            hour_date=0
        if hour_date>=0 and hour_date<6:
            return 6 - hour_date
        if hour_date>21 and hour_date<24:
            return 30 - hour_date

def sum_hours(cod_op,hours,hour_date,day):
    result = [0,0,""]
    return result

#----------------------------------------------///////--------------------------------//////------------------------

#metodo final
def updateElement(cod_op,hours,day,hour_date,element):
    while hours > 0:
        #sacar numero de horas y Tipo
        index = index_type_hour(hour_date,day)
        #verificar si hay cambio de tipo de hora
        #regresa un vector[contador,horas_restantes,dia_actual]
        data_hours = sum_hours(cod_op,hours,hour_date,day)
        #actualizar los parametros
        hours = data_hours[1]
        day = data_hours[2]
        #agregar la hora en el campo correspondiente
        element[index]=+data_hours[0]





def updateLine(name,cod_op,hours,hour_date,day,collection,line):
    index = index_name(name,collection)
    if(index == -1):
        line[0] = name
        #editar linea
        updateElement(cod_op,hours,day,hour_date,line)
        #agregar linea
        collection.append(element)
    else:
        line = collection[index]
        #editar linea
        updateElement(cod_op,hours,day,hour_date,line)
        #regresar linea
        collection[index]=line

def updateNovelty(novelty,collection,element,cod_nov,cod_per):
    #0: resta, 1:suma
    if cod_per==0:#una persona
        updateLine(novelty.GuarCausa,1,novelty.Hours,novelty.getDia(),novelty.getHour_Date(),collection,element)
    if cod_per==1:#dos personas
        if cod_nov != 3:
            updateLine(novelty.GuarCausa,0,novelty.Hours,novelty.getDia(),novelty.getHour_Date(),collection,element)
        updateLine(novelty.GuarCubre,1,novelty.Hours,novelty.getDia(),novelty.getHour_Date(),collection,element)





def generateElements(novelties):
    res = list()
    element = ["",0,0,0,0]
    for novelty in novelties:
        #verifica codigo de novedad
        cod_nov = novelty.getNov_cod()
        if(cod_nov==1):
            #dos nombres: Ausencia
            cod_per=1
        if(cod_nov==2):
            #un nombre: Tiempo extra
            cod_per=0
        if(cod_nov==3):
            #dos nombres: permiso
            cod_per=0
        if(cod_nov==4):
            #dos nombres: Salida antes
            cod_per=1
