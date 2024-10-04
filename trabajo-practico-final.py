import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, Toplevel, Scrollbar

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
        return f"{self.id_libro}, {self.titulo}, {self.autor}, {self.estado}."

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

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                self.libros.remove(libro)
                self.guardar_libros()
                return True
        return False

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
                    libro.estado = datos[3]
                    self.libros.append(libro)
        except FileNotFoundError:
            pass

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

class BibliotecaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Biblioteca")
        self.master.geometry("700x600")
        self.ruta_archivo = "Usuarios.txt"

        self.biblioteca = Biblioteca()
        self.usuarios = []
        self.favoritos = []

        self.ventana_login = tk.Frame(master)
        self.ventana_administrador = tk.Frame(master)
        self.ventana_cliente = tk.Frame(master)
        self.ventana_registro = tk.Frame(master)

        self.crear_widgets()
        self.cargar_usuarios()

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
        self.cerrar_ventanas()
        self.ventana_cliente.pack(expand=True, fill="both")
        tk.Label(self.ventana_cliente, text=f"Bienvenido, {rol}!").pack(pady=20)

        tk.Button(self.ventana_cliente, text="Visualizar Libros", command=self.visualizar_libros).pack(pady=10)
        tk.Button(self.ventana_cliente, text="Ver Detalles de Favoritos", command=self.ver_detalles).pack(pady=10)
        tk.Button(self.ventana_cliente, text="Regresar", command=self.volver_login).pack(pady=10)
        tk.Button(self.ventana_cliente, text="Cerrar Sesión", command=self.master.destroy).pack(pady=10)

    def visualizar_libros(self):
        if not self.biblioteca.libros:
            messagebox.showinfo("Información", "No hay libros disponibles.")
            return

        ventana_libros = Toplevel(self.master)
        ventana_libros.title("Seleccionar Libro")
        ventana_libros.geometry("300x400")

        listbox_libros = Listbox(ventana_libros)
        for libro in self.biblioteca.libros:
            listbox_libros.insert(tk.END, libro.titulo)
        listbox_libros.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(ventana_libros)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox_libros.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox_libros.yview)

        tk.Button(ventana_libros, text="Agregar a Favoritos", command=lambda: self.agregar_a_favoritos(listbox_libros.get(tk.ACTIVE))).pack(pady=10)

    def agregar_a_favoritos(self, titulo_libro):
        if titulo_libro:
            libro = self.biblioteca.buscar_libro(titulo_libro)
            if libro and libro.estado == "disponible":
                self.favoritos.append(libro)
                messagebox.showinfo("Éxito", "Libro agregado a favoritos.")
            else:
                messagebox.showerror("Error", "El libro no está disponible o no existe.")
        else:
            messagebox.showerror("Error", "No se ha seleccionado ningún libro.")

    def ver_detalles(self):
        if not self.favoritos:
            messagebox.showinfo("Favoritos", "No hay libros en la lista de favoritos.")
            return

        favoritos_str = "\n".join(libro.titulo for libro in self.favoritos)
        messagebox.showinfo("Libros Favoritos", "Tus libros favoritos:\n" + favoritos_str)

    def abrir_ventana_administrador(self, rol):
        self.cerrar_ventanas()
        self.ventana_administrador.pack(expand=True, fill="both")
        tk.Label(self.ventana_administrador, text=f"Bienvenido, {rol}!").pack(pady=20)

        tk.Button(self.ventana_administrador, text="Agregar Libro", command=self.agregar_libro).pack(pady=10)
        tk.Button(self.ventana_administrador, text="Modificar Libro", command=self.mostrar_libros_para_modificar).pack(pady=10)
        tk.Button(self.ventana_administrador, text="Eliminar Libro", command=self.eliminar_libro).pack(pady=10)
        tk.Button(self.ventana_administrador, text="Mostrar Libros", command=self.mostrar_libros).pack(pady=10)
        tk.Button(self.ventana_administrador, text="Regresar", command=self.volver_login).pack(pady=10)

    def cerrar_ventanas(self):
        self.ventana_login.pack_forget()
        self.ventana_administrador.pack_forget()
        self.ventana_cliente.pack_forget()
        self.ventana_registro.pack_forget()

    def volver_login(self):
        self.cerrar_ventanas()
        self.ventana_login.pack(expand=True, fill="both")

    def abrir_ventana_registro(self):
        self.cerrar_ventanas()
        self.ventana_registro.pack(expand=True, fill="both")
        tk.Label(self.ventana_registro, text="Registro de Usuario").pack(pady=10)
        tk.Label(self.ventana_registro, text="Nombre:").pack(pady=5)
        self.entrada_nombre = tk.Entry(self.ventana_registro)
        self.entrada_nombre.pack(pady=5)
        tk.Label(self.ventana_registro, text="Contraseña:").pack(pady=5)
        self.entrada_contrasenia = tk.Entry(self.ventana_registro, show="*")
        self.entrada_contrasenia.pack(pady=5)

        tk.Label(self.ventana_registro, text="Selecciona Rol:").pack(pady=5)
        self.listbox_roles = Listbox(self.ventana_registro, height=2)
        self.listbox_roles.insert(1, "Administrador")
        self.listbox_roles.insert(2, "Cliente")
        self.listbox_roles.pack(pady=5)

        tk.Button(self.ventana_registro, text="Registrar", command=self.registrar_usuario).pack(pady=10)
        tk.Button(self.ventana_registro, text="Volver", command=self.volver_login).pack(pady=10)

    def registrar_usuario(self):
        nombre = self.entrada_nombre.get().strip()
        contrasenia = self.entrada_contrasenia.get().strip()
        rol_seleccionado = self.listbox_roles.curselection()

        if nombre and contrasenia and rol_seleccionado:
            rol = self.listbox_roles.get(rol_seleccionado[0])
            nuevo_usuario = Usuario(nombre, contrasenia, rol)
            self.usuarios.append(nuevo_usuario)
            self.guardar_usuarios()
            messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            self.volver_login()
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos.")

    def agregar_libro(self):
        ventana_agregar = Toplevel(self.master)
        ventana_agregar.title("Agregar Libro")
        ventana_agregar.geometry("300x150")

        tk.Label(ventana_agregar, text="Título del libro:").pack(pady=5)
        entrada_titulo = tk.Entry(ventana_agregar)
        entrada_titulo.pack(pady=5)

        tk.Label(ventana_agregar, text="Autor del libro:").pack(pady=5)
        entrada_autor = tk.Entry(ventana_agregar)
        entrada_autor.pack(pady=5)

        def confirmar_agregar():
            titulo = entrada_titulo.get().strip()
            autor = entrada_autor.get().strip()
            if titulo and autor:
                self.biblioteca.agregar_libro(titulo, autor)
                messagebox.showinfo("Éxito", "Libro agregado con éxito.")
                ventana_agregar.destroy()
            else:
                messagebox.showerror("Error", "Los campos no pueden estar vacíos.")

        tk.Button(ventana_agregar, text="Agregar", command=confirmar_agregar).pack(pady=10)
        tk.Button(ventana_agregar, text="Cancelar", command=ventana_agregar.destroy).pack(pady=5)

    def mostrar_libros_para_modificar(self):
        if not self.biblioteca.libros:
            messagebox.showinfo("Información", "No hay libros para modificar.")
            return

        ventana_libros = Toplevel(self.master)
        ventana_libros.title("Seleccionar Libro a Modificar")
        ventana_libros.geometry("300x400")

        listbox_libros = Listbox(ventana_libros)
        for libro in self.biblioteca.libros:
            listbox_libros.insert(tk.END, libro.titulo)
        listbox_libros.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(ventana_libros)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox_libros.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox_libros.yview)

        tk.Button(ventana_libros, text="Modificar", command=lambda: self.modificar_libro(listbox_libros.get(tk.ACTIVE), ventana_libros)).pack(pady=10)

    def modificar_libro(self, titulo_libro, ventana):
        if titulo_libro:
            for libro in self.biblioteca.libros:
                if libro.titulo.lower() == titulo_libro.lower():
                    nuevo_titulo = simpledialog.askstring("Nuevo Título", "Nuevo título:", initialvalue=libro.titulo)
                    nuevo_autor = simpledialog.askstring("Nuevo Autor", "Nuevo autor:", initialvalue=libro.autor)
                    
                    if nuevo_titulo and nuevo_autor:
                        libro.titulo = nuevo_titulo
                        libro.autor = nuevo_autor
                        self.biblioteca.guardar_libros()
                        messagebox.showinfo("Éxito", "Libro modificado con éxito.")
                    else:
                        messagebox.showerror("Error", "Todos los campos son requeridos.")
                    ventana.destroy()
                    return
        messagebox.showerror("Error", "No se encontró el libro.")

    def eliminar_libro(self):
        if not self.biblioteca.libros:
            messagebox.showinfo("Información", "No hay libros que puedas eliminar.")
            return

        titulo_libro = simpledialog.askstring("Eliminar Libro", "Ingrese el título del libro a eliminar:")
        if titulo_libro:
            if self.biblioteca.eliminar_libro(titulo_libro):
                messagebox.showinfo("Éxito", "Libro eliminado con éxito.")
            else:
                messagebox.showerror("Error", "No se encuentra ningún libro con ese título.")
        else:
            messagebox.showerror("Error", "Título no válido.")

    def mostrar_libros(self):
        if self.biblioteca.libros:
            libros_str = "\n".join(str(libro) for libro in self.biblioteca.libros)
            messagebox.showinfo("Libros Registrados", libros_str)
        else:
            messagebox.showinfo("Libros Registrados", "No hay libros registrados.")

# Crear y ejecutar la aplicación
root = tk.Tk()
app = BibliotecaApp(root)
root.mainloop()