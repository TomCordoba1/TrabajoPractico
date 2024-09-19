import tkinter as tk
from tkinter import messagebox

def abrir_ventana_registro():
    
    def guardar_usuarios():
        nombre_usuario = entrada_crear_usuario.get()
        contrasenia_usuario = entrada_crear_contraseña.get()
        validar_contrasenia = entrada_validar_contrasenia.get()

        if contrasenia_usuario == validar_contrasenia:
            # Verificar si el usuario ya existe
            with open("usuarios.txt", "r") as archivo:
                for linea in archivo:
                    if (f"Usuario_ {nombre_usuario},") in linea:
                        messagebox.showerror("Error", "El usuario ya existe.")
                return
            
            # Guardar datos en archivo de texto
            with open("usuarios.txt", "a") as archivo:
                archivo.write(f"Usuario_ {nombre_usuario}, Contraseña: {contrasenia_usuario}\n")
            
            # Cerrar registro y volver a la ventana principal
            nueva_ventana_registro.destroy()
        else:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")

    nueva_ventana_registro = tk.Toplevel(ventana)
    nueva_ventana_registro.title("Registrarse")
    nueva_ventana_registro.geometry("300x400")

    # Etiquetas
    tk.Label(nueva_ventana_registro, text="Usuario:").place(x=100, y=110)
    tk.Label(nueva_ventana_registro, text="Contraseña:").place(x=100, y=150)
    tk.Label(nueva_ventana_registro, text="Verificar contraseña:").place(x=100, y=190)

    # Entradas de datos
    entrada_crear_usuario = tk.Entry(nueva_ventana_registro)
    entrada_crear_usuario.place(x=100, y=130)

    entrada_crear_contraseña = tk.Entry(nueva_ventana_registro, show="*")
    entrada_crear_contraseña.place(x=100, y=170)

    entrada_validar_contrasenia = tk.Entry(nueva_ventana_registro, show="*")
    entrada_validar_contrasenia.place(x=100, y=210)

    # Botones
    tk.Button(nueva_ventana_registro, text="Volver", command=nueva_ventana_registro.destroy).place(x=10, y=350)
    tk.Button(nueva_ventana_registro, text="Registrarse", command=guardar_usuarios).place(x=220, y=350)

# Ventana principal
ventana = tk.Tk()
ventana.title("Biblioteca")
ventana.geometry("700x600")

# Etiquetas
tk.Label(ventana, text="Bienvenido a la biblioteca").place(x=10, y=10)
tk.Label(ventana, text="Usuario:").place(x=250, y=130)
tk.Label(ventana, text="Contraseña:").place(x=230, y=160)

# Botones registro y login
tk.Button(ventana, text="Registrarse", command=abrir_ventana_registro).place(x=350, y=200)
tk.Button(ventana, text="Login").place(x=300, y=200)

# Entradas de datos
entrada_usuario = tk.Entry(ventana)
entrada_usuario.place(x=300, y=130)

entrada_contraseña = tk.Entry(ventana, show="*")
entrada_contraseña.place(x=300, y=160)

# Ejecutar
ventana.mainloop()