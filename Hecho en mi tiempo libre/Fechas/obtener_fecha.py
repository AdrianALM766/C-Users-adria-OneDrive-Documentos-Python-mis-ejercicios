import datetime
#obtener hora actual
horaActual= datetime.datetime.now()
print(horaActual)
print(type(horaActual))
print(horaActual.strftime('%d/%m/%Y %H:%M:%S'))
