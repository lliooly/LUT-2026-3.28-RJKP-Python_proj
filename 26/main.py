lst = [
    ("triangle", "shape"),
    ("red", "color"),
    ("square", "shape"),
    ("yellow", "color"),
    ("green", "color"),
    ("circle", "shape"),
]

swapped_sorted = sorted((label, value) for value, label in lst)
sorted_by_label = [(value, label) for label, value in swapped_sorted]
lst_colors = [value for value, label in lst if label == "color"]

print("按照标签排序后的列表：")
print(sorted_by_label)
print("颜色列表 lst_colors：")
print(lst_colors)
