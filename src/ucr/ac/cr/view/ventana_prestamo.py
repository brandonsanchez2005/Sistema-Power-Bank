import tkinter as tk
from tkinter import messagebox


class VentanaPrestamo:

    def __init__(self, root, controller, usuario, ventana_anterior):
        self.root = root
        self.controller = controller
        self.usuario = usuario
        self.ventana_anterior = ventana_anterior

        self.construir_ventana()

    def construir_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Préstamos")
        self.root.geometry("400x450")

        tk.Label(
            self.root,
            text="Realizar Préstamo",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Label(self.root, text="ID Préstamo").pack()
        self.entry_id_prestamo = tk.Entry(self.root)
        self.entry_id_prestamo.pack()

        tk.Label(self.root, text="ID Power Bank").pack()
        self.entry_id_powerbank = tk.Entry(self.root)
        self.entry_id_powerbank.pack()

        tk.Button(
            self.root,
            text="Realizar Préstamo",
            width=25,
            command=self.realizar_prestamo
        ).pack(pady=15)

        tk.Label(
            self.root,
            text="Realizar Devolución",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Label(self.root, text="ID Préstamo").pack()
        self.entry_devolucion = tk.Entry(self.root)
        self.entry_devolucion.pack()

        tk.Button(
            self.root,
            text="Realizar Devolución",
            width=25,
            command=self.realizar_devolucion
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="Volver",
            width=25,
            command=self.volver
        ).pack()

    def realizar_prestamo(self):
        respuesta = self.controller.realizar_prestamo(
            self.entry_id_prestamo.get(),
            self.usuario["id_usuario"],
            self.entry_id_powerbank.get()
        )

        if "correctamente" in respuesta:
            messagebox.showinfo("Resultado", respuesta)
        else:
            messagebox.showerror("Error", respuesta)

    def realizar_devolucion(self):
        respuesta = self.controller.realizar_devolucion(
            self.entry_devolucion.get()
        )

        if "correctamente" in respuesta:
            messagebox.showinfo("Devolución", respuesta)
        else:
            messagebox.showerror("Error", respuesta)

    def volver(self):
        self.ventana_anterior.construir_ventana()
