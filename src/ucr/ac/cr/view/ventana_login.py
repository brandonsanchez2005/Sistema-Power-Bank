import tkinter as tk
from tkinter import messagebox

from view.ventana_principal import VentanaPrincipal
from view.ventana_usuario import VentanaUsuario


class VentanaLogin:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("Login")
        self.root.geometry("350x300")

        self.construir_ventana()

    def construir_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(
            self.root,
            text="Sistema Power Bank",
            font=("Arial", 16)
        ).pack(pady=20)

        tk.Label(self.root, text="Correo").pack()

        self.entry_correo = tk.Entry(self.root)
        self.entry_correo.pack()

        tk.Label(self.root, text="Password").pack()

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        boton_login = tk.Button(
            self.root,
            text="Iniciar sesión",
            width=25,
            command=self.iniciar_sesion
        )

        boton_login.pack(pady=15)

        boton_registro = tk.Button(
            self.root,
            text="Registrar usuario",
            width=25,
            command=self.abrir_registro
        )

        boton_registro.pack()

    def iniciar_sesion(self):
        correo = self.entry_correo.get()
        password = self.entry_password.get()

        usuario = self.controller.validar_login(correo, password)

        if usuario is None:
            messagebox.showerror(
                "Error",
                "Correo o contraseña incorrectos"
            )
            return

        messagebox.showinfo(
            "Bienvenido",
            f"Hola {usuario['nombre']}"
        )

        VentanaPrincipal(self.root, self.controller, usuario)

    def abrir_registro(self):
        VentanaUsuario(self.root, self.controller, self)
