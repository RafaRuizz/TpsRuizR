import random
opciones = {1:"Piedra",2:"Papel",3:"Tijera"}
i="si"
while i != "no":
    opc = input("Ingrese:\nPiedra\nPapel\nTijera\n")
    opc = opc.capitalize()
    pc = opciones[random.choice(list(opciones.keys()))]
    if opc == pc:
        print("Empate!")
    elif (opc == "Piedra" and pc == "Tijera") or \
         (opc == "Papel" and pc == "Piedra") or \
         (opc == "Tijera" and pc == "Papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste (o no ingresaste caracter valido)")
    print(f"PC eligio: {pc}")
    i = input("Continuar? Si/No: ")
    i = i.lower()