abecedario=['A','B','C','D','E','F','G','H','I']
print(len(abecedario))
print(abecedario[0])
print(abecedario[len(abecedario)-1])
print(abecedario[len(abecedario)-5])
print(abecedario[5])
print(abecedario[1])
print(abecedario[3])
print(abecedario[-8])
print("si la letra E esta dentro de la lista ")
if "E"in abecedario:
    print("su nota es irregular")

notas=[10,9,8,7,6,5,4,3,2]
print(notas)
alumnos=[abecedario,notas]
print(alumnos)
abecedario.append("J")
abecedario.append("K")
abecedario.append("L")
print(abecedario)

alumnos.clear()
print(alumnos)
nota2=(20,21,22,23)
notas.extend(nota2)
print(notas)

notas.extend([1,2,3,4,5,6,7,8])
print(notas)
print(len(notas))

print(notas.count(2))
print(abecedario.index("H"))
print(abecedario[7])

print(notas.index(22))

notas.insert(5,10)
print(notas)  
print(len(notas))

notas.insert(-1,10)
print(notas)  
print(len(notas))
notas.pop(0)
notas.remove(9)