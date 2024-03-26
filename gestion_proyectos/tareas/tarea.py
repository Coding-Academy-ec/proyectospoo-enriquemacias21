class Tarea:
    def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin, estado, proyecto_asignado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_estado = estado
        self.proyecto_asignado = proyecto_asignado

    def __str__(self):
        return f"Nombre Tarea: {self.nombre}\nDescripción: {self.descripcion}\nFecha Inicio: {self.fecha_inicio}\nFecha Fin: {self.fecha_fin}\nEstado: {self.fecha_estado}\nProyecto Asignado: {self.proyecto_asignado}"