class Menu:
    def __init__(self):
        self.item = {}

    def add_menu(self, name, price):
        if name not in self.item:
            self.item[name] = price
            print('New menu has been added')
            self.save_menu()
        else:
            print('Menu already exists')

    def upgrade_price(self, name, price):
        if name in self.item:
            self.item[name] = price
            print('Price has been updated')
            self.save_menu()
        else:
            print('Menu does not exist')

    def remove_menu(self, name):
        if name in self.item:
            del self.item[name]
            print('Menu has been removed')
            self.save_menu()
        else:
            print('Menu does not exist')

    def get_price(self, name):
        if name in self.item:
            return round(float(self.item[name]), 3)
        else:
            print('Menu does not exist')

    def show_menu(self):
        count = 1
        print("\nHere's the restaurant menu: \n")
        for name, price in self.item.items():
            print(f'{count}| {name:20}: Rp{price}')
            count += 1
        print('0| Exit')

    def load_menu(self):
        with open('menu_book.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                items = line.strip().split(':')
                self.item[items[0]] = items[1]
    
    def save_menu(self):
        with open('menu_book.txt', 'w') as file:
            for item, price in self.item.items():
                file.write(f'{item}:{price}\n')
            