class Prestamo:

    def __init__(self, id_prestamo, usuario, powerbank,
                 fecha_prestamo, fecha_devolucion,
                 horas_limite, multa=0, estado="Activo"):

        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.powerbank = powerbank
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.horas_limite = horas_limite
        self.multa = multa
        self.estado = estado

    def __str__(self):
        return f"Prestamo {self.id_prestamo}"