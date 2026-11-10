Zerrenda = [5, 7, 3, 2, 1, 4, 6, 9]


def haundiena(num):
    aux = num[0]  
    for i in num:
        if i > aux:
            aux = i
    return aux  

print(haundiena(Zerrenda)) 