import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, Scrollbar

class Usuario:
    def __init__(self, nombre, contrasenia, rol):
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.rol = rol

    def __str__(self):
        return f"{self.nombre},{self.contrasenia},{self.rol}"

class Libro:
    def __init__(self, titulo, autor):
        self.id_libro = 0  
        self.titulo = titulo
        self.autor = autor
        self.estado = "disponible"

    def __str__(self):
        return f"{self.id_libro}, {self.titulo}, {self.estado}."

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.contador_libros = 0
        self.cargar_libros_archivo()

    def agregar_libro(self, titulo, autor):
        self.contador_libros += 1
        nuevo_libro = Libro(titulo, autor)
        nuevo_libro.id_libro = self.contador_libros
        self.libros.append(nuevo_libro)
        self.guardar_libros()

    def guardar_libros(self):
        with open("Libros.txt", "w") as archivo:
            for libro in self.libros:
                archivo.write(f"{libro.id_libro},{libro.titulo},{libro.autor},{libro.estado}\n")

    def cargar_libros_archivo(self):
        try:
            with open("Libros.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    libro = Libro(datos[1], datos[2])
                    libro.id_libro = int(datos[0])
                    self.libros.append(libro)
        except FileNotFoundError:
            pass

class BibliotecaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Biblioteca")
        self.master.geometry("700x600")
        self.ruta_archivo = "Usuarios.txt"

        self.biblioteca = Biblioteca()
        self.usuarios = []  # Para almacenar usuarios

        self.ventana_login = tk.Frame(master)
        self.ventana_administrador = tk.Frame(master)
        self.ventana_cliente = tk.Frame(master)
        self.ventana_registro = tk.Frame(master)

        self.crear_widgets()
        self.cargar_usuarios()  # Cargar usuarios desde el archivo

    def crear_widgets(self):
        # Login
        tk.Label(self.ventana_login, text="Bienvenido a la biblioteca").place(x=10, y=10)
        tk.Label(self.ventana_login, text="Usuario:").place(x=250, y=130)
        tk.Label(self.ventana_login, text="Contraseña:").place(x=230, y=160)

        self.entrada_usuario = tk.Entry(self.ventana_login)
        self.entrada_usuario.place(x=300, y=130)
        self.entrada_contrasenia = tk.Entry(self.ventana_login, show="*")
        self.entrada_contrasenia.place(x=300, y=160)

        tk.Button(self.ventana_login, text="Login", command=self.validar_login).place(x=300, y=200)
        tk.Button(self.ventana_login, text="Registrar", command=self.abrir_ventana_registro).place(x=300, y=230)
        tk.Button(self.ventana_login, text="Cerrar", command=self.master.destroy).place(x=20, y=550)

        # Inicializa la ventana de login
        self.ventana_login.pack(expand=True, fill="both")

    def cargar_usuarios(self):
        try:
            with open(self.ruta_archivo, "r") as archivo:
                for linea in archivo:
                    usuario_datos = linea.strip().split(",")
                    if len(usuario_datos) == 3:
                        usuario = Usuario(usuario_datos[0], usuario_datos[1], usuario_datos[2])
                        self.usuarios.append(usuario)
        except FileNotFoundError:
            print("El archivo de usuarios no se encontró.")

    def guardar_usuarios(self):
        with open(self.ruta_archivo, "w") as archivo:
            for usuario in self.usuarios:
                archivo.write(f"{usuario}\n")

    def validar_login(self):
        nombre_usuario = self.entrada_usuario.get().strip()
        contrasenia = self.entrada_contrasenia.get().strip()

        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario and usuario.contrasenia == contrasenia:
                if usuario.rol == "Administrador":
                    self.abrir_ventana_administrador(usuario.rol)
                else:
                    self.abrir_ventana_cliente(usuario.rol)
                return

        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def abrir_ventana_cliente(self, rol):
        self.ventana_login.pack_forget()
        self.ventana_cliente.pack(expand=True, fill="both")
        tk.Label(self.ventana_cliente, text=f"Bienvenido, {rol}!").pack(pady=20)
        tk.Button(self.ventana_cliente, text="Cerrar Sesión", command=self.master.destroy).pack(pady=10)

    def abrir_ventana_administrador(self, rol):
        self.ventana_login.pack_forget()
        self.ventana_administrador.pack(expand=True, fill="both")
        tk.Label(self.ventana_administrador, text=f"Bienvenido, {rol}!").pack(pady=20)

        tk.Button(self.ventana_administrador, text="Agregar Libro", command=self.agregar_libro).pack(pady=10)
        tk.Button(self.ventana_administrador, text="Eliminar Libro", command=self.eliminar_libro).pack(pady=10)
        tk.Button(self.ventana_administrador, text="Mostrar Libros", command=self.mostrar_libros).pack(pady=10)
        tk.Button(self.ventana_administrador, text="Eliminar Cliente", command=self.eliminar_cliente).pack(pady=10)
        tk.Button(self.ventana_administrador, text="Cerrar Sesión", command=self.master.destroy).pack(pady=10)

    def abrir_ventana_registro(self):
        self.ventana_login.pack_forget()
        self.ventana_registro.pack(expand=True, fill="both")
        tk.Label(self.ventana_registro, text="Registro de Usuario").pack(pady=10)
        tk.Label(self.ventana_registro, text="Nombre:").pack(pady=5)
        self.entrada_nombre = tk.Entry(self.ventana_registro)
        self.entrada_nombre.pack(pady=5)
        tk.Label(self.ventana_registro, text="Contraseña:").pack(pady=5)
        self.entrada_contrasenia = tk.Entry(self.ventana_registro, show="*")
        self.entrada_contrasenia.pack(pady=5)

        # Listbox para seleccionar el rol
        tk.Label(self.ventana_registro, text="Selecciona Rol:").pack(pady=5)
        self.listbox_roles = Listbox(self.ventana_registro, height=2)
        self.listbox_roles.insert(1, "Administrador")
        self.listbox_roles.insert(2, "Cliente")
        self.listbox_roles.pack(pady=5)

        tk.Button(self.ventana_registro, text="Registrar", command=self.registrar_usuario).pack(pady=10)
        tk.Button(self.ventana_registro, text="Volver", command=self.volver_login).pack(pady=10)

    def volver_login(self):
        self.ventana_registro.pack_forget()
        self.ventana_login.pack(expand=True, fill="both")

    def registrar_usuario(self):
        nombre = self.entrada_nombre.get().strip()
        contrasenia = self.entrada_contrasenia.get().strip()
        rol_seleccionado = self.listbox_roles.curselection()  # Obtener selección

        if nombre and contrasenia and rol_seleccionado:
            rol = self.listbox_roles.get(rol_seleccionado[0])  # Obtener el rol seleccionado
            nuevo_usuario = Usuario(nombre, contrasenia, rol)
            self.usuarios.append(nuevo_usuario)
            self.guardar_usuarios()  # Guarda el nuevo usuario
            messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            self.volver_login()
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos.")

    def agregar_libro(self):
        titulo = simpledialog.askstring("Agregar Libro", "Título del libro:")
        autor = simpledialog.askstring("Agregar Libro", "Autor del libro:")
        if titulo and autor:
            self.biblioteca.agregar_libro(titulo, autor)
            messagebox.showinfo("Éxito", "Libro agregado con éxito.")
        else:
            messagebox.showerror("Error", "Los campos no pueden estar vacíos.")

    def eliminar_libro(self):
        libro_id = simpledialog.askinteger("Eliminar Libro", "Ingrese el ID del libro a eliminar:")
        if libro_id is not None:
            libro_encontrado = False
            for libro in self.biblioteca.libros:
                if libro.id_libro == libro_id:
                    self.biblioteca.libros.remove(libro)
                    self.biblioteca.guardar_libros()
                    libro_encontrado = True
                    messagebox.showinfo("Éxito", "Libro eliminado con éxito.")
                    break
            if not libro_encontrado:
                messagebox.showerror("Error", "No se encontró un libro con ese ID.")
        else:
            messagebox.showerror("Error", "ID no válido.")

    def mostrar_libros(self):
        if self.biblioteca.libros:
            libros_str = "\n".join(str(libro) for libro in self.biblioteca.libros)
            messagebox.showinfo("Libros Registrados", libros_str)
        else:
            messagebox.showinfo("Libros Registrados", "No hay libros registrados.")

    def eliminar_cliente(self):
        nombre_cliente = simpledialog.askstring("Eliminar Cliente", "Ingrese el nombre del cliente a eliminar:")
        if nombre_cliente:
            usuario_encontrado = False
            for usuario in self.usuarios:
                if usuario.nombre == nombre_cliente and usuario.rol == "Cliente":
                    self.usuarios.remove(usuario)
                    self.guardar_usuarios()
                    usuario_encontrado = True
                    messagebox.showinfo("Éxito", "Cliente eliminado con éxito.")
                    break
            if not usuario_encontrado:
                messagebox.showerror("Error", "No se encontró un cliente con ese nombre.")
        else:
            messagebox.showerror("Error", "Nombre no válido.")

# Crear y ejecutar la aplicación
root = tk.Tk()
app = BibliotecaApp(root)
root.mainloop()