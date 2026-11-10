
def parentesis(parent):
    pila = []
    for i in range(len(parent)):
        if parent[i] in "{[(":
            pila.append(parent[i])
        if parent[i] in ")]}":
            if parent[i] == ")" and pila[-1]== "(":
                pila.pop()
            if parent[i] == "]" and pila[-1]== "[":
                pila.pop()
            if parent[i] == "}" and pila[-1]== "{":
                pila.pop()

    return len(pila) == 0
print(parentesis("{[(])}"))



#input: una lista de parentesis
#Output: Bool

#Logica:
#Recorrer la lista buscando los parentesis solo de aperturas.
#guardarlo en una lista y comparar el ultimo de la lista con el primero de cierre. 
#Si coinciden eliminas de la lista las dos 
#Si no coincide la lista ya es False no se elimina de la lista 
#mirar si la longitud de la pila es = 0 









