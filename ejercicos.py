precio = float(input("\ningrese la cuenta: "))
precio_y_propina = precio * 115/100
print(f"cuenta mas la propina: {precio_y_propina}")


nombre = input("\ningrese su nombre: ")
edad = int(input("ingrese su edad: "))
ciudad = input("ingrese se ciudad: ")
print(f"hola,{nombre} tienes {edad} años y vives en {ciudad}")


celsius = float(input("\ningrese temperatura grado celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}ºC son {fahrenheit}ºF\n")


nacimiento = int(input("ingrese su fecha de nacimiento: "))

edad2 = 2025 - nacimiento
if edad2 >= 18:
    print("eres mayor de edad\n")
elif edad2 <= 17:
    print("eres menor de edad\n")
else:
    print("valor invalido")

base = float(input("ingrese la base del rectangulo: "))
altura = float(input("ingrese la altura del rectangulo: "))

area = base * altura
perimetro = (base + altura) * 2

print(f"el area del rectangulo es {area}")
print(f"el perimetro del rectangulo es {perimetro}\n")

numero = float(input("ingrese un numero: "))
if numero >= 1:
    print(f"el numero {numero} es positivo")
elif numero == 0:
    print(f"el numero {numero} es cero")
elif numero <= -1:
    print(f"el numero {numero} es negativo")
else:
    print("valor invalido")

edad3 = int(input("\ningrese su edad: "))
nombre1 = input("ingrese su nombre: ")

if edad3 >= 18 and nombre1 == "Santiago" or nombre1 == "Petronila" or nombre1 == "Juan" or nombre1 == "daniel":
    print("eres mayor de edad y estas en la lista puedes pasar")
elif edad3 >= 18:
    print("eres mayor de edad pero no estas en la lista")
elif edad3 <= 17 and nombre1 == "Santiago" or nombre1 == "Petronila" or nombre1 == "Juan":
    print("estas en la lista pero no eres mayor de edad")
elif edad3 <= 17:
    print("no estas en la lista y eres menor de edad")
else:
    print("valor inavliado")

calificacion = float(input("\ningrese su calificacion: "))
if calificacion >= 90 and calificacion <= 100:
    print("felicidades tienes una A")
elif calificacion >= 80 and calificacion <= 89:
    print("bien sacaste una B")
elif calificacion >= 70 and calificacion <= 79:
    print("tienes una C pero podria ser mejor")
elif calificacion >= 60 and calificacion <= 69:
    print("tienes una D no esta tan bien...")
elif calificacion >= 0 and calificacion <= 59:
    print("tienes una F hay que mejorar :(")
else:
    print("valor invalido")

compra = float(input("\ningrese el costo de su compra: "))
if compra >= 100:
    compra_con_descuento = compra * 80/100
    print(f"el costo de tu compra mas el descuento es {compra_con_descuento}")
elif compra >= 50:
    compra_con_descuento = compra * 90/100
    print(f"el costo de tu compra mas el descuento es {compra_con_descuento}")
elif compra >= 0:
    print(f"el costo de tu compra es {compra}")

año = int(input("\ningresa un año: "))
if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print(f"el año {año} es un año biciesto")
else:
    print(f"el año {año} no es un año biciesto")
