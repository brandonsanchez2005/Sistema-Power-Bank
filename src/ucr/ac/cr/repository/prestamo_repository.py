import os

from repository.base_repository import BaseRepository


class PrestamoRepository(BaseRepository):

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
            "prestamos.json"
        )

        super().__init__(archivo)

    def guardar_prestamo(self, prestamo):
        prestamos = self.leer_datos()

        nuevo_prestamo = {
            "id_prestamo": prestamo.id_prestamo,
            "usuario": prestamo.usuario,
            "powerbank": prestamo.powerbank,
            "fecha_prestamo": prestamo.fecha_prestamo,
            "fecha_devolucion": prestamo.fecha_devolucion,
            "horas_limite": prestamo.horas_limite,
            "multa": prestamo.multa,
            "estado": prestamo.estado
        }

        prestamos.append(nuevo_prestamo)

        self.guardar_datos(prestamos)

    def obtener_prestamos(self):
        return self.leer_datos()

    def actualizar_prestamos(self, prestamos):
        self.guardar_datos(prestamos)
