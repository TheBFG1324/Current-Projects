from bnode import BNode
from executive import Executive
from poke import Poke


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def _rec_add(self, _object, current):
        if self._root == None:
            self._root = _object

        elif current.entry < _object.entry and current.right == None:
            current.right = _object

        elif current.entry > _object.entry and current.left == None:
            current.left = _object

        elif current.entry < _object.entry:
            self._rec_add(_object, current.right)

        elif current.entry > _object.entry:
            self._rec_add(_object, current.left)

        elif current.entry == _object.entry:
            raise IndexError("Already in The Binary Tree")

    def add(self, _object):
        new_node = BNode(_object)
        self._rec_add(new_node, self._root)

    def search(self, _object):
        return self._rec_search(_object, self._root)

    def _rec_search(self, _id, current):
        if self._root == None:
            return "It is not in the Tree"

        elif current == None:
            return "It is not in the Tree"

        elif current.entry == _id:
            return current.entry

        elif current.left == None and current.right == None:
            return "It is not in the Tree"

        elif current.entry < _id:
            return self._rec_search(_id, current.right)

        else:
            return self._rec_search(_id, current.left)

    def preOrder(self):
        self._rec_preorder(self._root)

    def _rec_preorder(self, current):
        print(current.entry)
        if current.left != None:
            self._rec_preorder(current.left)
        if current.right != None:
            self._rec_preorder(current.right)

    def inOrder(self):
        self._rec_inorder(self._root)

    def _rec_inorder(self, current):
        if current.left != None:
            self._rec_inorder(current.left)

        print(current.entry)

        if current.right != None:
            self._rec_inorder(current.right)

    def postOrder(self):
        self._rec_postorder(self._root)

    def _rec_postorder(self, current):
        if current.left != None:
            self._rec_postorder(current.left)

        if current.right != None:
            self._rec_postorder(current.right)

        print(current.entry)

    def find_min_in_right(self, current, prev):
        if current.left == None:

            if current.right != None:
                return (current, prev)

            else:
                return (current, None, prev)
        else:
            return self.find_min_in_right(current.left, current)

    def remove(self, _id):
        self._rec_remove(_id, self._root, None)

    def id_is_root(self, _id):
        if self._root.entry == _id:
            if self._root.left == None and self._root.right == None:
                self._root = None
            elif self._root.left == None and self._root.right != None:
                temp = self._root.right
                self._root = temp
            elif self._root.left != None and self._root.right == None:
                temp = self._root.left
                self._root = temp
            elif self._root.left != None and self._root.right != None:
                _replacement = self.find_min_in_right(self._root.right, None)[0]

                if self.find_min_in_right(self._root.right, None)[1] == None:
                    self.find_min_in_right(self._root.right, None)[2].left = None

                else:
                    self.find_min_in_right(self._root.right, None)[
                        1
                    ].left = _replacement.right  # here

                temp_left = self._root.left
                temp_right = self._root.right
                _replacement.left = temp_left
                _replacement.right = temp_right
                self._root = _replacement

    def _rec_remove(self, _id, current, prev):
        if self._root.entry == _id:
            self.id_is_root(_id)

        elif current.entry == _id:

            if current.left == None and current.right == None:  # No children
                if prev.entry > current.entry:
                    prev.left = None

                else:
                    prev.right = None

            elif current.left == None and current.right != None:  # One child
                if current.entry > prev.entry:
                    prev.right = current.right
                else:
                    prev.left = current.right

            elif current.left != None and current.right == None:  # One child
                if current.entry > prev.entry:
                    prev.right = current.left
                else:
                    prev.left = current.left

            elif current.left != None and current.right != None:  # two children
                replacement = self.find_min_in_right(current.right, None)[0]

                if current.right.entry == replacement.entry:  
                    new_left = current.left
                    replacement.left = new_left

                elif self.find_min_in_right(current.right, None)[1] == None:
                    self.find_min_in_right(current.right, None)[2].left = None

                elif self.find_min_in_right(current.right, None)[1] != None:

                    if (self.find_min_in_right(current.right, None)[1].entry> replacement.right.entry):
                        self.find_min_in_right(current.right, None)[1].left = replacement.right  

                if current.right.entry != replacement.entry:
                    new_left = current.left
                    new_right = current.right
                    replacement.left = new_left
                    replacement.right = new_right

                if current.entry < prev.entry:
                    prev.left = replacement

                else:
                    prev.right = replacement

        elif current.entry < _id:
            self._rec_remove(_id, current.right, current)

        else:
            self._rec_remove(_id, current.left, current)

    def copy(self):
        _copy = BinarySearchTree()
        return self._rec_copy(self._root, _copy)

    def _rec_copy(self, current, copy):
        object = current.entry
        copy.add(object)
        if current.left != None:
            self._rec_copy(current.left, copy)
        if current.right != None:
            self._rec_copy(current.right, copy)
        return copy
