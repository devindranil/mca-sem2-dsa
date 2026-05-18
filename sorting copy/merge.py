def merge_sort(arr):
    # recursion
    # base case
    if len(arr)<=1:
        return arr
    # find the mid value
    mid=len(arr)//2

    #divide array into two halves
    left=arr[:mid]
    right=arr[mid:]

    #recursively sort both halves
    left=merge_sort(left)
    right=merge_sort(right)

    #merge
    return merge(left,right)

def merge(left,right):
    res=[]
    # pointer for left and right array
    i=0
    j=0

    #compare elements from both arrays
    while i<len(left) and j<len(right):
        # add smaller element into the res array
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    #add remaining elements fromn left array
    while i<len(left):
        res.append(left[i])
        i+=1
    #add remaining elements from right array
    while j<len(right):
        res.append(right[j])
        j+=1
    
    return res

n=[38,27,43,3,9,82,10]
print(n)
sorted=merge_sort(n)
print(sorted)