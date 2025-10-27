# Análisis de Tiempos de Vuelta en F1 con FastF1

Este proyecto en Python permite comparar los tiempos de vuelta de dos pilotos en una carrera real de Fórmula 1, usando la biblioteca `FastF1`.

## Requisitos

- Python 3.8 o superior
- Conexión a internet (para descargar los datos)
- Paquetes requeridos: ver `requirements.txt`

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Salida

- Un gráfico de comparación de tiempos de vuelta (`comparacion_ritmo.png`)
- Visualización directa en pantalla

## Personalización

Podés cambiar los valores de:
- `year`: año de la carrera
- `gp`: nombre del Gran Premio (ej. `'Monaco'`, `'Brazil'`)
- `driver1` y `driver2`: códigos de 3 letras de los pilotos (ej. `'VER'`, `'HAM'`, `'LEC'`, `'ALO'`)