import json
import os


class BaseRepository:

    def __init__(self, archivo):
        self.archivo = archivo

    def cargar_datos(self):

        if not os.path.exists(self.archivo):
            return []

        with open(self.archivo, "r", encoding="utf-8") as file:
            return json.load(file)

    def guardar_datos(self, datos):

        with open(self.archivo, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=4)