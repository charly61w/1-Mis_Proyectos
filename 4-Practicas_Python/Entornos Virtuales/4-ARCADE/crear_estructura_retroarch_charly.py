import os

# Ruta base donde se creará la estructura (puede ser un pendrive o carpeta local)
# Ejemplo: en Windows podría ser "E:\\", y en Linux "/media/charly/PENDRIVE/"
base_path = input("📁 Ingresá la ruta donde querés crear la estructura (por ejemplo /media/charly/PENDRIVE/): ").strip()

# Nombre raíz del sistema
root_folder = "RetroArch_Charly_Portable"
root_path = os.path.join(base_path, root_folder)

# Estructura de carpetas
folders = [
    "playlists",
    "system",
    "cores",
    "roms/PS1",
    "roms/MAME",
    "saves/PS1",
    "saves/MAME",
    "states",
    "thumbnails/Sony - PlayStation",
    "thumbnails/MAME 2003-Plus",
    "assets",
    "overlays",
    "config",
    "shaders"
]

# Archivos vacíos de ejemplo
files = {
    "retroarch.cfg": "",
    "playlists/Sony - PlayStation.lpl": "",
    "playlists/MAME 2003-Plus.lpl": "",
    "system/SCPH1001.BIN": "",
    "system/neogeo.zip": "",
    "cores/pcsx_rearmed_libretro.so": "",
    "cores/mame2003_plus_libretro.so": "",
    "cores/fbalpha2012_libretro.so": "",
    "config/pcsx_rearmed_libretro.cfg": "",
    "config/mame2003_plus_libretro.cfg": ""
}

# Crear carpetas
for folder in folders:
    folder_path = os.path.join(root_path, folder)
    os.makedirs(folder_path, exist_ok=True)
    print(f"✅ Carpeta creada: {folder_path}")

# Crear archivos vacíos de ejemplo
for file, content in files.items():
    file_path = os.path.join(root_path, file)
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"📝 Archivo creado: {file_path}")

print("\n🎮 Estructura completa creada con éxito en:")
print(root_path)
print("\n💡 Ahora podés copiar tus ROMs, BIOS y configuraciones a sus carpetas correspondientes.")

