import os

from src.ucr.ac.cr.repository.base_repository import BaseRepository


class UsuarioRepository(BaseRepository):

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
            "usuarios.json"
        )

        super().__init__(archivo)

    def guardar_usuario(self, usuario):

        usuarios = self.leer_datos()

        nuevo_usuario = {
            "id_usuario": usuario.id_usuario,
            "nombre": usuario.nombre,
            "correo": usuario.correo,
            "telefono": usuario.telefono,
            "password": usuario.password
        }

        usuarios.append(nuevo_usuario)

        self.guardar_datos(usuarios)

    def obtener_usuarios(self):

        return self.leer_datos()

    def eliminar_usuario(self, id_usuario):
        usuarios = self.leer_datos()

        nuevos_usuarios = []

        for usuario in usuarios:
            if usuario["id_usuario"] != id_usuario:
                nuevos_usuarios.append(usuario)

        self.guardar_datos(nuevos_usuarios)
