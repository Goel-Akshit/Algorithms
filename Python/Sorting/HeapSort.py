# priority queue and heap sort are both implemented using the principle of heap
# we can use priority queue as a abstract data type to implement heap sort but that will lead to a space compexity of O(n)
# so to avoid extra space complexity and maintain in-place property we implement heap sort using binary heap DS.
# some key properties to focus on
#1. elements at leaf not to be checked
#2. right most index of the tree where to start changing is always floor(n//2) in binary heap tree
#3. no of elements at leaf <= all elemnts above leaf -1 (vice-versa)

def heapSort(array):
    size = len(array)
    if( size > 1):
        #building the heap for the binary heap property
        buildHeap(array)
        while(size):
            array[size-1],array[0] = array[0], array[size-1]
            size -= 1
            shiftDown(array, 0,size)
        return array
    else:
        return array

def buildHeap(array):
    #we cannot use zero index as it can't help in using index property to calculate left child and right child so always
    #buff a known value at the index 0 or maintain the size in the implementation.
    # len-2 because -1 fr o indexing and -1 for elements index  = len-1
    for index in range((len(array)-2)//2, -1, -1):
        shiftDown(array, index,len(array))

def shiftDown(queue, index, size):
    _size = size
    maxIndex = index
    leftIndi = left(index)
    if(leftIndi < _size and queue[leftIndi] > queue[maxIndex]):
        maxIndex = leftIndi

    rightIndi = right(index)
    if(rightIndi < _size and queue[rightIndi] > queue[maxIndex]):
        maxIndex = rightIndi

    if index != maxIndex:
        queue[maxIndex], queue[index] = queue[index], queue[maxIndex]
        shiftDown(queue, maxIndex,_size)

def parent(index):return index//2 if index%2 != 0 else (index//2)-1
def left(index):return (index*2)+1
def right(index):return (2*index)+2


if __name__ == "__main__":
    a = [7,8,9,3,2,1,1,2,3,4,5,6,7,8,9,0,753]
    print(heapSort(a))
