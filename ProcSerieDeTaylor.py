from tkinter import *
from sympy import *
import math
import SerieDeTaylor
try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk


class metodosyseries:

    def __init__(self, other, Op):
        print("Estoy en ProcSerieDeTaylor.py")
        #self.AproximacionLineal() # Prueba de Aproximación Lienal
        #print(str(SerieDeTaylor.windows.listbox))
        self.clsprin = other
        #Clasita.retunVAL(Clasita)
        SerieDeTaylor.windows.insertLisBox(other,other.listbox,"Ejecutando...", SerieDeTaylor.LEFT, "cls")
        self.Orden = []
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
        elif Op == '6':
            self.ConvertBase()

    def SerieTaylor(self):
        F_Derivar = self.clsprin.FuncionGET.get()
        A_aprox = self.clsprin.Xget.get()
        G_aprox = self.clsprin.spnBOX.get()
        X_aprox = self.clsprin.X.get()
        EBS_check = self.clsprin.EABSget.get()
        ERL_check = self.clsprin.ERELget.get()
        #---------------------------------->
        A = "0" #0 ó 1 / Mclaurin o Taylor
        self.Serie(F_Derivar, X_aprox, A_aprox, G_aprox)

    def Serie(self,F,X,A,G):#e^x,,0,5
        self.clsprin.Txt.insert(END, F)
        FD = self.Derivada(F, G)
        for i in range(0,len(FD)):
            SerieDeTaylor.windows.insertLisBox(self.clsprin, self.clsprin.lstDevA, str(FD[i]), SerieDeTaylor.LEFT, "",20,20)
        lenDerivadas = len(FD)
        x = Symbol('x')
        XiLimp = float(eval(X))  # 1.0466666666666666 // El float no es encuentra haciendo nada.
        ALimp = float(eval(A))  # 0.785 // Pasa de str a float // Valor a predecir pasado a float.
        OrdenRESULT = 0.0
        for i in range(0, lenDerivadas - 1):
            if OrdenRESULT == 0.0:
                FuncionEnA = FD[i].subs('x', ALimp)
            else:
                FuncionEnA = OrdenRESULT.subs('x', ALimp)
            FuncionDev = FD[i + 1].subs('x', ALimp)
            Exp = i + 1;
            FuncionRes = (XiLimp - ALimp) ** Exp
            Fact = factorial(i + 1)
            OrdenRESULT = FuncionEnA + ((FuncionDev * (FuncionRes ** 1)) / Fact)
            print(" | ", i, " | ", OrdenRESULT, " | ")
            SerieDeTaylor.windows.insertLisBox(self.clsprin, self.clsprin.ListDeriv, str(OrdenRESULT), SerieDeTaylor.LEFT, "")
        self.ErrorABSandREL(F,X,OrdenRESULT)
        self.clsprin.TxtPOL.insert(END,OrdenRESULT)

    def Derivada(self,Funcion,grado):
        Derivada = Funcion
        Derivadas = []
        x = Symbol('x')
        if grado == "0":
            cadena = Derivada.capitalize()
            coun = cadena.count("x")#Numero de x en la función
            Derivadas.insert(0, eval(Funcion))
            for i in range(1, coun + 1):
                Derivada = diff(Derivada)
                Derivadas.insert(i, Derivada)
        elif grado != "0":
            Derivadas.insert(0, eval(Funcion))
            for i in range(1, int(grado) + 1):
                Derivada = diff(Derivada,x)
                Derivadas.insert(i, Derivada)
        return Derivadas

    def ErrorABSandREL(self,F,X,ValE):
        x = Symbol('x')
        Xlimp = float(eval(X))
        FLimp = eval(F)
        ValT = FLimp.subs('x',Xlimp)
        ErrorABS = abs((ValT-ValE))
        ErrorREL = abs(((ErrorABS/ValT)*100))
        self.clsprin.TxtEA.insert(END,ErrorABS)
        self.clsprin.TxtER.insert(END,ErrorREL)

    def MetodoNewton(self):
        Count = 1
        print('Ingrese la Funcion')
        FuncionNew = input()
        print('Ingrese X')
        Xn =  input()
        DerivadaNew = []
        DerivadaNew = self.Derivada(FuncionNew,"0")
        print('|-----------------------------------|')
        print('|-------| Metodo de Newton |--------|')
        print('|___________________________________|')
        Xan = eval(Xn)
        Termina = false
        while Termina == false:
            ##Pruebas
            FuncionEVAL = Xan - (DerivadaNew[0].subs('x',Xan)/DerivadaNew[1].subs('x',Xan))
            print('| X ',Count,' | ',FuncionEVAL,' | ')
            ErrorAc = self.ErrorAcumulado(FuncionEVAL,Xan)
            print('| Error  | ', ErrorAc,'    | ')
            if Xan == FuncionEVAL:
                Termina = true
                print('|-----------------------------------|')
                print('| Final | ',FuncionEVAL,'     |')
                print('|___________________________________|')
            Xan = FuncionEVAL
            Count = Count + 1
            ##Pruebas

    def MetodoBiseccion(self):
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
                ErrAcum = self.ErrorAcumulado(Xr,XrUno)
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

    def MetodoSecante(self):
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

    def ErrorAcumulado(self,Vac,Van):
        Error = abs(((Vac-Van)/Vac)*100)
        return Error

    def AproximacionLineal(self):
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
        SumasVAL = self.sumaVAL(ValX)
        MutiVAL = self.MuliVAL(ValX)
        Elevar = self.Ala(ValX)
        self.CoeCor(CantVal,MutiVAL,SumasVAL,Elevar)
        self.RegresionCuadratica(CantVal,SumasVAL,MutiVAL,Elevar)

    def sumaVAL(self,Val):
        SumaX = 0;
        SumaY = 0;
        for J in range(0,int(len(Val)/2)):
            SumaY = int(Val[(J*2)+1]) + SumaY;
            SumaX = int(Val[J*2]) + SumaX;
        """print("SumaX = " + str(SumaX));
        print("SumaY = " + str(SumaY));"""
        return str(SumaX)+", "+str(SumaY)

    def MuliVAL(sef,Val):
        MultVAL = 0;
        for J in range(0,int(len(Val)/2)):
            MultVAL = (int(Val[(J*2)]) * int(Val[(J*2)+1]))+MultVAL;
        """print("E X*Y = " + str(MultVAL))"""
        return MultVAL

    def Ala(self,Val):
        XAla = 0;
        YAla = 0;
        for J in range(0,int(len(Val)/2)):
            YAla = (int(Val[((J*2)+1)])*int(Val[((J*2)+1)])) + YAla;
            XAla = (int(Val[(J*2)])*int(Val[(J*2)])) + XAla;
        """print("E X^2 = " + str(XAla));
        print("E Y^2 = " + str(YAla));"""
        return str(XAla)+", "+str(YAla)

    def RegresionCuadratica(self,CantVAL,SumasVAL,MutiVAL,Elevar):
        SumaVAL = []
        Ala = []
        SumaVAL = SumasVAL.split(", ")
        Ala = Elevar.split(", ")
        B=(int(CantVAL)*(MutiVAL)-((int(SumaVAL[0]))*(int(SumaVAL[1]))))/(int(CantVAL)*int(Ala[0])-(int(SumaVAL[0])*int(SumaVAL[0])))
        A=((int(SumaVAL[1])-B*(int(SumaVAL[0])))/int(CantVAL))
        print("|--------------------------------------|")
        print("| Y = " + str(A) + " + " + str(B) + "x |")
        print("|--------------------------------------|")
        self.predecir(A,B,"R")

    def predecir(self,A,B,P):
        if P == 'R':
            print("Ingrese el Y a predecir")
            Yinput = input()
            R=((A)+(B)*int(Yinput))
            print("El valor aproximado de " + Yinput + " es : " + str(R))

    def CoeCor(self,CantVal,MutiVal,SumasVAL,Elevar):
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

    def ConvertBase(self):
        n = self.clsprin.NumSIS.get()
        a = self.clsprin.a_base.get()
        ni = int(n)
        ai = int(a)
        ArrBanrio = []
        while ni // ai != 0:
            ArrBanrio.insert(len(ArrBanrio), str(ni%ai))
            ni = ni //ai
        j = len(ArrBanrio) - 1
        numBin = ""
        while j >= 0:
            numBin = numBin + "" + ArrBanrio[j]
            j = j - 1
        self.clsprin.textViewGEN.insert(END,n + " a base 2 = "+ numBin + " ~~~~~~~~")

#if Op == '1':
#    SerieTaylor();
#elif Op == '2':
#    MetodoNewton();
#elif Op == '3':
#    MetodoBiseccion();
#elif Op == '4':
#    MetodoSecante();
#elif Op == '5':
#    AproximacionLineal();


#Resolver la funcion para saber valor real
