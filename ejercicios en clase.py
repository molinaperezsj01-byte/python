numero1 = int(input("inserte el primer numero: "))
numero2 = int(input("inserte el segundo numero: "))
operacion = input(
    "inserte la operacion (suma, resta, multiplicacion, division): ")

if operacion == "suma":
    resultado = numero1 + numero2
    print(f"el resultado es {resultado}")

elif operacion == "resta":
    resultado = numero1 - numero2
    print(f"el resultado es {resultado}")

elif operacion == "multiplicacion":
    resultado = numero1 * numero2
    print(f"el resultado es {resultado}")

elif operacion == "division":
    resultado = numero1 / numero2
    print(f"el resultado es {resultado}")


lista = []

articulo1 = input("añada el articulo a comprar: ")
articulo2 = input("añada el articulo a comprar: ")
articulo3 = input("añada el articulo a comprar: ")

lista.append(articulo1)
lista.append(articulo2)
lista.append(articulo3)

print(f"lista de compra: \n{lista[0]} \n{lista[1]} \n{lista[2]}")


nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
ciudad = input("ingrese su ciudad de nacimiento: ")

tupla = (nombre, edad, ciudad)

print(f"hola {tupla[0]} tienes {tupla[1]} años y naciste en {tupla[2]}")


agenda = {
    "Santiago": "041212121",
    "Juan": "123123123"}

busqueda = input("¿a quien desea llamar?")
if busqueda == "Santiago":
    print(f"el numero de santiago es {agenda["Santiago"]}")

elif busqueda == "Juan":
    print(f"el numero de Juan es {agenda["Juan"]}")

else:
    print("contacto no encontrado")


calificacion = [12, 13, 19, 15, 20]
suma = 0

for x in calificacion:
    suma += x
promedio = suma / len(calificacion)
maxima = max(calificacion)
minina = min(calificacion)

print(
    f"el promedio es {promedio}, la nota maxima es {maxima} y la minima es {minina}")
