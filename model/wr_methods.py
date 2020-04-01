from model import calendar_methods as cl
from model import person as prs
from model import aux_methods as aux_m

def exist_name(namGuard,persons):
    for person in persons:
        if(person.name==namGuard):
            return person
    return False

def add_hours(person,hours,cod,day,month,hour_date,year):
    limit = cl.limit_hour(hour_date)
    #sale del metodo cuando no haya horas para sumar
    if(hours<=0):
        return 0
    if aux_m.is_diurnal(hour_date):
        if cl.is_holiday(day,month,year):
            if(hours<=limit):
                person.add_H_Fdiunrs(hours,cod)
                return 0
            person.add_H_Fdiunrs(limit,cod)
        else:
            if(hours<=limit):
                person.add_H_diunrs(hours,cod)
                return 0
            person.add_H_diunrs(limit,cod)
        return add_hours(person,cl.add_hour(hours,limit,1),cod,day,month,"21:00",year)
    else:
        hour_new="06:00"
        if cl.is_holiday(day,month,year):
            if hours <= limit:
                person.add_H_Fnocturns(hours,cod)
                return 0
            person.add_H_Fnocturns(limit,cod)
        else:
            if hours < limit:
                person.add_H_nocturns(hours,cod)
                return 0
            person.add_H_nocturns(limit,cod)

        if cl.is_change_day(hours,hour_date):
            if cl.is_end_month(day,month,year):
                day = "01"
                month = cl.add_month(month)
            else:
                day = cl.add_day(day)
            hour_new = "00:00"

        hour_date = hour_new

        return add_hours(person,cl.add_hour(hours,limit,1),cod,day,month,hour_date,year)

def generate_hours(novelties):
    persons = list()
    for novelty in novelties:
        cod_nov = novelty.getNov_cod()
        #Novedad con un solo actor
        if cod_nov == 0:
            person = exist_name(novelty.GuardCausa,persons)
            if not person:
                person = prs.Person(novelty.GuardCausa)
            add_hours(person,novelty.Horas,1,novelty.getDia(),novelty.getMonth(),novelty.getHour_Date(),novelty.getYear())
            persons.append(person)

        #Novedad con dos actores
        if cod_nov == 1:
            #actor que resta horas
            person = exist_name(novelty.GuardCausa,persons)
            if not person:
                person = prs.Person(novelty.GuardCausa)
            add_hours(person,novelty.Horas,0,novelty.getDia(),novelty.getMonth(),novelty.getHour_Date(),novelty.getYear())
            persons.append(person)

            #actor que suma
            person = exist_name(novelty.GuardCubre,persons)
            if not person:
                person = prs.Person(novelty.GuardCubre)
            add_hours(person,novelty.Horas,1,novelty.getDia(),novelty.getMonth(),novelty.getHour_Date(),novelty.getYear())
            persons.append(person)

    return persons
