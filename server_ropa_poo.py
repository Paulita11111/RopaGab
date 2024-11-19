from flask import Flask, jsonify, request
import ropa_controller_poo
from exchange_rate import get_xr
app = Flask(__name__)


@app.route("/prenda/create", methods=["POST"])
def insert_prenda(): # permite insertar una prenda, el index no puede repetirse por ser PK
    prenda_details = request.get_json()
    indexer = prenda_details["indexer"]
    product = prenda_details["product"]
    category = prenda_details["category"]
    sub_category= prenda_details["sub_category"]
    brand = prenda_details["brand"]
    sale_price = prenda_details["sale_price"]
    market_price = prenda_details["market_price"]
    typec = prenda_details ["typec"]
    rating = prenda_details ["rating"]
    description = prenda_details['description']
    result = ropa_controller_poo.insert_prenda(indexer, product, category, sub_category, brand, sale_price,market_price, typec, rating, description)
    return jsonify(result)

@app.route("/prenda/modify", methods=["PUT"])
def update_prenda(): # permite modificar una prenda, el index lo rescata del body del POST
    prenda_details = request.get_json()
    indexer = prenda_details["indexer"]
    product = prenda_details["product"]
    category = prenda_details["category"]
    sub_category= prenda_details["sub_category"]
    brand = prenda_details["brand"]
    sale_price = prenda_details["sale_price"]
    market_price = prenda_details["market_price"]
    typec = prenda_details ["typec"]
    rating = prenda_details ["rating"]
    description = prenda_details['description']
    result = ropa_controller_poo.update_prenda(indexer, product, category, sub_category, brand, sale_price,market_price, typec, rating, description)
    return jsonify(result)

@app.route("/prenda/eliminate/<indexer>", methods=["DELETE"])
def delete_prenda(indexer): # permite eliminar la prenda cuyo index se indique en la url
    result = ropa_controller_poo.delete_prenda(indexer)
    return jsonify(result)


@app.route("/prenda/pesos/<indexer>", methods=["GET"])
def get_prenda_by_id_pesos(indexer): # devuelve el precio en pesos de la prenda (la base tiene los precios en usd)
    prenda = ropa_controller_poo.get_by_id(indexer)
    xr = get_xr()
    sale_price_pesos = prenda['sale_price']*xr
    market_price_pesos = prenda['market_price']*xr
    prenda['sale_price'] = round(sale_price_pesos,2)
    prenda['market_price'] = round(market_price_pesos,2)
    return jsonify(prenda)

app.run()
