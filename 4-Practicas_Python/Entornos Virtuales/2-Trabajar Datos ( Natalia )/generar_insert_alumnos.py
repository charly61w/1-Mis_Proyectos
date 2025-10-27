import pandas as pd

# Ruta del archivo .xls
archivo_entrada = "cursada1.xls"  # Cambiá el nombre si tu archivo se llama distinto
archivo_salida = "insert_alumnos.sql"

# Columnas esperadas
columnas = ["tipo_documento", "documento", "nombre", "apellido", "email", "telefono", "instancia"]

# Leer archivo Excel
df = pd.read_excel(archivo_entrada, engine="xlrd")  # xlrd sirve para .xls (no .xlsx)
df.columns = [str(col).strip().lower() for col in df.columns]

# Asegurar que todas las columnas existan
for col in columnas:
    if col not in df.columns:
        df[col] = None

# Reordenar y llenar vacíos
df = df[columnas].fillna('NULL')

# Función para formatear valores SQL
def formatear_valor(val):
    if str(val).upper() == 'NULL':
        return 'NULL'
    val_str = str(val).strip().replace("'", "''")
    return f"'{val_str}'"

# Generar líneas de INSERT
valores_sql = []
for _, fila in df.iterrows():
    valores = ", ".join([formatear_valor(fila[col]) for col in columnas])
    valores_sql.append(f"({valores})")

# Armado final de la sentencia SQL
sentencia_sql = (
    "INSERT INTO alumnos (tipo_documento, documento, nombre, apellido, email, telefono, instancia) VALUES\n" +
    ",\n".join(valores_sql) +
    ";"
)

# Guardar en archivo .sql
with open(archivo_salida, "w", encoding="utf-8") as f:
    f.write(sentencia_sql)

print("✅ Archivo generado correctamente: insert_alumnos.sql")

