n = input().split()
l1 = ["+","-","*","/"]
if int(n[1]) == 0 :
    print("Divided by zero!")
elif not n[2] in l1 :
    print("Invalid operator!")
elif n[2] == l1[0] :
    y = int(n[0])+int(n[1])
    print(y)
elif n[2] == l1[1] :
    y = int(n[0])-int(n[1])
    print(y)
elif n[2] == l1[2] :
    y = int(n[0])*int(n[1])
    print(y)
elif n[2] == l1[3] :
    y = int(n[0])//int(n[1])
    print(y)
