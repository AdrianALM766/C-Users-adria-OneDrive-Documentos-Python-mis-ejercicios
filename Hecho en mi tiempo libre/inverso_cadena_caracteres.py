#invertir cadena:
cadena="Python"
for i in range(len(cadena)-1,-1,-1):
    print(cadena[i], end='')
print()
print(cadena[::-1])
#obtener inverso de numero:
def invertir_num(num):
    aux=0
    #siempre que num sea mayor a cero hacer
    while num>0:#num=345 /// num=34 /// num=3 /// num=0
        #aux sera igual a aux mas num modulo de 10 /// aux=aux+(5) igual a 5 /// aux+=4 igual a 54 /// aux+=3 igual a 543
        aux+=num%10
        #aux igual a aux por 10 /// aux=5*10 igual a 50 /// aux*=10 igual a 540 /// aux*=10 igual a 5430
        aux*=10
        #num igual a num division entera entre 10 /// num=345//10 igual a 34 /// num//=10 igual a 3 /// num//=10 igual a 0
        num//=10
    aux//=10 #aux//=10 igual a 543
    return aux #retorna 543
#print(invertir_num(345))  
print(13%10)