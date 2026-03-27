USD_TO_CNY = 6.868
CNY_TO_USD = 0.1456


def parse_input(text):
    text = text.strip()
    if not text:
        return None, None

    if text[0] in {"$", "￥", "¥"}:
        return text[0], float(text[1:])
    if text[-1] in {"$", "￥", "¥"}:
        return text[-1], float(text[:-1])
    return None, None


money_text = input("请输入要兑换的币值，并带上货币符号：")
symbol, amount = parse_input(money_text)

if symbol == "$":
    cny = amount * USD_TO_CNY
    print(f"{amount}美元可以兑换人民币{cny:.2f}元")
elif symbol in {"￥", "¥"}:
    usd = amount * CNY_TO_USD
    print(f"{amount}元人民币可以兑换{usd:.2f}美元")
else:
    print("输入格式错误，请在金额前后添加$、￥或¥。")
