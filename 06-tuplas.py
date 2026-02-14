
tupla = (1,2,3,4,5,2,3,2)

print(type(tupla))

print(tupla)

print("El elemento de la tupla es: ",tupla[2])

for i in tupla:
    print(i)

print("La cantidad de elementos de la tupla es: ",len(tupla))
print("La cantidad de veces que se repite el número 2 es: ",tupla.count(2))
print("El índice del número 3 es: ",tupla.index(3))

"tupla[1] = 2" #Esto marcará error ya que las tuplas son inmutables

datos =("Juan", 20, True)

una_tupla = (5,)

print(datos)
print(una_tupla)