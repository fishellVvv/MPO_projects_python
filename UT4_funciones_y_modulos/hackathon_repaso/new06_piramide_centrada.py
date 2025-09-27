num = 0
try:
    num = int(input("Introduce un número entero: "))
except ValueError:
    print("Error: el valor debe ser un número entero.")

for i in range(num):
    print(" "*(num-i-1) + "*"*i + "*" + "*"*i + " "*(num-i-1))
for i in range(num-2, -1, -1):
    print(" "*(num-i-1) + "*"*i + "*" + "*"*i + " "*(num-i-1))
