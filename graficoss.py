import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Distribución del precio de venta por categoría
def distribucion_precio_categoria(df):
    sns.boxplot(data=df, x='category', y='sale_price')
    plt.title('Distribución del Precio de Venta por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Precio de Venta (USD)')
    plt.xticks(rotation=90)
    plt.show()    


# Grafico de torta: proporción de productos por categoría
def graficar_proporcion_categoria(df):
    category_counts = df['category'].value_counts()  # Contar productos por categoría
    plt.figure(figsize=(8, 8))
    plt.pie(
        category_counts,
        labels=category_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.Paired.colors  # Colores agradables
    )
    plt.title('Proporción de Productos por Categoría', fontsize=14)
    plt.show()

# Gráfico de Barras: Promedio de Rating por Categoría
def promedio_rating_categoria(df):
    plt.figure(figsize=(10, 6))
    df.groupby('category')['rating'].mean().sort_values(ascending=False).plot(kind='bar', color='skyblue')
    plt.title('Promedio de Rating por Categoría', fontsize=14)
    plt.xlabel('Categoría', fontsize=12)
    plt.ylabel('Rating Promedio', fontsize=12)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Función para generar todos los gráficos
def generar_graficos():
    df = obtener_datos()  # Obtener los datos desde la base de datos
    distribucion_precio_categoria(df)
    graficar_proporcion_categoria(df)
    promedio_rating_categoria(df)

# Llamar la función para generar los gráficos
if __name__ == '__main__':
    generar_graficos()

