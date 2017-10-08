from sympy import *
import os
import math
#Pedir al usuario los datos
class metodosyseries:

    def __init__(self, Op):
        if Op == '1':
            self.SerieTaylor();
        elif Op == '2':
            self.MetodoNewton();
        elif Op == '3':
            self.MetodoBiseccion();
        elif Op == '4':
            self.MetodoSecante();
        elif Op == '5':
            self.AproximacionLineal();

    def SerieTaylor(self):
        print("ingrese la funcion :")
        Funcion = input()
        print("Ingrese el Xi")
        Xi = input()
        print("Predecir")
        a = input()
        print("Desea ingresar grado de la derivada? S/N")
        op2 = input()
        if op2 == "S":
            print("Ingrese el Grado")
            grad = input()
            self.Serie(Funcion, Xi, a, grad)
        if op2 == "N":
            self.Serie(Funcion, Xi, a, "0")

    def Serie(self,Funcion,Xi,a,Grado):
        Derivadas = []
        Derivadas = Derivada(Funcion, Grado)
        print(Derivadas)
        lenDerivadas = len(Derivadas)
        x = Symbol('x')
        XiLimp = float(eval(Xi))  # 1.0466666666666666
        ALimp = float(eval(a))  # 0.785
        OrdenRESULT = 0.0
        print('|-----------------------------------|')
        print('|-------|  Serie de Taylor |--------|')
        print('|___________________________________|')
        for i in range(0, lenDerivadas - 1):
            if OrdenRESULT == 0.0:
                FuncionEnA = Derivadas[i].subs('x', ALimp)
            else:
                FuncionEnA = OrdenRESULT.subs('x', ALimp)
            FuncionDev = Derivadas[i + 1].subs('x', ALimp)
            Exp = i + 1;
            FuncionRes = (XiLimp - ALimp) ** Exp
            Fact = factorial(i + 1)
            OrdenRESULT = FuncionEnA + ((FuncionDev * (FuncionRes ** 1)) / Fact)
            print(" | ", i, " | ", OrdenRESULT, " | ")
        print('______________________________')

    def Derivada(self,Funcion,grado):
        Derivada = Funcion
        Derivadas = []
        x = Symbol('x')
        if grado == "0":
            cadena = Derivada.capitalize()
            coun = cadena.count("x")
            Derivadas.insert(0, eval(Funcion))
            for i in range(1, coun + 1):
                Derivada = diff(Derivada)
                Derivadas.insert(i, Derivada)
        elif grado != "0":
            Derivadas.insert(0, eval(Funcion))
            for i in range(1, int(grado) + 1):
                Derivada = diff(Derivada)
                Derivadas.insert(i, Derivada)
        return Derivadas

    def SerieTaylor(self):
        print("ingrese la funcion :")
        Funcion = input()
        # Funcion
        print("Ingrese el Xi")
        Xi = input()
        XiResul = Xi
        # Xi
        print("Predecir")
        a = input()
        print("Desea ingresar grado de la derivada? S/N")
        op2 = input()
        if op2 == "S":
            print("Ingrese el Grado")
            grad = input()
            self.Serie(Funcion, Xi, a, grad)
        if op2 == "N":
            self.Serie(Funcion, Xi, a, "0")

    def Serie(self,Funcion,Xi,a,Grado):
        Derivadas=[]
        Derivadas = Derivada(Funcion,Grado)
        print(Derivadas)
        lenDerivadas = len(Derivadas)
        x=Symbol('x')
        XiLimp = float(eval(Xi))#1.0466666666666666
        ALimp = float(eval(a))#0.785
        OrdenRESULT = 0.0
        print('|-----------------------------------|')
        print('|-------|  Serie de Taylor |--------|')
        print('|___________________________________|')
        for i in range(0,lenDerivadas-1):
            if OrdenRESULT == 0.0:
                FuncionEnA = Derivadas[i].subs('x',ALimp)
            else:
                FuncionEnA = OrdenRESULT.subs('x',ALimp)
            FuncionDev = Derivadas[i+1].subs('x',ALimp)
            Exp = i +1;
            FuncionRes = (XiLimp-ALimp)**Exp
            Fact = factorial(i+1)
            OrdenRESULT = FuncionEnA+((FuncionDev*(FuncionRes**1))/Fact)
            print(" | ",i," | ",OrdenRESULT," | ")
        print('______________________________')

Orden=[]

def Derivada(Funcion,grado):
    Derivada = Funcion
    Derivadas=[]
    x=Symbol('x')
    if grado == "0":
        cadena = Derivada.capitalize()
        coun = cadena.count("x")
        Derivadas.insert(0,eval(Funcion))
        for i in range(1,coun+1):
            Derivada = diff(Derivada)
            Derivadas.insert(i,Derivada)
    elif grado != "0":
        Derivadas.insert(0,eval(Funcion))
        for i in range(1,int(grado)+1):
            Derivada = diff(Derivada)
            Derivadas.insert(i,Derivada)
    return Derivadas

def MetodoNewton():
    Count = 1
    print('Ingrese la Funcion')
    FuncionNew = input()
    print('Ingrese X')
    Xn =  input()
    DerivadaNew = []
    DerivadaNew = Derivada(FuncionNew,"0")
    print('|-----------------------------------|')
    print('|-------| Metodo de Newton |--------|')
    print('|___________________________________|')
    Xan = eval(Xn)
    Termina = false
    while Termina == false:
        ##Pruebas
        FuncionEVAL = Xan - (DerivadaNew[0].subs('x',Xan)/DerivadaNew[1].subs('x',Xan))
        print('| X ',Count,' | ',FuncionEVAL,' | ')
        ErrorAc = ErrorAcumulado(FuncionEVAL,Xan)
        print('| Error  | ', ErrorAc,'    | ')
        if Xan == FuncionEVAL:
            Termina = true
            print('|-----------------------------------|')
            print('| Final | ',FuncionEVAL,'     |')
            print('|___________________________________|')
        Xan = FuncionEVAL
        Count = Count + 1
        ##Pruebas

def MetodoBiseccion():
    x=Symbol('x')
    Tol = 0.005
    Termina = false
    print('Ingrese la Funcion')
    FunBis = input()
    FunBis = eval(FunBis)
    print('Intervalo A')
    InterA = input()
    InterA = float(eval(InterA))
    print('Intervalo B')
    InterB = input()
    InterB = float(eval(InterB))
    XrUno = 0;
    print('|-----------------------------------|')
    print('|-----| Metodo de Biseccion  |------|')
    print('|___________________________________|')
    Xr = 0
    while Termina == false:
        print('|------------------------------------|' )
        print('| Intervalos  | [',InterA,',',InterB,']' )
        print('|____________________________________|' )
        Xr = ((InterA + InterB)/2)
        if XrUno > 0:
            ErrAcum = ErrorAcumulado(Xr,XrUno)
            print('| ErrAcum     | ', ErrAcum)
            if ErrAcum < Tol:
                Termina = true
        print('| Xr          | ', Xr)
        FenA = FunBis.subs('x',InterA)
        print('| FenA        | ', FenA)
        FenXr = FunBis.subs('x',Xr)
        print('| FenXr       | ', FenXr)
        MulFAXR = FenA * FenXr
        print('| MulFAXR     | ', MulFAXR)
        if MulFAXR < 0:
            InterB = Xr
            print('| b           | ', Xr)
        if MulFAXR > 0:
            InterA = Xr
            print('| a           | ', Xr)
        XrUno = Xr
        print('---------------------------------------')
    print('| R          | ', Xr)
    print('_______________________________________')

def MetodoSecante():
    x=Symbol('x')
    print('Ingrese la Funcion')
    FunSec = input()
    FunSec = eval(FunSec)
    print('Ingrese Xo')
    Xo = input()
    Xo = float(eval(Xo))
    print('Ingrese X1')
    Xuno = input()
    Xuno = float(eval(Xuno))
    print('Desea ingresar el error? S/N')
    Op = input()
    if Op == "S":
        print('Ingrese el Error')
        Error = input()
    Xan = 0;
    Termina = false
    print('|------------------------------------|')
    print('|------| Metodo de Secante  |--------|')
    print('|____________________________________|')
    while Termina == false:
        FuncionEnXuno = FunSec.subs('x',Xuno)
        FuncionEnXo = FunSec.subs('x',Xo)
        X=Xuno-(((Xuno-Xo)/(FuncionEnXuno-FuncionEnXo))*FuncionEnXuno)
        if Xan > 0:
            ErrAcum = abs(X-Xan)
            print('| ErrAcum     | ', ErrAcum, '|')
            if ErrAcum < 0.05:
                Termina = true
        print('| X           | ', X)
        print('|------------------------------------|')
        Xan = X
        Xo = Xuno
        Xuno = X
    print('|____________________________________|')


def ErrorAcumulado(Vac,Van):
    Error = abs(((Vac-Van)/Vac)*100)
    return Error

def AproximacionLineal():
    limpiarCON()
    ValX = []
    print("Cuantos valores ingresara?");
    CantVal = input();
    for i in range(0,int(CantVal)):
        print("Ingrese los valores de X");
        InX = input();
        ValX.append(InX)
        print("Ingrese los valores de Y");
        InY = input();
        ValX.append(InY)
        print("|-----------------|")
        print("|   X    |   Y    |")
        print("|--------|--------|")
        for A in range(0,int(len(ValX)/2)):
            print("|---" + ValX[A*2] +  "---|---" + ValX[(A*2)+1] + "---|")
    SumasVAL = sumaVAL(ValX)
    MutiVAL = MuliVAL(ValX)
    Elevar = Ala(ValX)
    CoeCor(CantVal,MutiVAL,SumasVAL,Elevar)
    RegresionCuadratica(CantVal,SumasVAL,MutiVAL,Elevar)

def sumaVAL(Val):
    SumaX = 0;
    SumaY = 0;
    for J in range(0,int(len(Val)/2)):
        SumaY = int(Val[(J*2)+1]) + SumaY;
        SumaX = int(Val[J*2]) + SumaX;
    """print("SumaX = " + str(SumaX));
    print("SumaY = " + str(SumaY));"""
    return str(SumaX)+", "+str(SumaY)

def MuliVAL(Val):
    MultVAL = 0;
    for J in range(0,int(len(Val)/2)):
        MultVAL = (int(Val[(J*2)]) * int(Val[(J*2)+1]))+MultVAL;
    """print("E X*Y = " + str(MultVAL))"""
    return MultVAL

def Ala(Val):
    XAla = 0;
    YAla = 0;
    for J in range(0,int(len(Val)/2)):
        YAla = (int(Val[((J*2)+1)])*int(Val[((J*2)+1)])) + YAla;
        XAla = (int(Val[(J*2)])*int(Val[(J*2)])) + XAla;
    """print("E X^2 = " + str(XAla));
    print("E Y^2 = " + str(YAla));"""
    return str(XAla)+", "+str(YAla)

def RegresionCuadratica(CantVAL,SumasVAL,MutiVAL,Elevar):
    SumaVAL = []
    Ala = []
    SumaVAL = SumasVAL.split(", ")
    Ala = Elevar.split(", ")
    B=(int(CantVAL)*(MutiVAL)-((int(SumaVAL[0]))*(int(SumaVAL[1]))))/(int(CantVAL)*int(Ala[0])-(int(SumaVAL[0])*int(SumaVAL[0])))
    A=((int(SumaVAL[1])-B*(int(SumaVAL[0])))/int(CantVAL))
    print("|--------------------------------------|")
    print("| Y = " + str(A) + " + " + str(B) + "x |")
    print("|--------------------------------------|")
    predecir(A,B,"R")

def predecir(A,B,P):
    if P == 'R':
        print("Ingrese el Y a predecir")
        Yinput = input()
        R=((A)+(B)*int(Yinput))
        print("El valor aproximado de " + Yinput + " es : " + str(R))

def CoeCor(CantVal,MutiVal,SumasVAL,Elevar):
    limpiarCON()
    SumaVAL = []
    Ala = []
    SumaVAL = SumasVAL.split(", ")
    Ala = Elevar.split(", ")
    Corre=(int(CantVal)*(MutiVal)-int(SumaVAL[0])*int(SumaVAL[1]))/(math.sqrt((int(CantVal)*int(Ala[0]))-int(SumaVAL[0])*int(SumaVAL[0]))*math.sqrt((int(CantVal)*int(Ala[1]))-int(SumaVAL[1])*int(SumaVAL[1])))
    """R=(int(CantVal)*(MutiVal)-int(SumaVAL[0])*int(SumaVAL[1]))
    print("R ---> " + str(R))
    A=math.sqrt((int(CantVal)*int(Ala[0]))-int(SumaVAL[0])*int(SumaVAL[0]))
    print("A = " + str(A))
    B=math.sqrt((int(CantVal)*int(Ala[1]))-int(SumaVAL[1])*int(SumaVAL[1]))
    print("B = " + str(B))
    C=A*B
    print("C = " + str(C))"""
    print(" Coeficiente de Correlación " + str(Corre))

def limpiarCON():
    os.system("cls")


print("|------------------------------------------|")
print("| Desarrollado por Felipe Mora Fajardo/CTB |")
print("|------------------------------------------|")
print("1.) Serie de Taylor")
print("2.) Metodo de Newton")
print("3.) Metodo de Biseccion")
print("4.) Metodo de Secante")
print("5.) Aproximacion Lineal")
Op = input();
if Op == '1':
    SerieTaylor();
elif Op == '2':
    MetodoNewton();
elif Op == '3':
    MetodoBiseccion();
elif Op == '4':
    MetodoSecante();
elif Op == '5':
    AproximacionLineal();


#Resolver la funcion para saber valor real
