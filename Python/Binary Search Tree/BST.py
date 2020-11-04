#BST DS helps to perform insertion, Deletion, Search in O(logn). only if its basic property is maintain.
# to maintain its basic property and keep the time complexity of all operation caped at O(logn) one need to keep it balance
#one of the approaches to keep it balance is AVL implementation of BST.
#so this is a AVL implementation of BST that keeps our operation cost at O(Logn)
import random

class Node():
    def __init__(self, val):
        self.data = val
        self.root = None
        self.left = None
        self.right = None
        self.height = 0

    def getRoot(self): return self.root
    def getLeft(self): return self.left
    def getRight(self): return self.right
    def getValue(self): return self.data
    def getHeight(self): return self.height

    def setRoot(self, Node): self.root = Node
    def setLeft(self, Node): self.left = Node
    def setRight(self, Node): self.right = Node
    def setHeight(self, height): self.height = height
    def setValue(self, value): self.data = value

class BST(Node):

    def __init__(self):
        self.parentNode = None

    def getParentNode(self): return self.parentNode

    def getHeightDifference(self,node):
        if(node):
            l = node.getLeft()
            r = node.getRight()
            if(l and r):
                return abs(l.getHeight()-r.getHeight())
            elif(l):
                return l.getHeight()
            elif(r):
                return r.getHeight()
            else:
                return 1
        return 0

    def updateHeight(self, node):
        while(node != None):
            l = node.getLeft()
            r = node.getRight()
            if(l and r):
                if(self.getHeightDifference(node) > 1):
                    self.rotate(node)
                    return
                else:
                    h = 1+ max(l.getHeight(), r.getHeight())
            elif(l):
                if(l.getHeight() > 1):
                    self.rotate(node)
                    return
                else:
                    h = 1+ l.getHeight()
            elif(r):
                if(r.getHeight() > 1):
                    self.rotate(node)
                    return
                else:
                    h = 1+ r.getHeight()
            else:
                h = 1
            node.setHeight(h)
            node = node.getRoot()

    def LR(self, z):
        #w, x, y, z, root
        y = z.getLeft()
        x = y.getRight()

        #rotate at y, x becomes z' left child
        z.setLeft(x)
        x.setRoot(z)

        # x's left child becames right child  of y
        if x.getLeft():
            x.getLeft().setRoot(y)
        y.setRight(x.getLeft())
        #y becomes left child of x
        y.setRoot(x)
        x.setLeft(y)

        self.updateHeight(y)

    def RL(self, z):
        # w, x,y,z
        y = z.getRight()
        x = y.getLeft()

        #rotation at y , x becomes z's right child
        z.setRight(x)
        x.setRoot(z)

        #  x's right child beomes y's left child
        if x.getRight():
            x.getRight().setRoot(y)
        y.setLeft(x.getRight())

        # y becomes x's right child
        y.setRoot(x)
        x.setRight(y)

        self.updateHeight(y)

    def RR(self, z):
        # w, x, y, z , root
        # rotate at z
        # y ka root = root and root left = y

        root = z.getRoot()
        y = z.getRight()
        y.setRoot(root)

        if self.parentNode == z:
            self.parentNode = y

        if root:
            if root.getLeft() == z:
                root.setLeft(y)

            elif root.getRight() == z:
                root.setRight(y)

        z.setRoot(y)

        # y ka right z ka left
        if y.getLeft():
            y.getLeft().setRoot(z)
        z.setRight(y.getLeft())

        # z y ka right
        y.setLeft(z)

        #update height
        self.updateHeight(z)

    def LL(self, z):
        # w, x, y, z , root
        # rotate at z
        # y ka root = root and root left = y

        root = z.getRoot()
        y = z.getLeft()
        y.setRoot(root)
        if self.parentNode == z:
            self.parentNode = y

        if root:
            if root.getLeft() == z:
                root.setLeft(y)

            elif root.getRight() == z:
                root.setRight(y)

        z.setRoot(y)
        # y ka right z ka left
        z.setLeft(y.getRight())
        if y.getRight():
            y.getRight().setRoot(z)
        # z y ka right
        y.setRight(z)

        #update height
        self.updateHeight(z)

    def printNode(self, node):
        if node:
            print(f" {node.getValue()} root : {node.getRoot().getValue() if node.getRoot() else None} left: {node.getLeft().getValue() if node.getLeft() else None} right : {node.getRight().getValue() if node.getRight() else None} value: {node.getValue()} height: {node.getHeight()}")
        else:
            print("None")

    def findRotation(self, l, r, pathTracker):
        if(l and r):
            if l.getHeight() > r.getHeight():
                pathTracker += '0'
            else:
                pathTracker += '1'
        elif l:
            pathTracker += '0'
        elif r:
            pathTracker += '1'

        return pathTracker

    def rotate(self, node):
        # LL - 00, LR-01, RL-10, RR-11
        pathTracker = ""
        l = node.getLeft()
        r = node.getRight()
        pathTracker = self.findRotation(l, r, pathTracker)

        if pathTracker == "0":
            pathTracker = self.findRotation(l.getLeft(), l.getRight(), pathTracker)

        elif pathTracker == "1":
            pathTracker = self.findRotation(r.getLeft(), r.getRight(), pathTracker)

        if pathTracker == '00':
            self.LL(node)
        elif pathTracker == '01':
            self.LR(node)
        elif pathTracker == '10':
            self.RL(node)
        elif pathTracker == '11':
            self.RR(node)

    # just to check if there is a node corresponding to the desired value
    def find(self, rootNode, value):
        if rootNode:
            if rootNode.getValue() == value:
                return rootNode
            elif rootNode.getValue() < value:
                return self.find(rootNode.getRight(), value)
            else:
                return self.find(rootNode.getLeft(), value)

        return -1

    # function to see if there is a value against desired  value else return node where it can be
    def findModified(self, rootNode, value):
        if rootNode:
            if rootNode.getValue() == value:
                return rootNode

            elif rootNode.getValue() < value:
                if rootNode.getRight() != None:
                    return self.findModified(rootNode.getRight(), value)
                return rootNode
            else:
                if rootNode.getLeft() != None:
                    return self.findModified(rootNode.getLeft(), value)
                return rootNode

        return -1

    def addNode(self,val):
        #where to place
        placeHolder = self.findModified(self.parentNode, val)
        newNode = Node(val)
        if placeHolder == -1:
            self.parentNode = newNode
            newNode.setRoot(None)
            newNode.setHeight(1)

        else:
            #placeHolder's right
            if placeHolder.getValue() < val:
                placeHolder.setRight(newNode)

            #placeHolder's left
            elif placeHolder.getValue() > val:
                placeHolder.setLeft(newNode)

            #update root
            newNode.setRoot(placeHolder)

            #update height
            self.updateHeight(newNode)

    #returns the next bigger number
    def next(self, rootNode):
        if(rootNode != None):
            if rootNode.getRight() != None:
                return self.leftDescendant(rootNode.getRight())
            else:
                return self.rightAnsector(rootNode.getRoot())

        else:
            return -1

    # range method will always return list in ascending order because of use of next method for finding next element
    def range(self, x, y):
        listi = []
        lowerRoot = self.findModified(self.parentNode, x)
        while lowerRoot != None and lowerRoot.getValue() <= y :
            if lowerRoot.getValue() >= x:
                listi.append(lowerRoot.getValue())

            lowerRoot = self.next(lowerRoot)
        return listi

    def leftDescendant(self, rootNode):
        if rootNode.getLeft() == None:
            return rootNode
        else:
            return self.leftDescendant(rootNode.getLeft())

    def rightAnsector(self, rootNode):
        if rootNode.getRoot() != None:
            if rootNode.getValue() < rootNode.getRoot().getValue():
                return rootNode.getRoot()
            else:
                return self.rightAnsector(rootNode.getRoot())

    # returns 1 smaller
    def previous(self, rootNode):
        if rootNode.getLeft() == None:
            return rootNode
        else:
            return self.rightAnsector(rootNode.getRight())

    def delete(self, value):
        targetNode = self.find(self.parentNode, value)
        if targetNode != -1:
            # case 1:  both child are present or right child is present
            if targetNode.getRight():
                switchNode = self.leftDescendant(targetNode.getRight())
                temp = targetNode.getValue()
                targetNode.setValue(switchNode.getValue())
                switchNode.setValue(temp)
                if switchNode.getRight():
                    switchNode.getRight().setRoot(switchNode.getRoot())
                    switchNode.getRoot().setLeft(switchNode.getRight())

            # case 2 only left child is present
            elif targetNode.getLeft():
                targetNode.getRoot().s

            # case 3 leaf node

    #dfs- traversal
    def inOrder(self, node):

        if node == None:
            return

        if node.getLeft():
            self.inOrder(node.getLeft())

        print(f"value: {node.getValue()} height : {node.getHeight()}")

        if node.getRight():
            self.inOrder(node.getRight())

    def preOrder(self, node):
        if node == None:
            return
        print(f"value: {node.getValue()} height : {node.getHeight()}")
        if node.getLeft():
            self.preOrder(node.getLeft())
        if node.getRight():
            self.preOrder(node.getRight())

    def postOrder(self, node):
        if node == None:
            return
        if node.getLeft():
            self.postOrder(node.getLeft())
        if node.getRight():
            self.postOrder(node.getRight())
        print(f"value: {node.getValue()} height : {node.getHeight()}")

    #bfs-traversal

def printNode(temp):
    if temp == -1:
        print("False")
    else:
        print(f"Left: {temp.getLeft()}  Value: {temp.getValue()}  Right: {temp.getRight()}  ")

if __name__ == "__main__":
    bst = BST()
    my_list = list(range(1,25))
    random.shuffle(my_list)
    # /prin    t my_list # <- List of unique random numbers

    for i in my_list:
        print(i)
        bst.addNode(i)

    print("=======================================================")
    bst.inOrder(bst.getParentNode())
    # print("=======================================")
    # bst.preOrder(bst.getParentNode())
    # print("=======================================")
    # bst.postOrder(bst.getParentNode())
    # bst.addNode(12)
    # bst.addNode(9)
    # bst.addNode(5)
    # bst.addNode(10)
    # bst.addNode(7)
    # print(bst.range(0,500))







