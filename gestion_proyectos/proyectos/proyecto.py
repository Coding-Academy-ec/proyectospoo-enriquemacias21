class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, estado, equipo_asignado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado=estado
        self.equipo_asigando=equipo_asignado

    def __str__(self):
        return f"Proyecto: {self.nombre}\nDescripción: {self.descripcion}\nFecha de inicio: {self.fecha_inicio}\nFecha de fin: {self.fecha_fin}\nEstado: {self.estado}\nEquipo Asignado: {self.equipo_asigando}"