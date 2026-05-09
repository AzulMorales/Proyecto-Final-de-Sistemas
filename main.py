import time 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, font
from PIL import Image, ImageTk
from Proyecto.sistema import sistema_operativo

sistemaOp = sistema_operativo()
ventana_actual = None

#Centrar la ventana padre
def centrar_ventana(ventana,ancho,alto):
    
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = int((pantalla_ancho/2) - (ancho/2))
    y = int((pantalla_alto/2) - (alto/2))
    return ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

#estetica, en el que cambie de color el boton al tocarlo
def tocar_boton(e):
    
    e.widget['background'] = "#F57C00" 

def no_tocar_boton(e):
    e.widget['background'] ="#DDB885"

#Creación de la ventana principal
root= tk.Tk()
root.title("Sistema de un Restaurante")
centrar_ventana(root, 800,600)
root.iconbitmap('recursos\\favicon.ico')
root.configure(bg="#B22222")
root.resizable(False, False)

#texto
bienve = tk.Label(root,text="Bienvenido a este pequeño sistema que simula los procesos de cualquier tipo de restaurante.",font=("Helvetica", 17, "bold"),
                  background="#B22222",foreground="white", wraplength= 380,justify="right" )

bienve.place(relx=0.5, y=80, anchor="w")

#Imagen de un chef
frame_derecha = tk.Frame(root, bg="#B22222")
frame_derecha.pack(side=tk.RIGHT, fill="y")
#Redimensionar
immagen = Image.open("recursos\\chef.png")
imagen = immagen.resize((350, 350))   
imagen = ImageTk.PhotoImage(imagen)

# Un label como en Java
label_imagen = tk.Label(root, image=imagen, bg="#B22222")
label_imagen.image = imagen 

label_imagen.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)


#Menu izquierdo
def crear_menu(ventana):
    menu_izq = tk.Frame(ventana, width=130, bg="#8E7462")
    menu_izq.pack(side=tk.LEFT, fill="y")

    #Ocultar y mostrar el menu lateral
    def ocultar_ver_menu():
        #ocultar
        if menu_izq.winfo_ismapped():
            menu_izq.pack_forget()
        else:
            # Reaparece exactamente en su posición original
            menu_izq.pack(side=tk.LEFT, fill="y")

    boton_menu = tk.Button(ventana,text="≡",font="Verdana 15 bold",width=3, background="#DDB885", 
                        borderwidth=3,command=ocultar_ver_menu,)
    #Para que el boton no dependa de ninguno y no se mueva
    boton_menu.place(x=10, y=10)

    boton_menu.bind("<Enter>", tocar_boton)
    boton_menu.bind("<Leave>", no_tocar_boton)       

    #Botones del menu
    boton_crear_proceso = tk.Button(menu_izq,text="Crear Proceso",font="Helvetica 14", background="#DDB885", borderwidth=2,
                                    command= lambda: cambiar_ventana(crear_pedidos))
    boton_crear_proceso.pack(fill="x", pady=75)

    boton_crear_proceso.bind("<Enter>", tocar_boton)
    boton_crear_proceso.bind("<Leave>", no_tocar_boton)
                            
    boton_ver_proceso = tk.Button(menu_izq,text="Ver Proceso",font="Helvetica 14", background="#DDB885",borderwidth=2, 
                                  command=lambda: cambiar_ventana(ver_procesos))
    boton_ver_proceso.pack(fill="x", pady=0)

    boton_ver_proceso.bind("<Enter>", tocar_boton)
    boton_ver_proceso.bind("<Leave>", no_tocar_boton)

    boton_eliminar_proceso = tk.Button(menu_izq,text="Eliminar Proceso",font="Helvetica 14", background="#DDB885",borderwidth=2,
                                       command=lambda: cambiar_ventana(eliminar_procesos))
    boton_eliminar_proceso.pack(fill="x", pady=75)

    boton_eliminar_proceso.bind("<Enter>", tocar_boton)
    boton_eliminar_proceso.bind("<Leave>", no_tocar_boton)

def crear_ventana(titulo):
    global ventana_actual
    # Cerrar la ventana anterior
    if ventana_actual is not None:
        ventana_actual.destroy()

    ventana = tk.Toplevel(root)
    ventana.title(titulo)
    centrar_ventana(ventana, 800, 600)
    ventana.configure(bg="#B22222")
    ventana.resizable(False, False)

    # Frame contenedor del contenido
    ventana.contenido = tk.Frame(ventana, bg="#B22222")
    ventana.contenido.pack(side="right", fill="both", expand=True)

    # Crear menú en esta ventana
    crear_menu(ventana)
    ventana_actual = ventana
    return ventana

#cambiar de ventana si perder los datos
def cambiar_ventana(funcion):
    funcion()


#Ventana para crear pedidos
def crear_pedidos():
    ventana = crear_ventana("Crear Pedido")
    ventana.iconbitmap('recursos\\favicon.ico')
    
    # Frame para botones
    frame1 = tk.Frame(ventana.contenido, bg="#B22222")
    frame1.pack(side="top", pady=10)

    # Área de texto
    text_area = tk.Text(ventana.contenido, width=70, height=30)
    text_area.pack(pady=10)

    sistemaOp.set_contexto(ventana, text_area)
    
  

    # El usuario escribe el tiempo
    def pedir_tiempo(nombre_comida):
        ventana2 = tk.Toplevel(ventana)
        ventana2.title("Tiempo de preparación")
        ventana2.resizable(False, False)
    
        # Obtener posición de la ventana principal
        ancho = 300
        alto = 150
        ventana2.update_idletasks()
        x_root = ventana.winfo_x()
        y_root = ventana.winfo_y()
        w_root = ventana.winfo_width()
        h_root = ventana.winfo_height()
        x = x_root + (w_root // 2) - (ancho // 2)
        y = y_root + (h_root // 2) - (alto // 2)

        ventana2.geometry(f"{ancho}x{alto}+{x}+{y}")

        #label que sale en ventana
        tk.Label(ventana2, text=f"Tiempo para {nombre_comida} (segundos):").pack(pady=10)
        entrada = tk.Entry(ventana2)
        entrada.pack()

        #boton de confirmar
        def confirmar():
            tiempo = entrada.get().strip()
            if not tiempo.isdigit():
                messagebox.showerror("Error", "Debes ingresar un número válido.")
                return
            
            # Calculamos el ID basado en el historial para que sea único
            nuevo_id = len(sistemaOp.historial_pedidos) + 1
            
            # Enviamos los datos al sistema
            sistemaOp.agregar_pedido(nuevo_id, nombre_comida, int(tiempo))
            
            # Notificamos al usuario qué ID se generó
            messagebox.showinfo("Pedido Creado", 
                                f"Producto: {nombre_comida}\n"
                                f"ID Asignado: {nuevo_id}\n"
                                f"Tiempo: {tiempo} segundos")
            
            ventana2.destroy() # Cerramos la ventanita emergente

        # El botón de la ventana emergente llama a esta nueva versión de confirmar
        ttk.Button(ventana2, text="Aceptar", command=confirmar).pack(pady=10)


    #botones del crear procesos
    boton_hamburguesa = tk.Button(frame1,text="Hamburguesa",font=("Helvetica 13"), background="#DDB885", borderwidth=2, 
                                  command=lambda: pedir_tiempo("Hamburguesa"))
    boton_hamburguesa.pack(padx=10, side="left")
    boton_hamburguesa.bind("<Enter>", tocar_boton)
    boton_hamburguesa.bind("<Leave>", no_tocar_boton)   

    boton_tacos = tk.Button(frame1, text="Tacos de Birria",font=("Helvetica 13"), background="#DDB885", borderwidth=2, 
                            command=lambda: pedir_tiempo("Tacos de Birria"))
    boton_tacos.pack(padx=10, side="left")
    boton_tacos.bind("<Enter>", tocar_boton)
    boton_tacos.bind("<Leave>", no_tocar_boton)

    boton_boneless = tk.Button(frame1, text="Boneless",font=("Helvetica 13"), background="#DDB885", borderwidth=2,
                               command=lambda: pedir_tiempo("Boneless"))
    boton_boneless.pack(padx=10, side="left")
    boton_boneless.bind("<Enter>", tocar_boton)
    boton_boneless.bind("<Leave>", no_tocar_boton)
  

def ver_procesos():
    ventana= crear_ventana("Ver Procesos")
    ventana.iconbitmap('recursos\\favicon.ico')

    # Frame horizontal
    frame_botones = tk.Frame(ventana.contenido, bg="#B22222")
    frame_botones.pack(side="top", pady=10)

    # Área de texto
    text_area = tk.Text(ventana.contenido, width=70, height=30)
    text_area.pack(pady=10)

    sistemaOp.set_contexto(ventana, text_area)

   
    #Agregar botones
    def intentar_limpiar():
        # Llamamos al método y capturamos si tuvo éxito o no
        exito = sistemaOp.limpiar_historial()
        if not exito:
            messagebox.showwarning("Acción no permitida", 
                "Hay pedidos en espera. Debes procesarlos o eliminarlos antes de limpiar el historial.")

    
    
    boton_procesar = tk.Button(frame_botones, text="Procesar pedidos", font="Helvetica 13" ,background="#DDB885", command=sistemaOp.procesar_pedidos)
    boton_procesar.pack( side="left", padx=10)
    boton_procesar.bind("<Enter>", tocar_boton)
    boton_procesar.bind("<Leave>", no_tocar_boton)

    boton_historial = tk.Button(frame_botones, text="Mostrar historial", font="Helvetica 13" ,background="#DDB885", command=sistemaOp.mostrar_historial)
    boton_historial.pack(side="left",padx=10)
    boton_historial.bind("<Enter>", tocar_boton)
    boton_historial.bind("<Leave>", no_tocar_boton)

    boton_limpiar = tk.Button(frame_botones, text="Limpiar historial", 
                              font="Helvetica 13", background="#DDB885", 
                              command=intentar_limpiar)
    boton_limpiar.pack(side="left",padx=10)
    boton_limpiar.bind("<Enter>", tocar_boton)
    boton_limpiar.bind("<Leave>", no_tocar_boton)




    # Función interna para conectar la interfaz con el núcleo
def eliminar_procesos():
    ventana = crear_ventana("Eliminar Procesos")
    ventana.iconbitmap('recursos\\favicon.ico')

    # Frame para controles superiores
    frame_controles = tk.Frame(ventana.contenido, bg="#B22222")
    frame_controles.pack(side="top", pady=10)

    # NUEVO: Botón para consultar qué pedidos hay y sus IDs
    boton_consultar = tk.Button(frame_controles, text="Ver IDs en Cola", font="Helvetica 11 bold",
                                    background="#DDB885", command=sistemaOp.consultar_cola_actual)
    boton_consultar.pack(pady=5)

    # Frame para la entrada de ID
    frame_input = tk.Frame(ventana.contenido, bg="#B22222")
    frame_input.pack(side="top", pady=10)

    tk.Label(frame_input, text="ID a eliminar:", font="Helvetica 12 bold", 
                bg="#B22222", fg="white").pack(side="left", padx=5)
        
    entrada_id = tk.Entry(frame_input, font="Helvetica 12", width=10)
    entrada_id.pack(side="left", padx=5)

        # Área de texto
    text_area = tk.Text(ventana.contenido, width=70, height=20)
    text_area.pack(pady=10)

    sistemaOp.set_contexto(ventana, text_area)

    def ejecutar_eliminacion():
        id_texto = entrada_id.get().strip()
        if id_texto.isdigit():
            id_num = int(id_texto)
            sistemaOp.eliminar_procesos(id_num)
            entrada_id.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Ingrese un número de ID válido.")

    boton_confirmar = tk.Button(frame_input, text="Confirmar Eliminación", font="Helvetica 11", 
                                background="#F57C00", borderwidth=2, command= ejecutar_eliminacion)
    boton_confirmar.pack(side="left", padx=10)     

  

crear_menu(root)
#Esto tiene que ir al final del código, por lo que si se va a agregar algo, recuerde eso
root.mainloop()