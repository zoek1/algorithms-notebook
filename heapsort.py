from math import floor
# asa
iParent = lambda i: floor((i-1/2))
iLeftChild = lambda i: floor((i-1/2)) + 1
iRightChild = lambda i: floor((i-1/2)) + 2

def heapify(a, count):
    start = iParent(count-1)
    
    while start >= 0:
        siftDown(a, start, count-1)
        start -= 1
        
def siftDown(a, start, end):
    root = start
    
    while iLeftChild(root) <= end:
        child = iLeftChild(root)
        swap = root
        
        if a[swap] <= a[child]:
            swap = child
            
        if child + 1 <= end and a[swap] < a[child + 1]:
            swap = child + 1
            
        if swap == root:
            return
        else:
            temp = a[root]
            a[root] = a[swap]
            a[swap] = temp
            root = swap

def heapSort(a, count):
    heapify(a, count)
    end = count - 1
    
    while end > 0:
        temp = a[end]
        a[end] = a[0]
        a[0] = temp
        
        end -= 1
        
        siftDown(a, 0, end)
        
    return a
        
a = [1,2,43,66,3,64,56,356]
result = heapSort(a, len(a))
assert result == [1, 2, 3, 43, 56, 64, 66, 356]
print(result)