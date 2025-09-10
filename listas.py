#Ejercicio 1
numeros_multiplos_de_4 = list(range(0, 100, 4))
print(numeros_multiplos_de_4)

#Ejercicio 2
nombre = "letra"
edad = "numero"
lista_element = list(range(5))
lista_element = [1, 2, 3, nombre, edad]
print(lista_element [-2])

#Ejercicio 3
lista_vacia = []
lista_vacia.append("Mi nombre")
lista_vacia.append("es")
lista_vacia.append("Rodrigo")
print(lista_vacia)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
loro = "loro"
oso = "oso"
animales [-1] = oso
animales [1] = loro
print(animales)

#Ejercicio 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#La función max() devuelve el valor máximo de una lista.

#Ejercicio 6
lista = list(range(10, 30, 5))
print(lista [:2])

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[:2] = ["camioneta", "4x4"]
print(autos)

#Ejercicio 8
dobles = [5,10,15]
dobles.append(5)
dobles.append(10)
dobles.append(15)
print(dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10
lista_anidada = [15, "True", 25.5, 57.9, 30.6, "False"]
print(lista_anidada)