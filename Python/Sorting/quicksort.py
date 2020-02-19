def quicksort(A, left, right):
    if left >= right:
        return
    m = partation(A, left, right)
    quicksort(A, left, m-1)
    quicksort(A, m+1, right)

def partation(A, left, right):
    x = A[left]
    j = left

    for i in range(left+1, )
