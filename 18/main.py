def is_perfect_number(n):
    if n <= 1:
        return 0

    factor_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factor_sum += i
            if i != n // i:
                factor_sum += n // i

    return 1 if factor_sum == n else 0


number = int(input("请输入一个整数："))
result = is_perfect_number(number)

if result == 1:
    print(f"{number}是完数。")
else:
    print(f"{number}不是完数。")
