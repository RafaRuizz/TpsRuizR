import math


def imprimir_hola_mundo():
    print("Hola Mundo!")


def saludar_usuario(nombre):
    return f"Hola {nombre}!"


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def calcular_area_circulo(radio):
    return math.pi * radio ** 2


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


def segundos_a_horas(segundos):
    return segundos / 3600


def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return (suma, resta, multiplicacion, division)


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def calcular_promedio(a, b, c):
    return (a + b + c) / 3


def main():
    print("=== Ejercicio 1 ===")
    imprimir_hola_mundo()
    
    print("\n=== Ejercicio 2 ===")
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))
    
    print("\n=== Ejercicio 3 ===")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    residencia = input("Ingrese su residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    
    print("\n=== Ejercicio 4 ===")
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")
    
    print("\n=== Ejercicio 5 ===")
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
    
    print("\n=== Ejercicio 6 ===")
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)
    
    print("\n=== Ejercicio 7 ===")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    suma, resta, mult, div = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {mult}")
    print(f"División: {div}")
    
    print("\n=== Ejercicio 8 ===")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")
    
    print("\n=== Ejercicio 9 ===")
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
    
    print("\n=== Ejercicio 10 ===")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio es: {promedio:.2f}")


if __name__ == "__main__":
    main()