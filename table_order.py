class Order:
    def __init__(self):
        self.item = []
        self.total_price = 0

    def add_item(self, item, price):
        self.item.append((item, price))

    def remove_item(self, item):
        for i in range(len(self.item)):
            if self.item[i][0] == item:
                self.total_price -= self.item[i][1]
                self.item.pop(i)
                break

    def save_order(self, table_number):
        with open(f'table{table_number}.txt', 'w') as file:
            for item, price in self.item:
                file.write(f'{item}:{price}\n')

    def clear_order(self, table_number):
        with open(f'table{table_number}.txt', 'w'):
            pass

    def show_order(self, table_number):
        print("\nHere's the order:")
        print('------------------')
        with open(f'table{table_number}.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                item, price = line.strip().split(':')
                self.total_price += round(float(price), 3)
                self.item.append((item, price))
            for index, items in enumerate(self.item):
                print(f'{index + 1}| {items[0]:20}: Rp{float(items[1]):.3f}')
        print(f'\nTotal Price: Rp{float(self.total_price):.3f}')
        return self.total_price