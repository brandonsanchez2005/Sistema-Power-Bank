import tkinter as tk


class VentanaReportePrestamos:

    def __init__(self, root, controller, ventana_anterior):
        self.root = root
        self.controller = controller
        self.ventana_anterior = ventana_anterior

        self.construir_ventana()

    def construir_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Reporte de Préstamos")
        self.root.geometry("700x550")

        tk.Label(
            self.root,
            text="Reporte de Préstamos",
            font=("Arial", 16)
        ).pack(pady=15)

        tk.Label(self.root, text="Filtrar por ID de préstamo").pack()

        self.entry_filtro = tk.Entry(self.root)
        self.entry_filtro.pack()

        tk.Button(
            self.root,
            text="Buscar",
            width=25,
            command=self.mostrar_prestamos
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Mostrar todos",
            width=25,
            command=self.mostrar_todos
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Volver",
            width=25,
            command=self.volver
        ).pack(pady=5)

        self.texto = tk.Text(self.root, width=85, height=22)
        self.texto.pack(pady=10)

    def mostrar_todos(self):
        self.entry_filtro.delete(0, tk.END)
        self.mostrar_prestamos()

    def mostrar_prestamos(self):
        self.texto.delete("1.0", tk.END)

        filtro = self.entry_filtro.get()
        prestamos = self.controller.listar_prestamos()

        for prestamo in prestamos:
            if filtro != "" and prestamo["id_prestamo"] != filtro:
                continue

            self.texto.insert(tk.END, f"ID Préstamo: {prestamo['id_prestamo']}\n")
            self.texto.insert(tk.END, f"Usuario: {prestamo['usuario']['nombre']}\n")
            self.texto.insert(tk.END, f"Power Bank: {prestamo['powerbank']['id_powerbank']}\n")
            self.texto.insert(tk.END, f"Fecha préstamo: {prestamo['fecha_prestamo']}\n")
            self.texto.insert(tk.END, f"Fecha devolución: {prestamo['fecha_devolucion']}\n")
            self.texto.insert(tk.END, f"Multa: ₡{prestamo['multa']}\n")
            self.texto.insert(tk.END, f"Estado: {prestamo['estado']}\n\n")

    def volver(self):
        self.ventana_anterior.construir_ventana()