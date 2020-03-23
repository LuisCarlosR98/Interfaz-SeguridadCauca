#clase novedad, para mejor manejo de las novedades
class Novelty:
    def __init__(self,Guard_Causa,Guard_Cubre,Novedad,Horas,FechaRegistro):
        self.GuardCausa = Guard_Causa
        self.GuardCubre = Guard_Cubre
        self.Novedad = Novedad
        self.Horas = Horas
        self.FechaRegistro = FechaRegistro

    def getDia(self):
        if(self.FechaRegistro[8:9]=="0"):
            print(self.FechaRegistro[9:10])
            return self.FechaRegistro[9:10]
        return self.FechaRegistro[8:10]

    def getMonth(self):
        return  self.FechaRegistro[6:8]

    def getNov_str(self):
        return self.Novedad[1]

    def getNov_cod(self):
        return self.Novedad[0]

    def getHour_Date(self):
        return self.FechaRegistro[11:13]



novs = list()
nov1 = Novelty("g1","g2","NO",3,"fecha1")
novs.append(nov1)
nov1 = Novelty("g2","g3","NO",4,"fecha2")
novs.append(nov1)
nov1 = Novelty("g3","g1","NO",5,"fecha3")
novs.append(nov1)
nov1 = Novelty("g2","g3","NO",6,"fecha4")
novs.append(nov1)
