year = int(input())
if year <= 0 :
    print("Illegal year")
else :
    print("Legal year.")
    if year > 1949 and (year - 1949 ) % 10 == 0 : #建国十周年
        print("Luck year.")
    elif year > 1921 and not ((year - 1921 ) % 10 ) : #建党十周年
        print("Good year.")
    elif year % 4 == 0 and year % 100 or year % 400 == 0 : #普通闰年与世纪闰年的判断
        print("Leap year.")
    else :
        print("Common year")
