class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data=None):
        if data:
            self.__root = Node(data)

        else:
            self.__root = None

    def insert(self, value):
        parent = None
        x = self.__root
        while x:
            parent = x
            if value < x.data:
                x = x.left

            elif value > x.data:
                x = x.right

        if parent is None:
            self.__root = Node(value)

        elif value < parent.data:
            parent.left = value

        else:
            parent.right = value
