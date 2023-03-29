#ejercicios
#Christian Preciado
print("ejercicio1")
print("CURSO DE FUNDAMENTOS DE PYTHON")
print("NOMBRE: Christian Preciado\n")
a=int(input("ingrese numero1"))
b=int(input("ingrese numero2"))
respuesta=a==b
respuesta1=a!=b
respuesta2=a>b
respuesta3=a>=b
print("\nOPCION1")
print("los numeros:"+ str (a)+" y "+ str(b)+" son iguales: "+str (respuesta))
print("los numeros :"+ str (a)+" y "+ str(b)+" son diferentes: "+str (respuesta1))
print("los numeros :"+ str (a)+" y "+ str(b)+" es mayor que el segundo: "+str (respuesta2))
print("la suma de :"+ str (a)+" y "+ str(b)+" es mayor o igual que el primero: "+str (respuesta3))
print("\nOPCION 2")
print(f"los numeros : {a} y {b} son iguales: {respuesta}")
print(f"los numeros : {a} y {b} son diferentes: {respuesta1}")
print(f"los numeros : {a} y {b} es mayor que el segundo: {respuesta2}")
print(f"los numeros : {a} y {b} es mayor o igual que el primero: {respuesta3}")
print("\nOPCION 3")
print("los numeros: {} y {} son iguales: {}".format (a,b,respuesta))
print("los numeros: {} y {} son diferentes: {}".format (a,b,respuesta1))
print("los numeros: {} y {} es mayor que el segundo: {}".format (a,b,respuesta2))
print("los numeros: {} y {} es mayor o igual que el primero: {}".format (a,b,respuesta3))
print("\nOPCION4")
print("los numeros:",a,"y",b,"son iguales ",respuesta)
print("los numeros:",a,"y",b,"son diferentes ",respuesta1)
print("los numeros:",a,"y",b," es mayor que el segundo",respuesta2)
print("los numeros:",a,"y",b," es mayor o igual que el primero  ",respuesta3)