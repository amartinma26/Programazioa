import random

lehena_da = 0
with open("zenbakiak.txt", "w+") as fitxategia:
    fitxategia.writelines(f"{random.randint(0, 1000)}\n" for i in range(1000))
    fitxategia.seek(0)
    kontadorea = 0
    for lerroa in fitxategia:
        zenbakia = int(lerroa)
        if lehena_da(zenbakia):
            kontadorea += 1
    print(kontadorea)
