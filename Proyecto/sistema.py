import tkinter as tk
import time

class sistema_operativo:
    def __init__(self):
        self.root = None
        self.text_area = None

        self.cola_pedidos = []
        self.historial_pedidos = []

    def set_contexto(self, root, text_area):
        self.root = root
        self.text_area = text_area

    def agregar_pedido(self, id, comida, tiempo_preparacion):
        pedido = {"id": id, "comida": comida, "tiempo_preparacion": tiempo_preparacion}

        self.cola_pedidos.append(pedido)
        self.historial_pedidos.append(pedido)
        self.text_area.insert(tk.END, f"Pedido '{comida}' agregado a la cola.\n")
        #La vista siemore baja
        self.text_area.see(tk.END)

    def procesar_pedidos(self):
        self.text_area.insert(tk.END, "\n--- Iniciando cajero (FCFS) ---\n")
        self.text_area.see(tk.END)
        if not self.cola_pedidos:
            self.text_area.insert(tk.END, "No hay pedidos pendientes en la cola.\n")
            self.text_area.see(tk.END)
            return
        
        self._procesar_siguiente_pedido()

    def _procesar_siguiente_pedido(self):
        if not self.cola_pedidos:
            return

        # FCFS: Sale el primero de la cola
        pedido = self.cola_pedidos.pop(0) 
        self.text_area.insert(tk.END, f"Procesando pedido: '{pedido['comida']}'\n")
        self.text_area.see(tk.END)
        
        tiempo_segundos = pedido['tiempo_preparacion']
        
        if tiempo_segundos > 0:
            self.text_area.insert(tk.END, f"Preparando... ({tiempo_segundos} segundos)\n")
            self.text_area.see(tk.END)
            #segundos a milisegundos para que sea bien rapidin
            tiempo_ms = tiempo_segundos * 1000
            self.root.after(tiempo_ms, lambda: self._finalizar_pedido(pedido))
        else:
            self._finalizar_pedido(pedido)

    def _finalizar_pedido(self, pedido):
        self.text_area.insert(tk.END, f"¡Pedido '{pedido['comida']}' listo para servir!\n")
        self.text_area.see(tk.END)
        
        if self.cola_pedidos:
            self.text_area.insert(tk.END, "Siguiente pedido en la cola...\n")
            self.text_area.see(tk.END)
            self._procesar_siguiente_pedido()
        else:
            self.text_area.insert(tk.END, "No hay más pedidos pendientes.\n")
            self.text_area.see(tk.END) 
            self.text_area.insert(tk.END, "Todos los pedidos han sido procesados.\n\n")
            self.text_area.see(tk.END) 

    def mostrar_historial(self):
        if not self.historial_pedidos:
            self.text_area.insert(tk.END, "\nEl historial está vacío.\n")
            self.text_area.see(tk.END) 
            return
        
        self.text_area.insert(tk.END, "\n--- Historial de Pedidos ---\n")
        for pedido in self.historial_pedidos:
            self.text_area.insert(
                tk.END,
                f"ID: {pedido['id']} | Comida: {pedido['comida']} | Tiempo: {pedido['tiempo_preparacion']}s\n" )
            self.text_area.see(tk.END) 
        self.text_area.insert(tk.END, "----------------------------\n\n")
        self.text_area.see(tk.END) 

    def limpiar_historial(self):
        if self.cola_pedidos:
            self.text_area.insert(tk.END, "\n[BLOQUEADO] No se puede limpiar el historial mientras existan procesos en la cola.\n")
            self.text_area.see(tk.END)
            # Retornamos False para que la interfaz sepa que no se pudo limpiar
            return False
        
        self.historial_pedidos.clear()
        self.text_area.insert(tk.END, "\nHistorial limpiado correctamente.\n")
        self.text_area.see(tk.END)
        return True

    def eliminar_procesos(self, id_objetivo):
        # 1. Inicializamos la variable antes de cualquier bucle
        encontrado = False
        nueva_cola = []

        # 2. Filtramos la cola de pedidos
        for pedido in self.cola_pedidos:
            if pedido['id'] == id_objetivo:
                encontrado = True
                self.text_area.insert(tk.END, f"\nCancelando: '{pedido['comida']}' (ID: {id_objetivo}) de la cola.\n")
            else:
                nueva_cola.append(pedido)

        # 3. Actualizamos la cola con los que NO fueron eliminados
        self.cola_pedidos = nueva_cola

        # 4. También lo quitamos del historial 
        self.historial_pedidos = [p for p in self.historial_pedidos if p['id'] != id_objetivo]

        # 5. Verificamos si no se encontró
        if not encontrado:
            self.text_area.insert(tk.END, f"\nEl ID {id_objetivo} no se encontró en la cola de espera.\n")
        
        self.text_area.see(tk.END)

    def consultar_cola_actual(self):
        if not self.cola_pedidos:
            self.text_area.insert(tk.END, "\n--- La cola está vacía ---\n")
            return
        
        self.text_area.insert(tk.END, "\n--- Pedidos esperando en cola (ID | Nombre) ---\n")
        for pedido in self.cola_pedidos:
            self.text_area.insert(tk.END, f"ID: {pedido['id']} -> {pedido['comida']}\n")
        self.text_area.insert(tk.END, "-------------------------------------------\n")
        self.text_area.see(tk.END)
   

