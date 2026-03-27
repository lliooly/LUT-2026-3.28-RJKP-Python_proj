my_dict = {
    "方糖": 99,
    "X1": 499,
    "魔盒": 399,
    "曲奇": 299,
}

print("所有在售产品的价目表：")
for product, price in my_dict.items():
    print(f"{product}……{price}元")

average_price = sum(my_dict.values()) / len(my_dict)
max_product = max(my_dict, key=my_dict.get)

print(f"所有产品的平均价格为：{average_price:.2f}元")
print(f"价格最高的产品名称为：{max_product}")
