import memory
from memory import orders
from memory import menu

def process_take_order():
    print("------------ TAKE ORDER ------------")
    steward_id = input("Steward ID: ")
    table_id = input("Table ID: ")
    print("\n Avaiable Menu")
    for index, item in enumerate(menu):
        print(f"[{index}] {item["name"]} - Rs. {item["price"]}")
    items_input = input("Input food in this format (id:quantity) comma seperated:")
    items = items_input.split(",")
    order_items = {}
    for selected_item in items:
        selected_item_details = selected_item.split(":")
        print(selected_item_details)
        order_items[selected_item_details[0]] = selected_item_details[1]
    order = {
        "id": memory.next_order_id,
        "table_id": table_id,
        "steward_id": steward_id,
        "order_items": order_items,
        "status": "open",
    }
    orders.append(order)
    memory.next_order_id += 1
    print_kot(order)

def print_kot(order):
    print("\n----- KITCHEN ORDER TICKET -----")
    print(f"Order ID: {order["id"]}")
    print(f"Table ID: {order["table_id"]}")
    print(f"Steward ID: {order["steward_id"]}")
    print("Items:")
    for item_id, quantity in order["order_items"].items():
        item_name = menu[int(item_id)]["name"]
        print(f"  - {item_name} x {quantity}")
    print("--------------------------------\n")
