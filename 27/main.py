set_highjump = {"李朋", "王宇", "张锁", "刘松山", "白旭", "李晓亮"}
set_longjump = {"王宇", "唐英", "刘松山", "白旭", "刘小雨", "宁成"}

all_students = set_highjump | set_longjump
both_students = set_highjump & set_longjump
highjump_only = set_highjump - set_longjump
longjump_only = set_longjump - set_highjump
single_event = highjump_only | longjump_only


def print_students(title, students):
    print(title)
    print(sorted(students))


print_students("参加比赛的所有学生名单：", all_students)
print_students("两项比赛都参加的学生名单：", both_students)
print_students("仅参加跳高比赛的学生名单：", highjump_only)
print_students("仅参加跳远比赛的学生名单：", longjump_only)
print_students("仅参加一项比赛的学生名单：", single_event)
