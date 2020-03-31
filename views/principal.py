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
        lbl_title=(Label(window,text="INTERFAZ (VISITRACK-TURNOS)",font="bold,italic")).place(x=200,y=10)
        lbl_file1=(Label(window,text="Seleccione el archivo (visitrack):")).place(x=10,y=50)
        lbl_file2=(Label(window,text="Seleccione el archivo (turnos):")).place(x=10,y=120)
        self.lbl_path1=Label(window,text="Ruta del archivo")
        self.lbl_path1.place(x=180,y=80)
        self.lbl_path2=Label(window,text="Ruta del archivo")
        self.lbl_path2.place(x=180,y=150)
        lbl_sheet1=(Label(window,text="Nombre de la hoja (libro excel):")).place(x=350,y=50)
        lbl_sheet2=(Label(window,text="Nombre de la hoja (libro excel):")).place(x=325,y=120)
        ###Buttons
        btn_path1=(Button(window,text="Explorar (NOVEDADES)",command=lambda:self.read_file(1))).place(x=190,y=48)
        btn_path2=(Button(window,text="Explorar (TURNOS)",command=lambda:self.read_file(2))).place(x=180,y=118)
        btn_path1=(Button(window,text="REGISTRAR NOVEDADES",font="italic",command=lambda:self.execute_model())).place(x=200,y=190)
        ###Entrys
        self.ent_seet1=Entry(window)
        self.ent_seet1.place(x=525,y=52)
        self.ent_seet2=Entry(window)
        self.ent_seet2.place(x=500,y=122)
        ###mainloop
        window.mainloop()

    def read_file(self,num):
        filename = filedialog.askopenfilename(filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
        if num==1:
            self.path1 = filename
            self.lbl_path1.configure(text="Ruta del archivo: "+self.path1)
            self.lbl_path1.place(x=50,y=80)
        else:
            self.path2 = filename
            self.lbl_path2.configure(text="Ruta del archivo: "+self.path2)
            self.lbl_path2.place(x=50,y=150)

    def execute_model(self):
        if (self.path1 and self.path2)=="":
            if(self.path1 == ""):
                messagebox.showinfo(message=err.e_null_path+"NOVEDADES", title="Carga de archivos")
            if(self.path2 == ""):
                messagebox.showinfo(message=err.e_null_path+"TURNOS", title="Cargar de archivos")
        else:
            self.sheet1 = self.ent_seet1.get()
            self.sheet2 = self.ent_seet2.get()
            if (self.sheet1 and self.sheet2) == "":
                if(self.sheet1==""):
                    messagebox.showinfo(message=err.e_null_sheet+"NOVEDADES", title="Cargar de archivos")
                if(self.sheet2==""):
                    messagebox.showinfo(message=err.e_null_sheet+"TURNOS", title="Cargar de archivos")
            else:
                file_name = filedialog.asksaveasfilename(filetypes = (("csv files","*.csv"),("all files","*.*")))
                res = self.control.execute_process(self.path1,self.sheet1,self.path2,self.sheet2,file_name)
                if(res):
                    messagebox.showinfo(message="La carga de novedades se completo correctamente", title="Carga de novedades")
                else:
                    messagebox.showinfo(message=err.e_nov_failed+"carga de novedades", title="Carga de novedades")
