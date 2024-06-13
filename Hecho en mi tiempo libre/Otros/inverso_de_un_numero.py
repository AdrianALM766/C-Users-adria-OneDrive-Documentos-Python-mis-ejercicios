#obtener inverso de numero:
def invertir_num(num):
    aux=0
    while num>0:
        aux+=num%10
        aux*=10
        num//=10
    aux//=10
    return aux
print(invertir_num(154))