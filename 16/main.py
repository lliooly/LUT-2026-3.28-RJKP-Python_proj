dic_city = {
    "张三风": ["北京", "成都"],
    "李茉绸": ["上海", "广州", "兰州"],
    "慕容福": ["太原", "西安", "济南", "上海"],
}

for name, cities in dic_city.items():
    print(f"{name}去过{len(cities)}个城市")

visited_shanghai = [name for name, cities in dic_city.items() if "上海" in cities]
print(f"去过上海的有{len(visited_shanghai)}人，他们是{'、'.join(visited_shanghai)}")
