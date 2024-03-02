class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

class Nodo:
    def __init__(self,dato):
        self.dato=dato
        #anterior
        self.li = None
        #siguiente
        self.ld = None
        
class ListaDoblementeLigada:
    def __init__(self):
        self.pri = None
        self.fin=None

    def ins_alfinal(self,dato):
        nodo=Nodo(dato)
        if self.pri== None:
            self.pri=nodo
            self.fin=nodo
        else:
            self.fin.ld= nodo
            nodo.li=self.fin
            self.fin=nodo

    def mostrarListaAdelante(self,actual):
        if actual == None:
            print("")
        else:
            print(actual.dato, end=" -> ")
            self.mostrarListaAdelante(actual.ld)

    def mostrarListaAtras(self,actual):
        if actual==None:
            print("")
        else:
            print(actual.dato,end= " -> ")
            self.mostrarListaAtras(actual.li)
    def menu(self):
        me = True
        while me:
            print(Color.GREEN)
            print( "|" + "=" * 54 + "|")
            print("MENU".center(56))  # Centra el título en una línea de 56 caracteres
            print("1. Instanciar lista".center(56))
            print("2. Mostrar lista de adelante hacia atrás".center(56))
            print("3. Mostrar lista de atrás hacia adelante".center(56))
            print("4. Salir".center(56))
            print("|" + "=" * 54 + "|")
            print(Color.MAGENTA)
            opc = int(input("Ingrese la opción: ".center(50)))
            print(Color.RESET)
            if opc == 1:
                print(Color.YELLOW)
                dato = int(input("Ingrese dato: ".center(50)))
                print(Color.RESET)
                self.ins_alfinal(dato)
            elif opc == 2:
                print(Color.MAGENTA)
                aux = self.pri
                self.mostrarListaAdelante(aux)
                print(Color.RESET)
            elif opc == 3:
                print(Color.MAGENTA)
                aux = self.fin
                self.mostrarListaAtras(aux)
                print(Color.RESET)
            elif opc == 4:
                print(Color.RED)
                print("Saliendo del programa...".center(56))
                print(Color.RESET)
                me = False
            else:
                print(Color.RED)
                print("Elija otra opción.".center(56))
                print(Color.RESET)

l=ListaDoblementeLigada()
l.menu()