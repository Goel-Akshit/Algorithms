class queue():
    front = 0
    rear = 0
    queue = []

    def __init__(self,size):
        self.queue = [None]*size

    def enqueue(self,value):
        if self.rear == len(self.queue):
            print("Overflow")
        else:
            self.queue[self.rear] = value
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("underflow")

        else:
            print(self.queue[self.front])
            self.front += 1

    def Front(self):
        print(self.queue[self.front])

    def size(self):
        print(self.rear-self.front)

    def isempty(self):
        if self.rear == self.front:
            return True

        return False
