import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


rnd1 = random.randint(0, 100)
rnd2 = random.randint(0, 100)

max_gcd = gcd(rnd1, rnd2)
if max_gcd == 0:
    min_lcm = 0
else:
    min_lcm = abs(rnd1 * rnd2) // max_gcd

print(f"随机整数RND1为：{rnd1}")
print(f"随机整数RND2为：{rnd2}")
print(f"最大公约数为：{max_gcd}")
print(f"最小公倍数为：{min_lcm}")
