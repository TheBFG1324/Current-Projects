class Node:
    def __init__(self, entry):
        self.value = entry
        self.next = None

    def __str__(self):
        return self._value
