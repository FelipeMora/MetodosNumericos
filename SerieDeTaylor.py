#import sys
#sys.path.append('C:\Python27\Lib\lib-tk')
from tkinter import *

class windows:

    def __init__(self, master):
        self.prin = master
        self.winProDeri = Toplevel(master)
        self.winProDeri.title("Derivaciones")
        self.winProDeri.geometry("400x300+20+20")
        self.winProDeri.withdraw()

        self.LFrame = LabelFrame(master, text="Opciones",padx=10, pady=10)
        self.LFrame.pack(fill="both",expand="yes")
        self.FuncionGET = StringVar()
        self.createwidgest()

    def createwidgest(self):
        self.LblTexNor = Label(self.LFrame,text="Ingrese la función : ",font=("Agency FB", 14)).place(x=10,y=0)#Text
        self.CmpGET = Entry(self.LFrame,textvariable=self.FuncionGET).place(x=130,y=10)#Campo de entrada
        self.btnGET = Button(self.LFrame,text="Enviar",width=7,cursor="hand1",relief="groove",command=self.derivar).place(x=260,y=5)#Boton con evento

        self.LblTitleLis = Label(self.winProDeri, text="Derivadas", font=("Agency FB", 14)).place(x=10, y=0)#Label de las derivadas
        self.lstDeriv = Listbox(self.winProDeri, width=50)#listbox en donde se muestran las derivadas

        self.lstDeriv.insert(1, "-2x^3");
        # Termina de agregar
        self.lstDeriv.place(x=10, y=30)

    def derivar(self):
        print("The derivate!!!")
        Derivar = self.FuncionGET.get()
        text = "Procesando derivada... "
        if (Derivar == ""):
            text = "No ha ingresado derivada!"
        if (text == "Procesando derivada... "):
            self.winProDeri.deiconify()
        MosDerivada = Label(self.LFrame, text=text + Derivar, fg="red", font=("Agency FB", 14)).place(x=10, y=60)


root = Tk()
root.geometry("500x600")
root.title("Métodos Numericos")
b = windows(root)
root.mainloop()