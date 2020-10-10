class Node():
    def __init__(self,data):
        self.data = data
        self.rlink = None
        self.llink = None

    def getLL(self): return self.llink;
    def getRL(self): return self.rlink;
    def getData(self): return self.data;

    def setLL(self, Node): self.llink = Node
    def setRL(self, Node): self.rlink = Node


class DoublyLL(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def addHead(self, value):
        newNode = Node(value)
        if (self.head == None):
            self.head = newNode
            self.tail = newNode

        else:
            temp = self.head
            self.head = newNode
            newNode.setRL(temp)
            temp.setLL(newNode)
        self._size += 1

    def addTail(self, value):
        if(self.head == None):
            self.addHead(value)
        else:
            newNode = Node(value)
            self.tail.setRL(newNode)
            newNode.setLL(self.tail)
            self.tail = newNode
            self._size += 1

    def deleteHead(self):
        if self.head == None:
            return -1
        elif(self._size == 1):
            self.head = None
            self.tail = None
        else:
            temp = self.head.getRL()
            self.head.setRL(None)
            temp.setLL(None)
            self.head = temp
        self._size -= 1
        return 1

    def deleteTail(self):
        if self.tail == None:
            return -1
        elif(self._size == 1):
            self.head = None
            self.tail = None
        else:
            temp = self.tail.getLL()
            temp.setRL(None)
            self.tail.setLL(None)
            self.tail = temp
        self._size -= 1
        return 1

    def __str__(self):
        s = ""
        mover = self.head
        if(mover == None):
            s = "Empty Linked List"
        else:
            while(mover != None):
                s += f"{mover.getData()} -> "
                mover = mover.getRL()

        return s

    def printReverse(self):
        s = ""
        mover = self.tail
        if(mover == None):
            s = "Empty Linked List"
        else:
            while(mover != None):
                s += f" <- {mover.getData()}"
                mover = mover.getLL()

        print(s)
    def __len__(self): return self._size

    def isEmpty(self): return True if self._size == 0 else False

    def peekHead(self):
        try:
            return self.head.data
        except:
            return None

    def peekTail(self):
        try:
            return self.tail.data
        except:
            return None


if __name__ == "__main__":
    dd = DoublyLL()
    dd.addHead(5)
    dd.addHead(51)
    print(dd)
    dd.printReverse()
    dd.deleteHead()
    print(dd)
    dd.printReverse()
    dd.addHead(52)
    dd.addHead(53)
    dd.addHead(522)
    print(dd)
    dd.printReverse()
    dd.deleteTail()
    dd.deleteTail()
    dd.deleteTail()
    print(len(dd))
    dd.printReverse()


