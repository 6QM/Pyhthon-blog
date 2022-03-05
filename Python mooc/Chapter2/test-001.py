# l1 = ['ABCD','1234']
#
# l1[0] = 'D'+'C'+'B'+'A'
# print(l1)
# n = (1500*14+850+650+830)*40/1000
# print(n)
#
# n0 = int(input())
# n = abs(n0)
# l = len(str(n))
# print(l)
# while l != 0:
#     m = n
#     n %= 10
#     print(str(n),end="")
#     n = (m-n)//10
#     l -=1
# str = "00123"
# n1 = int(str)
# print(n1+1)
str_1 = 'abccdef'

#将字符串转换为list列表

lst = list(str_1)

#对列表进行反转操作,reverse()返回为None

lst.reverse()

print(''.join(lst))
MaxV = 0
Maxv = max([5,9,50])
print(max([5,9,50,22,100]))