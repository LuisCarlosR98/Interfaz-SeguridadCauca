from views.principal import Window
from model.model import Model
from tkinter import messagebox

#clase controlador
class Controller:
    #constructor de la clase controlador
    def __init__(self):
        self.window = Window(self)
        self.res

    #Metodo principal del controlador, para conectar vista y modelo
    def execute_process(self,path1,sheetName1,path2,sheetName2,path_solution):
        self.model = Model(path1,path2)
        self.res = self.model.write_solution(sheetName1,sheetName2,path_solution)
        return self.res
