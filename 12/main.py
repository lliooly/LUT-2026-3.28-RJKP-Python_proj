days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    month = int(input("请输入月份（输入0结束）："))

    if month == 0:
        print("程序结束。")
        break
    if 1 <= month <= 12:
        print(f"{month}月有{days_per_month[month - 1]}天。")
    else:
        print("输入的月份不正确。")
