import csv
import os

Archivo = "inventario.cvs"
def agregar_producto():
    nombre = input("Nombre del producto")
    precio =float(input("Precio:$"))
    stock = int(input("¿Cuantos hay en stock?:"))
    
    with open(Archivo, "a", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow([nombre,precio,stock])
    print(f"{nombre}agregado al inventario")

def ver_inventario():
    try:
        with open(Archivo, "r") as f:
            lector = csv.reader(f)
            print("\nINVENTARIO")
            print(f"{'Producto':<20} {'Precio':>10} {'Stock':>10}")
            print("-" * 42)
            for fila in lector:
               if len(fila) == 3:    # ← solo procesa filas con 3 columnas
                 print(f"{fila[0]:<20} ${float(fila[1]):>9.2f} {fila[2]:>10}")
    except FileNotFoundError:
        print("No hay productos aún, agrega uno primero")

def buscar_producto():
    busqueda = input("Nombre del producto que desea buscar?:").lower()
    encontrado = False
    with open(Archivo,"r") as f:
        lector = csv.reader(f)
        for fila in lector:
            if busqueda in fila[0].lower():
                print(f"\nProducto : {fila[0]}")
                print(f"\nPrecio:  ${float (fila[1]):.2f}")
                print(f"Stock: {fila[2]} unidades")
                encontrado = True
    if not  encontrado:
        print("Producto no encontrado")
def actualizar_stock():
    busqueda = input("Nombre del producto a actualizar: ").lower()
    productos = []
    encontrado = False

    with open(Archivo, "r") as f:
        lector = csv.reader(f)
        for fila in lector:
            if len(fila) == 3:          # ← ignora filas vacías
                if busqueda in fila[0].lower():
                    nuevo_stock = int(input(f"Nuevo stock para {fila[0]}: "))
                    fila[2] = str(nuevo_stock)
                    encontrado = True
                productos.append(fila)

    if encontrado:
        with open(Archivo, "w", newline="") as f:
            escritor = csv.writer(f)
            escritor.writerows(productos)
        print("✓ Stock actualizado")
    else:
        print("Producto no encontrado")

def productos_bajos():
    limite = int(input("¿Cuántas unidades consideras stock bajo? "))
    bajos = []

    with open(Archivo, "r") as f:
        lector = csv.reader(f)
        for fila in lector:
            if len(fila) == 3:
                if int(fila[2]) <= limite:
                    bajos.append(fila)

    if bajos:
        print(f"\n Productos con stock menor o igual a {limite}:")
        print(f"{'Producto':<20} {'Precio':>10} {'Stock':>10}")
        print("-" * 42)
        for p in bajos:
            print(f"{p[0]:<20} ${float(p[1]):>9.2f} {p[2]:>10}")
    else:
        print("Todos los productos tienen stock suficiente ✓")


def mostrar_menu():
    print("INVENTARIO DE LA TIENDA")
    print("1.Agregar producto")
    print("2.Ver Inventario")
    print("3.Buscar producto")
    print("4.Actualizar el stock")
    print("5.Productos bajos en stock")
    print("6.Salir")
while True:
    mostrar_menu()
    opcion = input("\n¿Que operacion desea realizar?")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_inventario()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        actualizar_stock()
    elif opcion == "5":
        productos_bajos()
    elif opcion == "6":
        print("Adios")
        break   
    else:
        print("Opcion no valida")             
              
              
