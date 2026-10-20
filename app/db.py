import sqlite3

from flask import Flask, request

app = Flask(__name__)


def connect():
    return sqlite3.connect("orders.db")


@app.route("/orders")
def orders():
    customer = request.args.get("customer")
    cursor = connect().cursor()
    cursor.execute(f"SELECT id, total FROM orders WHERE customer = '{customer}'")
    return {"orders": cursor.fetchall()}


@app.route("/order")
def order():
    order_id = request.args.get("id")
    cursor = connect().cursor()
    cursor.execute("SELECT id, total FROM orders WHERE id = " + order_id)
    return {"order": cursor.fetchone()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
