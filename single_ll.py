class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":

    first = Node(1)
    second = Node(2)
    third = Node(3)

    first.next = second
    second.next = third

    current = first
    while current:
        print(current.data, end=" ")
        current = current.next