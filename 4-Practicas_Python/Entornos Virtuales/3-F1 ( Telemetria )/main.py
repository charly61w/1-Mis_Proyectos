import fastf1
from fastf1.plotting import setup_mpl
import matplotlib.pyplot as plt
import os

# Habilita la caché para guardar datos descargados
fastf1.Cache.enable_cache('./cache')

# Parámetros del análisis
year = 2025
gp = 'Monaco'
session_type = 'R'  # 'R' = carrera
driver1 = 'VER'
driver2 = 'HAM'

print(f"Cargando datos de la carrera {gp} {year}...")
session = fastf1.get_session(year, gp, session_type)
session.load()

# Filtrar las vueltas de cada piloto
laps_driver1 = session.laps.pick_driver(driver1).pick_quicklaps()
laps_driver2 = session.laps.pick_driver(driver2).pick_quicklaps()

# Crear gráfico comparativo
setup_mpl()  # Aplicar estilos visuales

plt.figure(figsize=(10, 6))
plt.plot(laps_driver1['LapNumber'], laps_driver1['LapTime'].dt.total_seconds(), label=driver1)
plt.plot(laps_driver2['LapNumber'], laps_driver2['LapTime'].dt.total_seconds(), label=driver2)

plt.xlabel('Número de vuelta')
plt.ylabel('Tiempo de vuelta (segundos)')
plt.title(f'Comparación de ritmo: {driver1} vs {driver2} - {gp} {year}')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('comparacion_ritmo.png')
plt.show()
