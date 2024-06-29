import json

from datetime import datetime



ventas = []


precios_pizzas = {

  "Margarita": {"pequeña": 5500, "mediana": 8500, "familiar": 11000},

  "mexicana": {"pequeña": 7000, "mediana": 10000, "familiar": 13000},

  "Barbacoa": {"pequeña": 6500, "mediana": 9500, "familiar": 12500},

   "vegetariana": {"pequeña": 5000, "mediana": 8000, "familiar": 10500}

}


# funcion para mostrar el menu
def menu():

  print("\n--- Sistema de Ventas de Pizzas ---")

  print("1. Registrar una venta")

  print("2. Mostrar todas las ventas")

  print("3. Buscar ventas por cliente")

  print("4. Guardar las ventas en un archivo")

  print("5. Cargar las ventas desde un archivo")

  print("6. generar boleta")

  print("7. anular venta")

  print("8. Salir")

  opcion = input("Seleccione una opción: ")

  return opcion


# funcion para registar una venta
def registrar_venta():

  nombre_cliente = input("Nombre del cliente: ")

  tipo_cliente = input("Tipo de cliente (diurno/vespertino/administrativo): ").lower()

  tipo_pizza = input("Tipo de pizza (Margarita/mexicana/barbacoa/vegetariana): ").lower()

  tamaño_pizza = input("Tamaño de la pizza (pequeña / mediana / familiar): ").lower()

  cantidad = int(input("Cantidad de pizzas: "))

  

  if tipo_pizza not in precios_pizzas or tamaño_pizza not in precios_pizzas[tipo_pizza]:

    print("Tipo o tamaño de pizza inválido.")

    return

  

  precio_unitario = precios_pizzas[tipo_pizza][tamaño_pizza]

  

  descuento = 0

  if tipo_cliente == 'diurno':

    descuento = 0.15

  elif tipo_cliente == 'vespertino':

    descuento = 0.18

  elif tipo_cliente == 'administrativo':

    descuento = 0.11

  

  precio_total = precio_unitario * cantidad

  precio_final = precio_total * (1 - descuento)

  

  # Fecha y hora actual

  fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  

  venta = {

    "fecha_hora": fecha_hora,

    "nombre_cliente": nombre_cliente,

    "tipo_cliente": tipo_cliente,

    "tipo_pizza": tipo_pizza,

    "tamaño_pizza": tamaño_pizza,

    "cantidad": cantidad,

    "precio_unitario": precio_unitario,

    "precio_total": precio_total,

    "descuento": descuento,

    "precio_final": precio_final

  }

  ventas.append(venta)

  print(f"\nVenta registrada:\n")

  print(f"Fecha y hora: {fecha_hora}")

  print(f"Cliente: {nombre_cliente}")

  print(f"Tipo de cliente: {tipo_cliente}")

  print(f"Tipo de pizza: {tipo_pizza}")

  print(f"Tamaño de pizza: {tamaño_pizza}")

  print(f"Cantidad: {cantidad}")

  print(f"Precio unitario: {precio_unitario}")

  print(f"Precio total: {precio_total}")

  print(f"Descuento aplicado: {descuento * 100}%")

  print(f"Precio final: {precio_final}")


# funcion para mostrar todas las ventas 
def mostrar_ventas():

  if not ventas:

    print("No hay ventas registradas.")

  else:

    for venta in ventas:

      print("\n--- Detalles de la Venta ---")

      print(f"Fecha y hora: {venta['fecha_hora']}")

      print(f"Cliente: {venta['nombre_cliente']}")

      print(f"Tipo de cliente: {venta['tipo_cliente']}")

      print(f"Tipo de pizza: {venta['tipo_pizza']}")

      print(f"Tamaño de pizza: {venta['tamaño_pizza']}")

      print(f"Cantidad: {venta['cantidad']}")

      print(f"Precio unitario: {venta['precio_unitario']}")

      print(f"Precio total: {venta['precio_total']}")

      print(f"Descuento aplicado: {venta['descuento'] * 100}%")

      print(f"Precio final: {venta['precio_final']}")


# funcion para buscar ventas por clientes
def buscar_ventas():

  nombre_cliente = input("Ingrese el nombre del cliente a buscar: ")

  ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente]

  

  if not ventas_cliente:

    print(f"No se encontraron ventas para el cliente {nombre_cliente}.")

  else:

    for venta in ventas_cliente:

      print("\n--- Detalles de la Venta ---")

      print(f"Fecha y hora: {venta['fecha_hora']}")

      print(f"Cliente: {venta['nombre_cliente']}")

      print(f"Tipo de cliente: {venta['tipo_cliente']}")

      print(f"Tipo de pizza: {venta['tipo_pizza']}")

      print(f"Tamaño de pizza: {venta['tamaño_pizza']}")

      print(f"Cantidad: {venta['cantidad']}")

      print(f"Precio unitario: {venta['precio_unitario']}")

      print(f"Precio total: {venta['precio_total']}")

      print(f"Descuento aplicado: {venta['descuento'] * 100}%")

      print(f"Precio final: {venta['precio_final']}")


# funcion para guardar ventas 
def guardar_ventas():

  with open('ventas.json', 'w') as file:

    json.dump(ventas, file, indent=4)

  print("Ventas guardadas en 'ventas.json'.")


# funcion para cargar ventas 
def cargar_ventas():

  global ventas

  try:

    with open('ventas.json', 'r') as file:

      ventas = json.load(file)

    print("Ventas cargadas desde 'ventas.json'.")

  except FileNotFoundError:

    print("No se encontró el archivo 'ventas.json'.")

# funcion para generar boleta 

def generar_boleta():
    nombre_cliente = input("Ingrese nombre del cliente para generar la boleta: ")
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente and not venta["anulada"]]
    if ventas_cliente:
        print(f"Boleta para {nombre_cliente}:")
        total = 0
        for venta in ventas_cliente:
            print(f"Fecha y hora: {venta['fecha_hora']}")
            print(f"Tipo de pizza: {venta['tipo_pizza']}")
            print(f"Tamaño de pizza: {venta['tamaño_pizza']}")
            print(f"Cantidad: {venta['cantidad']}")
            print(f"Precio final: {venta['precio_final']}")
            total += venta["precio_final"]
        print(f"Total a pagar: {total}")
    else:
        print("No se encontraron ventas válidas para este cliente.")

  # funcion para anular ventas
   
def anular_venta():
    nombre_cliente = input("Ingrese nombre del cliente para anular la venta: ")
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == nombre_cliente and not venta["anulada"]]
    if ventas_cliente:
        for venta in ventas_cliente:
            venta["anulada"] = True
        print("Venta anulada con exito.")
    else:
        print("No se encontraron ventas para este cliente.") 

# funcion principal 
def main():

  while True:

    opcion = menu()

    if opcion == '1':

      registrar_venta()

    elif opcion == '2':

      mostrar_ventas()

    elif opcion == '3':

      buscar_ventas()

    elif opcion == '4':

      guardar_ventas()

    elif opcion == '5':

      cargar_ventas()

    elif opcion == '6':

      generar_boleta()

    elif opcion == '7':

      anular_venta()
    
    elif opcion == '8':

     print("Gracias por usar el sistema de ventas.")


     break
  
    else:

     print("Opción no válida, por favor intente de nuevo.")
if __name__ == "__main__":

  main()