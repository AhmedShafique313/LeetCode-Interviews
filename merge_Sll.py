class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_sorted_lists(list1, list2):
    dummy = Node(0)
    current = dummy
    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next  # <- You also missed this line in your original code

    # Append the remaining nodes
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next

def creating_linkedlist(arr):
    if not arr:
        return None
    head = Node(arr[0])  # FIXED: Start with the first value of arr
    current = head
    for num in arr[1:]:
        current.next = Node(num)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Test case
list1 = creating_linkedlist([1, 2, 4])
list2 = creating_linkedlist([1, 3, 4])
merged = merge_two_sorted_lists(list1, list2)
print_linked_list(merged)
