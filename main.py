import os

def main():
    main_manu()
    menu_id = int(input("# Enter Menu ID: "))
    clear_console()
    match menu_id: 
        case 1:
            print("You Selected Take Order")
        case 2:
            print("You Selected Edit Order")
        case 3:
            print("You Selected Edit Order")

def main_manu():
    print("------------ MAIN MENU ------------")
    print("[1] Take Order")
    print("[2] Edit Order")
    print("[3] Finalize The Order")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

main()