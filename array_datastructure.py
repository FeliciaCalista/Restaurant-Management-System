class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def append(self, item):
        if self.size == self.capacity:
            self.resize(self.capacity + 1)
        self.array[self.size] = item
        self.size += 1

    def resize(self, new_capacity):
        new_arr = [None]*new_capacity
        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr
        self.capacity = new_capacity

    def enumerate(self):
        for i in range(self.size):
            yield i, self.array[i]

    def pop(self, item):
        if item < 0 or item > len(self.array):
            print('Index out of range')
        else:
            for i in range(item, len(self.array) - 1):
                self.array[i] = self.array[i + 1]
            print('Item has been removed')

    def count(self, item):
        count = 0
        for i in self.array:
            if i == item:
                count += 1
        return count

    def len(self):
        return self.size

    def get_item(self, item_number):
        if item_number < self.len():
            return self.array[item_number]
