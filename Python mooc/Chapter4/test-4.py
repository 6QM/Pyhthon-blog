#递归函数（递归调用）-阶乘
# def Factorial(n):
#     if n < 2 :
#         return 1
#     else:
#         return n * Factorial(n-1)
# n = int(input())
# print(Factorial(n))
def f(n,m):

    if n == 0:

        return m

    elif m == 0:

        return n

    else:

        if n >= m:

            return f(m,n-m) + 1

        else:

            return f(n,m-n) + 2

print(f(3,4))