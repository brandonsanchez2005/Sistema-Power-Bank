import tkinter as tk
from tkinter import messagebox

from src.ucr.ac.cr.model.powerbank import PowerBank


class VentanaPowerBank:

    def __init__(self, root, controller, ventana_anterior):
        self.root = root
        self.controller = controller
        self.ventana_anterior = ventana_anterior

        self.construir_ventana()

    def construir_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Power Banks")
        self.root.geometry("400x420")

        tk.Label(
            self.root,
            text="Gestión de Power Banks",
            font=("Arial", 16)
        ).pack(pady=15)

        tk.Label(self.root, text="ID").pack()
        self.entry_id = tk.Entry(self.root)
        self.entry_id.pack()

        tk.Label(self.root, text="Marca").pack()
        self.entry_marca = tk.Entry(self.root)
        self.entry_marca.pack()

        tk.Label(self.root, text="Capacidad").pack()
        self.entry_capacidad = tk.Entry(self.root)
        self.entry_capacidad.pack()

        tk.Label(
            self.root,
            text="Estado inicial: Disponible"
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Registrar Power Bank",
            width=25,
            command=self.registrar_powerbank
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Eliminar Power Bank",
            width=25,
            command=self.eliminar_powerbank
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Volver",
            width=25,
            command=self.volver
        ).pack(pady=10)

    def registrar_powerbank(self):
        powerbank = PowerBank(
            self.entry_id.get(),
            self.entry_marca.get(),
            self.entry_capacidad.get(),
            "Disponible"
        )

        respuesta = self.controller.registrar_powerbank(powerbank)

        if "correctamente" in respuesta:
            messagebox.showinfo("Éxito", respuesta)
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", respuesta)

    def eliminar_powerbank(self):
        respuesta = self.controller.eliminar_powerbank(
            self.entry_id.get()
        )

        if "correctamente" in respuesta:
            messagebox.showinfo("Éxito", respuesta)
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", respuesta)

    def limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_capacidad.delete(0, tk.END)

    def volver(self):
        self.ventana_anterior.construir_ventana()
