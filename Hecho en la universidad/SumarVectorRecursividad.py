class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def suma_recursiva(vector, indice=1):
        if indice >=len(vector):
            return 0
        else:
            return vector[indice] + suma_recursiva(vector, indice + 1)

def menu():
    vector = [None]
    me = True
    while me:
        print(Color.GREEN)
        print("|" + "=" * 54 + "|")
        print("MENU".center(56))
        print("1. Crear vector".center(56))
        print("2. Mostrar suma".center(56))
        print("3. Salir".center(56))
        print("|" + "=" * 54 + "|")
        print(Color.RESET)
        opc = int(input(Color.YELLOW + "Ingrese la opción: ".center(56) + Color.RESET))
        if opc == 1:
            dato = int(input(Color.YELLOW + "Ingrese el dato: ".center(56) + Color.RESET))
            vector.append(dato)
        elif opc == 2:
            if len(vector) > 1:
                resul = suma_recursiva(vector)
                print(Color.MAGENTA)
                print("La suma recursiva es: {}".format(resul).center(56))
                print(Color.RESET)
            else:
                print(Color.RED + "No hay elementos en el vector." + Color.RESET)
        elif opc == 3:
            print(Color.RED + "Saliendo del programa...".center(56) + Color.RESET)
            me = False
        else:
            print(Color.RED + "Opción inválida. Por favor, elija otra opción." + Color.RESET)


menu()
