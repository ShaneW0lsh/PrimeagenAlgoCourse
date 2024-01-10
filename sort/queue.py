class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def print_out(self):
        if self.next is None:
            print(f"value: {self.value}")
        else:
            print(f"value: {self.value}, points to: {self.next.value}")


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, value):
        node = Node(value)
        self.length += 1
        if self.tail is None:
            self.tail = node
            self.head = node
            return

        self.tail.next = node
        self.tail = node

    def pop(self):
        if self.head is None:
            return None

        self.length -= 1
        previous_head = self.head
        self.head = self.head.next

        previous_head.next = None
        if self.length == 0:
            self.tail = None

        return previous_head.value

    def peek(self):
        if self.head is not None:
            return self.head.value
        return None
