import locale
locale.setlocale(locale.LC_ALL,"es_CO.UTF-8")
import calendar as cl
import holidays as hl
from datetime import datetime

#devuelve 1 si es festivo o 0 si no es festivo
def value_holiday(day_in,month):
    co_holidays = hl.CO(years=2020)
    for day in co_holidays.items():
        str_day= day[0].strftime("%d-%m-%Y")[0:2]
        str_month = day[0].strftime("%d-%m-%Y")[3:5]
        if (day_in==str_day and month==str_month):
            return 1
    return 0
