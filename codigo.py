import time 

# Estructuras de datos globales
cola_pedidos = []
historial_pedidos = []

def agregar_pedido(id, comida, tiempo_preparacion):
    pedido = {
        "id": id,
        "comida": comida,
        "tiempo_preparacion": tiempo_preparacion
    }
    cola_pedidos.append(pedido)
    historial_pedidos.append(pedido)
    print(f"Pedido '{comida}' agregado a la cola.")

def procesar_pedidos():
    print("\n--- Iniciando cajero ---")
    if not cola_pedidos:
        print("No hay pedidos pendientes en la cola.")
        return
    
    while cola_pedidos:
        pedido = cola_pedidos.pop(0) # FCFS: Primero en entrar, primero en salir
        print(f"Procesando pedido: '{pedido['comida']}'")
        
        if pedido['tiempo_preparacion'] > 0:
            print(f"Preparando... ({pedido['tiempo_preparacion']} segundos)")
            time.sleep(pedido['tiempo_preparacion'])
        
        print(f"¡Pedido '{pedido['comida']}' listo para servir!")
        
        if cola_pedidos:
            print("Siguiente pedido en la cola...")
        else:
            print("No hay más pedidos pendientes.")
            
    print("Todos los pedidos de la tanda actual han sido procesados.\n")

def mostrar_historial():
    if not historial_pedidos:
        print("\nEl historial está vacío.")
        return
    print("\n--- Historial de Pedidos ---")
    for pedido in historial_pedidos:
        print(f"ID: {pedido['id']} | Comida: {pedido['comida']} | Tiempo: {pedido['tiempo_preparacion']}s")
    print("----------------------------\n")

def limpiar_historial():
    historial_pedidos.clear()
    print("\nHistorial de pedidos limpiado correctamente.")

def menu():
    while True:
        print("======= SISTEMA DE TIENDA =======")
        print("1. Agregar pedido manualmente")
        print("2. Cargar pedidos de prueba (Hamburguesa, Pizza, etc.)")
        print("3. Procesar cola de pedidos (Simulación)")
        print("4. Mostrar historial completo")
        print("5. Limpiar historial")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                id_p = int(input("Ingrese el ID del pedido: "))
                comida = input("Ingrese el nombre de la comida: ")
                tiempo = int(input("Ingrese el tiempo de preparación (segundos): "))
                agregar_pedido(id_p, comida, tiempo)
            except ValueError:
                print("Error: ID y Tiempo deben ser números enteros.")
                
        elif opcion == "2":
            agregar_pedido(1, "Hamburguesa", 3)
            agregar_pedido(2, "Pizza", 5)
            agregar_pedido(3, "Ensalada", 2)
            print("Pedidos de prueba cargados.")
            
        elif opcion == "3":
            procesar_pedidos()
            
        elif opcion == "4":
            mostrar_historial()
            
        elif opcion == "5":
            limpiar_historial()
            
        elif opcion == "6":
            print("Saliendo del sistema. ¡Vuelva pronto!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
