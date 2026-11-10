import random 

with open("zenbakiak.txt","w") as fitxategia:

    for i in range(1000):
        fitxategia.write(f"{random.randint(0,300)}\n")

