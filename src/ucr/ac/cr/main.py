import tkinter as tk

from src.ucr.ac.cr.controller.sistema_controller import SistemaController
from src.ucr.ac.cr.view.ventana_login import VentanaLogin


def main():
    root = tk.Tk()

    controller = SistemaController()
    VentanaLogin(root, controller)

    root.mainloop()


if __name__ == "__main__":
    main()

