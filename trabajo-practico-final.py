import tkinter as tk
from tkinter import messagebox

# Funcion brir nueva ventana de registro
def abrir_ventana_registro():

    def guardar_usuarios():
        nombre_usuario = entrada_crear_usuario.get()
        contrasenia_usuario = entrada_crear_contraseña.get()
        validar_contrasenia = entrada_validar_contrasenia.get()

        if contrasenia_usuario == validar_contrasenia:
            #Guardar datos en archivo de texto
            with open ("BDUsuarios.txt", "a") as archivo:
                archivo.write(f"Usuario_ {nombre_usuario}, Contraseña: {contrasenia_usuario}\n")
            # CERRAR REGISTRO Y VOLVER A LA VENTANA PRINCIPAL
            nueva_ventana_registro.destroy
        else:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")

    nueva_ventana_registro = tk.Toplevel(ventana)
    nueva_ventana_registro.title("Registrarse")
    nueva_ventana_registro.geometry("300x400")

    #Etiqueta
    etiqueta_nuevo_registro = tk.Label(nueva_ventana_registro, text= "Usuario:")
    etiqueta_nuevo_registro.place(x = 100, y = 110)

    etiquta_contrasenia_registro = tk.Label(nueva_ventana_registro, text= "Contraseña:")
    etiquta_contrasenia_registro.place (x= 100, y = 150)   

    etiquta_contrasenia_validacion_registro = tk.Label(nueva_ventana_registro, text= "Verificar contraseña:")
    etiquta_contrasenia_validacion_registro.place (x= 100, y = 190)   

    #Cerrar ventana con boton
    cerrar_ventana_registro = tk.Button(nueva_ventana_registro,text= "Volver", command=nueva_ventana_registro.destroy())
    cerrar_ventana_registro.place(x = 10, y = 350)

    ingresar_desde_registro = tk.Button(nueva_ventana_registro,text= "Registrarse", command=guardar_usuarios.destroy)
    ingresar_desde_registro.place(x = 220, y = 350)  # ?????????????????????

    # Entrada de datos para nombre de ususario
    entrada_crear_usuario = tk.Entry(nueva_ventana_registro)
    entrada_crear_usuario.place(x = 100, y = 130)

    # Entrada de datos para contraseña de ususario
    entrada_crear_contraseña = tk.Entry(nueva_ventana_registro, show = "*") #Show oculta el texto
    entrada_crear_contraseña.place(x = 100, y = 170)
    
    # Entrada de datos para contraseña de ususario
    entrada_validar_contrasenia = tk.Entry(nueva_ventana_registro, show = "*") #Show oculta el texto
    entrada_validar_contrasenia.place(x = 100, y = 210)


# Ventana principal
ventana = tk.Tk()
ventana.title("Biblioteca")

#Tamaño
ventana.geometry("700x600")

#Etiqueta
etiqueta = tk.Label(ventana, text= "Bienvenido a la biblioteca")
etiqueta.place(x = 10, y = 10)

#Etiqueta para Usuario y Contraseña
etiqueta_usuario = tk.Label(ventana, text= "Usuario:")
etiqueta_usuario.place(x = 250, y = 130)

etiqueta_contraseña = tk.Label(ventana, text = "Contraseña:")
etiqueta_contraseña.place(x = 230, y = 160)

# Botones registro y login
boton_registro = tk.Button(ventana, text= "Registrarse", command = abrir_ventana_registro) #llamamos a la funcion
boton_registro.place(x = 350, y = 200)


boton_login = tk.Button(ventana, text= "Login")
boton_login.place(x = 300, y = 200)

# Entrada de datos para nombre de ususario
entrada_usuario = tk.Entry(ventana)
entrada_usuario.place(x = 300, y = 130)

# Entrada de datos para contraseña de ususario
entrada_contraseña = tk.Entry(ventana, show = "*") #Show oculta el texto
entrada_contraseña.place(x = 300, y = 160)

#ejecutar
ventana.mainloop()
