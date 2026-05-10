pq=[]
def enq(x):
    pq.append(x)

def dq():
    if len(pq)==0:
        print("Queue is empty...")
        return
    #find index of smallest element
    min_index=0
    for i in range(1,len(pq)):
        if pq[i]<pq[min_index]:
            min_index=i
    value=pq[min_index]
    #remove that element
    pq.pop(min_index)
    return value

def dis():
    print("Queue: ",pq)


# function call
enq(40)
enq(50)
enq(20)
dis()
dq()
dis()