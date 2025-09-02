#Ejercicio 1
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
mov = int(input("Ingrese corrimiento: "))
for oficial in range(1,6):
    mensaje = input("Ingrese mensaje: ").upper()
    encriptado = ""
    for letra in mensaje:
        encriptado += abc[(abc.index(letra) + mov) % 27] if letra in abc else letra
    print("Mensaje encriptado:", encriptado)