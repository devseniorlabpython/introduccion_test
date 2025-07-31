from producto_crud import agregar_producto, leer_productos, eliminar_producto, leer_producto, actualizar_producto, \
    exportar_productos_txt
import os

if __name__ == "__main__":
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Leer productos")
        print("3. Leer producto por ID")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Exportar productos a txt")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")
        
        os.system("cls" if os.name == "nt" else "clear")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = input("Ingrese el precio del producto: ")
            agregar_producto(nombre, precio)
            print()
            
        elif opcion == "2":
            leer_productos()
            
        elif opcion == "3":
            id_producto = int(input("Ingrese el ID del producto a buscar: "))
            leer_producto(id_producto)
            
        elif opcion == "4":
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            nuevo_precio = input("Ingrese el nuevo precio del producto: ")
            actualizar_producto(id_producto, nuevo_nombre, nuevo_precio)
            
        elif opcion == "5":
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            eliminar_producto(id_producto)

        elif opcion == "6":
            nombre_archivo = input("Ingrese el nombre del archivo para exportar los productos:")
            exportar_productos_txt(nombre_archivo)
            
        elif opcion == "7":
            break
        
        else:
            print("Opción no válida, intente de nuevo.")