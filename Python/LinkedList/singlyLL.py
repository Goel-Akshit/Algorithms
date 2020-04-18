class Node():
    def __init__(self, value):
        self.data = value
        self.rlink = None


class MySinglyLL(Node):
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0  #PEP8 says use underscore to tell end user about non_public_variables.


    def insert_at_head(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.rlink = self.head
            self.head = new_node
        self._size += 1


    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node

        else:
            self.tail.rlink = new_node
        self.tail = new_node
        self._size += 1


    def insert_at(self, value, position):
        if position > self._size:
            self.insert_at_tail(value)
        elif position == 1 or position == 0:
            self.insert_at_head(value)
        else:
            counter = 1
            pointer = self.head
            while(counter != position-1):
                pointer = pointer.rlink
                counter += 1
            new_node = Node(value)
            new_node.rlink = pointer.rlink
            pointer.rlink = new_node
            self._size += 1


    def insert(self, iterable):
        if len(iterable) < 1:
            print("Empty List can not be inserted")
            return

        for element in iterable:
            self.insert_at_tail(element)


# override print fuction
# imp this function must return a string and should not just print and return nothing.
    def __str__(self, reverse=False):
        if self._size == 0:
            s = "Empty Linked-List"
        else:
            s = ""
            temp = self.head
            while(temp.rlink != None):
                s += "{} -> ".format(temp.data)
                temp = temp.rlink
            s += str(temp.data)
        return s


    def reverse(self):
        new_ll = MySinglyLL()
        temp = self.head
        while(temp.rlink != None):
            new_ll.insert_at_head(temp.data)
            temp = temp.rlink
        new_ll.insert_at_head(temp.data)
        return new_ll

#underscore signifies no direct use from the main body of this variable.
    def __len__(self):return self._size


# return where head and tail are pointing.
    def Head(self): return self.head.data
    def Tail(self): return self.tail.data


    def delete_at_head(self):
        if self.head == None:
            print("Empty List. Element can't be deleted")
        else:
            self.head = self.head.rlink
            self._size -= 1


    def delete_at_tail(self):
        if self.tail == None:
            print("Empty list. can't delete")
        else:
            pointer = self.head
            while(pointer.rlink != self.tail):
                pointer = pointer.rlink
            self.tail = pointer
            pointer.rlink = None
            self._size -= 1


    def delete_at(self, position):
        if position >= self._size:
            self.delete_at_tail()
        elif position == 1 or position == 0:
            self.delete_at_head()
        else:
            counter = 1
            pointer = self.head
            while(counter != position-1):
                pointer = pointer.rlink
                counter += 1
            pointer.rlink = pointer.rlink.rlink
            self._size -= 1


    def delete(self, value):
        delet_flag = False
        if self.head == None:
            print("Cant delete from an Empty list")

        elif self.head.data == value:
            self.delete_at_head()
        elif self.tail.data == value:
            self.delete_at_tail()
        else:
            value_matcher = self.head
            previous_pointer = self.head
            while(value_matcher.rlink != None):
                if value_matcher.data == value:
                    previous_pointer.rlink = value_matcher.rlink
                    delet_flag = True
                    break
                previous_pointer = value_matcher
                value_matcher = value_matcher.rlink
            if delet_flag:
                self._size -= 1
            else:
                print("Element Doesn't exit")


    def sort(self):
        new_node = MySinglyLL()
        element = self.head
        new_node.insert_at_head(element.data)
        element = element.rlink
        count = 1
        while(count < len(self)):
            if element.data > new_node.head.data and element.data < new_node.tail.data:
                new_node_position = new_node.head
                counter = 1
                while(element.data > new_node_position.data):
                    new_node_position = new_node_position.rlink
                    counter += 1
                new_node.insert_at(element.data, counter)
            elif(element.data <= new_node.head.data):
                new_node.insert_at_head(element.data)
            else:
                new_node.insert_at_tail(element.data)

            element = element.rlink
            count += 1
        return new_node






















