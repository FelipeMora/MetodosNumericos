from sympy import *
#Pedir al usuario los datos
Orden=[]
def SerieTaylor():
    print("ingrese la funcion :")
    Funcion = input()
    #Funcion
    print("Ingrese el Xi")
    Xi = input()
    XiResul = Xi
    #Xi
    print("Predecir")
    a = input()
    print("Desea ingresar grado de la derivada? S/N")
    op2 = input()
    if op2 == "S":
        print("Ingrese el Grado")
        grad = input()
        Serie(Funcion,Xi,a,grad)
    if op2 == "N":
        Serie(Funcion,Xi,a,"0")

def Serie(Funcion,Xi,a,Grado):
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


print("1.) Serie de Taylor")
print("2.) Metodo de Newton")
print("3.) Metodo de Biseccion")
print("4.) Metodo de Secante")
Op = input();
if Op == '1':
    SerieTaylor();
elif Op == '2':
    MetodoNewton();
elif Op == '3':
    MetodoBiseccion();
elif Op == '4':
    MetodoSecante();


#Resolver la funcion para saber valor real
