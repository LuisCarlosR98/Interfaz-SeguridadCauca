from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from views import errors as err

#clase de la interfaz de usuario GUI
class Window:
    #contrustor de la clase WINDOW
    #parametros:(controlador)
    def __init__(self,control):
        self.path1 = ""
        self.path2 = ""
        self.sheet1 = ""
        self.sheet2 = ""
        self.control = control

        ###Window
        window = Tk()
        window.title("Interfaz VISITRACK")
        window.geometry('800x300')
        ###Labels
        lbl_title=(Label(window,text="INTERFAZ (VISITRACK-TURNOS)",font=("Britannic",14))).place(x=200,y=10)
        lbl_file1=(Label(window,text="Seleccione el archivo (visitrack):",font=("Sitka",10))).place(x=10,y=57)
        lbl_file2=(Label(window,text="Seleccione el archivo (turnos):",font=("Sitka",10))).place(x=10,y=127)
        self.lbl_path1=Label(window,text="Ruta del archivo",font=("Corbel",10))
        self.lbl_path1.place(x=180,y=87)
        self.lbl_path2=Label(window,text="Ruta del archivo",font=("Corbel",10))
        self.lbl_path2.place(x=180,y=157)
        lbl_sheet1=(Label(window,text="Nombre de la hoja (libro excel):",font=("Sitka",10))).place(x=350,y=58)
        lbl_sheet2=(Label(window,text="Nombre de la hoja (libro excel):",font=("Sitka",10))).place(x=325,y=127)
        ###Buttons
        btn_path1=(Button(window,text="Explorar (NOVEDADES)",font=("Corbel",10),relief=RAISED,cursor="hand2",command=lambda:self.read_file(1))).place(x=197,y=55)
        btn_path2=(Button(window,text="Explorar (TURNOS)",font=("Corbel",10),relief=RAISED,cursor="hand2",command=lambda:self.read_file(2))).place(x=187,y=125)
        btn_path1=(Button(window,text="REGISTRAR NOVEDADES",font=("Britannic",11),relief=RAISED,cursor="hand2",command=lambda:self.execute_model())).place(x=200,y=197)
        ###Entrys
        self.ent_seet1=Entry(window)
        self.ent_seet1.place(x=536,y=59)
        self.ent_seet2=Entry(window)
        self.ent_seet2.place(x=512,y=129)
        ###mainloop
        window.mainloop()

    def read_file(self,num):
        filename = filedialog.askopenfilename(filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
        if num==1:
            self.path1 = filename
            self.lbl_path1.configure(text="Ruta del archivo: "+self.path1)
            self.lbl_path1.place(x=50,y=87)
        else:
            self.path2 = filename
            self.lbl_path2.configure(text="Ruta del archivo: "+self.path2)
            self.lbl_path2.place(x=50,y=157)

    def execute_model(self):
        file_name = filedialog.asksaveasfilename(filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.control.execute_process(self.path1,self.ent_seet1.get(),self.path2,self.ent_seet2.get(),file_name)
        if self.control.res:
            messagebox.showinfo("Resultado de la operacion","Operacion realizada con exito")
