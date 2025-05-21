class Node:
    def __init__(self, table):
        self.table = table
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, table, from_file=False):
        new_table = Node(table)
        self.size += 1
        if self.head is None:
            self.head = new_table
            self.tail = new_table
        else:
            self.tail.next = new_table
            self.tail = new_table
        if not from_file:
            self.append_queue(new_table.table)

    def dequeue(self):
        if self.head is None:
            print('Queue is empty')
            return None
        temp = self.head.table
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        self.save_queue()
        return temp

    def remove_queue(self, table):
        self.load_queue()
        current = self.head
        prev = None
        while current:
            if current.table == int(table):
                if prev is None:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                self.size -= 1
                self.save_queue()
                return
            prev = current
            current = current.next

    def show_queue(self):
        current = self.head
        while current:
            print(f'Table: {current.table}')
            current = current.next
        print()

    def get_size(self):
        return self.size

    def save_queue(self):
        self.clear_queue()
        if self.head is not None:
            with open('queue_status.txt', 'w') as file:
                    current = self.head
                    while current:
                        file.write(str(current.table) + '\n')
                        current = current.next

    def clear_queue(self):
        with open('queue_status.txt', 'w') as file:
            file.write('')

    def save_queue_after_dequeue(self):
        if self.size == 0:
            self.clear_queue()
        else:
            self.save_queue()

    def append_queue(self, table):
        with open('queue_status.txt', 'a') as file:
            file.write(str(table) + '\n')

    def load_queue(self):
        self.head = None
        self.tail = None
        self.size = 0
        with open('queue_status.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.enqueue(int(line.strip()), from_file=True)
        