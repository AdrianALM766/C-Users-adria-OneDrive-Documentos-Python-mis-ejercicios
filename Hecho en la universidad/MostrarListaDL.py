class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.ld = None
        self.li = None
        
class ListaDoblementeLigada:
    def __init__(self):
        self.pri = None
        self.fin=None

    def ins_lista(self,dato):
        nodo=Nodo(dato)
        if(self.pri== None):
            self.pri=nodo
            self.fin=nodo
        else:
            nodo.ld= self.pri
            self.pri.li=nodo
            self.pri=nodo
    def mostrarListaAdelante(self):
        actual=self.pri
        print("")
        print("")
        print("")
        while actual != None:
            print(actual.dato,end= " -> ")
            actual=actual.ld
        print("")
        print("")
        print("")
    def mostrarListaAtras(self):
        actual=self.fin
        print("")
        print("")
        print("")
        while actual != None:
            print(actual.dato,end= " -> ")
            actual=actual.li
        print("")
        print("")
        print("")
    def menu (self):
        me=True
        while (me==True):
            print("MENU")
            print("Crear lista doblemente ligada=1")
            print("mostrar de adelante hacia atras=2")
            print("promedio de atras hacia adelante=3")
            print("salir=4")
            opc=int(input("Ingrese la opcion: "))
            print("-"*10)
            print("-"*10)
            if (opc==1):
                dato=int(input("digame el dato: "))
                self.ins_lista(dato)
            elif(opc==2):
                self.mostrarListaAdelante()
            elif(opc==3):
                self.mostrarListaAtras()
            elif(opc==4):
                print("listo")
                me=False
            else:
                print("elija otra opcion.")
l=ListaDoblementeLigada()
l.menu()