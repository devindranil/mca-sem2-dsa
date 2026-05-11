def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high
    while True:
        while i<=j and arr[i]<=pivot:
            i=i+1
        while i<=j and arr[j]>pivot:
            j=j-1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
            print("Swapped:",arr)
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    print("Pivot Swapped: ",arr)
    return j

def quick_sort(arr,low,high):
    if low<high:
        pivot_index=partition(arr,low,high)
        quick_sort(arr,low,pivot_index-1) #left side
        quick_sort(arr,pivot_index+1,high) #right side

n=[10,7,8,9,1,5]
print(n)
quick_sort(n,0,len(n)-1)
print(n)