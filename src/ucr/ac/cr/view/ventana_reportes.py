import tkinter as tk


class VentanaReportes:

    def __init__(self, root, controller, ventana_anterior):
        self.root = root
        self.controller = controller
        self.ventana_anterior = ventana_anterior

        self.construir_ventana()

    def construir_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Reportes")
        self.root.geometry("600x500")

        tk.Label(
            self.root,
            text="Reportes del Sistema",
            font=("Arial", 16)
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="Mostrar Usuarios",
            width=30,
            command=self.mostrar_usuarios
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
            width=70,
            height=18
        )

        self.texto.pack(pady=15)

    def mostrar_usuarios(self):
        self.texto.delete("1.0", tk.END)

        usuarios = self.controller.listar_usuarios()

        for usuario in usuarios:
            self.texto.insert(tk.END, f"ID: {usuario['id_usuario']}\n")
            self.texto.insert(tk.END, f"Nombre: {usuario['nombre']}\n")
            self.texto.insert(tk.END, f"Correo: {usuario['correo']}\n")
            self.texto.insert(tk.END, f"Teléfono: {usuario['telefono']}\n\n")

    def mostrar_powerbanks(self):
        self.texto.delete("1.0", tk.END)

        powerbanks = self.controller.listar_powerbanks()

        for powerbank in powerbanks:
            self.texto.insert(tk.END, f"ID: {powerbank['id_powerbank']}\n")
            self.texto.insert(tk.END, f"Marca: {powerbank['marca']}\n")
            self.texto.insert(tk.END, f"Capacidad: {powerbank['capacidad']}\n")
            self.texto.insert(tk.END, f"Estado: {powerbank['estado']}\n\n")

    def volver(self):
        self.ventana_anterior.construir_ventana()
