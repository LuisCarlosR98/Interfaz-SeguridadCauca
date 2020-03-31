#clase novedad, para mejor manejo de las novedades
class Novelty:
    def __init__(self,Guard_Causa,Guard_Cubre,Novedad,Horas,FechaRegistro):
        self.GuardCausa = Guard_Causa
        self.GuardCubre = Guard_Cubre
        self.Novedad = Novedad
        self.Horas = Horas
        self.FechaRegistro = FechaRegistro

    def getDia(self):
        return self.FechaRegistro[8:10]

    def getMonth(self):
        return  self.FechaRegistro[5:7]

    def getYear(self):
        return self.FechaRegistro[0:4]

    def getNov_str(self):
        return self.Novedad[1]

    def getNov_cod(self):
        return self.Novedad[0]

    def getHour_Date(self):
        return self.FechaRegistro[11:16]



    def setDay(self,day):
        new_date = self.FechaRegistro[0:8]
        new_date = new_date + day
        new_date = new_date + self.FechaRegistro[10:19]
        self.FechaRegistro = new_date

    def setHours(hours):
        self.Horas = hours
