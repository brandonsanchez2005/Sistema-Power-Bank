import tkinter as tk
from tkinter import messagebox

from src.ucr.ac.cr.model.usuario import Usuario


class VentanaUsuario:

    def __init__(self, root, controller, ventana_anterior=None):
        self.root = root
        self.controller = controller
        self.ventana_anterior = ventana_anterior

        self.construir_ventana()

    def construir_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Usuarios")
        self.root.geometry("400x500")

        tk.Label(
            self.root,
            text="Gestión de Usuarios",
            font=("Arial", 16)
        ).pack(pady=15)

        tk.Label(self.root, text="ID").pack()
        self.entry_id = tk.Entry(self.root)
        self.entry_id.pack()

        tk.Label(self.root, text="Nombre").pack()
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack()

        tk.Label(self.root, text="Correo").pack()
        self.entry_correo = tk.Entry(self.root)
        self.entry_correo.pack()

        tk.Label(self.root, text="Teléfono").pack()
        self.entry_telefono = tk.Entry(self.root)
        self.entry_telefono.pack()

        tk.Label(self.root, text="Password").pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        tk.Button(
            self.root,
            text="Registrar Usuario",
            width=25,
            command=self.registrar_usuario
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Eliminar Usuario",
            width=25,
            command=self.eliminar_usuario
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Volver",
            width=25,
            command=self.volver
        ).pack(pady=10)

    def registrar_usuario(self):
        usuario = Usuario(
            self.entry_id.get(),
            self.entry_nombre.get(),
            self.entry_correo.get(),
            self.entry_telefono.get(),
            self.entry_password.get()
        )

        respuesta = self.controller.registrar_usuario(usuario)

        if "correctamente" in respuesta:
            messagebox.showinfo("Éxito", respuesta)
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", respuesta)

    def eliminar_usuario(self):
        respuesta = self.controller.eliminar_usuario(
            self.entry_id.get()
        )

        if "correctamente" in respuesta:
            messagebox.showinfo("Éxito", respuesta)
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", respuesta)

    def limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def volver(self):
        if self.ventana_anterior is not None:
            self.ventana_anterior.construir_ventana()
