loteria_zenbakia = 78513

zenbaki_irabazlea = 48563

asmatuta = 0

while loteria_zenbakia > 0:
    x = loteria_zenbakia % 10
    i = zenbaki_irabazlea % 10
    if x == i:
        asmatuta += 1
        loteria_zenbakia = loteria_zenbakia // 10
        zenbaki_irabazlea = zenbaki_irabazlea // 10
    else:
        loteria_zenbakia = loteria_zenbakia // 10
        zenbaki_irabazlea = zenbaki_irabazlea // 10
        
print(asmatuta)


"""""
texto1 = str(loteria_zenbakia)
texto2 = str(zenbaki_irabazlea)

answ = 0
for i in texto1:
    for j in texto2:
        if i == j:
            answ = answ + 1
        else:
            continue
print(answ)
""" ""
