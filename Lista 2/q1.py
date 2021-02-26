def binary_search(arr, low, high, x):

    if high >= low:

        mid = (high + low) // 2
        if x < arr[low]:
            return 1

        elif x > arr[high]:
            return high + 2

        elif x < arr[mid] and x > arr[mid - 1]:
            return mid + 1

        elif x > arr[mid] and x < arr[mid + 1]:
            return mid + 2

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert(self, value):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next

            pointer.next = Node(value)
        else:
            self.head = Node(value)
        self._size += 1

    def check_order(self, value):
        pointer = self.head
        order = 1
        while pointer.data:
            if value < pointer.data:
                return order

            elif value > pointer.data:
                order += 1
                if pointer.next:
                    pointer = pointer.next

                else:
                    return order

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next

            else:
                raise IndexError("list index out of range")

        if pointer:
            return pointer.data

        else:
            raise IndexError("list index out of range")


def main():
    qty_numbers, qty_queries = input().split()
    qty_numbers = int(qty_numbers)
    qty_queries = int(qty_queries)
    linked_list = LinkedList()
    numbers_list = input().split()
    for i in range(qty_numbers):
        numbers_list[i] = int(numbers_list[i])

    for i in range(qty_queries):
        number_to_check = input()
        print(binary_search(numbers_list, 0, qty_numbers - 1, int(number_to_check)))


if __name__ == "__main__":
    main()
