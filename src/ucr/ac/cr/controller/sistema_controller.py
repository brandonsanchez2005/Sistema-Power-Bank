from src.ucr.ac.cr.service.usuario_service import UsuarioService
from src.ucr.ac.cr.service.powerbank_service import PowerBankService
from src.ucr.ac.cr.service.prestamo_service import PrestamoService


class SistemaController:

    def __init__(self):
        self.usuario_service = UsuarioService()
        self.powerbank_service = PowerBankService()
        self.prestamo_service = PrestamoService()

    def registrar_usuario(self, usuario):
        return self.usuario_service.registrar_usuario(usuario)

    def listar_usuarios(self):
        return self.usuario_service.listar_usuarios()

    def validar_login(self, correo, password):
        return self.usuario_service.validar_login(correo, password)

    def eliminar_usuario(self, id_usuario):
        return self.usuario_service.eliminar_usuario(id_usuario)

    def registrar_powerbank(self, powerbank):
        return self.powerbank_service.registrar_powerbank(powerbank)

    def listar_powerbanks(self):
        return self.powerbank_service.listar_powerbanks()

    def obtener_powerbanks_disponibles(self):
        return self.powerbank_service.obtener_disponibles()

    def eliminar_powerbank(self, id_powerbank):
        return self.powerbank_service.eliminar_powerbank(id_powerbank)

    def realizar_prestamo(self, id_prestamo, id_usuario, id_powerbank):
        return self.prestamo_service.realizar_prestamo(
            id_prestamo,
            id_usuario,
            id_powerbank
        )

    def realizar_devolucion(self, id_prestamo):
        return self.prestamo_service.realizar_devolucion(id_prestamo)

    def listar_prestamos(self):
        return self.prestamo_service.listar_prestamos()