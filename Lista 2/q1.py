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
        self.current_node = None

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
            self.current_node = self.__first

        else:
            parent.right = Node(value)
            parent.right.parent = parent.data

    def check_order(self, value):
        if value < self.current_node.data:
            return self.order

        elif value > self.current_node.data:
            self.order += 1

            if self.current_node.parent == None:
                self.order += 1
                return self.order

            elif value < self.current_node.parent:
                return self.order

            elif value > self.current_node.parent:
                self.current_node = self.current_node.parent
                self.check_order(value)


def main():
    qty_numbers, qty_queries = input().split()
    qty_numbers = int(qty_numbers)
    qty_queries = int(qty_queries)
    print(qty_numbers)
    print(qty_queries)
    tree = BinaryTree()
    numbers_list = input().split()
    for i in range(qty_numbers - 1, -1, -1):
        tree.insert(int(numbers_list[i]))

    for i in range(qty_queries):
        number_to_check = input()
        print(tree.check_order(int(number_to_check)))


if __name__ == "__main__":
    main()
