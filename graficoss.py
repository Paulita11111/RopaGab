import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from db_ropa import get_db

# Conexión con la base de datos
def get_db():
    conn = sqlite3.connect('ropa.db')
    conn.row_factory = sqlite3.Row  # Devuelve resultados como diccionarios
    return conn

# Función para obtener datos desde la base de datos
def obtener_datos():
    # Obtén los datos de la base de datos
    query = "SELECT product, category, sale_price, market_price, rating FROM product_catalog"
    conn = get_db()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Graficar precio de venta
def graficar_precio_venta(df):
    plt.figure(figsize=(10, 6))
    df_sorted = df[['product', 'sale_price']].sort_values(by='sale_price', ascending=False)
    plt.bar(df_sorted['product'], df_sorted['sale_price'], color='teal')
    plt.title('Precio de Venta por Producto', fontsize=14)
    plt.xlabel('Producto', fontsize=12)
    plt.ylabel('Precio de Venta (USD)', fontsize=12)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Graficar precio de venta vs. precio de mercado
def graficar_precio_venta_vs_mercado(df):
    plt.figure(figsize=(8, 5))
    plt.scatter(df['sale_price'], df['market_price'], color='orange')
    plt.title('Precio de Venta vs. Precio de Mercado', fontsize=14)
    plt.xlabel('Precio de Venta (USD)', fontsize=12)
    plt.ylabel('Precio de Mercado (USD)', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Graficar promedio de precio por categoría
def graficar_promedio_categoria(df):
    avg_sale_price = df.groupby('category')['sale_price'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    avg_sale_price.plot(kind='bar', color='salmon')
    plt.title('Promedio de Precio de Venta por Categoría', fontsize=14)
    plt.xlabel('Categoría', fontsize=12)
    plt.ylabel('Promedio de Precio de Venta (USD)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Función para generar todos los gráficos
def generar_graficos():
    df = obtener_datos()  # Obtener los datos desde la base de datos
    graficar_precio_venta(df)
    graficar_precio_venta_vs_mercado(df)
    graficar_promedio_categoria(df)

# Llamar la función para generar los gráficos
if __name__ == '__main__':
    generar_graficos()
