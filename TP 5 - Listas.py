alumnos = ["Alumno1", "Alumno2", "Alumno3", "Alumno4", "Alumno5", "Alumno6", "Alumno7", "Alumno8", "Alumno9", "Alumno10"]
notas = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

productos = ["Guitarra Ibanez","Microfono Shure","Batería Mapex","Bajo Solar","Teclado X3"]

lista = [1,2,3,4,5,10,15,30,80,90,100,50,19,13,11]
'''
1) Crear una lista con las notas de 10 estudiantes
.Mostrar la lista completa
.Calcular y mostrar el promedio
.Indicar la nota más alta y la más baja

2) Pedir al usuario que cargue 5 productos en una lista
.Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted()
.Preguntar al usuario qué producto desea eliminar y actualizar la lista

3) Generar una lista con 15 números enteros al azar entre 1 y 100
.Crear una lista con los pares y otra con los impares
.Mostrar cuántos números tiene cada lista

4) Dada una lista con valores repetidos:
datos = [1,3,5,3,7,1,9,5,3]
.Crear una nueva lista sin elementos repetidos.
.Mostrar el resultado.

5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
.Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
.Mostrar la lista final actualizada

6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana
.Calcular el promedio de las mínimas y el de las máximas
.Mostrar en qué día se registró la mayor amplitud térmica

8) Crear una matriz con las notas de 5 estudiantes en 3 materias
.Mostrar el promedio de cada estudiante
.Mostrar el promedio de cada materia

9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3)
.Inicializarlo con guiones "-" representando casillas vacías
.Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O"
.Mostrar el tablero después de cada jugada

10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7
.Mostrar el total vendido por cada producto
.Mostrar el día con mayores ventas totales
.Indicar cuál fue el producto más vendido en la semana
'''


#Ejercicio 1
notas = []
for i in range(10):
        nota = int(input(f"Ingrese la nota del estudiante {i+1}: "))
        notas.append(nota)
print("Lista de notas:", notas)
promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

#Ejercicio 2

productos = []
for i in range(5):
        producto = input(f"Ingrese el nombre del producto {i+1}: ")
        productos.append(producto)

print("Lista de productos ordenada:", sorted(productos))

decision = input("¿Desea eliminar algún producto? (S/N): ")
if decision.lower() == "s":
        producto_a_eliminar = input("Ingrese el nombre del producto a eliminar: ")
        if producto_a_eliminar in productos:
            productos.remove(producto_a_eliminar)
            print("Producto eliminado. Lista actualizada:", productos)
        else:
            print("El producto no está en la lista.")
    
#Ejercicio 3
    
lista = [1,2,3,4,5,10,15,30,80,90,100,50,19,13,11]

numeros_pares = [n for n in lista if n % 2 == 0]
numeros_impares = [n for n in lista if n % 2 != 0]

print("Los números pares son:", numeros_pares)
print("Los números impares son:", numeros_impares)

#Ejercicio 4

datos = [1,3,5,3,7,1,9,5,3]
datos_actualizados = list(dict.fromkeys(datos))

print("Datos actualizados: ", datos_actualizados)

#Ejercicio 5

# Lista inicial de estudiantes
alumnos = ["Rodrigo", "Leandro", "Marcelo", "Eugenia", "Martina", "Julieta", "Pablo", "Isabel"]

# Preguntar si se quiere agregar un estudiante
decision = input("¿Desea agregar nombre de nuevo estudiante a la lista? (S/N): ")

if decision.lower() == "s":
    agregar_alumno = input("Agregue el nombre del estudiante a la lista: ")
    if agregar_alumno in alumnos:
        print("El alumno ya existe en la lista.")
    else:
        alumnos.append(agregar_alumno)
        print("Alumno agregado. Lista actualizada:", alumnos)

# Preguntar si se quiere eliminar un estudiante
decision = input("¿Desea eliminar el nombre de un estudiante de la lista? (S/N): ")

if decision.lower() == "s":
    eliminar_alumno = input("Ingrese el nombre del alumno a eliminar: ")
    if eliminar_alumno in alumnos:
        alumnos.remove(eliminar_alumno)
        print("Alumno eliminado. Lista actualizada:", alumnos)
    else:
        print("El nombre no existe en la lista:", alumnos)

#Ejercicio 6

lista = [10,20,30,40,50,60,70]
for i in range(7):
    numero = int(input(f"Ingrese el número {i+1}:"))
    lista.append(numero)
print("Lista Original: ", lista)
lista_rotada = lista[-1:] + lista[:-1]
    
print("Lista rotada a la derecha:", lista_rotada)

#Ejercicio 7

temperaturas = []
for i in range(7):
    print(f"Ingresar temperatura del día {i+1}:")
    minima = float(input("Ingrese la temperatura mínima:"))
    maxima = float(input("Ingrese la temperatura máxima:"))
    temperaturas.append([minima,maxima])

suma_minima = 0
suma_maxima = 0
for dia in temperaturas:
    suma_minima += dia[0]
    suma_maxima += dia[1]

promedio_minimo = suma_minima / 7
promedio_maximo = suma_maxima / 7

mayor_amplitud = -1
dia_mayor = -1

for i in range(7):
    min_temp = temperaturas[i][0]
    max_temp = temperaturas[i][1]
    amplitud = max_temp - min_temp
    
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i + 1
print("Resultados:")
print("Promedio de mínimas:", round(promedio_minimo,2))
print("Promedio de máximas:", round(promedio_maximo,2))  
print(f"La mayor amplitud termica fue {mayor_amplitud}ºC y ocurrio el día {dia_mayor}")

#Ejercicio 8

alumnos = ["Rodrigo","Eugenia","Nicolas","Leandro","Julieta"]
materias = ["Programación","Arquitectura y Sistemas","Matemática"]
notas = [1,2,3,4,5,6,7,8,9,10]

for alumno in alumnos:
    fila = []
    print(f"Ingresar notas para {alumno}:")
    for materia in materias:
        nota = int(input(f"Nota en {materia}:"))
        fila.append(nota)
    notas.append(fila)
    
print("Matriz de notas:")
for i in range(len(alumnos)):
    print(f"{alumnos[i]}: {notas[i]}")
            
#Ejercicio 9

# Inicializar tablero
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
    print()

turno = "X"
for jugada in range(9):  # máximo 9 jugadas
    mostrar_tablero(tablero)
    print(f"Turno del jugador {turno}")
    
    while True:
        fila = int(input("Ingrese fila (0-2): "))
        columna = int(input("Ingrese columna (0-2): "))
        if 0 <= fila <= 2 and 0 <= columna <= 2:
            if tablero[fila][columna] == "-":
                tablero[fila][columna] = turno
                break
            else:
                print("La casilla ya está ocupada. Intente otra.")
        else:
            print("Fila o columna inválida. Debe estar entre 0 y 2.")
    
    turno = "O" if turno == "X" else "X"

# Mostrar tablero final
mostrar_tablero(tablero)
print("Juego terminado.")

#Ejercicio 10

num_productos = 4
num_dias = 7

ventas = []

for i in range(num_productos):
    fila = []
    print(f"Ingresar ventas del Producto {i+1}:")
    for j in range(num_dias):
        venta = int(input(f" Día {j+1}: "))
        fila.append(venta)
    ventas.append(fila)
    
totales_productos = []
print("Total vendido por producto:")
for i, producto in enumerate(ventas):
    total = sum(producto)
    totales_productos.append(total)
    print(f"Producto {i+1}: {total} unidades")
    
ventas_diarias = [sum(ventas[prod][dia] for prod in range(num_productos))for dia in range(num_dias)]
mayor_venta = max(ventas_diarias)
dia_mayor = ventas_diarias.index(mayor_venta) + 1
print(f"Día con mayores ventas totales: Día {dia_mayor} ({mayor_venta}unidades)")

mayor_producto = max(totales_productos)
producto_mas_vendido = totales_productos.index(mayor_producto) + 1
print(f"Producto más vendido en la semana: Producto {producto_mas_vendido} ({mayor_producto} unidades)")            