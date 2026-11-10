with open("zenbakiak.txt", "r") as fitxategia:
    kalkulatu = []
    for i in fitxategia:
        kalkulatu.append(int(i))
    ordenatu = sorted(kalkulatu)

    racha = 0
    contado_max = ordenatu[0]
    for i in range(len(ordenatu) - 1):
        if ordenatu[i] == ordenatu[i + 1]:
            racha += 1
        else:
            racha = 0

        if contado_max < racha:
            zenbakia = ordenatu[i]
            contado_max = racha
    print(ordenatu[::-1])

    print("Azken zenbakiak")
    print(
        f"Gehien errepikatzen den senbakia {zenbakia} da {contado_max + 1} aldiz errepikatzen da "
    )


# cual esla situacion optimaque tiene que estar la lista para poder hacer eso=
