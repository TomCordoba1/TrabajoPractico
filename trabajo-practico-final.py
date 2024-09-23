import tkinter as tk
from tkinter import messagebox
import os

class Usuario:
    def __init__(self, nombre, contrasenia, rol):
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.rol = rol

    def __str__(self):
        return f"{self.nombre},{self.contrasenia},{self.rol}"

class BibliotecaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Biblioteca")
        self.master.geometry("700x600")
        self.ruta_archivo = r"C:\Users\tomii\OneDrive\Escritorio\Tomi\ITEC\Python\Programacion 1\Ejercicios Python\TrabajoPractico\TrabajoPractico_clon\Usuarios.txt"

        self.ventana_login = tk.Frame(master)
        self.ventana_administrador = tk.Frame(master)
        self.nueva_ventana_registro = tk.Frame(master)

        self.crear_widgets()

    def crear_widgets(self):
        # Login
        tk.Label(self.ventana_login, text="Bienvenido a la biblioteca").place(x=10, y=10)
        tk.Label(self.ventana_login, text="Usuario:").place(x=250, y=130)
        tk.Label(self.ventana_login, text="Contraseña:").place(x=230, y=160)

        self.entrada_usuario = tk.Entry(self.ventana_login)
        self.entrada_usuario.place(x=300, y=130)
        self.entrada_contraseña = tk.Entry(self.ventana_login, show="*")
        self.entrada_contraseña.place(x=300, y=160)

        tk.Button(self.ventana_login, text="Registrarse", command=self.abrir_ventana_registro).place(x=350, y=200)
        tk.Button(self.ventana_login, text="Login", command=self.validar_login).place(x=300, y=200)
        tk.Button(self.ventana_login, text="Cerrar", command=self.master.destroy).place(x=20, y=550)

        # Registro
        tk.Label(self.nueva_ventana_registro, text="Usuario:").place(x=100, y=110)
        tk.Label(self.nueva_ventana_registro, text="Contraseña:").place(x=100, y=150)
        tk.Label(self.nueva_ventana_registro, text="Verificar contraseña:").place(x=100, y=190)

        self.entrada_crear_usuario = tk.Entry(self.nueva_ventana_registro)
        self.entrada_crear_usuario.place(x=100, y=130)
        self.entrada_crear_contraseña = tk.Entry(self.nueva_ventana_registro, show="*")
        self.entrada_crear_contraseña.place(x=100, y=170)
        self.entrada_validar_contrasenia = tk.Entry(self.nueva_ventana_registro, show="*")
        self.entrada_validar_contrasenia.place(x=100, y=210)

        tk.Button(self.nueva_ventana_registro, text="Volver", command=self.volver_inicio_registro).place(x=10, y=350)
        tk.Button(self.nueva_ventana_registro, text="Registrarse", command=self.cargar_usuario).place(x=250, y=350)

        # Listbox para seleccionar rol
        self.seleccion = tk.Listbox(self.nueva_ventana_registro)
        self.seleccion.place(x=100, y=250)
        self.seleccion.insert(1, "Administrador")
        self.seleccion.insert(2, "Cliente")

        # Inicializa la ventana de login
        self.ventana_login.pack(expand=True, fill="both")

    def cargar_usuario(self):
        nombre_usuario = self.entrada_crear_usuario.get()
        contrasenia_usuario = self.entrada_crear_contraseña.get()
        validar_contrasenia = self.entrada_validar_contrasenia.get()
        rol_usuario = self.seleccion.get(self.seleccion.curselection())

        if not nombre_usuario or not contrasenia_usuario or not validar_contrasenia:
            messagebox.showerror("Error", "Todos los campos deben ser completados.")
            return
    
        if contrasenia_usuario == validar_contrasenia:
            nuevo_usuario = Usuario(nombre_usuario, contrasenia_usuario, rol_usuario)

            try:
                with open(self.ruta_archivo, "a") as archivo:
                    archivo.write(f"{nuevo_usuario}\n")
                messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
                self.volver_inicio_registro()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el usuario: {e}")
        else:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")

    def validar_login(self):
        nombre_usuario = self.entrada_usuario.get().strip()
        contrasenia = self.entrada_contraseña.get().strip()
        print(f"Intentando iniciar sesión con: {nombre_usuario}, {contrasenia}")

        try:
            with open(self.ruta_archivo, "r") as archivo:
                for linea in archivo:
                    usuario_datos = linea.strip().split(",")
                    if len(usuario_datos) == 3:
                        if usuario_datos[0].strip() == nombre_usuario and usuario_datos[1].strip() == contrasenia:
                            self.abrir_ventana_administrador(usuario_datos[2])
                            return
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo de usuarios no existe.")
            return

        messagebox.showerror("Error", "El usuario ingresado no existe o la contraseña es incorrecta.")

    def volver_inicio_adm(self):
        self.ventana_administrador.pack_forget()
        for widget in self.ventana_administrador.winfo_children():
            widget.destroy()
        self.ventana_login.pack(expand=True, fill="both")

    def volver_inicio_registro(self):
        self.nueva_ventana_registro.pack_forget()
        for widget in self.nueva_ventana_registro.winfo_children():
            widget.destroy()
        self.ventana_login.pack(expand=True, fill="both")

    def abrir_ventana_registro(self):
        self.ventana_login.pack_forget()
        self.nueva_ventana_registro.pack(expand=True, fill="both")

    def abrir_ventana_administrador(self, rol):
        self.ventana_login.pack_forget()
        self.ventana_administrador.pack(expand=True, fill="both")
        tk.Label(self.ventana_administrador, text=f"Bienvenido, {rol}!").pack(pady=20)
        tk.Button(self.ventana_administrador, text="Cerrar Sesión", command=self.master.destroy).pack(pady=10)

# Crear y ejecutar la aplicación
root = tk.Tk()
app = BibliotecaApp(root)
root.mainloop()