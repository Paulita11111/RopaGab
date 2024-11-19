from db_ropa import get_db
from clase_ropa import Prenda


def insert_prenda(indexer, product, category, sub_category, brand, sale_price, market_price, typec, rating, description):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO prendas (indexer, product, category, sub_category, brand, sale_price, market_price, typec, rating, description) \
    VALUES ( ?, ?, ?, ? ,?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [indexer, product, category, sub_category, brand, sale_price, market_price, typec, rating, description])
    db.commit()
    return True

def update_prenda(indexer, product, category, sub_category, brand, sale_price, market_price, typec, rating, description):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE prendas SET product= ?, category= ?, sub_category= ?, brand= ?, sale_price= ?, market_price= ?,typec= ?, \
    rating= ?, description= ? WHERE indexer= ?"
    cursor.execute(statement, [product, category, sub_category, brand, sale_price, market_price, typec, rating, description, indexer])
    db.commit()
    return True


def delete_prenda(indexer):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM prendas WHERE indexer = ?"
    cursor.execute(statement, [indexer])
    db.commit()
    return True


def get_by_id(indexer):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT indexer, product, category, sub_category, brand, sale_price, market_price, typec, rating, \
    description FROM prendas WHERE indexer = ?"
    cursor.execute(statement, [indexer])
    single_prenda = cursor.fetchone()
    indexer= single_prenda[0]
    product = single_prenda[1]
    category = single_prenda[2]
    sub_category = single_prenda[3]
    brand = single_prenda[4]
    sale_price = single_prenda[5]
    market_price = single_prenda[6]
    typec= single_prenda[7]
    rating = single_prenda[8]
    description = single_prenda[9]
    prenda = Prenda(indexer, product, category, sub_category, brand, sale_price, market_price, typec, rating, description) 
    return prenda.serialize_details()
