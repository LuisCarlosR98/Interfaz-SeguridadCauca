#clase novedad, para mejor manejo de las novedades
class Novelty:
    def __init__(self,Guard_Causa,Guard_Cubre,Novedad,Horas,FechaRegistro,FechaFin):
        self.GuardCausa = Guard_Causa
        self.GuardCubre = Guard_Cubre
        self.Novedad = Novedad
        self.Horas = Horas
        self.FechaRegistro = FechaRegistro
        self.FechaFin = FechaFin

#obtener los datos de fecha inicio
    def get_day_start(self):
        return self.FechaRegistro[8:10]

    def get_month_start(self):
        return  self.FechaRegistro[5:7]

    def get_year_start(self):
        return self.FechaRegistro[0:4]

    def get_hour_date(self):
        return self.FechaRegistro[11:16]

#obtener los datos de fecha inicio
    def get_day_end(self):
        return self.FechaFin[8:10]

    def get_month_end(self):
        return  self.FechaFin[5:7]

    def get_year_end(self):
        return self.FechaFin[0:4]


#obtener los datos de la novedad
    def get_nov_str(self):
        return self.Novedad[1]

    def get_nov_cod(self):
        return self.Novedad[0]

#modificar el dia de la novedad
    def setDay(self,day):
        new_date = self.FechaRegistro[0:8]
        new_date = new_date + day
        new_date = new_date + self.FechaRegistro[10:19]
        self.FechaRegistro = new_date

#modificar las horas de la novedad
    def setHours(hours):
        self.Horas = hours
