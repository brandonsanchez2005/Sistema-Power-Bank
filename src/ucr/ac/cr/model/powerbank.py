class PowerBank:

    def __init__(self, id_powerbank, marca, capacidad, estado):
        self.id_powerbank = id_powerbank
        self.marca = marca
        self.capacidad = capacidad
        self.estado = estado

    def __str__(self):
        return f"{self.id_powerbank} - {self.marca}"
