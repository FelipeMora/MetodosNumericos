from tkinter import *
import time
import ProcSerieDeTaylor

try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk

def startGUI(title,OpG,sg):
    global WI,H
    WI = "879"#593
    H = "680"#460
    root = Tk()
    root.geometry(WI+"x"+H+"+379+66")
    root.title(title)
    root.resizable(width=FALSE,height=FALSE)
    windows(root,OpG,sg)
    root.mainloop()

class windows:

    def __init__(self, master, op,sg):
        self.ERELget = IntVar()
        self.EABSget = IntVar()
        self.Xget = StringVar()
        self.FuncionGET = StringVar()
        self.prin = master
        self.logoCTB = PhotoImage(file="img\ctb.png")
        self.createwidgest(op,sg)

    def createMenu(self):# ---> Pertenece a todas las opciones
        menu = Menu(self.prin)
        menu.configure(relief=GROOVE)
        menu.configure(borderwidth="10")
        self.prin.config(menu=menu)
        self.createSubMenu(menu, "Principal","", self.Op0)
        self.createSubMenu(menu, "Aproximación basicas", "Polinomio de Mclaurin/Taylor", self.Op1)
        self.createSubMenu(menu, "Sistema de Numeración posicional", "", self.Op2)
        self.createSubMenu(menu, "Fracciones Binarias", "", self.Op3)
        self.createSubMenu(menu, "Interpolacion", "Metodo de Newton", self.Op4)
        return menu

    def createSubMenu(self,MenuTO,title,subs,Gcommand):#Prueba de los menus y submenus ----> No se encuentra finalizado
        subMenu = Menu(MenuTO)
        if subs == "":
            MenuTO.add_command(label=title,command=Gcommand)
        else:
            MenuTO.add_cascade(label=title,menu=subMenu)
            subMenu.add_command(label=subs,command=Gcommand)
        #subMenu.add_separator()
        #subMenu.add_command(label="Metodo de Biseccion",command=self.nada)
        return subMenu

    def createConsole(self):#El scroll no esta bien implementado
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
        text = "Hola!! No hago nada, solo estoy para pruebas." #Debe destruir todo lo que este adentro del  Labelprincipal
        self.insertLisBox(self.listbox, text, LEFT, "cls")

    def Op0(self):
        self.prin.destroy()
        startGUI("Métodos Numéricos", "Prin","Principal")

    def Op1(self):
        self.insertLisBox(self.listbox, "Polinomio de Mclaurin/Taylor", LEFT, "cls")
        self.prin.destroy()
        startGUI("Métodos Numéricos","Op1","Aproximaciones Basicas")
        #Polinimio de Mclaurin/Taylor

    def Op2(self):
        self.insertLisBox(self.listbox, "Sistema de Numeracion posicional", LEFT, "cls")
        self.prin.destroy()
        startGUI("Métodos Numéricos", "Op2", "Sistema de Numeracion Posicional")
        #Sistema de Numeracion posicional

    def Op3(self):
        self.insertLisBox(self.listbox, "Fracciones binarias", LEFT, "cls")
        #Fracciones binarias

    def Op4(self):
        self.insertLisBox(self.listbox, "Metodo de Newton", LEFT, "cls")
        #Metodo de Newton

    def createTop_Level(self,title="Default",geometry="400x300+20+20"):
        TopLevel = Toplevel(self.prin)
        TopLevel.title(title)
        TopLevel.geometry(geometry)
        TopLevel.withdraw()
        return TopLevel

    def catalogacion(self,arg):
        switcher = {
            'Prin': self.createGUIPrin,
            'Op1': self.createGUIAprox,
            'Op2': "dos",
            'Op3': "dos",
            'Op4': "dos",
        }
        return switcher.get(arg,"nothing")

    def createGUIPrin(self):
        self.insertLisBox(self.listbox, "Cargando widgest principales...", LEFT, "cls")
        MsgIntro = self.createMessage(self.prin,'''Métodos Numéricos

Metodologias que utilizan operaciones algebraicas
y aritmeticas para resolver de forma aproximada 
ecuaciones complejas, en muchos de ellos es requerido
aplicar derivadas, integrales y ecuaciones diferenciales''',370,80,210)
        MsgNote = self.createMessage(self.prin,'''Notas

Este software no sera desarrollado bajo ninguna metodologia
en especial, ni tampoco se le aplicara un plan de pruebas
estructurado. Por tal motivo, es posible que contenga una
cantidad produente de errores.''',370,460,210)
        FraSeparador = self.createFrame(self.prin,5,125,NONE,10,0,0,430,210,0)
        self.configFrameDefault(FraSeparador,SUNKEN)
        #LabeIMG = self.createFrame(self.prin,145,115,NONE,0,0,0,80,60)
        LabeIMG = self.createLabel(self.prin,"",60,25,NONE)
        FraSeparador2 = self.createFrame(self.prin,745,5,0,0,0,0,70,360,0)
        self.configFrameDefault(FraSeparador2,RIDGE)
        self.insertLisBox(self.listbox, "GUI principal cargada con exito!!!", LEFT, "cls")

    def configFrameDefault(self,Contenedor,grelief):
        Contenedor.configure(relief=grelief)
        Contenedor.configure(borderwidth="2")
        #Contenedor.configure(background="#d9d9d9")

    def createGUIAprox(self):
        self.insertLisBox(self.listbox, "Cargando widgest...", LEFT, "cls")
        self.createLabel(self.LabelPrin,"F(X)",70,30)
        self.createLabel(self.LabelPrin,"Grado ",70,80)
        self.createLabel(self.LabelPrin,"X ",200,80)

        self.createEntry(self.LabelPrin, self.FuncionGET, 140, 30)
        self.createEntry(self.LabelPrin,self.Xget,230,80,0.04)
        self.spnBOX = self.createSpinbox(self.LabelPrin,1,50,140,80,0.04)

        btnSTART = self.createButton(self.prin,"Empezar","hand1",RAISED,self.derivar,350,55)
        btnSTART.configure(width=27)

        self.createCheckBTN(self.prin,"Error absoluto",self.EABSget,350,105)
        self.createCheckBTN(self.prin,"Error relativo",self.ERELget,460,105)

        FraSeparador = self.createFrame(self.prin,5,115,NONE,0,0,0,590,30,0)
        self.configFrameDefault(FraSeparador, SUNKEN)

        self.createMessage(self.prin,'''La aproximación sera realizada con el metodo de mclaurin y taylor, en el proceso, sera mostrada la grafica correspondiente a la funcion registrada.''',180,620,30)

        FraSeparador2 = self.createFrame(self.prin,745,5,NONE,0,0,0,60,170,0)
        self.configFrameDefault(FraSeparador2,RIDGE)
        #------------------------------------------------------------> SCROLL V.3
        frame_gen = Frame(self.prin,relief=RIDGE,borderwidth="1")
        scrollbarView = Scrollbar(frame_gen,orient=VERTICAL,takefocus=FALSE)
        self.textView = Text(frame_gen, wrap=WORD, width=91, highlightthickness=0,state=DISABLED)

        #FraProc = self.createFrame(textView, 745, 600, NONE, 0, 0, 0, 60, 190, 0)
        #lstDevA = self.createLisBox(FraProc, 15, 15, NONE, NONE)
        #lstDevA.place(x=20, y=20)
        #self.Txt = self.createText(FraProc, 140, 20, 95, 1, DISABLED)
        #self.createLabel(FraProc, "Aproximación", 140, 80, NONE)
        #self.TxtPOL = self.createText(FraProc, 240, 80, 78, 1, DISABLED)
        #self.createLabel(FraProc,"Error Absoluto",140,150,NONE)
        #self.TxtEA = self.createText(FraProc,240,150,26,1,DISABLED)
        #self.createLabel(FraProc, "Error Relativo", 440, 150, NONE)
        #self.TxtER = self.createText(FraProc, 550, 150, 26, 1, DISABLED)
        #self.createMessage(FraProc, "assfdfdfdfdf", 240, 340, 450)
        #self.createMessage(FraProc, "Polinomio de Mclaurin/Taylor", 240, 340, 225)
        #textView.window_create(INSERT,window=FraProc)

        scrollbarView.config(command=self.textView.yview)
        #textView.bind('<Configure>', self.defRegion(textView))
        self.textView.config(yscrollcommand=scrollbarView.set)
        scrollbarView.pack(side=RIGHT, fill=Y)
        #frame.place(side=LEFT,expand=TRUE,fill=BOTH)
        self.textView.pack(side=LEFT, expand=True, fill=BOTH)
        frame_gen.place(x=60, y=190)
        #------------------------------------------------------------> SCROLL V.3
        self.top_derivate = self.createTop_Level("Derivaciones")
        Label2 = self.createLabel(self.top_derivate, text="Derivadas", xc=10, yc=0)
        ListDeriv = self.createLisBox(self.top_derivate, 15, 63, NONE, NONE)
        self.insertLisBox(ListDeriv, "-2x^3", LEFT, "")
        ListDeriv.place(x=10, y=30)
        self.insertLisBox(self.listbox, "GUI cargada correctamente!!!", LEFT, "cls")

    def defRegion(self,event):
        event.configure(scrollregion=event.bbox(ALL))

    def createText(self,Contenedor,gw,gy,gW,gH,gstate):
        textgen = Text(Contenedor,background="white",foreground="black",width=gW,height=gH,state=gstate)#Debe ser ingresado
        textgen.configure(font="TkTextFont")
        textgen.configure(highlightbackground="#d9d9d9")
        textgen.configure(highlightcolor="black")
        textgen.configure(insertbackground="black")
        textgen.configure(selectbackground="#c4c4c4")
        textgen.configure(selectforeground="black")
        textgen.configure(undo="1")
        textgen.configure(wrap=WORD)
        textgen.place(x=gw,y=gy)
        return textgen

    def createwidgest(self,op,sg):
        self.LabelPrin = self.createLabelF(self.prin, sg, 10, 10)
        MenuPrin = self.createMenu()  # Creacion del menu principal
        self.createConsole() # Todas las Op tendran una consola
        self.insertLisBox(self.listbox, "Consola creada", LEFT, "cls")
        #Pertenece
        fun = self.catalogacion(op)
        fun()

    def createSpinbox(self,Contenedor,desde,hasta,gx,gy,grw):
        spinbox = Spinbox(Contenedor,from_=desde,to=hasta)
        spinbox.place(x=gx,y=gy,relwidth=grw)
        return spinbox

    def createCheckBTN(self,Contenedor,text,v,gx,gy):
        checkBTN = Checkbutton(Contenedor,text=text,variable=v,onvalue=1,offvalue=0)
        checkBTN.place(x=gx,y=gy)#Aun no devuelve

    def createCanvas(self,Contenedor,grelief,gw):
        cnv = Canvas(Contenedor,width=gw)
        cnv.configure(background="white")
        cnv.configure(relief=grelief)
        cnv.configure(borderwidth="2")
        return cnv

    def createMessage(self,Contenedor,text,gw,gx,gy):
        Msg = Message(Contenedor,width=gw)
        Msg.place(x=gx,y=gy)
        Msg.configure(text=text)

    def createScroll(self,Contenedor,Gorient):
        scrollbar = Scrollbar(Contenedor,orient=Gorient)#orient=Gorient
        return scrollbar

    def createFrame(self,Contenedor,Gwidth,Gheight,side,gpadx,gpady,pack,gx,gy,placepre):
        print("Creando Frame")
        if pack == 0:
            default = Frame(Contenedor,width=Gwidth,height=Gheight)
            if placepre == 0:
                default.place(x=gx, y=gy)
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
            if text!="":
                LblTexNor = Label(Contenedor, text=text + " = ").place(x=xc,y=yc)
            else:
                try:
                    LblTexNor = Label(Contenedor,image=self.logoCTB).place(x=xc,y=yc)
                except ImportWarning:
                    self.insertLisBox(self.listbox, "No se ha podido cargar la imagen, es posible que la imagen no se encuentre en la ruta por defecto!!!", LEFT, "cls")
        else:
            LblTexNor = Label(Contenedor, text=text).pack(side=side)
        return LblTexNor

    def createEntry(self, Contenedor, command=StringVar, xc=0, yc= 0,grw=NONE):
        print("Crea entry")
        if grw == NONE:
            CmpGET = Entry(Contenedor, textvariable=command).place(x=xc,y=yc)  #Campo de entrada
        else:
            CmpGET = Entry(Contenedor,textvariable=command).place(x=xc,y=yc,relwidth=grw)
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
        print("VALOR --> " + str(item))
        agregar = ""
        if  lpro == "cls":
            agregar = time.strftime("%c") + " >> "
            # -----> for item in ["one", "two", "three", "four"]:
        Contenedor.insert(END, agregar + item)
        Contenedor.see(END)
        Contenedor.pack(side=Gside)

    def ShowTop_level(self,top_level):
        print("Mostrar el top_level")
        top_level.deiconify()#Comprobar que se halla mostrado

    def destroy_widget(self,widget):
        try:
            widget.destroy()
        except ImportWarning:
            self.insertLisBox(self.listbox, "El objeto no puedo ser destruido - ERROR -", LEFT, "cls")

    def derivar(self):
        Derivar = self.FuncionGET.get()
        text = "Procesando derivada... "
        if (Derivar == ""):
            text = "No ha ingresado derivada!"
        if (text == "Procesando derivada... "):
            ProcSerieDeTaylor.metodosyseries(self,'1')
            self.ShowTop_level(self.top_derivate)
        self.insertLisBox(self.listbox, text, LEFT, "cls")

if __name__ == '__main__':
    startGUI("Métodos Numéricos V.0.0.1","Prin","Principal")