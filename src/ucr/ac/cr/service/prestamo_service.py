from datetime import datetime

from src.ucr.ac.cr.model.prestamo import Prestamo
from src.ucr.ac.cr.repository.prestamo_repository import PrestamoRepository
from src.ucr.ac.cr.service.usuario_service import UsuarioService
from src.ucr.ac.cr.service.powerbank_service import PowerBankService


class PrestamoService:

    def __init__(self):

        self.prestamo_repository = PrestamoRepository()
        self.usuario_service = UsuarioService()
        self.powerbank_service = PowerBankService()

    def realizar_prestamo(self, id_prestamo, id_usuario, id_powerbank):

        usuario = self.usuario_service.buscar_usuario(id_usuario)

        if usuario is None:
            return "Usuario no encontrado"

        powerbank = self.powerbank_service.buscar_powerbank(id_powerbank)

        if powerbank is None:
            return "Power Bank no encontrado"

        if not powerbank.disponible:
            return "Power Bank no disponible"

        fecha_prestamo = datetime.now()

        prestamo = Prestamo(
            id_prestamo,
            usuario,
            powerbank,
            fecha_prestamo,
            None,
            0
        )

        powerbank.disponible = False

        self.prestamo_repository.guardar_prestamo(prestamo)

        return "Préstamo realizado correctamente"

    def realizar_devolucion(self, id_prestamo):

        prestamos = self.prestamo_repository.obtener_prestamos()

        for prestamo in prestamos:

            if prestamo.id_prestamo == id_prestamo:

                fecha_devolucion = datetime.now()

                prestamo.fecha_devolucion = fecha_devolucion

                horas = (
                    fecha_devolucion - prestamo.fecha_prestamo
                ).total_seconds() / 3600

                multa = 0

                if horas > 2:
                    horas_extra = int(horas - 2)
                    multa = horas_extra * 500

                prestamo.multa = multa

                prestamo.powerbank.disponible = True

                self.prestamo_repository.actualizar_prestamos(prestamos)

                return multa

        return None