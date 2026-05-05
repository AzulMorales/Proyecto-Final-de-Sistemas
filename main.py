import time 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, font
from Proyecto.crearProcesos import sistema_operativo

#Creación de la ventana principal

root= tk.Tk()
root.title("Sistema de un Restaurante")
root.geometry("800x600") 
root.iconbitmap('recursos\\favicon.ico')
root.configure(bg="#edcc8a")

frame = tk.Frame(root)
frame.pack(pady=10)
text_area = tk.Text(root, width=70, height=30)
text_area.pack()
root.resizable(False, False)


sistemaOp = sistema_operativo(root, text_area)


# El usuario escribe el tiempo
def pedir_tiempo(nombre_comida):
    ventana = tk.Toplevel(root)
    ventana.title("Tiempo de preparación")
    ventana.geometry("300x150")
    ventana.resizable(False, False)


    ventana.update_idletasks()
    ancho = 300
    alto = 150

    # Obtener posición de la ventana principal
    x_root = root.winfo_x()
    y_root = root.winfo_y()
    w_root = root.winfo_width()
    h_root = root.winfo_height()

    x = x_root + (w_root // 2) - (ancho // 2)
    y = y_root + (h_root // 2) - (alto // 2)

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    tk.Label(ventana, text=f"Tiempo para {nombre_comida} (segundos):").pack(pady=10)
    entrada = tk.Entry(ventana)
    entrada.pack()

    #boton de confirmar
    def confirmar():
        tiempo = entrada.get().strip()
        if not tiempo.isdigit():
            messagebox.showerror("Error", "Debes ingresar un número válido.")
            return
        sistemaOp.agregar_pedido(nombre_comida, int(tiempo))
        ventana.destroy()
    ttk.Button(ventana, text="Aceptar", command=confirmar).pack(pady=10)

# Botones para agregar pedidos
ttk.Button(frame, text="Hamburguesa",
           command=lambda: pedir_tiempo("Hamburguesa")).grid(row=0, column=0, padx=5)

ttk.Button(frame, text="Tacos de birria",
           command=lambda: pedir_tiempo("Tacos de birria")).grid(row=0, column=1, padx=5)

ttk.Button(frame, text="Boneless",
           command=lambda: pedir_tiempo("Boneless")).grid(row=0, column=2, padx=5)




#Esto tiene que ir al final del código, por lo que si se va a agregar algo, recuerde eso
root.mainloop()