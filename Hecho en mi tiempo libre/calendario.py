#imprimir un año y mes especifico
import calendar


def Menu():
    print()
    year=int(input("Porfavor digite el numero del año: "))
    month=int(input("Porfavor digite el mes: "))
    while month>12 or month<1:
        if month>12 or month<1:
            print("Porfavor digite un mes que exista: ")
            month=int(input())
    print(calendar.month(year,month))

Menu()