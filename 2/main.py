num = int(input("请输入一个三位整数："))

if 100 <= num <= 999:
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    reversed_num = 100 * c + 10 * b + a
    print(f"这个三位数的反序数为：{reversed_num}")
else:
    print("输入的不是三位整数。")
