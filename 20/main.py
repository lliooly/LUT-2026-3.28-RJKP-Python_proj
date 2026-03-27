def m(i):
    if i == 1:
        return 1 / 3
    return m(i - 1) + i / (2 * i + 1)


n = int(input("请输入整数i："))
if n >= 1:
    print(f"m({n}) = {m(n):.6f}")
else:
    print("请输入大于等于1的整数。")
