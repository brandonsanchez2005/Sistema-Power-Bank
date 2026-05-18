class Usuario:

    def __init__(self, id_usuario, nombre, correo, telefono,
                 password, multa_pendiente=0, rol="Usuario"):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.password = password
        self.multa_pendiente = multa_pendiente
        self.rol = rol

    def __str__(self):
        return f"{self.id_usuario} - {self.nombre}"