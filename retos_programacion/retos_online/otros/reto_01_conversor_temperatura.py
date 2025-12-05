# El programa pide una temperatura y la transforma de Celsius (°C) a Fahrenheit (°F) o viceversa.

temperatura = float(input("Ingrese temperatura a convertir: "))
escala_temp = input("Es Fahrenheit(F) a Celsius(C)?:").lower()

if escala_temp == "c":
    print((temperatura * 9/5) + 32)
elif escala_temp == "f":
    print((temperatura - 32) * 5/9)
else:
    print("Escala incorrecta.")