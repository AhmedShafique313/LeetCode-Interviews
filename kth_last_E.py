class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def kthLastElement(head, k):
    fast = slow = head
    for i in range(k):
        if not fast:
            return False
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    return slow

def creating_linkedList(arr):
    if not arr:
        return False
    
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head


array = [10, 20, 30, 40, 50]
k = 2
head = creating_linkedList(array)
result = kthLastElement(head, k)
print(f"The {k}-th last element is:", result.data)