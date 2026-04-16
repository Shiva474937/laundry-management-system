from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []
order_id = 1

prices = {
    "shirt": 10,
    "pants": 15,
    "saree": 20
}

# 1. Create Order
@app.route('/create', methods=['POST'])
def create_order():
    global order_id

    data = request.json
    total = 0

    for item in data['garments']:
        total += prices[item['type']] * item['quantity']

    order = {
        "id": order_id,
        "name": data['name'],
        "phone": data['phone'],
        "garments": data['garments'],
        "total": total,
        "status": "RECEIVED"
    }

    orders.append(order)
    order_id += 1

    return jsonify(order)


# 2. View Orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)


# 3. Update Status
@app.route('/status/<int:id>', methods=['PUT'])
def update_status(id):
    data = request.json

    for order in orders:
        if order['id'] == id:
            order['status'] = data['status']
            return jsonify(order)

    return {"message": "Order not found"}


# 4. Dashboard
@app.route('/dashboard', methods=['GET'])
def dashboard():
    total_orders = len(orders)
    total_money = sum(o['total'] for o in orders)

    return {
        "total_orders": total_orders,
        "total_revenue": total_money
    }


app.run(debug=True)