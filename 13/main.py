lst_student = [["001", "李梅", 19], ["002", "刘祥", 20], ["003", "张武", 18]]

lst_student.append(["004", "刘宁", 20])
lst_student.append(["006", "梁峰", 19])
lst_student.insert(4, ["005", "林歌", 20])

for student in lst_student:
    if student[0] == "003":
        print(f"学号为003的学生信息：{student}")
        break

print("所有学生的姓名：")
for student in lst_student:
    print(student[1])

print("年龄大于19的所有学生信息：")
for student in lst_student:
    if student[2] > 19:
        print(student)
