# Ejercicio 5

# Escribe un programa que pida el nombre de un día de la semana y muestre si es "laborable" o "fin de semana".

dia = input("Introduce el nombre de un día de la semana: ").lower()

if dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
    print(f"{dia.capitalize()} es un día laborable.")
elif dia in ["sábado", "domingo"]:
    print(f"{dia.capitalize()} es fin de semana.")
else:
    print(f"{dia.capitalize()} no es un día válido. Debe ser un día de la semana (lunes, martes, miércoles, jueves, viernes, sábado o domingo).")