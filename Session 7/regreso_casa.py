import time

hora_salida = 19
hora_actual = int(time.strftime("%H"))
minutos_actual = int(time.strftime("%M"))

print("Calculo de tiempo para la jornada laboral")

if hora_actual < hora_salida:
    minutos_faltantes = 60 - minutos_actual
    hora_faltante = 18 - hora_actual
    print("Falta aun ", hora_faltante,":", minutos_faltantes, "Horas")

else:
    print("Ya se te acabo la jornada laboral")