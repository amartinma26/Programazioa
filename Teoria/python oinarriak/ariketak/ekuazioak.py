print("Demagun ekuazio hau daukagula ax2² + bx + c = 0")
a = int(input("Emaidazu a"))
b = int(input("Emaidazu b"))
c = int(input("Emaidazu c"))


ekuazio = (b**2) - (4 * a * c)

if ekuazio > 0:
    print("Daka bi erantzun")
elif ekuazio == 0:
    print("Soluzio bakarra dauka ")
else:
    print(" Ez daka erantzuna")
