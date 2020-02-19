class Node:
    def __init__(self, value, link):
        self.data = value
        self.next = link

class LinkedList(Node):
    def __init__(self):
        self.header = None

    def createNode(self, value):
        new_node = Node(value, None)
        if self.header == None:
            self.header = new_node
        else:
            temp = self.header
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
        print("node {} created".format(value))

    def printList(self):
        if(self.header == None):
            print("Empty List")
        else:
            temp = self.header
            while(temp.next != None):
                print("{} ---->".format(temp.data),end="")
                temp = temp.next
        print(temp.data)


mylist = LinkedList()
mylist.createNode(2)
mylist.createNode(3)
mylist.createNode(4)
mylist.createNode(5)
mylist.printList()
