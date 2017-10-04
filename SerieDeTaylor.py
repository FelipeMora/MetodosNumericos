#import sys
#sys.path.append('C:\Python27\Lib\lib-tk')
from tkinter import *
def Derivada():
    Derivar = FuncionGET.get()
    Show = "Procesando derivada... "
    if Derivar == "":
        Show = "No ha ingresado derivada!"
    else:
        VentanaProcDeriv.deiconify()
        ValReal(Derivar)
    MosDerivada = Label(ventana,text=Show + Derivar,fg="red",font=("Agency FB",14)).place(x=20,y=60)

def ValReal(Derivar):
    print("Sacar el valor real de " + Derivar)
    #Creacion de un nuevo LabelFrame
    LFrame2 = LabelFrame(ventana, text="Serie de Taylor",padx=10,pady=10,cursor="arrow")
    LFrame2.pack(fill="both",expand="yes")
    LFrame2.config(width=50)
    #Widgets pertenecientes a el LabelFrame
    lbValRe = Label(LFrame2,text="Valor real: ",font=("Agency FB",14)).place(x=10,y=80)
    lbValXi = Label(LFrame2,text="Xi = ",font=("Agency FB",14)).place(x=130,y=80)
    campoGETXi = Entry(LFrame2,textvariable=Xi).place(x=230,y=80)

#Creating windows
ventana = Tk()
ventana.geometry("500x600+50+50")
ventana.title("Métodos Numéricos")

VentanaProcDeriv = Toplevel(ventana)
VentanaProcDeriv.title("Derivaciones")
VentanaProcDeriv.geometry("400x300")
VentanaProcDeriv.withdraw()

LFrame = LabelFrame(ventana, text="Opciones",padx=10,pady=10)
LFrame.pack(fill="both",expand="yes")

Xi = IntVar()
FuncionGET = StringVar()

Etiqueta = Label(LFrame,text="Ingrese la funcion: ",font=("Agency FB",14)).place(x=10,y=0)
campoGET = Entry(LFrame,textvariable=FuncionGET).place(x=130,y=10)
botonGETFun = Button(LFrame,text="Enviar",width=7, height=0,cursor="hand1",relief="groove",command=Derivada).place(x=260,y=5)
#Windows of derived
LabelTitleLis = Label(VentanaProcDeriv,text="Derivadas",font=("Agency FB",14)).place(x=10,y=0)
lstDeriv = Listbox(VentanaProcDeriv, width=60)
#Add to list
lstDeriv.insert(1,"-2x^3");
#End of add
lstDeriv.place(x=10,y=30)
#Show the windows
ventana.mainloop();
