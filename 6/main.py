year = int(input("请输入一个4位年份："))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year}年是闰年。")
else:
    print(f"{year}年不是闰年。")
