monthDays = [-1,31,28,31,30,31,30,31,31,30,31,30,31]
days = 0
lst = input().split()
year,month,date = int(lst[0]),int(lst[1]),int(lst[2])
for y in range(2012,year):                        #先累加过掉的整年的天数（包含了开始的year在这一年）
    if y %4 == 0 and y %100 != 0 or y%400 == 0 :         #润年366天
        days += 366
    else:
        days += 365
if y%4 == 0 and y%100 != 0 or y%400 == 0:
    monthDays[2] = 29                                  #润年的第2个月是29天（不是28天）
for i in range(1,month):
    days += monthDays[i]                  #再累加year那年过掉的整月的天数
days += date #累加year年month那个月的天数
days -= 22                #最后扣除(减去)2012年当年已经过了的天数（2012年1月22日是星期天）
print(days % 7)          #星期天算一周的第0天

