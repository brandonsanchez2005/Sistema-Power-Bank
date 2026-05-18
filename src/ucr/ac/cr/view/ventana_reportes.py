import tkinter as tk


class VentanaReportes:

    def __init__(self, root, controller, usuario, ventana_anterior):
        self.root = root
        self.controller = controller
        self.usuario = usuario
        self.ventana_anterior = ventana_anterior

        self.construir_ventana()

    def construir_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Reportes")
        self.root.geometry("650x520")

        tk.Label(
            self.root,
            text="Reportes",
            font=("Arial", 16)
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="Historial de préstamos",
            width=30,
            command=self.mostrar_historial_prestamos
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Mostrar Power Banks",
            width=30,
            command=self.mostrar_powerbanks
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Volver",
            width=30,
            command=self.volver
        ).pack(pady=5)

        self.texto = tk.Text(
            self.root,
            width=75,
            height=20
        )

        self.texto.pack(pady=15)

    def mostrar_historial_prestamos(self):
        self.texto.delete("1.0", tk.END)

        prestamos = self.controller.listar_prestamos()
        id_usuario = self.usuario["id_usuario"]
        encontro_prestamos = False

        for prestamo in prestamos:
            if prestamo["usuario"]["id_usuario"] == id_usuario:
                encontro_prestamos = True

                self.texto.insert(
                    tk.END,
                    f"ID Préstamo: {prestamo['id_prestamo']}\n"
                )

                self.texto.insert(
                    tk.END,
                    f"Power Bank: {prestamo['powerbank']['id_powerbank']}\n"
                )

                self.texto.insert(
                    tk.END,
                    f"Marca: {prestamo['powerbank']['marca']}\n"
                )

                self.texto.insert(
                    tk.END,
                    f"Fecha préstamo: {prestamo['fecha_prestamo']}\n"
                )

                self.texto.insert(
                    tk.END,
                    f"Fecha devolución: {prestamo['fecha_devolucion']}\n"
                )

                self.texto.insert(
                    tk.END,
                    f"Multa: ₡{prestamo['multa']}\n"
                )

                self.texto.insert(
                    tk.END,
                    f"Estado: {prestamo['estado']}\n\n"
                )

        if not encontro_prestamos:
            self.texto.insert(
                tk.END,
                "Este usuario no tiene préstamos registrados."
            )

    def mostrar_powerbanks(self):
        self.texto.delete("1.0", tk.END)

        powerbanks = self.controller.listar_powerbanks()

        for powerbank in powerbanks:
            self.texto.insert(
                tk.END,
                f"ID: {powerbank['id_powerbank']}\n"
            )

            self.texto.insert(
                tk.END,
                f"Marca: {powerbank['marca']}\n"
            )

            self.texto.insert(
                tk.END,
                f"Capacidad: {powerbank['capacidad']}\n"
            )

            self.texto.insert(
                tk.END,
                f"Estado: {powerbank['estado']}\n\n"
            )

    def volver(self):
        self.ventana_anterior.construir_ventana()