import time
import Sorting

t = open("sample.txt",'r')
ti = t.read().split(",")
array = [int(i) for i in ti]


a = Sorting.bubblesort(array)

print(a)
start_time = time.time()
counter = 1
end_time =time.time()
print("{:f}".format(end_time - start_time))
