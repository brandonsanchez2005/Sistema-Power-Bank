import tkinter as tk

from src.ucr.ac.cr.view.ventana_powerbank import VentanaPowerBank
from src.ucr.ac.cr.view.ventana_usuario import VentanaUsuario
from src.ucr.ac.cr.view.ventana_reporte_prestamos import VentanaReportePrestamos


class VentanaAdmin:

    def __init__(self, root, controller, usuario, ventana_anterior):
        self.root = root
        self.controller = controller
        self.usuario = usuario
        self.ventana_anterior = ventana_anterior

        self.construir_ventana()

    def construir_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Administración")
        self.root.geometry("400x400")

        tk.Label(
            self.root,
            text="Panel de Administración",
            font=("Arial", 16)
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Registrar / Eliminar Power Banks",
            width=30,
            command=self.abrir_powerbanks
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Eliminar Usuarios",
            width=30,
            command=self.abrir_usuarios
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Reporte de Préstamos",
            width=30,
            command=self.abrir_reporte_prestamos
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Volver",
            width=30,
            command=self.volver
        ).pack(pady=10)

    def abrir_powerbanks(self):
        VentanaPowerBank(self.root, self.controller, self)

    def abrir_usuarios(self):
        VentanaUsuario(self.root, self.controller, self, True)

    def abrir_reporte_prestamos(self):
        VentanaReportePrestamos(self.root, self.controller, self)

    def volver(self):
        self.ventana_anterior.construir_ventana()