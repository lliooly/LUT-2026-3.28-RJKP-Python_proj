lst_score = [9, 10, 8, 9, 10, 7, 6, 8, 7, 8]
sorted_scores = sorted(lst_score)

sorted_scores.pop()
sorted_scores.pop(0)

final_score = sum(sorted_scores) / len(sorted_scores)

print(f"去掉一个最高分和一个最低分后的评分列表：{sorted_scores}")
print(f"该参赛选手的最终得分为：{final_score:.2f}")
