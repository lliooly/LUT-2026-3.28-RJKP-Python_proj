def digit_sum(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total


number = int(input("请输入一个正整数："))
print(f"{number}各位数字之和为：{digit_sum(number)}")
