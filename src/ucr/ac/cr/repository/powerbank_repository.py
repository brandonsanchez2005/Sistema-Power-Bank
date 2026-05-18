import os

from src.ucr.ac.cr.repository.base_repository import BaseRepository


class PowerBankRepository(BaseRepository):

    def __init__(self):
        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            os.path.dirname(__file__)
                        )
                    )
                )
            )
        )

        archivo = os.path.join(
            base_dir,
            "data",
            "powerbanks.json"
        )

        super().__init__(archivo)

    def guardar_powerbank(self, powerbank):
        powerbanks = self.leer_datos()

        nueva_powerbank = {
            "id_powerbank": powerbank.id_powerbank,
            "marca": powerbank.marca,
            "capacidad": powerbank.capacidad,
            "estado": powerbank.estado
        }

        powerbanks.append(nueva_powerbank)

        self.guardar_datos(powerbanks)

    def obtener_powerbanks(self):
        return self.leer_datos()

    def eliminar_powerbank(self, id_powerbank):
        powerbanks = self.leer_datos()

        nuevos_powerbanks = []

        for powerbank in powerbanks:
            if powerbank["id_powerbank"] != id_powerbank:
                nuevos_powerbanks.append(powerbank)

        self.guardar_datos(nuevos_powerbanks)
