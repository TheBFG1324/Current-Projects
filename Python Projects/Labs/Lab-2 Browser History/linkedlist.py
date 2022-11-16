'''
Cameron Denton
2981510
9/19/22
last Mod: 9/20/22
Purpose: Creates the linkedList Object
'''
from node import Node

class LinkedList:
    def __init__(self):

        self._front = None
        self._length = 0

 

    def get_entry(self, index):
        if self._length == 0:
            raise IndexError

        elif index >= 0 and index <= (self._length - 1):
            return self._get_node(index)._value

 

        else:
            raise IndexError

 

    def insert(self, index, entry):
        new_node = Node(entry)
        if index >= 0 and index <= self._length:
            if index == 0:
                new_node._next = self._front
                self._front = new_node
                self._length += 1
                
            else:

                left_node = self._get_node(index - 1)
                new_node._next = left_node._next
                left_node._next = new_node
                self._length += 1

        else:
            raise IndexError

 

    def remove(self, index):
        if index >= 0 and index <= self._length-1:
            if index == 0:
                temp = self._front._value
                self._front = self._front._next
                self._length -= 1
                return temp

            else:
                left_node = self._get_node(index-1)
                remove_node = self._get_node(index)
                temp = remove_node
                left_node._next = temp._next
                self._length -= 1

                return temp._value


 

        else:
            raise IndexError

 

 

    def _get_node(self, index):
        jumper = self._front
        for i in range(index):
            jumper = jumper._next

        return jumper

    def length(self):
        return self._length

    def clear(self):
        self._front=None
        self._length=0


