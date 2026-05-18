import tkinter as tk

from src.ucr.ac.cr.view.ventana_prestamo import VentanaPrestamo
from src.ucr.ac.cr.view.ventana_reportes import VentanaReportes
from src.ucr.ac.cr.view.ventana_admin import VentanaAdmin


class VentanaPrincipal:

    def __init__(self, root, controller, usuario):
        self.root = root
        self.controller = controller
        self.usuario = usuario

        self.construir_ventana()

    def construir_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Sistema Power Bank")
        self.root.geometry("400x500")

        tk.Label(
            self.root,
            text="Sistema de Préstamo de Power Banks",
            font=("Arial", 15)
        ).pack(pady=20)

        tk.Label(
            self.root,
            text=f"Usuario: {self.usuario['nombre']}"
        ).pack()

        tk.Label(
            self.root,
            text=f"Rol: {self.usuario.get('rol', 'Usuario')}"
        ).pack(pady=5)

        if self.usuario.get("rol") != "Admin":
            tk.Button(
                self.root,
                text="Préstamos y Devoluciones",
                width=30,
                command=self.abrir_prestamos
            ).pack(pady=10)

        tk.Button(
            self.root,
            text="Reportes",
            width=30,
            command=self.abrir_reportes
        ).pack(pady=10)

        if self.usuario.get("rol") == "Admin":
            tk.Button(
                self.root,
                text="Administración",
                width=30,
                command=self.abrir_admin
            ).pack(pady=10)

        tk.Button(
            self.root,
            text="Salir",
            width=30,
            command=self.root.destroy
        ).pack(pady=10)

    def abrir_prestamos(self):
        VentanaPrestamo(self.root, self.controller, self.usuario, self)

    def abrir_reportes(self):
        VentanaReportes(self.root, self.controller, self.usuario, self)

    def abrir_admin(self):
        VentanaAdmin(self.root, self.controller, self.usuario, self)