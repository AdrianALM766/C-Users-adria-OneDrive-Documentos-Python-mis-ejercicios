def suma_recursiva(vector, indice):
    if indice == 0:
        return vector[0]
    else:
        return vector[indice] + suma_recursiva(vector, indice - 1)


v= [4, 2, 3, 1, 5,4]
resul = suma_recursiva(v, len(v) - 1)
print("La suma recursiva del vector es:", resul)
