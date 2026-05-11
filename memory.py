menu = [
    {
        "name":"String Hoppers",
        "price":7
    }
]

orders = []

ADMIN_PASSWORD = "admin123"

next_order_id = 1

def find_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            return order
    return None

def verify_admin():
    password = input("Enter admin password: ")
    if password == ADMIN_PASSWORD:
        return True
    print("Invalid admin password.")
    return False
