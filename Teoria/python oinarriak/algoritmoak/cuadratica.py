zerrenda = [7, 5, 8, 3, 4, 3, 8, 4]


def errepikatuta(zerrenda):
    n = len(zerrenda)
    for i in range(n):
        for j in range(i + 1, n):
            if zerrenda[i] == zerrenda[j]:
                return True  
    return False  


print(errepikatuta(zerrenda))
