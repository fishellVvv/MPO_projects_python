'''
Escribe un programa que reciba un número n entero positivo y que escriba
    esta secuencia de números: un uno, dos doses, tres treses... hasta n enes.
Por ejemplo, si el usuario introduce 5, el programa debe imprimir: 122333444455555
'''

num = int(input("Introduce un número entero positivo: "))

for i in range(num):
    print(f"{i + 1}" * (i + 1), end="")