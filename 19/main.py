def judge(password):
    level = 0

    if any(ch.isdigit() for ch in password):
        level += 1
    if any(ch.isupper() for ch in password):
        level += 1
    if any(ch.islower() for ch in password):
        level += 1
    if len(password) >= 8:
        level += 1

    return level


password = input("请输入测试密码：")
print(f"{password}的密码强度为{judge(password)}级")
