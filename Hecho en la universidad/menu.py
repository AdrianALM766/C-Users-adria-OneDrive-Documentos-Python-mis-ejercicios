import random
class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.liga=None
        
class ListaSL: #esa SL es simplemente ligada
    def __init__(self):
        self.pri=None
        
    def mostrar_lista(self):
        actual=lista.pri
        print("")
        print("")
        print("")
        while actual != None:
            print(actual.dato,end= " -> ")
            actual=actual.liga
        print("")
        print("")
        print("")
        
    def promedio_numeros(self):
        actual = self.pri
        aco=0
        con=0
        while actual != None:
            print(actual.dato)
            aco+=actual.dato
            actual = actual.liga
            con+=1   
        pro=aco/con
        print("El promedio es: ",pro)
    
    def suma_mul_de3(self):
        actual = self.pri
        aco=0
        while actual != None:
            if actual.dato%3==0:
                print(actual.dato)
                aco+=actual.dato
            actual = actual.liga   
        print("la suma es: ",aco)
        
    def ins_lista(self):
        if (self.pri==None):
            nodo=Nodo(random.randrange(1,100))
            self.pri=nodo
        else:        
            nodo = Nodo(random.randrange(1,100))
            nodo.liga = self.pri
            self.pri = nodo 
def menu ():
    me=True
    while (me==True):
        print("--------------------------------------------------------------- ----")
        print("--                              MENU                              --")
        print("--------------------------------------------------------------------")
        print("Crear lista=1,Mostrar=2,Sumar multiplos del 3=3,promedio=4,Salir=5--")
        print("--------------------------------------------------------------------")
        opc=int(input("Ingrese la opcion: "))
        if (opc==1):
            lista.ins_lista()
        elif(opc==2):
            lista.mostrar_lista()
        elif(opc==3):
            lista.suma_mul_de3()
        elif(opc==4):
            lista.promedio_numeros()
        elif(opc==5):
            print("ponga buena nota profe")
            me=False
                

lista=ListaSL()          
menu()
