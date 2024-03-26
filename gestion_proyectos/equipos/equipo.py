class Equipo:
    def __init__(self, nombre, lider, objetivo, fecha_creacion):
        self.nombre = nombre
        self.lider = lider
        self.objetivo=objetivo
        self.fecha_creacion = fecha_creacion

    def __str__(self):
        return f"Equipo: {self.nombre}\nLíder: {self.lider}\nObjetivo: {self.objetivo}\nFecha creación: {self.fecha_creacion}"