from src.ucr.ac.cr.repository.usuario_repository import UsuarioRepository


class UsuarioService:

    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def registrar_usuario(self, usuario):
        usuarios = self.usuario_repository.obtener_usuarios()

        for usuario_existente in usuarios:
            if usuario_existente["id_usuario"] == usuario.id_usuario:
                return "Ya existe un usuario con ese ID"

            if usuario_existente["correo"] == usuario.correo:
                return "Ya existe un usuario con ese correo"

        self.usuario_repository.guardar_usuario(usuario)
        return "Usuario registrado correctamente"

    def listar_usuarios(self):
        return self.usuario_repository.obtener_usuarios()

    def buscar_usuario(self, id_usuario):
        usuarios = self.usuario_repository.obtener_usuarios()

        for usuario in usuarios:
            if usuario["id_usuario"] == id_usuario:
                return usuario

        return None

    def validar_login(self, correo, password):
        usuarios = self.usuario_repository.obtener_usuarios()

        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                if "rol" not in usuario:
                    usuario["rol"] = "Usuario"

                return usuario

        return None

    def eliminar_usuario(self, id_usuario):
        usuario = self.buscar_usuario(id_usuario)

        if usuario is None:
            return "Usuario no encontrado"

        if usuario.get("rol") == "Admin":
            return "No se puede eliminar un administrador"

        self.usuario_repository.eliminar_usuario(id_usuario)
        return "Usuario eliminado correctamente"