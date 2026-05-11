from memory import menu, find_order, verify_admin

def process_finalize_order():
    print("------------ FINALIZE ORDER ------------")
    order_id = int(input("Order ID: "))
    order = find_order(order_id)
    if order is None:
        print(f"Order {order_id} not found.")
        return

    print_guest_check(order)

    confirmed = input("Is guest check confirmed? (y/n): ").strip().lower()
    if confirmed == "y":
        print_final_check(order)
        order["status"] = "finalized"
        return

    issue = input("Describe the issue: ")
    print(f"Issue noted: {issue}")
    if not verify_admin():
        print("Admin verification failed. Finalization aborted.")
        return
    print_guest_check(order)
    print_final_check(order)
    order["status"] = "finalized"

def print_guest_check(order):
    print("\n----- GUEST CHECK -----")
    print(f"Order ID: {order["id"]}")
    print(f"Table ID: {order["table_id"]}")
    total = 0
    for item_id, quantity in order["order_items"].items():
        item = menu[int(item_id)]
        line_total = item["price"] * int(quantity)
        total += line_total
        print(f"  {item["name"]} x {quantity} - Rs. {line_total}")
    print(f"TOTAL: Rs. {total}")
    print("-----------------------\n")

def print_final_check(order):
    print("\n===== FINAL CHECK =====")
    print(f"Order ID: {order["id"]}")
    print(f"Table ID: {order["table_id"]}")
    total = 0
    for item_id, quantity in order["order_items"].items():
        item = menu[int(item_id)]
        line_total = item["price"] * int(quantity)
        total += line_total
        print(f"  {item["name"]} x {quantity} - Rs. {line_total}")
    print(f"TOTAL: Rs. {total}")
    print("=======================\n")
