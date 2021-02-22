class Node:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    def __str__(self):
        return str(self.__data)


class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.__root = node

        else:
            self.__root = None

    def add_left(self, data):
        self.__root.left = Node(data)

    def add_right(self, data):
        self.__root.right = Node(data)

    def root(self):
        return self.__root

    def left_child(self):
        return self.__root.left

    def right_child(self):
        return self.__root.right


if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.add_left(18)
    tree.add_right(14)

    print(tree.root())
    print(tree.left_child())
    print(tree.right_child())
