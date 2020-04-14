from model import calendar_methods as cl
from model import person as prs
from model import aux_methods as aux_m

def exist_name(namGuard,persons):
    for person in persons:
        if(person.name==namGuard):
            return person
    return False

def add_person(person,persons):
    index = 0
    while index < len(persons):
        if persons[index].name == person.name:
            persons[index]=person
            return 0
        index = index + 1
    persons.append(person)


def add_hours(person,hours,cod,day,month,hour_date,year):
    limit = cl.limit_hour(hour_date)
    #sale del metodo cuando no haya horas para sumar
    if(hours<=0):
        return 0
    if aux_m.is_diurnal(hour_date):
        if cl.is_holiday(day,month,year):
            print(limit,hour_date)
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

        if cl.is_change_day(hour_date):
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
        cod_nov = novelty.get_nov_cod()
        #Novedad con un solo actor
        if cod_nov == 0:
            person = exist_name(novelty.GuardCausa,persons)
            if not person:
                person = prs.Person(novelty.GuardCausa)
            add_hours(person,novelty.Horas,1,novelty.get_day_start(),novelty.get_month_start(),novelty.get_hour_date(),novelty.get_year_start())
            add_person(person,persons)

        #Novedad con dos actores
        if cod_nov == 1:
            #actor que resta horas
            person = exist_name(novelty.GuardCausa,persons)
            if not person:
                person = prs.Person(novelty.GuardCausa)
            add_hours(person,novelty.Horas,0,novelty.get_day_start(),novelty.get_month_start(),novelty.get_hour_date(),novelty.get_year_start())
            add_person(person,persons)

            #actor que suma
            person = exist_name(novelty.GuardCubre,persons)
            if not person:
                person = prs.Person(novelty.GuardCubre)
            add_hours(person,novelty.Horas,1,novelty.get_day_start(),novelty.get_month_end(),novelty.get_hour_date(),novelty.get_year_start())
            add_person(person,persons)

    return persons

def final_data(dataframe):
    data = {'Nombre':[],
        'H DIU-Positivas':[],
        'H NOC-Positivas':[],
        'FES DIU-Positivas':[],
        'FES NOC-Positivas':[],
        '--':[],
        'H DIU-Negativas':[],
        'H NOC-Negativas':[],
        'FES DIU-Negativas':[],
        'FES NOC-Negativas':[]}
    names = dataframe.get("Nombre")
    data['Nombre']=names
    index=0
    for name in names:
        data['H DIU-Positivas'].append(str("%.2f"%dataframe.values[index][1]).replace(".",":") if dataframe.values[index][1]>0.0 else "00:00")
        data['H NOC-Positivas'].append(str("%.2f"%dataframe.values[index][2]).replace(".",":") if dataframe.values[index][2]>0.0 else "00:00")
        data['FES DIU-Positivas'].append(str("%.2f"%dataframe.values[index][3]).replace(".",":") if dataframe.values[index][3]>0.0 else "00:00")
        data['FES NOC-Positivas'].append(str("%.2f"%dataframe.values[index][4]).replace(".",":") if dataframe.values[index][4]>0.0 else "00:00")
        data['--'].append("--")
        data['H DIU-Negativas'].append(str("%.2f"%dataframe.values[index][1]).replace(".",":").replace("-","") if dataframe.values[index][1]<0.0 else "00:00")
        data['H NOC-Negativas'].append(str("%.2f"%dataframe.values[index][2]).replace(".",":").replace("-","") if dataframe.values[index][2]<0.0 else "00:00")
        data['FES DIU-Negativas'].append(str("%.2f"%dataframe.values[index][3]).replace(".",":").replace("-","") if dataframe.values[index][3]<0.0 else "00:00")
        data['FES NOC-Negativas'].append(str("%.2f"%dataframe.values[index][4]).replace(".",":").replace("-","") if dataframe.values[index][4]<0.0 else "00:00")
        index = index + 1

    return data

def add_novs_turns(result,names,days,novelty):
    nam_index = aux_m.name_index(names,novelty.GuardCausa)
    day_index = aux_m.day_index(days,novelty.get_day_start())
    nam_index2 = -1
    cod = novelty.get_nov_cod()
    if cod == 1:
        nam_index2 = aux_m.name_index(names,novelty.GuardCubre)
    if cod == 0:
        nam_index2 = -2
    if nam_index < 0 and nam_index2==-1:
        return False

    index = 0
    var_days = int(novelty.get_day_end())-int(novelty.get_day_start())

    while index <= var_days:
        result['rows'].append(nam_index)
        result['columns'].append(day_index)
        result['data'].append(novelty.get_nov_str())
        if cod == 1:
            result['rows'].append(nam_index2)
            result['columns'].append(day_index)
            result['data'].append("C-"+novelty.get_nov_str())
        day_index = day_index+1
        index = index + 1
    return True

def generate_file_turns(dataframe,novelties):
    result = {'columns':[],'rows':[],'data':[]}
    names = dataframe.get("ADMINISTRATIVOS").tolist()
    days = dataframe.columns.tolist()
    for novelty in novelties:
        add_novs_turns(result,names,days,novelty)
    return result
