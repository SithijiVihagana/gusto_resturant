import os

from create_order import process_take_order
from finalize_order import process_finalize_order
from edit_order import process_edit_order
from view_order import process_view_order

def main():
    main_manu()
    menu_id = int(input("# Enter Menu ID: "))
    clear_console()
    match menu_id: 
        case 1:
            process_take_order()
        case 2:
            process_edit_order()
        case 3:
            process_finalize_order()
        case 4:
            process_view_order()

def main_manu():
    print("------------ MAIN MENU ------------")
    print("[1] Take Order")
    print("[2] Edit Order")
    print("[3] Finalize The Order")
    print("[4] View The Order")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

main()