class Nodo:
    def __init__(self,edad,sexo):
        self.edad = edad
        self.sexo=sexo
        self.ld = None
        self.li = None
        
class ListaDoblementeLigada:
    def __init__(self):
        self.pri = None
        self.fin=None

    def ins_lista(self,edad,sexo):
        nodo=Nodo(edad,sexo)
        if(self.pri== None):
            self.pri=nodo
            self.fin=nodo
        else:
            nodo.ld= self.pri
            self.pri.li=nodo
            self.pri=nodo

    def promedioH(self):
        actual = self.pri
        acu=0
        con=0
        while actual != None:
            if  actual.sexo == 1:
                acu+=actual.edad
                con+=1
            actual = actual.ld   
        pro=acu/con
        print("El promedio de edad en Hombres es: ",pro)

    def promedioM(self):
        actual = self.pri
        acu=0
        con=0
        while actual != None:
            if actual.sexo == 2:
                acu+=actual.edad
                con+=1
            actual = actual.ld   
        pro=acu/con
        print("El promedio de edad en Mujeres es: ",pro)

    def menu (self):
        me=True
        while (me==True):
            print("MENU")
            print("Crear lista doblemente ligada=1")
            print("promedio edad hombre=2")
            print("promedio edad mujer=3")
            print("salir=4")
            opc=int(input("Ingrese la opcion: "))
            print("-"*10)
            print("-"*10)
            if (opc==1):
                edad=int(input("digame la edad: "))
                sexo=int(input("digame el sexo: "))
                while sexo>2:
                    sexo=int(input("el sexo que ingreso no es valido en esta carrera no me importa si usted es un avion sovietico o no solo elija 1=hombre 2=mujer: "))
                self.ins_lista(edad,sexo)
            elif(opc==2):
                self.promedioH()
            elif(opc==3):
                self.promedioM()
            elif(opc==4):
                print("profe pa que vea que en este curso si nos esforzamos.")
                me=False
            else:
                print("elija otra opcion.")

lista_prueba1=ListaDoblementeLigada()
lista_prueba1.menu()
