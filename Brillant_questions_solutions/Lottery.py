# Problem Description
# Task. You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
# each point, the number of segments that contain this point.
# Input Format. The first line contains two non-negative integers 𝑠 and 𝑝 defining the number of segments
# and the number of points on a line, respectively. The next 𝑠 lines contain two integers 𝑎𝑖
# , 𝑏𝑖 defining
# the 𝑖-th segment [𝑎𝑖
# , 𝑏𝑖
# ]. The next line contains 𝑝 integers defining points 𝑥1, 𝑥2, . . . , 𝑥𝑝.
# Constraints. 1 ≤ 𝑠, 𝑝 ≤ 50000; −108 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 108
# for all 0 ≤ 𝑖 < 𝑠; −108 ≤ 𝑥𝑗 ≤ 108
# for all 0 ≤ 𝑗 < 𝑝.
# Output Format. Output 𝑝 non-negative integers 𝑘0, 𝑘1, . . . , 𝑘𝑝−1 where 𝑘𝑖
# is the number of segments which
# contain 𝑥𝑖
# . More formally,
# 𝑘𝑖 = |{𝑗 : 𝑎𝑗 ≤ 𝑥𝑖 ≤ 𝑏𝑗}| .
# Input:
# 3 2
# 0 5
# -3 2
# 7 10
# 1 6
# Output:
# 2 0


master_list = list()
s, p = [int(i) for i in input().split()]

for i in range(s):
    a, b = [int(i) for i in input().split()]
    master_list.append((a,'l'))
    master_list.append((b,'r'))

points = input().split()
for i in points:
    master_list.append((int(i),'p'))

master_list.sort()

segment_count = 0
point_segment_map = dict()
for i in master_list:
    if i[1] == 'l': segment_count += 1
    elif i[1] == 'r': segment_count -= 1
    else:
        point_segment_map[i[0]] = segment_count #dic is use to keep record for more than one segment crossing

temp = ''
for i in points:
    temp += str(point_segment_map[int(i)]) + ' '
print(temp[:-1])
