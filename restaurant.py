from array_datastructure import Array
from menu import Menu
from queue_order import Queue
from table import Table

class Restaurant:
    def __init__(self):
        self.table_status = Array(5)
        self.menu = Menu()
        self.queue = Queue()
        self.table = None

    def load_table_status(self):
        with open('table_status.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                self.table_status.append(line)
                
    def save_table_status(self):
        with open('table_status.txt', 'w') as file:
            for i in self.table_status.array:
                file.write(f'{i}\n')

    def ask_for_empty_table(self):
        print(f'\nThere are {self.table_status.count("True")} empty tables:')
        for i in range(self.table_status.len()):
            if self.table_status.array[i] == 'True':
                print(f' Table {i + 1}')

    def equipped_table(self, table_number):
        table_number = int(table_number)
        if table_number < 1 or table_number > self.table_status.len():
            print('\nTable does not exist')
            return False
        elif self.table_status.array[table_number - 1] == 'False':
            print(f'\nTable {table_number} is already equipped')
            return False
        elif self.table_status.array[table_number - 1] == 'True':
            self.table_status.array[table_number - 1] = 'False'
            print(f'\nNow, table {table_number} is equipped')
            self.save_table_status()
            return True
        else:
            print('\nInvalid request')
            return False

    def ask_for_order(self, table_number):
        self.menu.load_menu()
        self.menu.show_menu()
        menu_lst = Array(1)
        order_lst = Array(1)
        print()
        count = 1
        for i in self.menu.item:
            menu_lst.append(i)
        while True:
            try:
                print(f'Menu {count}')
                item_number = int(input('Input number: '))
            except ValueError:
                print('Input menu number')
                pass
            else:
                if item_number < (menu_lst.len() + 1) and item_number != 0:
                    order_lst.append(menu_lst.get_item(item_number - 1))
                    count += 1
                elif item_number == 0:
                    print('\nMenu has been inputed')
                    break
                else:
                    print('Menu does not exist.')
        self.table = Table()
        self.table.add_menu_list(order_lst.array, table_number)
        self.queue.enqueue(table_number)

    def ask_for_next_order(self):
        self.queue.load_queue()
        if self.queue.get_size() == 0:
            print('\nNo more orders')
        else:
            table_number = self.queue.dequeue()
            self.table = Table()
            self.queue.save_queue_after_dequeue()
            print(f'\nTable {table_number}:')
            self.table.show_order(table_number)

    def ask_for_total_order(self):
        self.queue.load_queue()
        print(f'\nTotal order: {self.queue.get_size()}')

    def ask_for_bill(self, table_number):
        print()
        self.table = Table()
        if self.table_status.array[table_number - 1] == 'False':
            total_price = self.table.show_order(table_number)
            while True:
                status = input('\nIs it paid? (y:yes/n:no): ')
                if status == 'y' or status == 'yes':
                    print('\nThank you and have a nice day')
                    self.table_status.array[table_number - 1] = 'True'
                    self.table.clear_order(table_number)
                    self.table = None
                    with open('order_history.txt', 'a') as file:
                        file.write(f'{table_number}:{total_price}\n')
                    self.save_table_status()
                    self.queue.remove_queue(table_number)
                    break
                elif status == 'n' or status == 'no':
                    print('\nEnjoy your meal and remember to pay')
                    break
                else:
                    print('Invalid answer')
        else:
            print('There is no order for this table')

    def ask_for_order_history(self):
        total_income = 0
        print("\nHere's the restaurant's income:")
        print('-------------------------------\n')
        with open('order_history.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                table_number, total_price = line.strip().split(':')
                total_income += round(float(total_price), 3)
                print(f'Table {table_number}: Rp{float(total_price):.3f}')
        print(f'\nTotal Income: Rp{float(total_income):.3f}')

    def ask_to_cancel_order(self, table_number):
        self.table = Table()
        if self.table_status.array[table_number - 1] == 'True':
            print('\nTable is already empty')
        else:
            self.table_status.array[table_number - 1] = 'True'
            self.table.clear_order(table_number)
            self.table = None
            self.queue.remove_queue(table_number)
            self.save_table_status()
            print('\nThank you and come again.')
            