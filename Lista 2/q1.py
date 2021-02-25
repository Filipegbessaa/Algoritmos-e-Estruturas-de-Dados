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
            self.__first = Node(value)
            self.current_node = self.__first

        else:
            parent.right = Node(value)

    def check_order(self, value, num_nodes):
        order = num_nodes
        current_node = self.__root
        for i in range(num_nodes):
            if value > current_node.data:
                order += 1
                if current_node == self.__root:
                    return order

            elif value < current_node.data:
                current_node = current_node.left
                if current_node.left == None:
                    return 1
                order -= 1
                if value > current_node.left.data:
                    return order


def main():
    qty_numbers, qty_queries = input().split()
    qty_numbers = int(qty_numbers)
    qty_queries = int(qty_queries)
    tree = BinaryTree()
    numbers_list = input().split()
    for i in range(qty_numbers - 1, -1, -1):
        tree.insert(int(numbers_list[i]))

    for i in range(qty_queries):
        number_to_check = input()
        print(tree.check_order(int(number_to_check), qty_numbers))


if __name__ == "__main__":
    main()
