import os
import datetime
import webbrowser
import random
import pyttsx3

# Inicializar motor de voz
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # velocidad
engine.setProperty('volume', 1.0)

def hablar(texto):
    print(f"NOVA 🧠: {texto}")
    engine.say(texto)
    engine.runAndWait()

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

def mostrar_menu():
    print("\n--- Asistente NOVA v2.0 🚀 ---")
    print("1. Mostrar saludo")
    print("2. Mostrar hora actual")
    print("3. Abrir navegador Firefox")
    print("4. Abrir carpeta de proyectos")
    print("5. Buscar en Google")
    print("6. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        hablar(saludar())
    elif opcion == "2":
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        hablar(f"La hora actual es {hora_actual}")
    elif opcion == "3":
        hablar("Abriendo Firefox...")
        os.system("firefox &" if os.name != "nt" else "start firefox")
    elif opcion == "4":
        ruta = os.path.expanduser("~/Proyectos")
        hablar(f"Abriendo la carpeta de proyectos: {ruta}")
        os.makedirs(ruta, exist_ok=True)
        os.system(f'xdg-open "{ruta}"' if os.name != "nt" else f'start {ruta}')
    elif opcion == "5":
        consulta = input("🔍 ¿Qué querés buscar en Google?: ")
        hablar(f"Buscando {consulta} en Google.")
        webbrowser.open(f"https://www.google.com/search?q={consulta}")
    elif opcion == "6":
        hablar("Hasta luego, Charly. NOVA desconectándose 💫")
        exit()
    else:
        hablar("Opción no válida. Intentá de nuevo.")

def main():
    hablar(f"Hola Charly, soy NOVA, tu asistente digital.")
    hablar(motivar())
    while True:
        mostrar_menu()
        opcion = input("\nElegí una opción: ")
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()

