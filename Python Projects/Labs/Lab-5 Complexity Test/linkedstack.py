from node import Node


class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def is_empty(self):
        return self.top == None

    def pop(self):
        if self.is_empty() == False:
            popped_value = self.top.value
            self.top = self.top.next
            return popped_value

        else:
            raise RuntimeError("Error empty stack")

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Error empty stack")
        else:
            return self.top.value
