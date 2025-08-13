# Proyecto

print("\nEL NAUFRAGIO\n")
print("Despiertas en una playa desierta, con la ropa rasgada y la cabeza golpeada.\n"
      "El sol quema tu piel, y a tu alrededor solo hay arena, palmeras y el sonido de las olas.\n"
      "A lo lejos, los restos de tu barco humean en el agua.\n")

print("¿Que elijes?")

decision = input(
    "A) Explorar la jungla\nB) Investigarla cueva\nC) Quedarte en la playa\n")

if decision == "A" or decision == "a":
    print("La vegetación es tan densa que apenas pasa la luz. Entre los árboles, encuentras:\n"

          "Un río contaminado con un barril metálico brillante.\n"

          "Un sendero antiguo que sube hacia una colina cubierta de niebla.\n")

    print("¿Que desición tomas?\n")

    da = input("A) INSPECCIONAR EL BARRIL (Podría ser útil… o peligroso).\n"

               "B) SEGUIR EL SENDERO (Quizás lleve a algo importante).\n")

    if da == "A" or da == "a":
        print("El barril tiene símbolos de peligro y un líquido verde que burbujea.\n")

        print("Opciones:\n")

        d1 = input("A) ABRIRLO\nB) RODARLO AL RÍO\nC) ESCONDERLO\n")

        if d1 == "A" or d1 == "a":
            print(" Liberas un gas tóxico. (Mueres intoxicado.)")

        elif d1 == "B" or d1 == "b":
            print("Envenenas el agua. (Sin agua potable, mueres deshidratado.)")

        elif d1 == "C" or d1 == "c":
            print("Más tarde, criaturas lo encuentran y te atacan. (Huyes, pero quedas herido y mueres desangrado.)")

        else:
            print("Opcion Invalida.")

    elif da == "B" or da == "b":
        print("Llegas a una aldea abandonada con cabañas en ruinas. Hay un ídolo de piedra en el centro.")

        print("Opciones.\n")

        d2 = input("A) TOCAR EL ÍDOLO\nB)HUIR DE LA ALDEA\n")

        if d2 == "A" or d2 == "a":
            print(
                "Una maldición te convierte en piedra. (Final: Eres una estatua más.)\n")

        elif d2 == "B" or d2 == "b":
            print(
                "Regresas a la playa, pero ya es de noche.(Mueres por las criaturas que acechan por la noche).")

    else:
        print("Opcion Invalida")


elif decision == "b" or decision == "B":
    print("El aire es frío y huele a musgo.\n"
          " Tus pasos resuenan en las paredes húmedas.\n"
          " Dentro encuentras:\nUna tablilla de piedra con símbolos extraños.\n"
          "Un túnel estrecho que desciende hacia la oscuridad.")
    print("¿Que elijes?")
    decisionb = input("A)TOMAR LA TABLILLA.\n"
                      "B)AVENTURARSE EN EL TÚNEL. \n"
                      "C)SALIR DE LA CUEVA.\n")

    if decisionb == "a" or decisionb == "A":
        print("Los símbolos forman un mapa hacia un templo oculto en la jungla.")
        print("¿Que elijes?")
        decisionba = input("A)SEGUIR EL MAPA\n"
                           "B)IGNORARLO\n"
                           "c)ROMPERLA\n")
        if decisionba == "a" or decisionba == "A":
            print("encuentras un templo está cubierto de enredaderas y estatuas de dioses olvidados.\n"
                  "En el centro hay un altar con un artefacto brillante.")
            print("¿Que elijes?\n")

            decisionbaa = input("A)TOMAR EL ARTEFACO\nB)HUIR DEL TEMPLO\n")

            if decisionbaa == "a" or decisionbaa == "A":
                print("Tomas el artefacto y este te da poderes")
                print("¿Que elijes?")
                decisionbaaa = input(
                    "A)TE QUEDAS A PROTEGER EL TEMPLO.\nB)HUYES DEL TEMPLO\n")

                if decisionbaaa == "A" or decisionbaaa == "a":
                    print(
                        "Te quedas a proteger el templo por el resto de la eternidad. fin")
                elif decisionbaaa == "B" or decisionbaaa == "b":
                    print(
                        "Intestas escapar del templo pero te teletransportas a un lugar al azar del templo donde quedas atrapado para siempre. fin")
                else:
                    print("opcion invalida")

            elif decisionbaa == "B" or decisionbaa == "b":
                print(
                    "huyes del templo y esperas en la playa a que te rescaten pero nunca llega nadie. fin")
            else:
                print("opcion invalida")
        elif decisionba == "B" or decisionba == "b":
            print("lo ignoras y te pierdes para siempre en la jungla. fin")

        elif decisionba == "C" or decisionba == "c":
            print("rompes la tabla y se libera una maldicion que cae sobre ti. fin")
        else:
            print("opcion invalida")

    elif decisionb == "B" or decisionb == "b":
        print("caes en una trampa antigua y mueres de hambre. fin")

    elif decisionb == "C" or decisionb == "c":
        print("sales de la cueva y quedas atrapado en la jungla para siempre. fin")
    else:
        print("opcion invalida")

elif decision == "C" or decision == "c":
    print("Construyes una señal de ayuda y esperas(se hace de noche y mueres por las criaturas que acechan.)")

else:
    print("opcion invalida")
