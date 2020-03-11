from views.principal import WINDOW
from model.model import MODEL
from tkinter import messagebox

#clase controlador
class CONTROLLER:
    #constructor de la clase controlador
    def __init__(self):
        self.window = WINDOW(self)
        self.res
    #Metodo principal del controlador, para conectar vista y modelo
    def ExecuteProcess(self,path1,sheetName1,path2,sheetName2,path):
        self.model = MODEL(path1,path2)
        self.res = self.model.WriteSolution(sheetName1,sheetName2,path)
        return self.res
