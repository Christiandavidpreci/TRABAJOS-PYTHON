##1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.
def contador_ascendente(num):
    cont=0
    while cont<=num:
        print(cont)
        cont+=1
#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.
def contador_descendente(num):
    while num>=0:
        print(num)
        num-=1
#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.

#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.

#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado, el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir "¡Felicitaciones, adivinaste el número!" y terminar.
import random
def adivinar(aleatorio):
    numero=0
    while numero!=aleatorio:
        numero=int(input("ingrese un numero del 1 al 100"))
        if numero>=aleatorio:
            print("el numero ingresado es mayor al numero a adivinar")
        elif numero<aleatorio:
            print("el numero ingresado es mayor al numero a adivinar")
        else:
            print(aleatorio,"feliciades adivino el numero",numero) 
aleatorio=random.randint(1,10)
print(str(aleatorio))


#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.


#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde cero hasta ese número y lo imprima en la pantalla.
def suma_nume_pares(numero):
    cont=0
    suma=0
    while cont<=numero:
        if cont%2==0:
            suma=suma+cont
        cont+=1
    print(suma)
#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la base elevada al exponente y lo imprima en la pantalla.
def potencia(num,exp):
    cont=1
    potencia=1
    while cont<=exp:
        potencia=potencia=num
        cont+=1
    print(potencia)
#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la pantalla.
def calcular_promedio(lista):
    suma=0
    cont=0
    while cont<=len(lista):
        suma=suma+float(lista[cont])
    promedio=suma/len(lista)
    print(promedio)
#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena. Para simplificar el problema, puedes considerar que las palabras están separadas por espacios en blanco.
def contador_palabras(cadenas):
    contador=0
    index=0
if len(cadena)==0:
    contador=0
else:
    contador=1
while index<len(cadena):
    if cadena[index]=="":
        contador+=1
        index+=1
    print(contador)


##menu de opciones###
opcion=1
while opcion>=0 and opcion<=10:
    print("##### menu de opciones####")
    print("1.contador Ascedente")
    print("2.contador Descendiente")
    print("3. suma de numeros")
    print("4. Factorial")
    print("5. Adivinar un numero")
    print("6. contador de vocales")
    print("7. suma de numeros pares")
    print("8. calculo de potencia")
    print("9. calculo de promedio")
    print("10 contador de palabras")
    print("0. salir")
    opcion=int(input("ingrese una opcion:"))
    if opcion==0:
        print("ha seleccionado salir")
        break
    elif opcion==1:
        print("contador ascendente")
        num=int(input("ingrese numero"))
        contador_ascendente(num)
    elif opcion==2:
        print("contador descendente")
        num=int(input("ingresar un numero"))
        contador_descendente(num)
    elif opcion==3:
        print("suma de numeros")
        num=int(input("ingresar un numero"))
        suma_de_numeros(num)
    elif opcion==4:
        print("factorial") 
        num=int(input("ingresar un numero"))
        factorial(num)
    elif opcion==5:
        print("adivinar un numero")
        num=int(input("ingresar un numero del 1 a el 10"))
        adivinar_un_numero(num)
    elif opcion==6:
        print("contador de vocales")
        cadena=int(input("ingresar un mensaje"))
        contadorvocales(cadena)
    elif opcion==7:
       print("suma de numeros pares")
       num=int(input("ingresar numero"))
       suma_de_numeros(num)
    elif opcion==8:
        print("calculo de potencia")
        num=int(input("ingrese un numero"))
        exp=int(input("ingrese un exponente"))
        calculo_de_potencias(num,exp)
    elif opcion==9:
        print("calculo dee promedio")
        lista=input("ingrese las notas suspedidas por comas")
        lista=lista.split(",")
        calculo_de_promedio(lista)
    elif opcion==10:
        print("contador de palabra")

    else:
        print("la opcion no exite en el menu")