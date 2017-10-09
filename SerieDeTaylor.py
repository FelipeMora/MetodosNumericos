from tkinter import *
from tkinter.tix import ScrolledListBox
import time
try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk

def startGUI():
    global WI,H
    WI = "593"
    H = "460"
    root = Tk()
    root.geometry(WI+"x"+H+"+481+153")
    root.title("Métodos Numericos")
    b = windows(root)
    root.mainloop()

class windows:

    def __init__(self, master):
        self.prin = master
        self.exito = 0
        self.FuncionGET = StringVar()  # No debe ir aca
        self.top_derivate=self.createTop_Level("Derivaciones")#Creacion de un Top Level
        self.createwidgest()

    def createMenu(self):
        menu = Menu(self.prin)
        menu.configure(relief=GROOVE)
        menu.configure(borderwidth="10")
        self.prin.config(menu=menu)
        return menu

    def createSubMenu(self,MenuTO,title,subs):#Prueba de los menus y submenus ----> No se encuentra finalizado
        subMenu = Menu(MenuTO)
        if subs == "":
            MenuTO.add_command(label=title,command=self.nada)
        else:
            MenuTO.add_cascade(label=title,menu=subMenu)
            subMenu.add_command(label=subs,command=self.nada)
        #subMenu.add_separator()
        #subMenu.add_command(label="Metodo de Biseccion",command=self.nada)
        return subMenu

    def createConsole(self):
        print("Creando consola")
        #Creando Scrollbar
        Eje = "y"
        yScrollbar = self.createScroll(self.prin,VERTICAL)
        #Creando lista
        self.listbox = self.createLisBox(self.prin, 5, WI, yScrollbar, Eje)
        self.listbox['bg'] = "#fff"
        if Eje == "y":
            print("yview")
            yScrollbar['command'] = self.listbox.yview
        else:
            yScrollbar['command'] = self.listbox.xview
        #Configuracion de list
        self.listbox.configure(relief=GROOVE)
        self.listbox.configure(borderwidth="2")
        #FrameConsole = self.createFrame(self.prin, W, 50, BOTTOM, 10, 0, 0)

    def nada(self):
        text = "Hola!! No hago nada, solo estoy para pruebas."
        self.insertLisBox(self.listbox, text, LEFT, "cls")

    def createTop_Level(self,title="Default",geometry="400x300+20+20"):#Todas deberian retornar para agregar a cualquier varibale
        TopLevel = Toplevel(self.prin)
        TopLevel.title(title)
        TopLevel.geometry(geometry)
        TopLevel.withdraw()
        return TopLevel

    def createwidgest(self):
        MenuPrin = self.createMenu()  # Creacion del menu principal
        #Creando submenus
        subMenuPrin = self.createSubMenu(MenuPrin, "Aproximación basicas","Polinomio de Mclaurin/Taylor")
        subMenuPrin2 = self.createSubMenu(MenuPrin, "Sistema de Numeración posicional", "")
        subMenuPrin3 = self.createSubMenu(MenuPrin, "Fracciones Binarias", "")
        subMenuPrin4 = self.createSubMenu(MenuPrin, "Interpolacion","Metodo de Newton (Espacios equidistantes)")
        self.createConsole()
        #Widgeste del Frame principal
        LabelPrin = self.createLabelF(self.prin,"Opciones",10,10)
        Label1 = self.createLabel(LabelPrin, "Función", 10, 0)
        EntryFun = self.createEntry(LabelPrin, self.FuncionGET, 130, 10)
        btnSTART = self.createButton(LabelPrin, text="Empezar", cursor="hand1", Grelief="groove", command=self.derivar, xc=260, yc=5)
        Label2 = self.createLabel(self.top_derivate, text="Derivadas", xc=10, yc=0)
        ListDeriv = self.createLisBox(self.top_derivate,15,63,NONE,NONE)
        self.insertLisBox(self.listbox,"Consola creada", LEFT,"cls")
        self.insertLisBox(ListDeriv,"-2x^3",LEFT,"")
        ListDeriv.place(x=10, y=30)

    def createScroll(self,Contenedor,Gorient):
        scrollbar = Scrollbar(Contenedor,orient=Gorient)
        return scrollbar

    def createFrame(self,Contenedor,Gwidth,Gheight,side,gpadx,gpady,pack):
        print("Creando Frame")
        if pack == 0:
            default = Frame(Contenedor,width=Gwidth,height=Gheight,padx=gpadx,pady=gpady)
        else:
            default = Frame(Contenedor, width=Gwidth, height=Gheight, padx=gpadx, pady=gpady)
            default.pack(side=side, padx=gpadx, pady=gpady)
        return default

    def createLabelF(self,Contenedor,text="Default",Gpadx=0,Gpady=0):
        print("Crea label frame")
        LFrame = LabelFrame(Contenedor, text=text, padx=Gpadx, pady=Gpady)
        LFrame.pack(fill="both", expand="yes")
        return LFrame

    def createLabel(self,Contenedor,text="Default",xc = 0,yc= 0,side=NONE):
        print("Crea label")
        if xc >= 0 and yc >= 0:
            LblTexNor = Label(Contenedor, text=text + " : ", font=("Agency FB", 14)).place(x=xc,y=yc)
        else:
            LblTexNor = Label(Contenedor, text=text, font=("Agency FB", 9)).pack(side=side)
        return LblTexNor

    def createEntry(self, Contenedor, command=StringVar, xc=0, yc= 0):
        print("Crea entry")
        CmpGET = Entry(Contenedor, textvariable=command).place(x=xc,y=yc)  #Campo de entrada
        return CmpGET

    def createButton(self,Contenedor,text="Default",cursor="hand1",Grelief="groove",command=StringVar,xc = 0,yc = 0):
        print("Crea button")
        btnGET = Button(Contenedor, text=text, width=7, cursor=cursor, relief=Grelief,command=command) # Boton con evento
        btnGET.place(x=xc, y=yc)
        return btnGET

    def createLisBox(self,Contenedor,Gheight,Gwidth=50,command=NONE,eje=NONE):
        print("Crea listBox")
        lstBox = Listbox(Contenedor, height=Gheight, width=Gwidth)
        if eje == "y":
            print("Y scroll command")
            lstBox['yscrollcommand'] = command.set
        if eje == "x":
            lstBox['xscrollcommand'] = command.set
        return lstBox

    def insertLisBox(self,Contenedor,item,Gside,lpro):#El return debe ser la confirmacon de su agregaccion
        print("Insertar valores a list")
        agregar = ""
        if  lpro == "cls":
            agregar = time.strftime("%c") + " >> "
            # -----> for item in ["one", "two", "three", "four"]:
        Contenedor.insert(END, agregar + item)
        Contenedor.pack(side=Gside)

    def ShowTop_level(self,top_level):
        print("Mostrar el top_level")
        top_level.deiconify()#Comprobar que se halla mostrado

    def destroy_widget(self,widget):
        try:
            widget.destroy()
        except ImportWarning:
            print("El widget no pudo ser destruido")

    def derivar(self):
        Derivar = self.FuncionGET.get()
        text = "Procesando derivada... "
        if (Derivar == ""):
            text = "No ha ingresado derivada!"
        if (text == "Procesando derivada... "):
            self.ShowTop_level(self.top_derivate)
        self.insertLisBox(self.listbox, text, LEFT, "cls")

if __name__ == '__main__':
    startGUI()