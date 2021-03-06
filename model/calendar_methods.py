import locale
locale.setlocale(locale.LC_ALL,"es_CO.UTF-8")
import calendar as cl
import holidays as hl
from datetime import datetime

#devuelve 1 si es festivo o 0 si no es festivo
# Parametros: (dia String,mes String)
def is_holiday(day_in,month,year):
    str_date = month+"-"+day_in+"-"+year
    date_wk = datetime.strptime(str_date,'%m-%d-%Y')
    if (date_wk.weekday() == 6):
        return True
    co_holidays = hl.CO(years=int(year))
    for day in co_holidays.items():
        str_day= day[0].strftime("%d-%m-%Y")[0:2]
        str_month = day[0].strftime("%d-%m-%Y")[3:5]
        if (day_in==str_day and month==str_month):
            return True
    return False

#limite de horas: diurnas, nocturnas, segun la hora de llegada
def limit_hour(hours_date):
    hours = float(hours_date[0:2])
    minuts = float(hours_date[3:5])
    presicion = 0
    hours_aux = hours
    #controla la presicion en los minutos
    if minuts >= 15:
        hours_aux = hours + 1
    if minuts >= 15 and minuts < 30:
        presicion = 0.45
    if minuts >= 30 and minuts < 45:
        presicion = 0.30
    if minuts == 45:
        presicion = 0.15
    #obtiene el limite de horas mas la presicion
    if hours >= 6 and hours < 21:
        return (21-hours_aux)+presicion
    else:
        if hours >= 21:
            return (24-hours_aux)+presicion
        if hours >= 0 and hours < 6:
            return (6-hours_aux)+presicion


#si hay cambio de mes
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

#indice, de una palabra dentro de una cadena
def index_cad(cad, palabra):
    indice = 0
    while indice < len(palabra):
        if palabra[indice] == cad:
            return indice
        indice += 1
    return -1

#cod = 0 SUMA cod = 1 RESTA
def add_hour(hour1,hour2,cod):
    index = index_cad(".",str(hour1))
    hr1_hr = int(str(hour1)[:index])
    hr1_mt = int(str(hour1)[index+1:]) if int(str(hour1)[index+1:])>9 else int(str(hour1)[index+1:])*10
    index = index_cad(".",str(hour2))
    hr2_hr = int(str(hour2)[:index])
    hr2_mt = int(str(hour2)[index+1:]) if int(str(hour2)[index+1:])>9 else int(str(hour2)[index+1:])*10
    hour = 0
    minuts = 0

    #suma hora1 + hora2
    if cod==0:
        if hour1<0:
            if hour1+hour2>0:
                 return add_hour(hour2,(-hour1),1)
            else:
                minuts = hr1_mt-hr2_mt if hr1_mt>=hr2_mt else (hr1_mt+60)-hr2_mt
                hour = hr1_hr+hr2_hr if hr1_mt>=hr2_mt else (hr1_hr+1)+hr2_hr
                return float(str(hour)+'.'+str(minuts)) if float(str(hour)+'.'+str(minuts))<=0 else float('-'+str(hour)+'.'+str(minuts))

        minuts = hr1_mt+hr2_mt if (hr1_mt+hr2_mt)/60<1 else (hr1_mt+hr2_mt)%60
        hour = hr1_hr+hr2_hr if (hr1_mt+hr2_mt)/60<1 else hr1_hr+hr2_hr+1
        return float(str(hour)+"."+str(minuts))
    #resta hora1-hora2
    else:
        if hour1<0:
            return -(add_hour(-hour1,hour2,0))
        if hour1<hour2:
            return -add_hour(hour2,hour1,1)

        minuts = hr1_mt-hr2_mt if hr1_mt>=hr2_mt else (hr1_mt+60)-hr2_mt
        hour = hr1_hr-hr2_hr if hr1_mt>=hr2_mt else hr1_hr-hr2_hr-1
        print(hour1,'-',hour2,'=',str(hour)+'.'+str(minuts))
        return float(str(hour)+'.'+str(minuts))

#avanzar un dia
def add_day(day):
    day_aux = int(day)
    day_aux += 1
    if day<"09":
        return "0"+str(day_aux)
    return str(day_aux)

#avanzar un mes
def add_month(month):
    if month == "12":
        return "01"
    month_aux = int(month)
    month_aux += 1
    if month<"09":
        return "0"+str(month_aux)
    return str(month_aux)

#si hay cambio de dia
def is_change_day(hours_date):
    if(hours_date>="21:00"):
        return True
    return False
