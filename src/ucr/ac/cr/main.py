from src.ucr.ac.cr.repository.usuario_repository import UsuarioRepository

repo = UsuarioRepository()

datos = repo.cargar_datos()

print(datos)