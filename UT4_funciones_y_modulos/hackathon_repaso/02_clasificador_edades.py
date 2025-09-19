edad = int(input("Introduce tu edad: "))

if edad <= 12:
    grupo = "niño"
elif edad <= 17:
    grupo = "adolescente"
elif edad <= 64:
    grupo = "adulto"
else:
    grupo = "senior"

print(f"Tu grupo demográfico es {grupo}")
