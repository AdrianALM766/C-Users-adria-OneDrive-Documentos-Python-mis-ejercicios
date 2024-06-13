#calcular area de un circulo
#importar la libreria math
from math import pi
#pedir dato al usuario
r=float(input("escriba el radio del circulo: "))
#area es igual a 3.14(r)^2 donde r es radio
area= pi * r**2
print("el area del circulo es: {}".format(area))