def suma_recursiva(vector, indice=0):
    if indice >=len(vector):
        return 0
    else:
        return vector[indice] + suma_recursiva(vector, indice + 1)




def menu():
    vector=[]
    me=True
    while (me==True):
            print("MENU")
            print("Crear vector=1")
            print("mostrar suma=2")
            print("salir=3")
            opc=int(input("Ingrese la opcion: "))
            print("-"*10)
            print("-"*10)
            if (opc==1):
                dato=int(input("ingrese el dato: "))
                vector+=[dato]
                print(vector)
            elif(opc==2):
                resul=suma_recursiva(vector)
                print("la suma recursiva es: ",resul)
            elif(opc==3):
                print("listo")
                me=False
            else:
                print("elija otra opcion.")

menu()
