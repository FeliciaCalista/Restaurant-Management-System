from menu import Menu
from table_order import Order 

class Table:
    def __init__(self):
        self.order = Order()
        self.menu = Menu()
        self.menu.load_menu()

    def add_menu_list(self, lst, table_number):
        for item in lst:
            price = self.menu.get_price(item)
            self.order.add_item(item, price)
        self.order.save_order(table_number)

    def show_order(self, table_number):
        return self.order.show_order(table_number)

    def clear_order(self, table_number):
        self.order.clear_order(table_number)

