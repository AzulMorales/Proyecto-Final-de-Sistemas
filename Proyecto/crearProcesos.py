import time 
import tkinter as tk

class Proceso:
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo_total = tiempo
        self.tiempo_restante= tiempo
        self.estado = "Listo"  # Listo, Ejecutando, Terminado

    def __str__(self):
        return f"{self.nombre} | Restante: {self.tiempo_restante} | Estado: {self.estado}"


class sistema_operativo:
    def __init__(self, root, text_widget):
        
        self.cola_pedidos = []
        self.root = root
        self.text_widget = text_widget
        self.procesando = False
        #Colores
        self.text_widget.tag_config("verde", foreground = "green")
        self.text_widget.tag_config("rojo", foreground ="red" )

    def agregar_pedido(self, nombre, tiempo):
        proceso = Proceso(nombre, tiempo)
        self.cola_pedidos.append(proceso)
        self.mostrar(f"Pedido agregado: {proceso.nombre} (tiempo: {tiempo} segundos)", color="verde")
        
        if not self.procesando:
            self.procesar_pedidos()

    def procesar_pedidos(self):
        if not self.cola_pedidos:
            self.mostrar("No hay más pedidos en la cola", color= "rojo")
            self.procesando = False
            return
        self.procesando = True
        proceso = self.cola_pedidos[0]

        if proceso.tiempo_restante == proceso.tiempo_total:
            proceso.estado = "Ejecutando"
            self.mostrar(f"Ejecutando pedido: {proceso.nombre}")

        if proceso.tiempo_restante > 0:
            proceso.tiempo_restante -=1
            self.mostrar(F"El pedido {proceso.nombre} tiene tiempo restante de: {proceso.tiempo_restante} segundos")
            self.root.after(1000, self.procesar_pedidos) #temporizador, 1 segundo despues

        else:
            proceso.estado = "Terminado"
            self.mostrar(f"Pedido listo: {proceso.nombre}", color="verde")
            self.cola_pedidos.pop(0)
            self.root.after(500, self.procesar_pedidos)

    def mostrar(self, mensaje, color= None):
        if color:
            self.text_widget.insert(tk.END, mensaje + "\n", color)
        else:
            self.text_widget.insert(tk.END, mensaje +"\n")