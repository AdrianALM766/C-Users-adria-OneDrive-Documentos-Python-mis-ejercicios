class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.ligaIzquierda=None
        self.ligaDerecha=None

class ListaDL:
    def __init__(self):
        self.primero=None
        self.ultimo=None
    
    def agregar_final(self,dato):
        nodo=Nodo(dato)
        if self.primero==None and self.ultimo==None:
            self.primero=nodo
            self.ultimo=nodo
        else:
            self.ultimo.ligaDerecha= nodo
            nodo.ligaIzquierda=self.ultimo
            self.ultimo=nodo
    
    def agregar_principio(self,dato):
        nodo=Nodo(dato)
        if self.primero==None and self.ultimo==None:
            self.primero=nodo
            self.ultimo=nodo
        else:
            nodo.ligaDerecha= self.primero
            self.primero.ligaIzquierda=nodo
            self.primero=nodo
    
    def mostrar_lista(self):
        actual=self.primero
        print("")
        while actual != None:
            print(actual.dato,end= " -> ")
            actual=actual.ligaDerecha
        print("")



