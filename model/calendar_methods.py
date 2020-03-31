import locale
locale.setlocale(locale.LC_ALL,"es_CO.UTF-8")
import calendar as cl
import holidays as hl
from datetime import datetime
import datetime as dt

#devuelve 1 si es festivo o 0 si no es festivo
def is_holiday(day_in,month):
    co_holidays = hl.CO(years=2020)
    for day in co_holidays.items():
        str_day= day[0].strftime("%d-%m-%Y")[0:2]
        str_month = day[0].strftime("%d-%m-%Y")[3:5]
        if (day_in==str_day and month==str_month):
            return True
    return False



def limit_hour(hours_date):
    hours = float(hours_date[0:2])
    minuts = float(hours_date[3:5])
    presicion = 0
    #controla la presicion en los minutos
    if minuts >= 15:
        hours += 1
    if minuts >= 15 and minuts < 30:
        presicion = 0.45
    if minuts >= 30 and minuts < 45:
        presicion = 0.30
    if minuts == 45:
        presicion = 0.15
    #obtiene el limite de horas mas la presicion
    if hours >= 6 and hours < 21:
        return (21-hours)+presicion
    else:
        if hours < 6:
            return (6-hours)+presicion
        else:
            return (24-hours+6)+presicion

def is_end_month(day,month,year):
    #regresa true si un año es bisiesto
    if cl.isleap(int(year)):
        if day == "29" and month == "02":
            return True
    else:
        if day == "28" and month == "02":
            return True
    if day == "30":
        if month == "04" or month =="06" or month =="09" or month =="11":
            return True
    if day == "31":
        if month == "01" or month =="03" or month =="05" or month =="07" or month =="08" or month =="10" or month =="12":
            return True
    return False

def index_cad(cad, palabra):
    indice = 0
    while indice < len(palabra):
        if palabra[indice] == cad:
            return indice
        indice += 1
    return -1

def sum_minuts(min1,min2):
    if min1+min2 < 60:
        res = "0."+str((min1 + min2))
        return float(res)
    else:
        res = "1."+str((min1 + min2)-60)
        return float(res)

def res_minuts(min1,min2):
    if min1 - min2 >= 0:
        res = "0."+str((min1 - min2))
        return float(res)
    else:
        res = "1."+str((min1 - min2)+60)
        return float(res)

#cod = 0 SUMA cod = 1 RESTA
def add_hour(hour1,hour2,cod):
    index = index_cad(".",str(hour1))
    hr1_hr = int(str(hour1)[:index])
    hr1_mt = int(str(hour1)[index+1:])
    index = index_cad(".",str(hour2))
    hr2_hr = int(str(hour2)[:index])
    hr2_mt = int(str(hour2)[index+1:])

    hour = 0
    minuts = 0

    #suma hora1 + hora2
    if cod==0:
        print(hour1," :suma: ",hour2)
        #sumamos los minutos
        min=sum_minuts(hr1_mt,hr2_mt)
        return (hr1_hr + hr2_hr) + min
    #resta hora1-hora2
    else:
        print(hour1," :resta: ",hour2)
        if hour1==0.0:
            return -hour2
        if hour1<0:
            return -(add_hour(-hour1,hour2,0))
        #restamos los minutos
        hr = (hr1_hr-hr2_hr)
        res = res_minuts(hr1_mt,hr2_mt)

        if res < 1.0:
            return (hr1_hr-hr2_hr) + res
        else:
            aux = str(int((hr1_hr-hr2_hr)-1.0))+str(res)[1:]
            return float(aux)

hr1= 10.45
lm = 4.15
print(add_hour(hr1,lm,0))



def add_day(day):
    day_aux = int(day)
    day_aux += 1
    if day<"09":
        return "0"+str(day_aux)
    return str(day_aux)

def add_month(month):
    if month == "12":
        return "01"
    month_aux = int(month)
    month_aux += 1
    if month<"09":
        return "0"+str(month_aux)
    return str(month_aux)

def is_change_day(hours,hours_date):
    aux = int(hours_date[0:2])
    if(hours+aux>24):
        return True
    return False
