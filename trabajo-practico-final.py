import tkinter as tk
from tkinter import messagebox

class Usuario:
    def __init__(self, nombre, contrasenia, rol):
        self.nombre = nombre
        self.contrasenia = contrasenia  # Asegúrate de usar el nombre correcto
        self.rol = rol
        
    def __str__(self):
        return f"{self.nombre},{self.contrasenia},{self.rol}"  # Formato adecuado

def cargar_usuario():
    nombre_usuario = entrada_crear_usuario.get()
    contrasenia_usuario = entrada_crear_contraseña.get()
    validar_contrasenia = entrada_validar_contrasenia.get()
    rol_usuario = seleccion.get(seleccion.curselection())

    # Verificar que las contraseñas coincidan
    if contrasenia_usuario == validar_contrasenia:
        nuevo_usuario = Usuario(nombre_usuario, contrasenia_usuario, rol_usuario)
        
        # Guardar el usuario en el archivo
        with open("Usuarios.txt", "a") as archivo:
            archivo.write(f"{nuevo_usuario}\n")  # Aquí se usa el método __str__
        messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
        volver_inicio()  # Volver a la ventana de login
    else:
        messagebox.showerror("Error", "Las contraseñas no coinciden.")

def validar_login():
    nombre_usuario = entrada_usuario.get()
    contrasenia = entrada_contraseña.get()
    try:
        with open("Usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario_datos = linea.strip().split(",")
                if len(usuario_datos) == 3:  # Asegúrate de que hay 3 partes
                    if usuario_datos[0] == nombre_usuario and usuario_datos[1] == contrasenia:
                        abrir_ventana_administrador(usuario_datos[2])  # Pasa el rol
                        return
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo de usuarios no existe.")

    messagebox.showerror("Error", "El usuario ingresado no existe o la contraseña es incorrecta.")

def abrir_ventana_registro():
    ventana_login.pack_forget()  # Cerrar frame de login
    nueva_ventana_registro.pack(expand=True, fill="both")

def volver_inicio():
    nueva_ventana_registro.pack_forget()
    ventana_login.pack(expand=True, fill="both")

def abrir_ventana_administrador(rol):
    ventana_administrador.pack_forget()
    ventana_administrador.pack(expand=True, fill="both")
    tk.Label(ventana_administrador, text=f"Bienvenido, {rol}!").pack(pady=20)

# Ventana principal
ventana = tk.Tk()
ventana.title("Biblioteca")
ventana.geometry("700x600")
# 
ventana_login = tk.Frame(ventana)
ventana_login.pack(expand=True, fill="both")

# VENTANA ADMINISTRADOR
ventana_administrador = tk.Frame(ventana)

# Ventana registro
nueva_ventana_registro = tk.Frame(ventana)

# Etiquetas
tk.Label(ventana_login, text="Bienvenido a la biblioteca").place(x=10, y=10)
tk.Label(ventana_login, text="Usuario:").place(x=250, y=130)
tk.Label(ventana_login, text="Contraseña:").place(x=230, y=160)

# Botones registro y login
tk.Button(ventana_login, text="Registrarse", command=abrir_ventana_registro).place(x=350, y=200)
tk.Button(ventana_login, text="Login", command=validar_login).place(x=300, y=200)

# Entradas de datos
entrada_usuario = tk.Entry(ventana_login)
entrada_usuario.place(x=300, y=130)

entrada_contraseña = tk.Entry(ventana_login, show="*")
entrada_contraseña.place(x=300, y=160)

# Etiquetas del registro
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
tk.Button(nueva_ventana_registro, text="Volver", command=volver_inicio).place(x=10, y=350)
tk.Button(nueva_ventana_registro, text="Registrarse", command=cargar_usuario).place(x=220, y=350)

# Listbox para seleccionar rol
seleccion = tk.Listbox(nueva_ventana_registro)
seleccion.place(x=250, y=380)
seleccion.insert(1, "Administrador")
seleccion.insert(2, "Normalito")

# Ejecutar
ventana.mainloop()