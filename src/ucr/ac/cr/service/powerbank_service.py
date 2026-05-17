from src.ucr.ac.cr.repository.powerbank_repository import PowerBankRepository


class PowerBankService:

    def __init__(self):
        self.powerbank_repository = PowerBankRepository()

    def registrar_powerbank(self, powerbank):
        self.powerbank_repository.guardar_powerbank(powerbank)

    def listar_powerbanks(self):
        return self.powerbank_repository.obtener_powerbanks()

    def buscar_powerbank(self, id_powerbank):

        powerbanks = self.powerbank_repository.obtener_powerbanks()

        for powerbank in powerbanks:
            if powerbank.id_powerbank == id_powerbank:
                return powerbank

        return None

    def obtener_disponibles(self):

        disponibles = []

        for powerbank in self.listar_powerbanks():

            if powerbank.disponible:
                disponibles.append(powerbank)

        return disponibles