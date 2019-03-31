import xml.etree.ElementTree as rd
import win32api


class rdxml:

    def __init__(self):
        self.in_tree = rd.parse("menu.xml")
        self.__root = self.in_tree.getroot()
        self.__dat_menu = []
        #for child in self.root.findall("./menu/[@comand]"):#Los que tienen comand.
        #    print(child.attrib["comand"])

    def defind_estructure(self):
        for child in self.__root:
            try: self.set_arr(child.attrib["title"] + "," + child.attrib["comand"])
            except: self.set_arr(child.attrib["title"])
            for child_child in child.getchildren():
                if len(child_child.getchildren()) > 0:
                    for grandchild in child_child.getchildren():
                        self.set_arr(grandchild.text + "," + grandchild.attrib["comand"])
                        #Relación directa con CreateUI, especificamente con createSubMenu

    def set_arr(self,dat_set):
        dat_split = dat_set.split(',')
        if len(dat_split)==1:
            for a in range(len(dat_split)):
                self.__dat_menu.insert(len(self.__dat_menu), dat_split[a])
        else: self.__dat_menu.insert(len(self.__dat_menu),dat_set)
            

    @property
    def get_arr_dat(self):
        return self.__dat_menu

    #@get_arr_dat.setter
    #def get_arr_dat(self,tree):
    #    print("Cambio de arbol")

if __name__ == '__main__':
    v = rdxml()
    v.defind_estructure()
    menu = v.get_arr_dat
    for i in range(len(menu)):
        print(menu[i])
