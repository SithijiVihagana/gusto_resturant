from memory import menu, find_order

def process_view_order():
    print("------------ VIEW ORDER ------------")
    order_id = int(input("Order ID: "))
    order = find_order(order_id)
    if order is None:
        print(f"Order {order_id} not found.")
        return

    print(f"\nOrder ID: {order["id"]}")
    print(f"Table ID: {order["table_id"]}")
    print(f"Steward ID: {order["steward_id"]}")
    print(f"Status: {order["status"]}")
    print("Items:")
    if not order["order_items"]:
        print("  (no items)")
        return
    for item_id, quantity in order["order_items"].items():
        item_name = menu[int(item_id)]["name"]
        print(f"  - {item_name} x {quantity}")
