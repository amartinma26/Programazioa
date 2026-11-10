def kapikua(num):
    texto = str(num)
    lista = list(texto)
    return lista[::-1] == lista


print(kapikua(1234321))

# Respuesta de Pablo

zenbakia = int(input(" Zenbaki bat eman"))

aux = zenbakia
aldrebes = 0

print(aux, aldrebes)
while aux < 0:
    azken_zenbakia = aux % 10
    aldrebes = aldrebes * 10 + azken_zenbakia
    print(aux, aldrebes)

if aldrebes == zenbakia:
    print("kapikua")
else:
    print("ez da kapikua")
