#for min just implement buildMin heap function to it.
# priority queue can also be use for d-tree(where parent has d-childrens (do if pleases you))
class PriorityQueue():
    def __init__(self):
        self._size = 0
        self.queue  = []

    # we cantnot start from zero index since all our cal are done on index
    # so zero will hault our parent child index calculation
    # my suggestion start with a element at index zero say ($)
    def parent(self, index):return (index-1)//2
    def left(self, index):return (index*2+1)
    def right(self, index):return (2*index)+2

    def shifUp(self, index):
        # valid index check, parent of root node check, is shifting needed check
        while(index > 0 and self.queue[self.parent(index)] < self.queue[index]):
            self.queue[self.parent(index)], self.queue[index] =  self.queue[index], self.queue[self.parent(index)]
            index = self.parent(index)

    def shiftDown(self, index):
        maxIndex = index
        leftIndi = self.left(index)
        if(leftIndi < self._size and self.queue[leftIndi] > self.queue[maxIndex]):
            maxIndex = leftIndi

        rightIndi = self.right(index)
        if(rightIndi < self._size and self.queue[rightIndi] > self.queue[maxIndex]):
            maxIndex = rightIndi

        if index != maxIndex:
            self.queue[maxIndex], self.queue[index] = self.queue[index], self.queue[maxIndex]
            self.shiftDown(maxIndex)

    def add(self, value):
        self.queue.append(value)
        self.shifUp(self._size)
        self._size += 1

    def extractMax(self):
        if self._size > 1:
            result = self.queue[0]
            self.queue[0] = self.queue.pop()
            self._size -= 1
            self.shiftDown(0)

        elif(self._size == 1):
            self._size = 0
            result =  self.queue[0]
            self.queue=[]
        else:
            result =  None

        return result
    def remove(self, index):
        if index >= 0 and index < self._size:
            #method to set infinity in python also can use math or decimal
            self.queue[index] = float('inf')
            self.shifUp(index)
            self.extractMax()

    def changePriority(self, index, priorityValue):
        if index >= 0 and index < self._size:
            oldPriority = self.queue[index]
            self.queue[index] = priorityValue
            if priorityValue > oldPriority:
                self.shifUp(index)
            else:
                self.shiftDown(index)

    def isEmpty(self): return True if self._size == 0 else False

    def __str__(self):
        s = ""
        if(not self.isEmpty()):
            for i in range(self._size):
                s += f"{self.queue[i]} "
        else:
            s = "Empty Queue"
        return s

    def peekMax(self):
        if(not self.isEmpty()):
            return self.queue[0]
        else:
            return "Empty Queue"



if __name__ == "__main__":
    pq = PriorityQueue()
    pq.add(7)
    pq.add(17)
    pq.add(71)
    pq.add(77)
    pq.add(27)
    print(pq)
    print(pq.extractMax())
    print(pq.extractMax())
    print(pq.extractMax())
    print(pq.extractMax())
    # print(pq)
    print(pq.extractMax())
    print(pq.extractMax())
    pq.add(7)
    print(pq.peekMax())
    pq.add(17)
    print(pq)
    pq.remove(0)
    print(pq)
    pq.add(71)
    pq.add(77777)
    print(pq)
    pq.add(27)
    print(pq)
    print(pq.peekMax())
    pq.changePriority(0,32)
    print(pq.peekMax())
    print(pq)
