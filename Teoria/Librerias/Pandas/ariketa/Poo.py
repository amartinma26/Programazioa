list = []


class ikasleen:
    def __init__(self, izena, adina, ikasgela, nota):
        self.nota = nota
        self.izena = izena
        self.adina = adina
        self.ikasgela = ikasgela


with open("ikasleak.csv", "r") as fitxategia:
    for linea in fitxategia:
        ikasleen(linea.strip())
