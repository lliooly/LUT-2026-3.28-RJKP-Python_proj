days = 365
up_value = 1
down_value = 1

for _ in range(days):
    up_value *= 1.01
    down_value *= 0.99

print(f"一年后每天练功的武力值为：{up_value:.2f}")
print(f"一年后每天不练功的武力值为：{down_value:.2f}")
