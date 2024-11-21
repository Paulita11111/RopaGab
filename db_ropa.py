import sqlite3
import pandas as pd

# Constantes
CSV_FILE = 'Updated_Clothing_Products.csv'
DATABASE = 'ropa.db'

# Función para obtener la conexión a la base de datos
def get_db():
    """
    Obtiene una conexión a la base de datos SQLite.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Permite devolver resultados como diccionarios
    return conn

# Función para crear la tabla en la base de datos
def crear_tabla():
    """
    Crea la tabla 'product_catalog' en la base de datos si no existe.
    """
    with get_db() as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS product_catalog (
                indexer INTEGER PRIMARY KEY,
                product TEXT,
                category TEXT,
                sub_category TEXT,
                brand TEXT,
                sale_price REAL,
                market_price REAL,
                typec TEXT,
                rating REAL,
                description TEXT,
                sale_price_euro REAL,
                market_price_euro REAL
            )
        ''')
        conn.commit()
    print("Tabla 'product_catalog' creada (o ya existía).")

# Función para cargar los datos del CSV a la base de datos
def cargar_datos_csv():
    """
    Carga los datos del archivo CSV en la tabla 'product_catalog' de la base de datos.
    """
    try:
        # Leer el archivo CSV
        df = pd.read_csv(CSV_FILE)
        
        # Limpieza de los nombres de las columnas
        df.columns = df.columns.str.strip()

        # Renombrar columnas para que coincidan con las de la base de datos
        df.rename(columns={
            'index': 'indexer',
            'type': 'typec'
            # Puedes agregar más renombres si es necesario
        }, inplace=True)

        # Verificar columnas del DataFrame
        print("Columnas del CSV después de limpieza:")
        for column in df.columns:
            print(f"- {column}")

        # Insertar los datos en la tabla
        with get_db() as conn:
            df.to_sql('product_catalog', conn, if_exists='replace', index=False)
        
        print("Datos cargados en la base de datos exitosamente.")
    except Exception as e:
        print(f"Error al cargar datos del CSV: {e}")

# Función para mostrar las columnas de la tabla 'product_catalog'
def mostrar_columnas():
    try:
        connection = get_db()
        cursor = connection.cursor()
        
        # Consulta para obtener las columnas
        cursor.execute("PRAGMA table_info(product_catalog);")
        
        columnas = cursor.fetchall()
        
        # Mostrar las columnas en formato legible
        print("Columnas de la tabla 'product_catalog':")
        for col in columnas:
            print(f"- {col['name']}")

    except Exception as e:
        print(f"Error al obtener columnas: {e}")
    finally:
        cursor.close()

# Función principal para ejecutar todo
def main():
    """
    Ejecuta la creación de la tabla y la carga de datos del CSV.
    """
    crear_tabla()
    cargar_datos_csv()
    mostrar_columnas() 

# Ejecutar la función principal
if __name__ == "__main__":
    main()
