# -*- coding: utf-8 -*-
"""
Asistente NOVA - Voz Latina (gTTS)
Autor: charlyporty & NOVA 💪
"""
    
from gtts import gTTS
import os

# Mensaje de prueba
mensaje = "Hola Charly, soy NOVA. Tu asistente está listo para comenzar un nuevo día de programación y aprendizaje."

# Crear voz con acento latino (tld="com.ar" mejora el tono argentino)
voz = gTTS(text=mensaje, lang="es", tld="com.ar")

# Guardar archivo MP3
voz.save("voz_nova.mp3")

# Reproducir el archivo según el sistema operativo
# En Linux o macOS:
os.system("mpg123 voz_nova.mp3")  # Necesita tener mpg123 instalado

# En Windows (alternativa si usás ese entorno):
# os.system("start voz_nova.mp3")

print("✅ NOVA: Mensaje reproducido correctamente.")

