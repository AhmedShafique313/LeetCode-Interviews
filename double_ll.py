class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    third = Node(3)

    first.next = second
    second.prev = first
    second.next = third
    third.prev = second

    print('forward: ', end=" ")
    current = first
    while current:
        print(current.data, end=" ")
        last = current
        current = current.next
    print()

    print('reverse: ', end=' ')
    current = last
    while current:
        print(current.data, end=" ")
        current = current.prev