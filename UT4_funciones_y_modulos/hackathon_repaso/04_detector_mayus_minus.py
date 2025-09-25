texto = input("Introduce una frase: ")

mayus = 0
minus = 0

for c in texto:
    if c.isupper():
        mayus += 1
    elif c.islower():
        minus += 1

print(f"Hay {minus} minúsculas y {mayus} mayúsculas.")
