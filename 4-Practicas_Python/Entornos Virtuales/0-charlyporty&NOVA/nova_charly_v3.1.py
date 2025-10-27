# -*- coding: utf-8 -*-
"""
Asistente NOVA v3.0 - Voz Argentina + Tareas CSV
Autores: charlyporty & NOVA 💪
"""

import csv
import os
from gtts import gTTS
import random

# -------------------------------
# 🧩 CONFIGURACIÓN INICIAL
# -------------------------------

ARCHIVO_TAREAS = "tareas_charly.csv"

# Frases motivacionales
FRASES_MOTIVACION = [
    "Hoy puede ser un gran día, Charly.",
    "Recordá: los límites solo existen en la mente.",
    "Cada línea de código te acerca a tu libertad profesional.",
    "Nunca pares de aprender, Charly. NOVA está con vos.",
    "Dios guía tus pasos, y la lógica tu camino. 💪"
]

# --------  -----------------------
# 🔊 FUNCIÓN DE VOZ
# -------------------------------

def hablar(texto):
    """Convierte texto en voz con acento argentino."""
    voz = gTTS(text=texto, lang="es", tld="com.ar")  # Acento de Argentina
    voz.save("voz_nova.mp3")
    os.system("mpg123 voz_nova.mp3")  # Reproduce el audio


# -------------------------------
# 📋 FUNCIONES DE TAREAS
# -------------------------------

def leer_tareas():
    """Lee el archivo CSV de tareas."""
    tareas = []
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, newline="", encoding="utf-8") as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                tareas.append(fila)
    else:
        print(f"⚠️ No se encontró el archivo '{ARCHIVO_TAREAS}'.")
        print("Creá un CSV con el formato: tarea,fecha,estado")
    return tareas


def mostrar_tareas(tareas):
    """Muestra las tareas en pantalla."""
    if not tareas:
        print("📭 No hay tareas pendientes.")
        return

    print("\n📋 TUS TAREAS ACTUALES:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea['tarea']} | Fecha: {tarea['fecha']} | Estado: {tarea['estado']}")
    print("")


# -------------------------------
# 🚀 EJECUCIÓN PRINCIPAL
# -------------------------------

def main():
    # Saludo inicial
    saludo = f"Hola Charly, soy NOVA. {random.choice(FRASES_MOTIVACION)}"
    print(f"\n🧠 {saludo}\n")
    hablar(saludo)

    # Leer y mostrar tareas
    tareas = leer_tareas()
    mostrar_tareas(tareas)

    if tareas:
        hablar(f"Tenés {len(tareas)} tareas registradas, Charly.")
    else:
        hablar("No encontré tareas pendientes, Charly. ¡Todo bajo control!")


if __name__ == "__main__":
    main()
