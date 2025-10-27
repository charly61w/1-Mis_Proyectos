import csv
import os
from gtts import gTTS
import random

# === CONFIGURACIÓN INICIAL ===
ARCHIVO_TAREAS = "tareas_charly.txt"

# Frases motivacionales
FRASES_MOTIVACION = [
    "Hoy puede ser un gran día, Charly.",
    "Recordá: los límites solo existen en la mente.",
    "Cada línea de código te acerca a tu libertad profesional.",
    "Nunca pares de aprender, Charly. NOVA está con vos.",
    "Dios guía tus pasos, y la lógica tu camino. 💪"
]

# === FUNCIONES DE VOZ ===
def hablar(texto):
    """Convierte texto en voz con acento argentino."""
    voz = gTTS(text=texto, lang="es", tld="com.ar")  # Acento de Argentina
    voz.save("voz_nova.mp3")
    os.system("mpg123 voz_nova.mp3")  # Reproduce el audio
    
# === FUNCIONES PRINCIPALES ===
def saludar():
    hora = datetime.datetime.now().hour
    if hora < 12:
        return "Buen día, Charly ☀️"
    elif hora < 19:
        return "Buenas tardes, Charly 🌤️"
    else:
        return "Buenas noches, Charly 🌙"

def motivar():
    frases = [
        "Recordá, Charly: los grandes proyectos empiezan con pequeños pasos.",
        "Tu código puede cambiar tu futuro, línea por línea.",
        "Nunca subestimes lo que podés lograr con constancia y fe.",
        "Hoy puede ser el día en que algo grande empiece a tomar forma.",
        "No te detengas, Charly. El esfuerzo siempre encuentra su recompensa."
    ]
    return random.choice(frases)

# === TAREAS ===
def crear_archivo_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "w") as f:
            f.write("- Crear mi primera tarea\n")

def leer_tareas():
    crear_archivo_tareas()
    with open(ARCHIVO_TAREAS, "r") as f:
        tareas = [line.strip() for line in f.readlines() if line.strip()]
    return tareas

def mostrar_tareas():
    tareas = leer_tareas()
    if not tareas:
        hablar("No tenés tareas pendientes, Charly. ¡Todo al día!")
    else:
        hablar(f"Tenés {len(tareas)} tareas pendientes:")
        for i, t in enumerate(tareas, 1):
            print(f"{i}. {t}")

def agregar_tarea():
    nueva = input("✏️ Escribí la nueva tarea: ").strip()
    if nueva:
        with open(ARCHIVO_TAREAS, "a") as f:
            f.write(f"- {nueva}\n")
        hablar(f"Tarea agregada: {nueva}")
    else:
        hablar("No se agregó ninguna tarea.")

# === MENÚ ===
def mostrar_menu():
    print("\n--- Asistente NOVA v3.0 🚀 ---")
    print("1. Mostrar saludo")
    print("2. Mostrar hora actual")
    print("3. Ver tareas pendientes")
    print("4. Agregar nueva tarea")
    print("5. Buscar en Google")
    print("6. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        hablar(saludar())
    elif opcion == "2":
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        hablar(f"La hora actual es {hora_actual}")
    elif opcion == "3":
        mostrar_tareas()
    elif opcion == "4":
        agregar_tarea()
    elif opcion == "5":
        consulta = input("🔍 ¿Qué querés buscar en Google?: ")
        hablar(f"Buscando {consulta} en Google.")
        webbrowser.open(f"https://www.google.com/search?q={consulta}")
    elif opcion == "6":
        hablar("Hasta luego, Charly. NOVA desconectándose 💫")
        exit()
    else:
        hablar("Opción no válida. Intentá de nuevo.")

# === PRINCIPAL ===
def main():
    hablar("Hola Charly, soy NOVA, tu asistente digital.")
    hablar(motivar())
    mostrar_tareas()

    while True:
        mostrar_menu()
        opcion = input("\nElegí una opción: ")
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()

