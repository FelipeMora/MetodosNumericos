from tkinter import *
import time
import xml.etree.ElementTree as rd

try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk


class parameters_interfaces:
    def __init__(self, master):
        self.__master = master
        self.photo = PhotoImage(file="img\ctb.png")

    def parameters_ui_p(self):
        print("Principal")
        creation.create_message(self.__master, '''Métodos Numéricos

        Metodologías que utilizan operaciones algebraicas
        y aritmeticas para resolver de forma aproximada 
        ecuaciones complejas, en muchos de ellos es requerido 
        derivadas, integrales y ecuaciones difereniales.''', w=370, x=80, y=210)
        creation.create_message(self.__master, '''Notas

        Este software no sera desarrollado bajo ninguna metodologia
        en especial, ni tampoco se le aplicara un plan de pruebas
        estructurado. Por tal motivo, es posible que contenga una
        cantidad produente de errores.''', w=370, x=460, y=210)
        creation.create_frame(self.__master, g_width=5, g_height=125, side=NONE, g_pad_x=10, g_pad_y=0, pack=0, gx=430,
                              gy=210, place_pre=0, config_edge=RIDGE)
        creation.create_label(self.__master, text="", xc=60, yc=25, side=NONE,
                              img_url=self.photo)  # No esta agregando la imagen
        creation.create_frame(self.__master, g_width=745, g_height=5, side=0, g_pad_x=0, g_pad_y=0, pack=0, gx=70,
                              gy=360, place_pre=0, config_edge=RIDGE)

    def parameters_ui_pmt(self):
        print("Polinomio de Mclaurin/Taylor")

    def parameters_ui_snp(self):
        print("Sistema de numeración posicional")

    def parameters_ui_fb(self):
        print("Fracciones binarias")

    def parameters_ui_mn(self):
        print("Metodo de Newton")


class creation(parameters_interfaces):
    def __init__(self, master, heigth, width):
        super(creation, self).__init__(master)
        self.in_tree = rd.parse("menu.xml")
        self.__root = self.in_tree.getroot()
        self.__master = master
        self.console = NONE
        self.heigth = heigth
        self.width = width
        # variables iniciales

    @staticmethod
    def create_labelframe(container, text="Default", g_padx=0, g_pady=0):
        print("Crea label frame")
        l_frame = LabelFrame(container, text=text, padx=g_padx, pady=g_pady)
        l_frame.pack(fill="both", expand="yes")
        return l_frame

    def __init_menu(self):
        menu = Menu(self.__master)
        menu.configure(relief=GROOVE, borderwidth="10")
        self.__master.config(menu=menu)
        return menu

    @staticmethod
    def __create_submenu(menu, title, sub, cmad):  # titles debe ser una lista)
        sub_menu = Menu(menu)
        menu.configure(relief=GROOVE, borderwidth="10")
        if sub == "":
            menu.add_command(label=title, command=cmad)
        else:
            menu.add_cascade(label=title, menu=sub_menu), sub_menu.add_command(label=sub, command=cmad)
        return menu

    def __defined_structure_menu(self, menu):
        for child in self.__root:
            try:
                self.__create_submenu(menu, child.attrib["title"], "", child.attrib["command"])
            except TypeError:
                for child_child in child.getchildren():
                    if len(child_child.getchildren()) > 0:
                        for grandchild in child_child.getchildren():
                            self.__create_submenu(menu, child.attrib["title"], grandchild.text,
                                                  grandchild.attrib["command"])

    @staticmethod
    def __create_scroll(container, Gorient):  # Contenedor y la orientación.
        scrollbar = Scrollbar(container, orient=Gorient)  # orient=Gorient
        scrollbar.pack(side=RIGHT, fill=Y)
        return scrollbar

    @staticmethod
    def __create_lisbox(container, g_height, g_width=50, command=NONE, eje=NONE):  # Crea una lista
        lst_box = Listbox(container, height=g_height, width=g_width)
        if eje == "y": lst_box['yscrollcommand'] = command.set
        if eje == "x": lst_box['xscrollcommand'] = command.set
        lst_box["bg"] = "#fff"
        return lst_box

    def create_menu(self):
        # self.parameters_ui_p()
        menu = self.__init_menu()
        self.__defined_structure_menu(menu)

    def __create_console(self):
        Eje = "y"
        y_scrollbar = self.__create_scroll(self.__master, VERTICAL)
        list_scrollbar = self.__create_lisbox(self.__master, 5, self.width, y_scrollbar, eje="y")
        if Eje == "y":
            y_scrollbar['command'] = list_scrollbar.yview
        else:
            y_scrollbar['command'] = list_scrollbar.xview
        list_scrollbar.configure(relief=GROOVE)
        list_scrollbar.configure(borderwidth="2")
        list_scrollbar.pack(side=LEFT)
        return list_scrollbar

    @property
    def create_console(self):
        self.console = self.__create_console()
        return self.console

    @create_console.setter
    def create_console(self, element):
        self.console.insert(END, time.strftime("%c") + " >> " + element)
        self.console.see(END)

    @staticmethod
    def create_message(container, text, w, x, y):
        msg = Message(container, width=w)
        msg.place(x=x, y=y)
        msg.configure(text=text)

    @staticmethod
    def create_frame(container, g_width, g_height, side, g_pad_x, g_pad_y, pack, gx, gy, place_pre, config_edge):
        if pack == 0:
            frame = Frame(container, width=g_width, height=g_height)
            if place_pre == 0: frame.place(x=gx, y=gy)
        else:
            frame = Frame(container, width=g_width, height=g_height, padx=g_pad_x, pady=g_pad_y)
            frame.pack(side=side, padx=g_pad_x, pady=g_pad_y)
        frame.configure(relief=config_edge)
        frame.configure(borderwidth="2")
        return frame

    @staticmethod  # REVISIÓN
    def create_label(container, text="Default", xc=0, yc=0, side=NONE, img_url=NONE):
        if xc >= 0 and yc >= 0:
            if text != "":
                LblTexNor = Label(container, text=text + " = ").place(x=xc, y=yc)
            else:
                try:
                    LblTexNor = Label(container, relief=SOLID, image=img_url).place(x=xc, y=yc)
                except ImportWarning:
                    print("Error")
                    # self.insertLisBox(listbox,"No se ha podido cargar la imagen, es posible que la imagen no se encuentre en la ruta por defecto!!!",LEFT, "cls")
        else:
            LblTexNor = Label(container, text=text).pack(side=side)

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
