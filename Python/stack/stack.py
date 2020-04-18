class Node():
    def __init__(self, value):
        self.data = value
        self.link = None



class Stack(Node):
    def __init__(self):
        self.head = None
        self._size = 0


    def push(self, value):
        new_node = Node(value)
        new_node.link = self.head
        self.head = new_node
        self._size += 1
        # print("{} pushed".format(value))


    def pop(self):
        if self.isempty():
            temp = None
        else:
            temp = self.head.data
            self.head = self.head.link
            self._size -= 1
            # temp = "value poped is {}".format(temp)

        return temp

    def peek(self):
        s = "Top --> {}".format(self.head.data)
        return s

    def __str__(self):
        if self.isempty():
            s = "Empty Stack"
        else:
            s = ""
            position = self.head
            while(position != None):
                s += str(position.data)+"\n"
                position = position.link

        return s

    def search(self, value):
        position = self.head
        count = 1
        while(position.link != None):
            if position.data == value:
                return count
            position = position.link
            count += 1
        return 0


    def __len__(self): return self._size


    def isempty(self):
        Flag = False
        if self._size == 0:
            Flag = True

        return Flag
