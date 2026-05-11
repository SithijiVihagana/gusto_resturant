from memory import menu, find_order, verify_admin
from take_order import print_kot

def process_edit_order():
    print("------------ EDIT ORDER ------------")
    order_id = int(input("Order ID: "))
    order = find_order(order_id)
    if order is None:
        print(f"Order {order_id} not found.")
        return

    while True:
        show_current_items(order)
        print("\n[1] Add items")
        print("[2] Remove items")
        print("[3] Save & send to kitchen")
        print("[4] Cancel")
        sub_id = int(input("# Enter Option: "))

        match sub_id:
            case 1:
                add_items(order)
            case 2:
                if not verify_admin():
                    continue
                remove_items(order)
            case 3:
                if not verify_admin():
                    continue
                print_kot(order)
                return
            case 4:
                print("Edit cancelled.")
                return
            case _:
                print("Invalid option.")

def show_current_items(order):
    print(f"\nCurrent items for Order {order["id"]}:")
    if not order["order_items"]:
        print("  (no items)")
        return
    for item_id, quantity in order["order_items"].items():
        item_name = menu[int(item_id)]["name"]
        print(f"  [{item_id}] {item_name} x {quantity}")

def add_items(order):
    print("\n Avaiable Menu")
    for index, item in enumerate(menu):
        print(f"[{index}] {item["name"]} - Rs. {item["price"]}")
    items_input = input("Input food in this format (id:quantity) comma seperated:")
    items = items_input.split(",")
    for selected_item in items:
        selected_item_details = selected_item.split(":")
        item_id = selected_item_details[0]
        quantity = selected_item_details[1]
        if item_id in order["order_items"]:
            order["order_items"][item_id] = str(int(order["order_items"][item_id]) + int(quantity))
        else:
            order["order_items"][item_id] = quantity

def remove_items(order):
    ids_input = input("Item IDs to remove (comma seperated): ")
    ids = ids_input.split(",")
    for item_id in ids:
        item_id = item_id.strip()
        if item_id in order["order_items"]:
            del order["order_items"][item_id]
        else:
            print(f"Item {item_id} not in order.")
