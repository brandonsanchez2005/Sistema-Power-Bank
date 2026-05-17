from src.ucr.ac.cr.repository.base_repository import BaseRepository


class PrestamoRepository(BaseRepository):

    def __init__(self):
        super().__init__(
            "src/ucr/ac/cr/data/prestamos.json"
        )