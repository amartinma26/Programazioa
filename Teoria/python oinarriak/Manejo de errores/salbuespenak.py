balio_du = False
"""
while not balio_du:
    try:
        zenbakia = input("Emaidazu zenbaki bat")
        zenbakia = int(zenbakia)
        print(f"zenbakia{zenbakia}da, eta hurrengoa {zenbakia + 1} da")
    except ValueError:
        print("Idatzitakoa ez da zenbaki bat")
        zenbakia = input("Emaidazu zenbaki bat")
        zenbakia = int(zenbakia)
        print(f"zenbakia{zenbakia}da, eta hurrengoa {zenbakia + 1} da")
"""
"""
import urllib.request

try:
    with open("quijote_1.txt", "r") as fitxategia:
        print(fitxategia.read())
except FileNotFoundError:
    print("Fitxategia ez du aurkitua")
    url = "https://gist.github.com/jsdario/6d6c69398cb0c73111e49f1218960f79"
    urllib.request.urlretrive(url, "quijote_1.txt")


try:
    zatikia = 7
    zatitzailea = "a"
    print(zatikia / zatitzailea)

except Exception as e:
    print(f"Errore mota: {type(e).__name__}, mezua: {e}")

"""
def egiaztatu_adina(adina):
    if adina < 0:
        raise ValueError("Adinak ezin du negatiboa izan")
    return adina

try:
    egiaztatu_adina(-5)
except ValueError as e:
    print("Errorea harrapatuta:", e)