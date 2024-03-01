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

l=ListaDoblementeLigada()
aux=5
a=6
l.ins_lista(aux)
l.ins_lista(a)
l.mostrarListaAdelante()
l.mostrarListaAtras()