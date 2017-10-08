#import sys
#sys.path.append('C:\Python27\Lib\lib-tk')
from tkinter import *
try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk

def startGUI():
    root = Tk()
    root.geometry("593x460+481+153")
    root.title("Métodos Numericos")
    b = windows(root)
    root.mainloop()

class windows:

    def __init__(self, master):
        self.prin = master
        self.exito = 0
        self.FuncionGET = StringVar()  # No debe ir aca
        self.top_derivate=self.createTop_Level("Derivaciones")#Creacion de un Top Level
        self.MenuPrin=self.createMenu()#Creacion del menu principal
        self.subMenuPrin=self.createSubMenu(self.MenuPrin)#Agregando un submenu en base al menu principal creado
        self.createwidgest()

    def createMenu(self):
        menu = Menu(self.prin)
        self.prin.config(menu=menu)
        return menu

    def createSubMenu(self,MenuTO):#Prueba de los menus y submenus ----> No se encuentra finalizado
        subMenu = Menu(MenuTO)
        MenuTO.add_cascade(label="Métodos Numéricos",menu=subMenu)
        subMenu.add_command(label="Polinomio de Taylor",command=self.nada)
        subMenu.add_command(label="Regresión cuadratica",command=self.nada)
        subMenu.add_separator()
        subMenu.add_command(label="Metodo de Biseccion",command=self.nada)
        return subMenu
        #No debe ir aca ---- Es solo prueba
        #self.createConsole()

    def createConsole(self):
        creFrame =self.createFrame(self.prin,BOTTOM,10,10)
        return creFrame

    def nada(self):
        print("Hola!! No hago nada.")

    def createTop_Level(self,title="Default",geometry="400x300+20+20"):#Todas deberian retornar para agregar a cualquier varibale
        TopLevel = Toplevel(self.prin)
        TopLevel.title(title)
        TopLevel.geometry(geometry)
        TopLevel.withdraw()
        return TopLevel

    def createwidgest(self):
        LabelPrin = self.createLabelF(self.prin,"Opciones",10,10)
        Label1 = self.createLabel(LabelPrin, "Función", 10, 0)
        EntryFun = self.createEntry(LabelPrin, self.FuncionGET, 130, 10)
        btnSTART = self.createButton(LabelPrin, text="Empezar", cursor="hand1", Grelief="groove", command=self.derivar, xc=260, yc=5)
        Label2 = self.createLabel(self.top_derivate, text="Derivadas", xc=10, yc=0)
        ListDeriv = self.createLisBox(self.top_derivate,width=50)
        #No debe ir aca, se debe encontrar en la derivada
        self.insertLisBox(ListDeriv,1,"-2x^3")
        ListDeriv.place(x=10, y=30)

    def createFrame(self,Contenedor,side,gpadx,gpady):
        print("Creando Frame")
        default = Frame(Contenedor,bg="blue")
        default.pack(side=side, padx=gpadx, pady=gpady)
        return default

    def createLabelF(self,Contenedor,text="Default",Gpadx=0,Gpady=0):
        print("Crea label frame")
        LFrame = LabelFrame(Contenedor, text=text, padx=Gpadx, pady=Gpady)
        LFrame.pack(fill="both", expand="yes")
        return LFrame

    def createLabel(self,Contenedor,text="Default",xc = 0,yc= 0):
        print("Crea label")
        LblTexNor = Label(Contenedor, text=text + " : ", font=("Agency FB", 14)).place(x=xc,y=yc)
        return LblTexNor

    def createEntry(self, Contenedor, command=StringVar, xc=0, yc= 0):
        print("Crea entry")
        CmpGET = Entry(Contenedor, textvariable=command).place(x=xc,y=yc)  #Campo de entrada
        return CmpGET

    def createButton(self,Contenedor,text="Default",cursor="hand1",Grelief="groove",command=StringVar,xc = 0,yc = 0):
        print("Crea button")
        btnGET = Button(Contenedor, text=text, width=7, cursor=cursor, relief=Grelief,command=command).place(x=xc, y=yc)  # Boton con evento
        return btnGET

    def createLisBox(self,Contenedor,width=50):
        print("Crea listBox")
        lstBox = Listbox(Contenedor, width=width)  #listbox en donde se muestran las derivadas
        return lstBox

    def insertLisBox(self,Contenedor,posicion,valor):#El return debe ser la confirmacon de su agregaccion
        print("Insertar valores a list")
        Contenedor.insert(posicion,valor)

    def ShowTop_level(self,top_level):
        print("Mostrar el top_level")
        top_level.deiconify()#Comprobar que se halla mostrado

    def destroy_widget(self,widget):
        try:
            widget.destroy()
        except ImportWarning:
            print("El widget no pudo ser destruido")

    def derivar(self):
        print("En la derivada!!!")
        Derivar = self.FuncionGET.get()
        text = "Procesando derivada... "
        if (Derivar == ""):
            text = "No ha ingresado derivada!"
        if (text == "Procesando derivada... "):
            self.ShowTop_level(self.winProDeri)
        #self.MosDerivada = self.createLabel(self.LFrame,text + Derivar,10,60)#Debe ser mostrado en consola


if __name__ == '__main__':
    startGUI()