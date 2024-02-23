"""
Nodo: 
En programacion, concretamente en estructuras de datos, un nodo es uno de los
elementos de una lista enlazada, de un arbol o de un grafo, cada nodo sera una estructura o
registro que dispondra de varios campos, y almenos uno de esos campos sera
un puntero o referencia a otro nodo, de forma que, conocido un nodo, apartir de
esa referencia, sera posible en teoria tener acceso a otros nodos de la estructura

"""

#clase nodo
class Nodo:
    def __init__(self,dato):
        #dato
        self.dato=dato
        #liga
        self.liga=None
#clase lista simplemente ligada
class Lista_simplente_ligada:
    def __init__(self):
        #esta sera la llave para acceder al primer nodo 
        self.pri=None
    def ins_lista(self,dato):
        #si self.pri igual a None entonces:
        if (self.pri==None):
            #crear nodo e ingresar dato
            nodo=Nodo(dato)
            #el self.pri sera nodo
            self.pri=nodo
        else:
            #crear nodo e ingresar dato      
            nodo = Nodo(dato)
            #la liga del nodo sera self.pri(osea la dirreccion de memoria del nodo anterior)
            nodo.liga = self.pri
            #self.pri sera ahora la dirreccion de memoria de este nodo
            self.pri = nodo 
    #mostrar lista
    def mostrar_lista(self):
        actual=self.pri
        print("")
        while actual != None:
            print(actual.dato,end= " -> ")
            actual=actual.liga
        print("")

prueba1= Lista_simplente_ligada()
prueba1.ins_lista(input("escribe algo: "))
prueba1.ins_lista(input("escribe algo: "))
prueba1.mostrar_lista()
