from itertools import permutations

students = ["A", "B", "C", "D", "E"]


def is_valid(ranking):
    return (
        (ranking[1] == "D") + (ranking[2] == "B") == 1
        and (ranking[1] == "C") + (ranking[3] == "E") == 1
        and (ranking[0] == "E") + (ranking[4] == "A") == 1
        and (ranking[2] == "C") + (ranking[3] == "A") == 1
        and (ranking[1] == "B") + (ranking[4] == "D") == 1
    )


real_ranking = next(ranking for ranking in permutations(students) if is_valid(ranking))
rank_lookup = {name: index + 1 for index, name in enumerate(real_ranking)}

print("真实名次如下：")
for index, name in enumerate(real_ranking, start=1):
    print(f"第{index}名：{name}")

print("按同学查看名次：")
for name in students:
    print(f"{name}：第{rank_lookup[name]}名")
