from src.ucr.ac.cr.repository.powerbank_repository import PowerBankRepository


class PowerBankService:

    def __init__(self):
        self.powerbank_repository = PowerBankRepository()

    def registrar_powerbank(self, powerbank):
        powerbanks = self.powerbank_repository.obtener_powerbanks()

        for powerbank_existente in powerbanks:
            if powerbank_existente["id_powerbank"] == powerbank.id_powerbank:
                return "Ya existe un Power Bank con ese ID"

        self.powerbank_repository.guardar_powerbank(powerbank)

        return "Power Bank registrado correctamente"

    def listar_powerbanks(self):
        return self.powerbank_repository.obtener_powerbanks()

    def buscar_powerbank(self, id_powerbank):
        powerbanks = self.powerbank_repository.obtener_powerbanks()

        for powerbank in powerbanks:
            if powerbank["id_powerbank"] == id_powerbank:
                return powerbank

        return None

    def obtener_disponibles(self):
        disponibles = []

        for powerbank in self.listar_powerbanks():
            if powerbank["estado"] == "Disponible":
                disponibles.append(powerbank)

        return disponibles

    def eliminar_powerbank(self, id_powerbank):
        powerbank = self.buscar_powerbank(id_powerbank)

        if powerbank is None:
            return "Power Bank no encontrado"

        if powerbank["estado"] != "Disponible":
            return "No se puede eliminar un Power Bank prestado"

        self.powerbank_repository.eliminar_powerbank(id_powerbank)

        return "Power Bank eliminado correctamente"

