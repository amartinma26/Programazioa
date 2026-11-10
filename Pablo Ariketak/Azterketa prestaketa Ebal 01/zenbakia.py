import re
texto_num = "Hola me llamo asier tengo 20 años naci en 2006 con este numero de telefono 59680954"  # 14
x=re.findall(r"\w+", texto_num)
answ= 0 
for i in x:
    answ+=1

print(answ)



