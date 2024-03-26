from gestion_proyectos.equipos.equipo import Equipo
from gestion_proyectos.proyectos.proyecto import Proyecto
from gestion_proyectos.tareas.tarea import Tarea

def main():
    # Crear equipos
    equipo1 = Equipo("ML 1", "JAvier Macías", "Algoritmo de predicción área agricola","2024-03-1")
    equipo2 = Equipo("ML 2", "Jaleida", "Algoritmo de predicción área educación","2022-12-20")
    
    # Crear proyectos
    proyecto1 = Proyecto("Investigación de Tipo de suelo", "Crear un algortimo que me prediga el tipo de suelo",
                          "2024-03-26", "2024-04-26","Desarrollo","ML 1")
    proyecto2 = Proyecto("Deteccón de Deserción", "Crear un algortimo que me permita predecir la deserción de estudiantes",
                          "2023-01-01", "2024-03-30","Terminado","ML 2")

    # crear tareas
    tarea1 = Tarea("SLR", "Busqueda y proceso de información " +
                   "Aplicar Pasfit y PRISMA", "2024-04-01","2024-04-10","Desarrollo","Investigación de Tipo de suelo" )
    
    tarea2 = Tarea("Realziar los resultados", "Hacer nubes de palabras", "2023-01-10","2023-02-10","Terminado","Deteccón de Deserción")

    # Mostrar detalles de las transacciones
    print("Proyectos del Equipo 1:")
    print(equipo1)
    print(proyecto1)
    print("Tarea:", tarea1)

    print("\nProyectos del Equipo 2:")
    print(equipo2)
    print(proyecto2)
    print("Tarea:", tarea2)

if __name__ == "__main__":
    main()