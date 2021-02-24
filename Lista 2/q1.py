class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:
    def __init__(self, data=None):
        if data:
            self.__root = Node(data)

        else:
            self.__root = None

        self.__first = None
        self.order = 1
        self.current_node = self.__first

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
            parent.left = Node(value)
            parent.left.parent = parent.data
            self.__first = Node(value)

        else:
            parent.right = Node(value)
            parent.right.parent = parent.data

    def check_order(self, value):
        if value < self.current_node.data:
            return self.order

        elif value > self.current_node.data:
            self.order += 1

            if value < self.current_node.parent:
                return self.order

            elif value > self.current_node.parent:
                self.current_node = self.current_node.parent
                self.check_order(value)
