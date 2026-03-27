result = 0

for i in range(1, 50, 2):
    result += i * (i + 1) * (i + 2)

print(f"1×2×3+3×4×5+...+49×50×51的值为：{result}")
