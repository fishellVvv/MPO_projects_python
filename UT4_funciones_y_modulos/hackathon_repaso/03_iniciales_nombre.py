nombre = input("Introduce tu nombre completo: ").split()

iniciales = ""
for p in nombre:
    iniciales += p[0]
    
print(iniciales)