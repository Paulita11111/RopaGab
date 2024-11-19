import sqlite3
import pandas as pd

# Ruta del archivo CSV
CSV_FILE = 'Updated_Clothing_Products.csv'
DATABASE = 'ropa.db'

# Función para crear la tabla en la base de datos
def crear_tabla():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        
        # Crear la tabla product_catalog
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

# Función para cargar los datos del CSV a la base de datos
def cargar_datos_csv():
    
    df = pd.read_csv(CSV_FILE)
    
    df.columns=df.columns.str.strip()

    # Renombrar las columnas del DataFrame para que coincidan con las de la base de datos
    df.rename(columns={
        'index': 'indexer',
        'type': 'typec',
        'sale_price_euro': 'sale_price_euro',
        'market_price_euro': 'market_price_euro'
        # Agrega más renombres si es necesario
    }, inplace=True)

    columns = df.columns
    for column in columns:
        print(column)
    
    # Insertar los datos en la base de datos
    with sqlite3.connect(DATABASE) as conn:
        df.to_sql('product_catalog', conn, if_exists='replace', index=False)
        
    print("Datos cargados en la base de datos exitosamente.")

# Crear la tabla
crear_tabla()
cargar_datos_csv()
