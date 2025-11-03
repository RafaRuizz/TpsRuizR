# Sistema de Gestión de Productos con Archivos
# Práctica - Programación I

def crear_archivo_inicial():
    """Actividad 1: Crear archivo inicial con productos"""
    productos_iniciales = [
        "Lapicera,120.5,30",
        "Cuaderno,250.0,15",
        "Mochila,3500.0,8"
    ]
    
    with open('productos.txt', 'w') as archivo:
        for producto in productos_iniciales:
            archivo.write(producto + '\n')
    print("✓ Archivo productos.txt creado exitosamente\n")


def leer_y_mostrar_productos():
    """Actividad 2: Leer y mostrar productos"""
    print("=== PRODUCTOS DISPONIBLES ===")
    try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:  # Evitar líneas vacías
                    datos = linea.split(',')
                    nombre = datos[0]
                    precio = datos[1]
                    cantidad = datos[2]
                    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    except FileNotFoundError:
        print("Error: El archivo productos.txt no existe.")
    print()


def agregar_producto_desde_teclado():
    """Actividad 3: Agregar productos desde teclado"""
    print("=== AGREGAR NUEVO PRODUCTO ===")
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio: ")
    cantidad = input("Ingrese la cantidad: ")
    
    with open('productos.txt', 'a') as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    print(f"✓ Producto '{nombre}' agregado exitosamente\n")


def cargar_productos_en_lista():
    """Actividad 4: Cargar productos en una lista de diccionarios"""
    productos = []
    
    try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    datos = linea.split(',')
                    producto = {
                        'nombre': datos[0],
                        'precio': float(datos[1]),
                        'cantidad': int(datos[2])
                    }
                    productos.append(producto)
    except FileNotFoundError:
        print("Error: El archivo productos.txt no existe.")
    
    return productos


def buscar_producto_por_nombre(productos):
    """Actividad 5: Buscar producto por nombre"""
    print("=== BUSCAR PRODUCTO ===")
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ")
    
    encontrado = False
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscado.lower():
            print(f"\n✓ Producto encontrado:")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']}")
            print(f"  Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"\n✗ Error: El producto '{nombre_buscado}' no existe en el sistema.")
    print()


def guardar_productos_actualizados(productos):
    """Actividad 6: Guardar los productos actualizados"""
    with open('productos.txt', 'w') as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("✓ Archivo actualizado correctamente\n")


def mostrar_menu():
    """Mostrar menú de opciones"""
    print("\n" + "="*40)
    print("  SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("="*40)
    print("1. Crear archivo inicial")
    print("2. Mostrar todos los productos")
    print("3. Agregar nuevo producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar productos (desde lista)")
    print("6. Salir")
    print("="*40)


def main():
    """Función principal del programa"""
    productos = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            crear_archivo_inicial()
            
        elif opcion == '2':
            leer_y_mostrar_productos()
            
        elif opcion == '3':
            agregar_producto_desde_teclado()
            
        elif opcion == '4':
            productos = cargar_productos_en_lista()
            if productos:
                buscar_producto_por_nombre(productos)
            
        elif opcion == '5':
            productos = cargar_productos_en_lista()
            if productos:
                print("\n=== PRODUCTOS (desde lista de diccionarios) ===")
                for i, prod in enumerate(productos, 1):
                    print(f"{i}. {prod['nombre']} - ${prod['precio']} - Stock: {prod['cantidad']}")
                print()
            else:
                print("No hay productos cargados.\n")
        
        elif opcion == '6':
            print("\n¡Gracias por usar el sistema!")
            break
            
        else:
            print("\n✗ Opción inválida. Intente nuevamente.\n")


if __name__ == "__main__":
    main()