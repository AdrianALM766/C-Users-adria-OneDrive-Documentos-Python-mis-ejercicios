#suma de numeros pares
def Sumar_npar(lista):
    suma=0
    i=0
    #recorer lista
    while i<len(lista):
        #si el numero en la lista es par
        if lista[i]%2==0:
            #suma total de los numeros pares
            suma+=lista[i]
        i+=1
    return suma
li=[1,2,2,4,10]
var=Sumar_npar(li)
print(var)