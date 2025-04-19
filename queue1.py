def creating_queue():
    queue = []
    return queue

def empty_queue(queue):
    return len(queue)==0

def enqueue(queue, data):
    queue.append(data)
    print('Enqueued: ' + data)

def dequeue(queue):
    if empty_queue(queue):
        return 'Empty'
    return queue.pop(0)

def front(queue):
    if empty_queue(queue):
        return "Queue is empty"
    return queue[0]

def display(queue):
    print("Queue:", queue)


queue = creating_queue()

enqueue(queue, 'A')
enqueue(queue, 'B')
enqueue(queue, 'C')

display(queue) 
print("Dequeued:", dequeue(queue))
print("Front item:", front(queue))

display(queue)
