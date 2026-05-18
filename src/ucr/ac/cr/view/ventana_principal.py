import tkinter as tk

from view.ventana_powerbank import VentanaPowerBank
from view.ventana_prestamo import VentanaPrestamo
from view.ventana_reportes import VentanaReportes


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
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Préstamos y Devoluciones",
            width=30,
            command=self.abrir_prestamos
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Registrar Power Bank",
            width=30,
            command=self.abrir_powerbanks
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Reportes",
            width=30,
            command=self.abrir_reportes
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Salir",
            width=30,
            command=self.root.destroy
        ).pack(pady=10)

    def abrir_prestamos(self):
        VentanaPrestamo(self.root, self.controller, self.usuario, self)

    def abrir_powerbanks(self):
        VentanaPowerBank(self.root, self.controller, self)

    def abrir_reportes(self):
        VentanaReportes(self.root, self.controller, self)
