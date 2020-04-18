from singlyLL import MySinglyLL

ll = MySinglyLL()

ll.insert_at_head(9568456)
print("head --> {} ".format(ll.Head()))
print("tail --> {} ".format(ll.Tail()))

ll.insert_at_tail(1)
print("head --> {} ".format(ll.Head()))
print("tail --> {} ".format(ll.Tail()))

ll.insert_at(309,2)
print(ll)

ll.insert((5,78,4545,3,19,6))
print(ll)

print(ll.sort())

ll.delete_at_head()
ll.delete_at_tail()
print(ll)
ll.delete_at(3)
print(ll)
ll.delete(4545)
print(ll)

print(ll.reverse())
