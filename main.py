from menu import Menu
from restaurant import Restaurant

def print_welcoming_menu():
    print("Welcome to The Restaurant")
    print('-------------------------------')
    print('1. I am a worker')
    print('2. I am a customer')

def print_customer_menu():
    print('\nHow can I help you?')
    print('-------------------')
    print('1. Ask for empty table')
    print('2. Ask for order')
    print('3. Ask for bill')
    print('4. Cancelling order')
    print('0. Exit')

def print_worker_menu():
    print('\nHow can I help you?')
    print('-------------------')
    print('1. Add menu')
    print('2. Upgrade menu')
    print('3. Delete menu')
    print('4. Ask for next order')
    print('5. Ask for total order')
    print('6. Ask for order history')
    print('7. Show menu')
    print('0. Exit')

if __name__ == '__main__':
    R = Restaurant()
    M = Menu()
    R.load_table_status()
    M.load_menu()

    while True:
        print_welcoming_menu()
        print('\nWho are you?')
        identity = input('\nInput number: ')
        
        if identity == '1':
            
            while True:
                print_worker_menu()
                print('\nWhat do you want to do?')
                choice = input('Input number: ').strip()
                
                if choice == '1':
                    name = input('\nInput new item: ').title()
                    while True:
                        try:
                            price = float(input("Input new item's price: "))
                            price = f'{price:,.2f}'.replace(',', '.')[:-3]
                        except ValueError:
                            print('Please input price in number')
                        else:
                            M.add_menu(name, price)
                            break
                    
                elif choice == '2':
                    name = input('\nInput item: ').title()
                    while True:
                        try:
                            price = float(input("Input new item's price: "))
                            price = f'{price:,.2f}'.replace(',', '.')[:-3]
                        except ValueError:
                            print('Please input price in number')
                        else:
                            M.upgrade_price(name, price)
                            break
                    
                elif choice == '3':
                    name = input('\nInput item: ').title()
                    M.remove_menu(name)
                    
                elif choice == '4':
                    R.ask_for_next_order()
                    
                elif choice == '5':
                    R.ask_for_total_order()
                    
                elif choice == '6':
                    R.ask_for_order_history()
        
                elif choice == '7':
                    M.show_menu()
    
                elif choice == '0':
                    break
                    
                else:
                    print('\nInvalid choice')

            break
                
        elif identity == '2':
            
            while True:
                print_customer_menu()
                print('\nWhat do you want to do?')
                choice = input('\nInput number: ').strip()
                
                if choice == '1':
                    R.ask_for_empty_table()
                    
                    
                elif choice == '2':
                    while True:
                        try:
                            table_number = int(input('\nYour table number: '))
                            status = R.equipped_table(table_number)
                        except ValueError:
                            print('Please input table number')
                            pass
                        else:
                            if status:
                                R.ask_for_order(table_number)
                                break
                    
                elif choice == '3':
                    while True:
                        try:
                            table_number = int(input('\nYour table number: '))
                        except ValueError:
                            print('Input number')
                            pass
                        else:
                            R.ask_for_bill(table_number)
                            break
                    break
    
                elif choice == '4':
                    while True:
                        try:
                            table_number = int(input('\nYour table number: '))
                        except ValueError:
                            print('Input number')
                            pass
                        else:
                            R.ask_to_cancel_order(table_number)
                            break
                    break
        
                elif choice == '0':
                    break
                    
                else:
                    print('Invalid choice')
            break
    
        else:
            print('Invalid choice\n')