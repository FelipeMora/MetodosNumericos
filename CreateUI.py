from tkinter import *
import time
import xml.etree.ElementTree as rd
try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk

class parameters_interfaces:

    def __init__(self,master):
        self.__master = master

    def parameters_ui_P(self):
        print("Principal")
        creation.createMessage(self.__master, '''Métodos Numéricos

        Metodologías que utilizan operaciones algebraicas
        y aritmeticas para resolver de forma aproximada 
        ecuaciones complejas, en muchos de ellos es requerido 
        derivadas, integrales y ecuaciones difereniales.''', w=370, x=80, y=210)
        creation.createMessage(self.__master, '''Notas

        Este software no sera desarrollado bajo ninguna metodologia
        en especial, ni tampoco se le aplicara un plan de pruebas
        estructurado. Por tal motivo, es posible que contenga una
        cantidad produente de errores.''', w=370, x=460, y=210)

        frame_separator = creation.createFrame(self.__master,g_width=5,g_height=125,side=NONE,g_pad_x=10,g_pad_y=0,pack=0,gx=430,gy=210,place_pre=0,config_edge=SUNKEN)


    def parameters_ui_PMT(self):
        print("Polinomio de Mclaurin/Taylor")

    def parameters_ui_SNP(self):
        print("Sistema de numeración posicional")

    def parameters_ui_FB(self):
        print("Fracciones binarias")

    def parameters_ui_MN(self):
        print("Metodo de Newton")



class creation(parameters_interfaces):

    def __init__(self,master, heigth, width):
        super(creation, self).__init__(master)
        self.in_tree = rd.parse("menu.xml")
        self.__root = self.in_tree.getroot()
        self.__master = master
        self.heigth = heigth
        self.width = width
        #variables iniciales

    @staticmethod
    def createLabelFrame(container, text="Default", Gpadx=0, Gpady=0):
        print("Crea label frame")
        LFrame = LabelFrame(container, text=text, padx=Gpadx, pady=Gpady)
        LFrame.pack(fill="both", expand="yes")
        return LFrame

    def __init_Menu(self):
        menu = Menu(self.__master)
        menu.configure(relief=GROOVE,borderwidth="10")
        self.__master.config(menu=menu)
        return menu

    @staticmethod
    def __createSubMenu(menu, title, sub, cmad): #titles debe ser una lista)
        subMenu = Menu(menu)
        menu.configure(relief=GROOVE, borderwidth="10")
        if sub == "": menu.add_command(label=title,command=cmad)
        else: menu.add_cascade(label=title,menu=subMenu), subMenu.add_command(label=sub,command=cmad)
        return menu

    def __defind_estructure_menu(self,menu):
        for child in self.__root:
            try: self.__createSubMenu(menu,child.attrib["title"],"",child.attrib["comand"])
            except:
                for child_child in child.getchildren():
                    if len(child_child.getchildren()) > 0:
                        for grandchild in child_child.getchildren():
                            self.__createSubMenu(menu,child.attrib["title"],grandchild.text,grandchild.attrib["comand"])

    @staticmethod
    def __createScroll(container, Gorient): #Contenedor y la orientación.
        scrollbar = Scrollbar(container,orient=Gorient)#orient=Gorient
        scrollbar.pack(side = RIGHT, fill = Y)
        return scrollbar

    @staticmethod
    def __createlisBox(container, Gheight, Gwidth=50, command=NONE, eje=NONE): #Crea una lista
        lstBox = Listbox(container, height=Gheight, width=Gwidth)
        if eje == "y": lstBox['yscrollcommand'] = command.set
        if eje == "x": lstBox['xscrollcommand'] = command.set
        lstBox["bg"] = "#fff"
        return lstBox

    def create_menu(self):
        self.parameters_ui_P()
        menu = self.__init_Menu()
        self.__defind_estructure_menu(menu)

    def __create_console(self):
        Eje = "y"; y_scrollBar = self.__createScroll(self.__master,VERTICAL)
        list_scrollBar = self.__createlisBox(self.__master,5,self.width,y_scrollBar,eje="y")
        if Eje == "y": y_scrollBar['command'] = list_scrollBar.yview
        else: y_scrollBar['command'] = list_scrollBar.xview
        list_scrollBar.configure(relief=GROOVE)
        list_scrollBar.configure(borderwidth="2")
        list_scrollBar.pack(side=LEFT)
        return  list_scrollBar

    @property
    def console(self):
        console = self.__create_console()
        return console

    @staticmethod
    def createMessage(container,text,w,x,y):
        msg = Message(container, width=w)
        msg.place(x=x, y=y)
        msg.configure(text=text)

    @staticmethod
    def createFrame(container, g_width, g_height, side, g_pad_x, g_pad_y, pack, gx, gy, place_pre,config_edge):
        if pack == 0:
            frame = Frame(container, width=g_width, height=g_height)
            if place_pre == 0: frame.place(x=gx, y=gy)
        else:
            frame = Frame(container, width=g_width, height=g_height, padx=g_pad_x, pady=g_pad_y)
            frame.pack(side=side, padx=g_pad_x, pady=g_pad_y)
        frame.configure(relief=config_edge)
        frame.configure(borderwidth="2")
        return frame

    @staticmethod
    def createLabel(container,text="Default",xc = 0,yc= 0,side=NONE,img_url = NONE):
        if xc >= 0 and yc >= 0:
            if text != "":
                LblTexNor = Label(container, text=text + " = ").place(x=xc, y=yc)
            else:
                try:
                    LblTexNor = Label(container, relief=SOLID,image=img_url).place(x=xc, y=yc)
                except ImportWarning:
                    print("")
                    #self.insertLisBox(listbox,"No se ha podido cargar la imagen, es posible que la imagen no se encuentre en la ruta por defecto!!!",LEFT, "cls")
        else:
            LblTexNor = Label(container, text=text).pack(side=side)
        #return LblTexNor



    #def create_interface_p(self):
        #time.strftime("%c") + " >> " +

# class console:
#
#     creat = creation
#
#     def __init__(self):
#         self.__console = console.creat.console
#
#     @property
#     def console_param(self):
#         return self.__console
#
#     @console_param.setter
#     def console_param(self,item):
#         #llenar consola
#         self.__console.insert(END,item)
#         self.console_param = "PAram"

