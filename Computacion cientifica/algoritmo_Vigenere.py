#en proceso
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
#funcion vigenere
def vigenere(mensaje,clave):
    #auxilar es igual a la clave dada por el sistema
    auxiliar=clave
    i=0
    mensaje_encryptado=""
    #siempre que el tamaño de la clave sea diferente del tamaño del mensaje entonces
    while len(auxiliar) != len(mensaje):
        #esto hace que la clave tenga la misma cantidad de caracteres quel mensaje 
        #ejemplo la clave es key y el mensaje es dolor el auxiliar tomara valor de keyke
        auxiliar=auxiliar+clave[i]
        i=i+1
    i=0
    j=0
    vectM=[]
    vectK=[]
    #pasar el mensaje a numeros
    while len(vectM) != len(mensaje):
        if mensaje[j] == alfabeto[i]:
            vectM.append(i)
            j=j+1
            if j >= len(mensaje):
                break
        i=i+1
        if i>=len(alfabeto):
            i-=len(alfabeto)
    i=0
    j=0
    #pasar la clave a numeros
    while len(vectK) != len(auxiliar):
        if auxiliar[j] == alfabeto[i]:
            vectK.append(i)
            j=j+1
            if j >= len(auxiliar):
                break
        i=i+1
        if i>=len(alfabeto):
            i-=len(alfabeto)
    a=0
    #sumar los numeros de la clave y el mensaje, esos numeros pasarlos a letras
    while len(mensaje_encryptado) != len(mensaje):
        num=vectM[a]+vectK[a]
        if num>=len(alfabeto):
            num-=len(alfabeto)
        mensaje_encryptado+=alfabeto[num]
        a=a+1
    return mensaje_encryptado

mensaje="hola"
key="key"
mensaje_encrip=vigenere(mensaje,key)
print("el  mensaje encriptado es: {}, la clave es: {}".format(mensaje_encrip,key))
print("el mensaje original es: {}".format(mensaje))
