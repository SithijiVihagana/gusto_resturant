from memory import orders
from memory import menu

def process_take_order():
    print("------------ TAKE ORDER ------------")
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
    steward_name = input("Steward Name: ")
    orders.append({
        "order_items":order_items,
        "steward_name":steward_name
    })