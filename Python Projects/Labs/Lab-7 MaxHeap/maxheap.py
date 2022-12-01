# minheap.py
class MaxHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        self._heap.append(entry)
        self._upheap(len(self._heap) - 1)

    def _upheap(self, index):

        if index == 0:
            return True

        elif (index - 1) // 2 >= 0:

            if self._heap[(index - 1) // 2] < self._heap[index]:
                self._heap = self._swap(index, (index - 1) // 2, self._heap)

                return self._upheap((index - 1) // 2)
        else:
            return True

    def downheap(self):
        replacement = self._heap[len(self._heap) - 1]
        self._heap[0] = replacement
        self._heap.pop()
        self._rec_downheap(0)

    def get_left_child(self, index):
        child = index * 2 + 1
        if child < len(self._heap):
            return (True, child)
        else:
            return (False, None)

    def get_right_child(self, index):
        child = index * 2 + 2
        if child < len(self._heap):
            return (True, child)
        else:
            return (False, None)

    def _swap(self, index1, index2, _list):
        _list[index1], _list[index2] = _list[index2], _list[index1]
        return _list

    def _rec_downheap(self, index):
        if index < len(self._heap):

            if (
                self.get_right_child(index)[0] and self.get_left_child(index)[0]
            ):  # Two children

                if (
                    self._heap[index] > self._heap[self.get_right_child(index)[1]]
                    and self._heap[index] > self._heap[self.get_left_child(index)[1]]
                ):
                    return
                

                elif (
                    self._heap[self.get_right_child(index)[1]]
                    > self._heap[self.get_left_child(index)[1]]
                ):
                    new_index = self.get_right_child(index)[1]
                    self._heap = self._swap(
                        index, self.get_right_child(index)[1], self._heap
                    )
                    self._rec_downheap(new_index)

                else:
                    new_index = self.get_left_child(index)[1]
                    self._heap = self._swap(
                        index, self.get_left_child(index)[1], self._heap
                    )
                    self._rec_downheap(new_index)

            elif (
                self.get_right_child(index)[0]
                and self.get_left_child(index)[0] == False
            ):  # One Child
                if self._heap[index] > self._heap[self.get_right_child(index)[1]]:
                    return

                elif self._heap[index] < self._heap[self.get_right_child(index)[1]]:
                    new_index = self.get_right_child(index)[1]
                    self._heap = self._swap(
                        self.get_right_child(index)[1], index, self._heap
                    )
                    self._rec_downheap(new_index)

                else:
                    return

            elif (
                self.get_right_child(index)[0] == False
                and self.get_left_child(index)[0]
            ):  # One Child
                if self._heap[index] > self._heap[self.get_left_child(index)[1]]:
                    return

                elif self._heap[index] < self._heap[self.get_left_child(index)[1]]:
                    new_index = self.get_left_child(index)[1]
                    self._heap = self._swap(
                        self.get_left_child(index)[1], index, self._heap
                    )
                    self._rec_downheap(new_index)

                else:
                    return

            elif (
                self.get_right_child(index)[0] == False
                and self.get_left_child(index)[0] == False
            ):  # No children
                return

            else:
                print("you fucked up ur code cam")
        else:
            return

    def count(self):
        return len(self._heap)
    
    def peek(self):
        if len(self._heap)!=0:
            return self._heap[0]
        else:
            return "The Queue is Empty"





