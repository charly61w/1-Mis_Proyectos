import csv
from datetime import datetime

# Nombre del archivo CSV
ARCHIVO = "nova_tareas.csv"

# Crear archivo CSV con encabezados (solo la primera vez)
def crear_archivo():
    with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["ID", "Fecha", "Tarea", "Estado", "Prioridad", "Notas"])
    print("✅ Archivo CSV creado correctamente.")

# Agregar una nueva tarea
def agregar_tarea(tarea, prioridad="Media", notas=""):
    fecha = datetime.now().strftime("%Y-%m-%d")
    with open(ARCHIVO, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        # Contar tareas existentes para asignar ID
        with open(ARCHIVO, "r", encoding="utf-8") as f_lectura:
            lineas = list(csv.reader(f_lectura))
            nuevo_id = len(lineas)
        escritor.writerow([nuevo_id, fecha, tarea, "Pendiente", prioridad, notas])
    print(f"🆕 Tarea agregada: {tarea}")

# Mostrar todas las tareas
def mostrar_tareas():
    with open(ARCHIVO, mode="r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            print(f"{fila['ID']}. {fila['Tarea']} ({fila['Estado']}) - Prioridad: {fila['Prioridad']}")

# Actualizar estado de tarea (por ID)
def actualizar_estado(id_tarea, nuevo_estado):
    filas = []
    with open(ARCHIVO, mode="r", encoding="utf-8") as f:
        lector = csv.reader(f)
        encabezado = next(lector)
        for fila in lector:
            if fila[0] == str(id_tarea):
                fila[3] = nuevo_estado
            filas.append(fila)
    with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(encabezado)
        escritor.writerows(filas)
    print(f"🔁 Estado actualizado para tarea {id_tarea}: {nuevo_estado}")

# Ejemplo de uso
if __name__ == "__main__":
    crear_archivo()
    agregar_tarea("Configurar entorno NOVA v3.0", "Alta", "Preparar entorno en Cursor")
    agregar_tarea("Crear base de datos inicial", "Media", "MySQL/MariaDB")
    mostrar_tareas()
    actualizar_estado(1, "Completada")
    mostrar_tareas()

