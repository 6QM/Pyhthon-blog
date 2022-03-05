# 三角形三边的关系：两边之和大于第三边,两边之差小于第三边。 定义：在一个平面内,不在同一直线上的三条线段首尾相连组成的图形。
line = input().split()
l1,l2,l3 = float(line[0]),float(line[1]),float(line[2])
if (l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1) and (l1 - l2 < l3 and l3 - l1 < l2 and l2 - l3 <= l1) :
    print("yes")
else :
    print("no")