from tkinter import *
import ProcSerieDeTaylor
import CreateUI as c

try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk


def start_gui(title, op_g, sg):
    global WI, H
    WI = "879"  # 593
    H = "680"  # 460
    root = Tk()
    root.geometry(WI + "x" + H + "+379+66")
    root.title(title)
    windows(root, op_g, sg, H, WI)
    root.mainloop()


class windows:
    def __init__(self, master, init, sg, h, w):
        self.prin = master
        self.c_UI = c.creation(master, h, w)  # Inicializa instancia de creación
        self.console = NONE
        self.ERELget = IntVar()
        self.EABSget = IntVar()
        self.NumSIS = StringVar()
        self.Xget = StringVar()
        self.X = StringVar()
        self.__defined_images()
        self.FuncionGET = StringVar()
        self.create_elements(init, sg)

    def __defined_images(self):
        self.ctb_img = PhotoImage(file="img\ctb.png")
        self.taylor_img = PhotoImage(file="img\ml_taylor.png")
        # self.c_UI.createLabel(self.prin, text="", xc=60, yc=25, side=NONE, img_url=self.taylor_img)

    # def createMenu(self):# ---> Pertenece a todas las opciones
    #     menu = Menu(self.prin) #Inicia menu
    #     menu.configure(relief=GROOVE)
    #     menu.configure(borderwidth="10")
    #     self.prin.config(menu=menu) #Agrega menu a label principal
    #     rd = rdml.rdxml()
    #     rd.defind_estructure()
    #     print(rd.get_arr_dat)
    #     self.createSubMenu(menu, "Principal","", self.Op0)
    #     self.createSubMenu(menu, "Aproximación basicas", "Polinomio de Mclaurin/Taylor", self.Op1)
    #     self.createSubMenu(menu, "Sistema de Numeración posicional", "", self.Op2)
    #     self.createSubMenu(menu, "Fracciones Binarias", "", self.Op3)
    #     self.createSubMenu(menu, "Interpolacion", "Metodo de Newton", self.Op4)
    #     return menu

    # def createSubMenu(self,MenuTO,title,subs,Gcommand):#Prueba de los menus y submenus ----> No se encuentra finalizado
    #     subMenu = Menu(MenuTO)#Inicia submenu
    #     if subs == "":
    #         MenuTO.add_command(label=title,command=Gcommand)#Menu principal
    #     else:
    #         MenuTO.add_cascade(label=title,menu=subMenu)
    #         subMenu.add_command(label=subs,command=Gcommand)
    #     return MenuTO

    # def createConsole(self):#El scroll no esta bien implementado
    #     #Creando Scrollbar
    #     Eje = "y"
    #     yScrollbar = self.createScroll(self.prin,VERTICAL)#contenedor(root) y orientación(vertical)
    #     #Creando lista relacionada con el scrollbar
    #     self.listbox = self.createLisBox(self.prin, 5, WI, yScrollbar, Eje)
    #     self.listbox['bg'] = "#fff"
    #     #configurar el scrollbar para la lista
    #     if Eje == "y": yScrollbar['command'] = self.listbox.yview
    #     else: yScrollbar['command'] = self.listbox.xview
    #     #Configuracion de list
    #     self.listbox.configure(relief=GROOVE)
    #     self.listbox.configure(borderwidth="2")
    #     #FrameConsole = self.createFrame(self.prin, W, 50, BOTTOM, 10, 0, 0)

    # def nada(self):
    #     text = "Hola!! No hago nada, solo estoy para pruebas."  # Debe destruir todo lo que este adentro del  Labelprincipal
    #     self.insertLisBox(self.listbox, text, LEFT, "cls")
    #
    # def Op0(self):
    #     self.prin.destroy()
    #     startGUI("Métodos Numéricos", "Prin", "Principal")
    #
    # def Op1(self):
    #     self.insertLisBox(self.listbox, "Polinomio de Mclaurin/Taylor", LEFT, "cls")
    #     self.prin.destroy()
    #     startGUI("Métodos Numéricos V.0.0.1", "Op1", "Aproximaciones Basicas")
    #     # Polinimio de Mclaurin/Taylor
    #
    # def Op2(self):
    #     self.insertLisBox(self.listbox, "Sistema de Numeracion posicional", LEFT, "cls")
    #     self.prin.destroy()
    #     startGUI("Métodos Numéricos V.0.0.1", "Op2", "Sistema de Numeracion Posicional")
    #     # Sistema de Numeracion posicional
    #
    # def Op3(self):
    #     self.insertLisBox(self.listbox, "Fracciones binarias", LEFT, "cls")
    #     # Fracciones binarias
    #
    # def Op4(self):
    #     self.insertLisBox(self.listbox, "Metodo de Newton", LEFT, "cls")
    #     # Metodo de Newton

    def createTop_Level(self, title="Default", geometry="400x300+20+20"):
        TopLevel = Toplevel(self.prin)
        TopLevel.title(title)
        TopLevel.geometry(geometry)
        TopLevel.withdraw()
        return TopLevel

    def get_choice(self, arg):
        switcher = {'P': self.c_UI.parameters_ui_p, 'PMT': self.c_UI.parameters_ui_pmt(),
                    'SNP': self.c_UI.parameters_ui_snp, 'FB': self.c_UI.parameters_ui_fb,
                    'MN': self.c_UI.parameters_ui_mn, }
        return switcher.get(arg, "nothing")

    #     def createGUIPrin(self):  # Carga todos los elementos que conforman la interfaz
    #         self.insertElement_Console("Cargando parametros principales...")
    #         self.c_UI.createMessage(self.prin,'''Métodos Numéricos
    #
    # Metodologías que utilizan operaciones algebraicas
    # y aritmeticas para resolver de forma aproximada
    # ecuaciones complejas, en muchos de ellos es requerido
    # derivadas, integrales y ecuaciones difereniales.''',w=370,x=80,y=210)
    #         self.c_UI.createMessage(self.prin,'''Notas
    #
    # Este software no sera desarrollado bajo ninguna metodologia
    # en especial, ni tampoco se le aplicara un plan de pruebas
    # estructurado. Por tal motivo, es posible que contenga una
    # cantidad produente de errores.''',w=370,x=460,y=210)
    #
    #         self.c_UI.createFrame(self.prin,5,125,NONE,10,0,0,430,210,0,RIDGE)
    #         self.c_UI.createLabel(self.prin,text="",xc=60,yc=25,side=NONE,img_url=self.taylor_img)#No esta agregando la imagen
    #
    #         self.c_UI.createFrame(self.prin,745,5,0,0,0,0,70,360,0,RIDGE)
    #         self.insertElement_Console("Principal cargada con exito")

    # def configFrameDefault(self,Contenedor,grelief): #configuración para el Frame por defecto
    #     Contenedor.configure(relief=grelief)
    #     Contenedor.configure(borderwidth="2")
    #    #Contenedor.configure(background="#d9d9d9")

    def createGUIAprox(self):
        self.insertLisBox(self.listbox, "Cargando widgest...", LEFT, "cls")
        self.createLabel(self.LabelPrin, "F(X)", 70, 30)
        self.createLabel(self.LabelPrin, "Grado ", 70, 80)
        self.createLabel(self.LabelPrin, "X ", 70, 120)
        self.createLabel(self.LabelPrin, "A ", 200, 80)

        self.createEntry(self.LabelPrin, self.FuncionGET, 140, 30)
        self.createEntry(self.LabelPrin, self.Xget, 230, 80, 0.04)
        self.createEntry(self.LabelPrin, self.X, 140, 120)
        self.spnBOX = self.createSpinbox(self.LabelPrin, 1, 50, 140, 80, 0.04)

        btnSTART = self.createButton(self.prin, "Empezar", "hand1", RAISED, self.derivar, 350, 55)
        btnSTART.configure(width=27)

        btnCLS = self.createButton(self.prin, "Limpiar", "hand1", RAISED, self.cls, 350, 140)
        btnCLS.configure(width=27)

        self.createCheckBTN(self.prin, "Error absoluto", self.EABSget, 350, 105)
        self.createCheckBTN(self.prin, "Error relativo", self.ERELget, 460, 105)

        FraSeparador = self.createFrame(self.prin, 5, 115, NONE, 0, 0, 0, 590, 55, 0)
        self.configFrameDefault(FraSeparador, SUNKEN)

        self.createMessage(self.prin,
                           '''La aproximación sera realizada con el metodo de mclaurin y taylor, en el proceso, sera mostrada la grafica correspondiente a la funcion registrada.''',
                           180, 620, 55)

        FraSeparador2 = self.createFrame(self.prin, 745, 5, NONE, 0, 0, 0, 60, 180, 0)
        self.configFrameDefault(FraSeparador2, RIDGE)
        # ------------------------------------------------------------> SCROLL V.3
        frame_gen = Frame(self.prin, relief=RIDGE, borderwidth="1")
        scrollbarView = Scrollbar(frame_gen, orient=VERTICAL, takefocus=FALSE)
        self.textView = Text(frame_gen, wrap=WORD, width=91, highlightthickness=0, state=DISABLED)
        #########################################################################################
        FraProc = self.createFrame(self.textView, 745, 600, NONE, 0, 0, 0, 60, 190, 0)
        self.lstDevA = self.createLisBox(FraProc, 15, 15, NONE, NONE)
        self.lstDevA.place(x=20, y=20)
        self.Txt = self.createText(FraProc, 140, 20, 95, 1, NORMAL)
        self.createLabel(FraProc, "Aproximación", 140, 80, NONE)
        self.TxtPOL = self.createText(FraProc, 240, 80, 78, 1, NORMAL)
        self.createLabel(FraProc, "Error Absoluto", 140, 150, NONE)
        self.TxtEA = self.createText(FraProc, 240, 150, 26, 1, NORMAL)
        self.createLabel(FraProc, "Error Relativo", 440, 150, DISABLED)
        self.TxtER = self.createText(FraProc, 550, 150, 26, 1, NORMAL)
        self.createMessage(FraProc, "assfdfdfdfdf", 240, 340, 450)
        self.createMessage(FraProc, "Polinomio de Mclaurin/Taylor", 240, 340, 225)
        self.textView.window_create(INSERT, window=FraProc)
        ##########################################################################################
        scrollbarView.config(command=self.textView.yview)
        # textView.bind('<Configure>', self.defRegion(textView))
        self.textView.config(yscrollcommand=scrollbarView.set)
        scrollbarView.pack(side=RIGHT, fill=Y)
        # frame.place(side=LEFT,expand=TRUE,fill=BOTH)
        self.textView.pack(side=LEFT, expand=True, fill=BOTH)
        frame_gen.place(x=60, y=190)
        # ------------------------------------------------------------> SCROLL V.3
        self.top_derivate = self.createTop_Level("Aproximaciones", "400x300+20+20")
        Label2 = self.createLabel(self.top_derivate, text="Aproximaciones sucesivas", xc=10, yc=0)
        self.ListDeriv = self.createLisBox(self.top_derivate, 15, 63, NONE, NONE)
        self.ListDeriv.place(x=10, y=30)
        # -------------------------------------------------------------> Formula
        self.top_formula = self.createTop_Level("Formula Serie de Taylor", "400x141+2+20")
        LabelMGF = self.createLabel(self.top_formula, "", 0, 0, NONE, self.formtaylor)
        self.ShowTop_level(self.top_formula)
        # -------------------------------------------------------------> Formula
        self.insertLisBox(self.listbox, "GUI cargada correctamente!!!", LEFT, "cls")

    def createGUISisPos(self):

        self.insertLisBox(self.listbox, "Cargando widgest...", LEFT, "cls")
        self.createLabel(self.LabelPrin, "Numero", 70, 40)

        self.createLabel(self.LabelPrin, "De ", 70, 90)
        self.createEntry(self.LabelPrin, self.NumSIS, 140, 40)

        Spinbox(self.LabelPrin, values=(2, 8, 10, 16)).place(x=140, y=90, relwidth=0.04)

        self.createLabel(self.LabelPrin, "A ", 190, 90)
        self.a_base = Spinbox(self.LabelPrin, values=(2, 8, 10, 16))
        self.a_base.place(x=230, y=90, relwidth=0.04)

        FraSeparador = self.createFrame(self.prin, 5, 115, NONE, 0, 0, 0, 590, 55, 0)
        self.configFrameDefault(FraSeparador, SUNKEN)

        self.createMessage(self.prin,
                           '''Se encuentran incorporados la conversion de la Base 10, Base 2, Base 8 y Base 16. Junto con sus posibles combinaciones.''',
                           180, 620, 55)

        btnSTART = self.createButton(self.prin, "Convertir", "hand1", RAISED, self.SisNUM, 350, 65)
        btnSTART.configure(width=27)

        self.createMessage(self.prin,
                           '''Para evitar procesos innecesarios no sera permitido convertir asi mismo.''',
                           180, 350, 100)

        FraSeparador2 = self.createFrame(self.prin, 745, 5, NONE, 0, 0, 0, 60, 180, 0)
        self.configFrameDefault(FraSeparador2, RIDGE)

        frame_gen = Frame(self.prin, relief=RIDGE, borderwidth="1")
        scrollbarView = Scrollbar(frame_gen, orient=VERTICAL, takefocus=FALSE)
        self.textViewGEN = Text(frame_gen, wrap=WORD, width=91, highlightthickness=0, state=NORMAL)
        scrollbarView.config(command=self.textViewGEN.yview)
        # textView.bind('<Configure>', self.defRegion(textView))
        self.textViewGEN.config(yscrollcommand=scrollbarView.set)
        scrollbarView.pack(side=RIGHT, fill=Y)
        # frame.place(side=LEFT,expand=TRUE,fill=BOTH)
        self.textViewGEN.pack(side=LEFT, expand=True, fill=BOTH)
        frame_gen.place(x=60, y=190)

        self.insertLisBox(self.listbox, "GUI cargada correctamente!!!", LEFT, "cls")

    def defRegion(self, event):
        event.configure(scrollregion=event.bbox(ALL))

    def createText(self, Contenedor, gw, gy, gW, gH, gstate):
        textgen = Text(Contenedor, background="white", foreground="black", width=gW, height=gH,
                       state=gstate)  # Debe ser ingresado
        textgen.configure(font="TkTextFont")
        textgen.configure(highlightbackground="#d9d9d9")
        textgen.configure(highlightcolor="black")
        textgen.configure(insertbackground="black")
        textgen.configure(selectbackground="#c4c4c4")
        textgen.configure(selectforeground="black")
        textgen.configure(undo="1")
        textgen.configure(wrap=WORD)
        textgen.place(x=gw, y=gy)
        return textgen

    def create_elements(self, init_choice, sg):
        self.c_UI.create_labelframe(self.prin, sg, 10, 10)  # Contenedor de los parametros de interfaz.
        self.c_UI.create_menu()

        self.console = self.c_UI.create_console
        self.c_UI.create_console = "Consola creada"

        exec_choice = self.get_choice(init_choice)
        self.c_UI.create_console = "Cargando elementos"
        exec_choice()
        self.c_UI.create_console = "Elementos cargados"

    def createSpinbox(self, Contenedor, desde, hasta, gx, gy, grw):
        spinbox = Spinbox(Contenedor, from_=desde, to=hasta)
        spinbox.place(x=gx, y=gy, relwidth=grw)
        return spinbox

    def createCheckBTN(self, Contenedor, text, v, gx, gy):
        checkBTN = Checkbutton(Contenedor, text=text, variable=v, onvalue=1, offvalue=0)
        checkBTN.place(x=gx, y=gy)  # Aun no devuelve

    def createCanvas(self, Contenedor, grelief, gw):
        cnv = Canvas(Contenedor, width=gw)
        cnv.configure(background="white")
        cnv.configure(relief=grelief)
        cnv.configure(borderwidth="2")
        return cnv

    # def createMessage(self,Contenedor,text,gw,gx,gy):
    #     Msg = Message(Contenedor,width=gw)
    #     Msg.place(x=gx,y=gy)
    #     Msg.configure(text=text)

    # def createScroll(self,Contenedor,Gorient): #Contenedor y la orientación.
    #     scrollbar = Scrollbar(Contenedor,orient=Gorient)#orient=Gorient
    #     scrollbar.pack(side = RIGHT, fill = Y)
    #     return scrollbar

    # def createFrame(self,Contenedor,Gwidth,Gheight,side,gpadx,gpady,pack,gx,gy,placepre):
    #     print("Creando Frame")
    #     if pack == 0:
    #         default = Frame(Contenedor,width=Gwidth,height=Gheight)
    #         if placepre == 0:
    #             default.place(x=gx, y=gy)
    #     else:
    #         default = Frame(Contenedor, width=Gwidth, height=Gheight, padx=gpadx, pady=gpady)
    #         default.pack(side=side, padx=gpadx, pady=gpady)
    #     return default

    # def createLabelF(self,Contenedor,text="Default",Gpadx=0,Gpady=0):
    #     print("Crea label frame")
    #     LFrame = LabelFrame(Contenedor, text=text, padx=Gpadx, pady=Gpady)
    #     LFrame.pack(fill="both", expand="yes")
    #     return LFrame

    def createLabel(self, container, text="DEFAULT", xc=0, yc=0, side=NONE, imgURL=NONE):

        if xc >= 0 and yc >= 0:
            if text != "":  # Si tiene text="" lo que se agrega es una imagen
                Label(container, text=text + " = ").place(x=xc, y=yc)
            else:
                try:
                    Label(container, relief="solid", image=self.ctb_img).place(x=xc, y=yc)
                    # Label_text_norm = Label(container, relief="solid", image=logoCTB).place(x=xc, y=yc)
                except:
                    self.insertElement_Console("No se ha podido cargar la imagen")
        else:
            Label(container, text=text).pack(side=side)
        # return Label_text_norm

    def createEntry(self, Contenedor, command=StringVar, xc=0, yc=0, grw=NONE):
        print("Crea entry")
        if grw == NONE:
            CmpGET = Entry(Contenedor, textvariable=command).place(x=xc, y=yc)  # Campo de entrada
        else:
            CmpGET = Entry(Contenedor, textvariable=command).place(x=xc, y=yc, relwidth=grw)
        return CmpGET

    def createButton(self, Contenedor, text="Default", cursor="hand1", Grelief="groove", command=StringVar, xc=0, yc=0):
        print("Crea button")
        btnGET = Button(Contenedor, text=text, width=7, cursor=cursor, relief=Grelief,
                        command=command)  # Boton con evento
        btnGET.place(x=xc, y=yc)
        return btnGET

    # def createLisBox(self,Contenedor,Gheight,Gwidth=50,command=NONE,eje=NONE): #Crea una lista
    #     lstBox = Listbox(Contenedor, height=Gheight, width=Gwidth)
    #     if eje == "y":
    #         lstBox['yscrollcommand'] = command.set
    #     if eje == "x":
    #         lstBox['xscrollcommand'] = command.set
    #     return lstBox

    # def insertElement_Console(self,element):
    #     self.console.insert(END, time.strftime("%c") + " >> " + element)
    #     self.console.see(END)

    def ShowTop_level(self, top_level):
        print("Mostrar el top_level")
        top_level.deiconify()  # Comprobar que se halla mostrado

    def destroy_widget(self, widget):
        try:
            widget.destroy()
        except ImportWarning:
            self.insertLisBox(self.listbox, "El objeto no puedo ser destruido - ERROR -", LEFT, "cls")

    def derivar(self):  # Verificar que todos los campos esten llenos.
        F_Derivar = self.FuncionGET.get()
        X_aprox = self.Xget.get()
        text = "Procesando derivada..."
        if (F_Derivar == NONE or X_aprox == NONE):
            text = "!Debe ingresar todos los datos!"
        if (text == "Procesando derivada... "):
            ProcSerieDeTaylor.metodosyseries(self, '1')
            self.ShowTop_level(self.top_derivate)
        self.insertLisBox(self.listbox, text, LEFT, "cls")

    def clean_master(self):
        self.prin.destroy()
        startGUI("Métodos Numéricos V.0.0.1", "Op1", "Aproximaciones Basicas")

    def SisNUM(self):
        # Revisar campos
        Num_SIS = self.NumSIS.get()
        text = "Convirtiendo"
        if Num_SIS == "":
            text = "¡ Debe ingresar el numero !"
        else:
            ProcSerieDeTaylor.metodosyseries(self, '6')
        self.insertLisBox(self.listbox, text, LEFT, "cls")


if __name__ == '__main__':
    start_gui("Métodos Númericos V.0.0.1", "P", "Principal")
