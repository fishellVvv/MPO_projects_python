# Crear dos variables utilizando los objetos fecha.

# En la primera se representa la fecha (día, mes, año) actual.
# En la segunda se representa la fecha de nacimiento.

# Calcular cuántos años han transcurrido entre ambas fechas y muestra su resultado de maneras diferentes.
# Día, mes y año.
# Hora, minuto y segundo.
# Día de año.
# Día de la semana.
# Nombre del mes.

# Pistas: buscar sobre el paquete datetime para fechas y horas.

from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


entrada = input("Porfa, dime tu fecha de nacimiento (dd/mm/aaaa): ") # solicitamos la fecha de nacimiento
fecha_nacimiento = datetime.strptime(entrada, "%d/%m/%Y") # la convertimos al formato datetime
fecha_actual = datetime.today() # y registramos la fecha de hoy

diferencia_fechas = relativedelta(fecha_actual, fecha_nacimiento) # calculamos el tiempo que ha pasado entre ambas fechas en formato fecha
tiempo_vivido = fecha_actual - fecha_nacimiento # y en formato tiempo

print(f"\nHas vivido ya {diferencia_fechas.years} años, {diferencia_fechas.months} meses y {diferencia_fechas.days} días (casi nada!).")

print(f'Teniendo en cuenta que hoy es {fecha_actual.strftime("%A")}, {fecha_actual.day} de {fecha_actual.strftime("%B")} de {fecha_actual.year} y que son las {fecha_actual.strftime("%H:%M:%S")} :')

print(f"Te informo de que han pasado {fecha_actual.timetuple().tm_yday} días desde el inicio del año (que son {(fecha_actual.timetuple().tm_yday * 24) + fecha_actual.hour} horas).")

# A partir de aquí se me ha ocurrido complicarme la vida y voy a imprimir los dias y horas desde que naciste

print(f"\n(y desde que naciste han pasado {tiempo_vivido.days} días, que son unas {int(tiempo_vivido.total_seconds() // 3600)} horas)\n")