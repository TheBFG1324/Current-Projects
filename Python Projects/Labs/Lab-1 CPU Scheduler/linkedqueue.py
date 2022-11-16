#Queue
from node import Node

class LinkedQueue:
    def __init__(self):
        self._front=None
        self._back=None
        

    def is_empty(self):
        return self._front==None
    
    def enqueue(self, value):
        new_node=Node(value)
        if self.is_empty():
            self._front=new_node
            self._back=new_node

        else:
            self._back.next=new_node
            self._back=new_node

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Error empty queue")

        if self._front==self._back:
            pop_value=self._front.value
            self._front=None
            self._back=None
            return pop_value
            
        else:
            new_top=self._front.next
            pop_value=self._front.value
            self._front=new_top
            return pop_value

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Error empty queue")
        else:
            return self._front.value
        
        
        

    
