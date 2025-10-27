import os
import shutil

# --- CONFIGURACIÓN ---
nombre_carpeta = "RetroArch_MiBoxS_Charly"
ruta_usb = input("Ruta completa del pendrive (ej: /media/charly/RETROUSB o E:\\): ").strip()

ruta_base = os.path.join(ruta_usb, nombre_carpeta)
subcarpetas = [
    "ROMs/NES",
    "ROMs/SNES",
    "ROMs/SEGA",
    "ROMs/PS1",
    "ROMs/ARCADE",
    "SAVES/states",
    "SAVES/saves",
    "playlists",
    "thumbnails",
    "assets/xmb"
]

archivos_texto = {
    "LEEME.txt": "Coloca tus ROMs en las carpetas dentro de /ROMs.\nGuarda automáticos y manuales se generan en /SAVES.\n",
    "cores_packs.txt": "Cores recomendados: Nestopia, Snes9x, Genesis Plus GX, PCSX ReARMed, FBNeo.",
    "CONTROLES_PS4.txt": "DualShock 4 - mantener Share + PS para emparejar por Bluetooth.\nRetroArch lo detectará automáticamente.",
}

# --- CREAR ESTRUCTURA ---
print(f"\nCreando estructura en: {ruta_base}\n")
os.makedirs(ruta_base, exist_ok=True)

for carpeta in subcarpetas:
    os.makedirs(os.path.join(ruta_base, carpeta), exist_ok=True)
    print(f"✅ Carpeta creada: {carpeta}")

for nombre, contenido in archivos_texto.items():
    archivo = os.path.join(ruta_base, nombre)
    with open(archivo, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"📄 Archivo creado: {nombre}")

# --- ARCHIVO DE CONFIGURACIÓN BASE ---
retroarch_cfg = """# Configuracion basica para Mi Box S
menu_driver = "xmb"
input_driver = "android"
savefile_directory = "SAVES/saves"
savestate_directory = "SAVES/states"
system_directory = "ROMs"
assets_directory = "assets/xmb"
thumbnails_directory = "thumbnails"
playlist_directory = "playlists"
cheat_database_path = "cheats"
video_threaded = true
video_fullscreen = true
video_vsync = true
video_smooth = true
ui_companion_start_on_boot = true
"""
with open(os.path.join(ruta_base, "retroarch.cfg"), "w", encoding="utf-8") as f:
    f.write(retroarch_cfg)

print("\n🎮 Estructura completa lista.")
print(f"\n👉 Pendrive preparado en: {ruta_base}")
print("Copiá tus ROMs en las carpetas dentro de /ROMs antes de conectarlo a la TV Box.")

