q=[] #empty list in python
# enqueue operation
q.append(10)
q.append(20)
q.append(30)
print("Queue after enqueue: ",q)

#dequeue operation
if len(q)>0:
    removed=q.pop(0)
    print("Deque element: ",removed)

print("Queue after dequeue: ",q)
