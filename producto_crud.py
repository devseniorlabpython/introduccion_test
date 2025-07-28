from typing import Dict

class Producto:
    def __init__(self, nombre:str, precio:str):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio}"

fake_db : Dict[int, Producto] = {}
id_counter = 1

def agregar_producto(nombre_producto, precio):
    global id_counter
    producto = Producto(nombre_producto, precio)
    fake_db[id_counter] = producto
    id_counter += 1
    print(f"Producto agregado: {producto.nombre}")
    
def eliminar_producto(id_producto):
    if id_producto in fake_db:
        producto = fake_db.pop(id_producto)
        print(f"Producto eliminado: {producto.nombre}")
    else:
        print("Producto no encontrado.")
        
def leer_productos():
    if not fake_db:
        print("No hay productos en la base de datos.")
    else:
        for id_producto, producto in fake_db.items():
            print(f"ID: {id_producto}, Producto: {producto}")
            
def leer_producto(id_producto):
    if id_producto in fake_db:
        producto = fake_db[id_producto]
        print(f"Producto encontrado: {producto}")
    else:
        print("Producto no encontrado.")
        
def actualizar_producto(id_producto, nuevo_nombre, nuevo_precio):
    if id_producto in fake_db:
        producto = fake_db[id_producto]
        producto.nombre = nuevo_nombre
        producto.precio = nuevo_precio
        print(f"Producto actualizado: {producto}")
    else:
        print("Producto no encontrado.")