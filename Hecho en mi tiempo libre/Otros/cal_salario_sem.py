"""Escribe un programa que calcule el salario semanal 
de un empleado, considerando que se le paga por horas trabajadas. 
El programa debe solicitar al usuario las horas trabajadas por día 
de la semana y la tarifa por hora. Luego, debe calcular el salario 
semanal sumando las horas trabajadas en la semana y aplicando la tarifa por hora"""
#pedir datos
horas_trabajadas=int(input("hola podria definir cuantas horas trabajo esta semana: "))
salario_hora=int(input("digame cuanto es la tarifa por hora: "))
#calcular salario
salario_semanal=horas_trabajadas*salario_hora
#imprimir salario
print("este es el salario semanal: {}".format(salario_semanal))