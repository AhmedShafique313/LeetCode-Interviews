
def creating_stack():
    stack = []
    return stack

def empty_Stack(Stack):
    return len(Stack)==0

def inserting(stack, data):
    stack.append(data)
    print('Pushed item: ' + data)

def remove(stack):
    if(empty_Stack(stack)):
        return 'empty'
    return stack.pop()

stack = creating_stack()
inserting(stack, str(1))
print(str(stack))

    