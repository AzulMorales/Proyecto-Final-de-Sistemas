#sistema de tienda
import time 

cola_pedidos = []
def agregar_pedido(id,comida,tiempo_preparacion):
    pedido = {
        "id": id,
        "comida": comida,
        "tiempo_preparacion": tiempo_preparacion
    }
    cola_pedidos.append(pedido)
    print(f"Pedido '{comida}' agregado a la cola.")

def procesar_pedidos():
    print("Iniciando cajero...")
    if not cola_pedidos:
        print("No hay pedidos en la cola.")
        return
    while cola_pedidos:
        pedido = cola_pedidos.pop(0)
        print(f"Procesando pedido: '{pedido['comida']}'")
        if pedido['tiempo_preparacion'] > 0:
            print(f"Pedido '{pedido['comida']}' se esta elaborando.")

        time.sleep(pedido['tiempo_preparacion'])
        print(f"Pedido '{pedido['comida']}' listo para servir.")

        if agregar_pedido:
            print("Siguiente pedido en la cola...")
        else:
            print("No hay más pedidos en la cola.")
            
    print("Todos los pedidos han sido procesados.")

agregar_pedido(1,"Hamburguesa",3)
agregar_pedido(2,"Pizza",12)
agregar_pedido(3,"Ensalada",6)
    
procesar_pedidos()
