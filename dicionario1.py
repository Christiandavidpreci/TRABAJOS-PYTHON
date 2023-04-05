instituto={"carreras":["Big data","Sotware","electrcidad","finanzas","entrenamiento deportivo"],
           "materias":["datos relacionales","datos no relacionales","estadistica","investigacion","aprendizaje de maquina","legislacion"],
           "profesores":["hector mejia","vernonica segarra","diana romero","khaterine alvear","lady sangacha","germania diaz"],
           "notas":[54,70,81,76,71,82]
           }

print("carreras del instituto son: \n\t",instituto["carreras"])
print("las materias de la carrera son : \n\t",instituto["materias"])
print("los profesores de las materias son : \n\t",instituto["profesores"])
print("las notas de las materias son : \n\t",instituto["notas"])

print("el promedio de las notas de la carrera de Big data son :\n\t", sum(instituto["notas"])/len(instituto["notas"]))

suma=0
for e in instituto["notas"]:
    suma += e
print(suma/len(instituto["notas"]))
print(round(suma/len(instituto["notas"]),2))

print(min(instituto["notas"]))
print(max(instituto["notas"]))
print("la nota menor es:",instituto["notas"].index(min(instituto["notas"])))
print(instituto["profesores"][instituto["notas"].index(min(instituto["notas"]))])
print(instituto["materias"][instituto["notas"].index(min(instituto["notas"]))])

