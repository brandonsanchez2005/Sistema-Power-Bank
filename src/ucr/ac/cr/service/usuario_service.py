from src.ucr.ac.cr.repository.usuario_repository import UsuarioRepository


class UsuarioService:

    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def registrar_usuario(self, usuario):
        self.usuario_repository.guardar_usuario(usuario)

    def listar_usuarios(self):
        return self.usuario_repository.obtener_usuarios()

    def buscar_usuario(self, id_usuario):
        usuarios = self.usuario_repository.obtener_usuarios()

        for usuario in usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario

        return None