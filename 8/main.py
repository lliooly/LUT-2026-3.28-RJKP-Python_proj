score = float(input("请输入百分制分数："))

if score >= 90:
    grade = "优"
elif score >= 80:
    grade = "良"
elif score >= 70:
    grade = "中"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"对应的等级为：{grade}")
