correos = input("Introduce correos separados por comas: ").split(", ")
dic_correos = {}

for correo in correos:
    dominio = correo.split("@")[1].split(".")[0]
    if dominio not in dic_correos.keys():
        dic_correos[dominio] = list()
    dic_correos[dominio].append(correo)

print(dic_correos)
