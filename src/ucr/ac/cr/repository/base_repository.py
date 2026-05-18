import json
import os


class BaseRepository:

    def __init__(self, archivo):

        self.archivo = archivo

        carpeta = os.path.dirname(self.archivo)

        if not os.path.exists(carpeta):

            os.makedirs(carpeta)

        if not os.path.exists(self.archivo):

            with open(self.archivo, "w") as file:

                json.dump([], file)

    def leer_datos(self):

        with open(self.archivo, "r") as file:

            return json.load(file)

    def guardar_datos(self, datos):

        with open(self.archivo, "w") as file:

            json.dump(datos, file, indent=4)