s = "www.moe.gov.cn"

print(f"第一个字符：{s[0]}")
print(f"前三个字符：{s[:3]}")
print(f"后三个字符：{s[-3:]}")
print(f"字符串总长度：{len(s)}")
print(f"字符'o'第一次出现的位置索引：{s.index('o')}")
print(f"字符'o'出现的总次数：{s.count('o')}")
print(f"将'.'替换为'-'后的结果：{s.replace('.', '-')}")
print(f"全部转换为大写后的结果：{s.upper()}")

parts = s.split(".")
print(f"删除标点符号并拆分后的四个字符串：{parts}")

print(f"再次输出原字符串：{s}")
print("原字符串没有变化，因为字符串是不可变类型。")
