numeros = [1,2,3,4,5]
print(numeros)
nombres=["kevin","shakira","Bruce","Rene","Lenin"]
print(nombres[0])
pares=[1,2,3,4,5,6,7,8,9,10]
for e in pares:
    if e%2==0:
        print("El numero es par",e)

lista=[1,2,3,4,5,6,7,8,9,10]
suma=0
for e in lista:
    suma=suma + e
print(suma)


lista=[1,2,3,4,5,6,7,8,9,10]
suma=0
for e in lista:
    suma +=e

print(suma)
print(sum(lista))