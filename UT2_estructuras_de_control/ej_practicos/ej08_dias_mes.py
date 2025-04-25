# Ejercicio 8

# Escribe un programa que pida el nombre de un mes y muestre cuántos días tiene (puedes simplificar febrero a 28 días siempre).

mes = input("Introduce el nombre de un mes: ").lower()

if mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]:
    print(f"{mes.capitalize()} tiene 31 días.")
elif mes in ["abril", "junio", "septiembre", "noviembre"]:
    print(f"{mes.capitalize()} tiene 30 días.")
elif mes == "febrero":
    print(f"{mes.capitalize()} tiene 28 días.")
else:
    print(f"{mes.capitalize()} no es un mes válido.")