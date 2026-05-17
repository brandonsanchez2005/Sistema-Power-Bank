from src.ucr.ac.cr.repository.base_repository import BaseRepository


class UsuarioRepository(BaseRepository):

    def __init__(self):
        super().__init__(
            "src/ucr/ac/cr/data/usuarios.json"
        )