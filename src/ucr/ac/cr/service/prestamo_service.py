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
        prestamos = self.prestamo_repository.obtener_prestamos()

        for prestamo_existente in prestamos:
            if prestamo_existente["id_prestamo"] == id_prestamo:
                return "Ya existe un préstamo con ese ID"

        usuario = self.usuario_service.buscar_usuario(id_usuario)

        if usuario is None:
            return "Usuario no encontrado"

        powerbank = self.powerbank_service.buscar_powerbank(id_powerbank)

        if powerbank is None:
            return "Power Bank no encontrado"

        if powerbank["estado"] != "Disponible":
            return "Power Bank no disponible"

        for prestamo in prestamos:
            if (
                prestamo["usuario"]["id_usuario"] == id_usuario
                and prestamo["estado"] == "Activo"
            ):
                return "El usuario ya tiene un préstamo activo"

        fecha_prestamo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        prestamo = Prestamo(
            id_prestamo,
            usuario,
            powerbank,
            fecha_prestamo,
            None,
            2,
            0,
            "Activo"
        )

        self.prestamo_repository.guardar_prestamo(prestamo)
        self.cambiar_estado_powerbank(id_powerbank, "Prestado")

        return "Préstamo realizado correctamente"

    def realizar_devolucion(self, id_prestamo):
        prestamos = self.prestamo_repository.obtener_prestamos()

        for prestamo in prestamos:
            if prestamo["id_prestamo"] == id_prestamo:

                if prestamo["estado"] == "Devuelto":
                    return "El préstamo ya fue devuelto"

                fecha_devolucion = datetime.now()

                fecha_prestamo = datetime.strptime(
                    prestamo["fecha_prestamo"],
                    "%Y-%m-%d %H:%M:%S"
                )

                horas = (
                    fecha_devolucion - fecha_prestamo
                ).total_seconds() / 3600

                multa = 0

                if horas > prestamo["horas_limite"]:
                    horas_extra = int(horas - prestamo["horas_limite"])
                    multa = horas_extra * 500

                prestamo["fecha_devolucion"] = fecha_devolucion.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                prestamo["multa"] = multa
                prestamo["estado"] = "Devuelto"

                id_powerbank = prestamo["powerbank"]["id_powerbank"]

                self.cambiar_estado_powerbank(id_powerbank, "Disponible")
                self.prestamo_repository.actualizar_prestamos(prestamos)

                return f"Devolución realizada correctamente. Multa: ₡{multa}"

        return "Préstamo no encontrado"

    def cambiar_estado_powerbank(self, id_powerbank, nuevo_estado):
        powerbanks = self.powerbank_service.listar_powerbanks()

        for powerbank in powerbanks:
            if powerbank["id_powerbank"] == id_powerbank:
                powerbank["estado"] = nuevo_estado

        self.powerbank_service.powerbank_repository.guardar_datos(powerbanks)
