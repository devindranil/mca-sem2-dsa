size=5
q=[None]*size #list -> array
front= -1
rear= -1

#enq operation
def enq(x):
    global front,rear
    #check if queue is full or not
    if (rear+1)%size==front:
        print("Queue is full..")
    #first element insertion
    elif front==-1:
        front=rear=0
        q[rear]=x
    #remaining element
    else:
        rear=(rear+1)%size
        q[rear]=x

#deq operation
def deq():
    global front,rear
    if front== -1:
        print("Queue is empty....")
        return
    removed=q[front]
    #if only one element
    if front==rear:
        front=rear-1
    else:
        front=(front+1)%size
    return removed

#display queue
def dis():
    if front==-1:
        print("Queue is empty....")
    #traversal
    i=front
    while True:
        print(q[i],end=" ")
        if i==rear:
            break
        i=(i+1)%size
    print()

#function call
enq(10)
enq(20)
enq(30)
enq(40)
enq(50)
dis()
print("Dequeue: ",deq())
print("Dequeue: ",deq())
dis()
enq(60)
dis()
