def transfer_one_Stack_to_another(stack):
    temp = []
    while stack:
        temp.append(stack.pop())
    while temp:
        stack.append(temp.pop())
    return stack

l = [0, 1, 3, 5, 2, 4]
print(transfer_one_Stack_to_another(l))
