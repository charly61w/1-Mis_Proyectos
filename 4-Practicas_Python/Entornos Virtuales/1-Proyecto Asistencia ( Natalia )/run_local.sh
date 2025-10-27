#!/bin/bash

# Ruta al entorno virtual
VENV_PATH="/home/charly/Mis Proyectos/Python_3.11/Proyecto_Asistencia_Natalia/venv"

# Activar entorno virtual
source "$VENV_PATH/bin/activate"

# Navegar al proyecto
cd "/home/charly/Mis Proyectos/Python_3.11/Proyecto_Asistencia_Natalia"

# Ejecutar la app
python app.py

