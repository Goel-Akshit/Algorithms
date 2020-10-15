# step 1 create individual nodes and makethem there own parent array - parent(keeps record of parent)
# step 2 maintain a rank record to know which tree to join with which tree array- rank(keeps record of ranks)
# step 3 implement path compression in find method for faster procedding operations. uses parents array for root reteraval and updation.
# operations - add, union, find
# implementation - array - or linked list
# implementation works for unique values so if u are passing repeated values modify at algo design step only. using some hashing or anything

class DisjointSet():
    def __init__(self):
        # master can be thought as a n-dimensional hash table having nodes and its rank and parents.
        self.master = {}

    # value is its own parent and rank stands at 0
    def add(self, val):
        self.master[val] = [val, 0]

    # updates parent on the basis of rank comparison
    def union(self, val1, val2):
        while self.master[val1][0] != val1:
            val1 = self.master[val1][0]

        while self.master[val2][0] != val2:
            val2 = self.master[val2][0]

        rankParent1 = self.master[val1][1]
        rankParent2 = self.master[val2][1]

        if val1 != val2:
            if rankParent1 < rankParent2:
                self.master[val1][0] = self.master[val2][0]

            elif rankParent1 > rankParent2:
                self.master[val2][0] = self.master[val1][0]
            else:
                if val1 < val2:
                    self.master[val2][0] = self.master[val1][0]
                    self.master[val1][1] += 1
                else:
                    self.master[val1][0] = self.master[val2][0]
                    self.master[val2][1] += 1

    # 1st find the root to the parent
    # 2nd attach all those sub roots to the parent directly for faster find next time.(some hat like caching)
    def find(self, val):
        pathRootNodes = []
        while self.master[val][0] != val:
            pathRootNodes.append(val)
            val = self.master[val][0]

        for i in pathRootNodes:
            self.master[i][0] = val
            self.master[i][1] = 0

        return val

    def __str__(self):
        s = ""
        for i in self.master:
            s += f"{i} :{self.master[i]}\n"

        return s

if __name__ == "__main__":
    ds = DisjointSet()
    for i in range(1,65):
        ds.add(i)
    for i in range(1,32):
        ds.union(i, i*2)

    ds.union(8, 3)
    # print(ds)
    print(ds.find(12))
    print(ds)
    # for i in range(10):
    #     ds.union(i, i*3)

    # print(ds)

    # for i in range(10):
    #     ds.union(i, i*2)

    # print(ds)
    # print(ds.find(5))
    # print(ds.find(15))
    # print(ds.find(7))
    # print(ds.find(4))
    # print(ds.find(2))
    # print(ds.find(11))








