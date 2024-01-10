class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        self.length += 1
        node.prev = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return None

        self.length -= 1
        saved_head = self.head
        self.head = self.head.prev

        saved_head.prev = None
        return saved_head.value

    def peek(self):
        if self.head is not None:
            return self.head.value
        return None
