# ===============================================
# TP6 – Estructuras de datos complejas
# Versión final con validaciones y manejo de errores donde corresponde
# ===============================================

# 1) Diccionario de precios de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("1) Diccionario con frutas agregadas:", precios_frutas)


# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("2) Diccionario actualizado:", precios_frutas)


# 3) Lista con solo las frutas
frutas = list(precios_frutas.keys())
print("3) Lista de frutas:", frutas)


# 4) Agenda telefónica con validaciones
contactos = {}
for i in range(5):
    while True:
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")
    while True:
        numero = input(f"Ingrese el número de teléfono de {nombre}: ").strip()
        if numero:
            break
        print("El número no puede estar vacío.")
    contactos[nombre] = numero

while True:
    consulta = input("Ingrese un nombre para consultar su número: ").strip()
    if not consulta:
        print("El nombre no puede estar vacío.")
        continue
    if consulta in contactos:
        print(f"El número de {consulta} es {contactos[consulta]}")
        break
    else:
        print("El contacto no existe. Intente nuevamente.")


# 5) Frase: palabras únicas y conteo
frase = input("Ingrese una frase: ").lower()
palabras = frase.split()

palabras_unicas = set(palabras)
print("5) Palabras únicas:", palabras_unicas)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("   Cantidad de veces que aparece cada palabra:", conteo)


# 6) Promedio de notas
alumnos = {}
for i in range(3):
    while True:
        nombre = input(f"Nombre del alumno {i+1}: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Debe ingresar un número válido.")
    alumnos[nombre] = tuple(notas)

print("\n6) Promedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"   {nombre}: {promedio:.2f}")


# 7) Sets de aprobados
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

print("\n7) Aprobados:")
print("   Ambos parciales:", parcial1 & parcial2)
print("   Solo uno:", parcial1 ^ parcial2)
print("   Al menos uno:", parcial1 | parcial2)


# 8) Control de stock (versión mejorada)
stock = {'Arroz': 10, 'Fideos': 5, 'Aceite': 8}

while True:
    producto = input("Ingrese el producto a consultar: ").strip()
    if producto:
        break
    print("El nombre del producto no puede estar vacío.")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    while True:
        try:
            agregar = int(input("Ingrese cantidad para agregar (0 si no desea): "))
            if agregar < 0:
                print("No puede ingresar números negativos.")
                continue
            stock[producto] += agregar
            break
        except ValueError:
            print("Debe ingresar un número entero válido.")
else:
    while True:
        try:
            nuevo = int(input(f"Producto '{producto}' no encontrado. Ingrese stock inicial: "))
            if nuevo < 0:
                print("El stock inicial no puede ser negativo.")
                continue
            stock[producto] = nuevo
            break
        except ValueError:
            print("Debe ingresar un número entero válido.")

print("8) Stock actualizado:", stock)


# 9) Agenda con tuplas
agenda = {
    ('Lunes', '10:00'): 'Reunión',
    ('Martes', '15:00'): 'Clase',
    ('Viernes', '18:00'): 'Gimnasio'
}

dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")

actividad = agenda.get((dia, hora))
if actividad:
    print("9) Actividad:", actividad)
else:
    print("No hay actividad programada.")


# 10) Invertir diccionario país → capital
paises = {
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Brasil': 'Brasilia'
}

capitales = {capital: pais for pais, capital in paises.items()}
print("\n10) Diccionario invertido:", capitales)
