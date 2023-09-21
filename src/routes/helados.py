from flask import Blueprint, jsonify
#models
from models.heladosModelo import HeladosModelo
main=Blueprint('helado_blueprint', __name__)

@main.route('/')
def get_helado():
    try:
        inventario=HeladosModelo.get_Inventory()
        return jsonify(inventario)

    except Exception as ex:
        return jsonify({'message': str(ex)}),500