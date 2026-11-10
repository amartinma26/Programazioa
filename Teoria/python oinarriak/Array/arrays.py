zerrenda = [3, 7, 1, 9, 4, 6]

print(zerrenda)
print(zerrenda[2])
print(zerrenda[-1])
print(len(zerrenda))


print(zerrenda[1:3])  # -> de la primera posicon hasta la 3
print(zerrenda[:3])  # -> desde el principio hasta el 3
print(zerrenda[3:])  # ->empieza del 3 hasta el final
print(zerrenda[::2])  # ->del principio a fin pero en paso de 2[2,4,6,8,10]
print(zerrenda[::-1])  # ->lista completa (al reves)
# Indica la primera:segunda:paso

zerrenda.append(10)  # -> añadimos el numero a la lista ( al final)
zerrenda.insert(1, 100)  # ->añadimos el numero 100 en la primera posicon
# poscion, numero

zerrenda.remove(100)  # -> Elimina EL VALOR que indiquemos no la posicion
azkena = zerrenda.pop(100)  # -> elimina el numero que indiqemos mediante posicion ( y luego nos lo devuelve)Por defecto elimina el ultimo
del zerrenda[0]#->Elimina directamente el numero de la psicion
