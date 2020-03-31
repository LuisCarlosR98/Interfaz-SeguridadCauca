from model import calendar_methods as cl
class Person:
    def __init__(self,name):
        self.name=name
        self.h_diurns=0.0
        self.h_nocturns=0.0
        self.h_Fdiurns=0.0
        self.h_Fnocturns=0.0

    #metodos
    #suma o resta de horas
    def add_H_diunrs(self, hr,cod):
        if cod == 1:
            self.h_diurns = cl.add_hour(self.h_diurns,hr,0)
        else:
            self.h_diurns = cl.add_hour(self.h_diurns,hr,1)
        print(self.h_diurns," :ope: ",hr," :: ",self.h_diurns)

    def add_H_nocturns(self, hr, cod):
        if cod == 1:
            self.h_nocturns = cl.add_hour(self.h_nocturns,hr,0)
        else:
            self.h_nocturns = cl.add_hour(self.h_nocturns,hr,1)
        print(self.h_nocturns," :ope: ",hr," :: ",self.h_nocturns)

    def add_H_Fdiunrs(self, hr, cod):
        print("horitas: "+hr)
        if cod == 1:
            self.h_diurns = cl.add_hour(self.h_diurns,hr,0)
        else:
            self.h_diurns = cl.add_hour(self.h_diurns,hr,1)

    def add_H_Fnocturns(self, hr, cod):
        if cod == 1:
            self.h_diurns = cl.add_hour(self.h_diurns,hr,0)
        else:
            self.h_diurns = cl.add_hour(self.h_diurns,hr,1)
