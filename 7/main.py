import math

a = float(input("请输入第一条边长："))
b = float(input("请输入第二条边长："))
c = float(input("请输入第三条边长："))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    p = perimeter / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"三角形的周长为：{perimeter:.1f}")
    print(f"三角形的面积为：{area:.1f}")
else:
    print("输入的三边无法构成三角形")
