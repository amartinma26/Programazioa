# Usamos una busqueda binaria para encontrar el numero que buscamos partiendo por la mitad la lista
zerrend = [12, 45, 7, 89, 23, 56, 91, 34]

sorted_list = sorted(zerrend)


def bilakera_bitarra(zerrenda, bilatua):
    hasiera, bukaera = 0, len(zerrenda) - 1

    while hasiera <= bukaera:
        erdikoa = (hasiera + bukaera) // 2
        if zerrenda[erdikoa] == bilatua:
            return True
        elif zerrenda[erdikoa] < bilatua:
            hasiera = erdikoa + 1
        else:
            bukaera = erdikoa - 1

    return False



print(bilakera_bitarra(sorted_list, 7))  
