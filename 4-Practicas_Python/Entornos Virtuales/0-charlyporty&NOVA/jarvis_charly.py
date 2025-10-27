import os
import datetime
import webbrowser

def saludar():
    hora = datetime.datetime.now().hour
    if hora < 12:
        return "Buen día, Charly ☀️"
    elif hora < 19:
        return "Buenas tardes, Charly 🌤️"
    else:
        return "Buenas noches, Charly 🌙"

def mostrar_menu():
    print("\n--- Jarvis de CharlyPorty 💻 ---")
    print("1. Mostrar saludo")
    print("2. Mostrar hora actual")
    print("3. Abrir navegador Firefox")
    print("4. Abrir carpeta de proyectos")
    print("5. Buscar en Google")
    print("6. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        print(saludar())
    elif opcion == "2":
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"🕒 Hora actual: {hora_actual}")
    elif opcion == "3":
        print("🌐 Abriendo Firefox...")
        os.system("firefox &" if os.name != "nt" else "start firefox")
    elif opcion == "4":
        ruta = os.path.expanduser("~/Proyectos")
        print(f"📂 Abriendo carpeta: {ruta}")
        os.makedirs(ruta, exist_ok=True)
        os.system(f'xdg-open "{ruta}"' if os.name != "nt" else f'start {ruta}')
    elif opcion == "5":
        consulta = input("🔍 ¿Qué querés buscar en Google?: ")
        webbrowser.open(f"https://www.google.com/search?q={consulta}")
    elif opcion == "6":
        print("Hasta luego, Charly 💪 Jarvis apagándose...")
        exit()
    else:
        print("⚠️ Opción no válida. Probá de nuevo.")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElegí una opción: ")
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()

