#process.py
from linkedstack import LinkedStack
from function import Function
class Process:
    def __init__(self):
        self.stack=LinkedStack()
        self.stack.push("main")
        self.name=""

    def process_push(self, _function):
        self.stack.push(_function)

    def process_pop(self):
        return (self.stack.pop())

    def __str__(self):
        return self.name
    
        
