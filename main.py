import json

# Función para cargar los estudiantes desde un archivo JSON
def cargar_estudiantes():
    try:
        with open('estudiantes.json', 'r') as file:
            estudiantes = json.load(file)
    except FileNotFoundError:
        estudiantes = []  # Si el archivo no existe, devolver una lista vacía
    return estudiantes

# Función para guardar los estudiantes en un archivo JSON
def guardar_estudiantes(estudiantes):
    with open('estudiantes.json', 'w') as file:
        json.dump(estudiantes, file)

# Función para agregar un estudiante y sus calificaciones
def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    try:
        # Solicitar las calificaciones del estudiante
        calificaciones = list(map(float, input(f"Ingrese las calificaciones de {nombre}, separadas por espacios: ").split()))
        estudiantes.append({"nombre": nombre, "calificaciones": calificaciones})
        guardar_estudiantes(estudiantes)  # Guardar los cambios en el archivo
        print(f"Estudiante {nombre} agregado exitosamente.\n")
    except ValueError:
        print("Error: Las calificaciones deben ser números.\n")

# Función para mostrar la lista de estudiantes y sus promedios
def ver_estudiantes(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.\n")
    else:
        print("Lista de estudiantes y sus promedios:")
        for estudiante in estudiantes:
            promedio = sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])
            estado = "Aprobado" if promedio >= 6 else "Reprobado"
            print(f"{estudiante['nombre']} - Promedio: {promedio:.2f} - Estado: {estado}")
        print()

# Función para modificar la calificación de un estudiante
def modificar_calificacion(estudiantes):
    nombre = input("Ingrese el nombre del estudiante cuya calificación desea modificar: ")
    estudiante = next((est for est in estudiantes if est['nombre'] == nombre), None)
    if estudiante:
        try:
            # Mostrar las calificaciones actuales
            print(f"Calificaciones actuales de {nombre}: {estudiante['calificaciones']}")
            indice = int(input(f"Ingrese el número de la calificación que desea modificar (1-{len(estudiante['calificaciones'])}): ")) - 1
            if 0 <= indice < len(estudiante['calificaciones']):
                nueva_calificacion = float(input("Ingrese la nueva calificación: "))
                estudiante['calificaciones'][indice] = nueva_calificacion
                guardar_estudiantes(estudiantes)  # Guardar los cambios en el archivo
                print(f"Calificación modificada exitosamente. Las nuevas calificaciones son: {estudiante['calificaciones']}\n")
            else:
                print("Índice inválido. Intente nuevamente.\n")
        except (ValueError, IndexError):
            print("Error: Entrada no válida.\n")
    else:
        print(f"Estudiante {nombre} no encontrado.\n")

# Función principal para el menú interactivo
def menu():
    estudiantes = cargar_estudiantes()  # Cargar los estudiantes al inicio
    opciones = {
        1: "Agregar estudiante y notas",
        2: "Ver lista de estudiantes y promedios",
        3: "Modificar calificación",
        4: "Salir"
    }

    while True:
        # Mostrar el menú
        print("----- Menú -----")
        for key, value in opciones.items():
            print(f"{key}. {value}")
        
        try:
            seleccion = int(input("\nSeleccione una opción (1-4): "))
            if seleccion == 1:
                agregar_estudiante(estudiantes)
            elif seleccion == 2:
                ver_estudiantes(estudiantes)
            elif seleccion == 3:
                modificar_calificacion(estudiantes)
            elif seleccion == 4:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.\n")
        except ValueError:
            print("Por favor, ingrese un número válido entre 1 y 4.\n")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
