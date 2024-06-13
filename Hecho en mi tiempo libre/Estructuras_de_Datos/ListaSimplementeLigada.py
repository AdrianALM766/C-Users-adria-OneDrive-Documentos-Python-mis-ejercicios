#clase nodo
class Nodo:
    def __init__(self,dato):
        #dato
        self.dato=dato
        #liga
        self.liga=None
#esta lista inserta los nodos de atras hacia adelante
class listaSL_AgregarAlPrincipio:
    def __init__(self):
        self.primero=None
    
    def instanciar_lista(self,datos):
        nodo= Nodo(datos)
        if self.primero==None:
            self.primero=nodo
        else:
            nodo.liga=self.primero
            self.primero=nodo
    def mostrar_lista(self):
        actual=self.primero
        print("")
        while actual != None:
            print(actual.dato,end= " -> ")
            actual=actual.liga
        print("")

#esta lista inserta los nodos de adelante hacia atras
class listaSL_AgregarAlFinal:
    def __init__(self):
        self.primero=None
    
    def instanciar_lista(self,datos):
        nodo= Nodo(datos)
        if self.primero==None:
            self.primero=nodo
        else:
            actual=self.primero
            while actual.liga is not None:
                actual= actual.liga
            actual.liga=nodo
    def mostrar_lista(self):
        actual=self.primero
        print("")
        while actual != None:
            print(actual.dato,end= " -> ")
            actual=actual.liga
        print("")
