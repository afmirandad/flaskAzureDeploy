# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if 0 <= item_id < len(items):
        return jsonify(items[item_id])
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if 0 <= item_id < len(items):
        data = request.get_json()
        items[item_id] = data
        return jsonify(data)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(items):
        item = items.pop(item_id)
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/')
def roothello():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'Hello, Azure!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
