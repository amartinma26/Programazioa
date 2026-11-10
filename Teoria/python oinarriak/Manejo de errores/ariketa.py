zenbaki_1 = int(input("Esan zenbaki bat ->"))
zenbaki_2 = int(input("Esan beste zenbaki bat->"))


def zatiketa(zen1, zen2):
    asnw = zen1 / zen2
    return asnw


try:
    print(zatiketa(zenbaki_1, zenbaki_2))
except ZeroDivisionError:
    print("Mesedez jarri 0 ez den zenbaki bat!")
except ValueError:
    print("Mesedez zenbaki bat jarri")


def egiaztatu_nota(nota):
    if nota > 10 or nota < 10:
        raise ValueError("Nota 10 baino txikiagoa izan behar du")


try:
    egiaztatu_nota(5)
except ValueError as e:
    print("Errorea arrapatuta:", e)
