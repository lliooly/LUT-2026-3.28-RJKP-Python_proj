import sys

try:
    import jieba
    import jieba.posseg as pseg
except ModuleNotFoundError:
    print("请先安装jieba库，例如：pip3 install jieba")
    sys.exit(0)

s = "外观很好，画质也不错。但是音质真的太糟糕了！操作也不方便。"

degree_dict = {"很": 2, "大": 3, "非常": 2, "较": 1, "极": 3, "无比": 4, "太": 3}
positive_words = {"好": 1, "不错": 1, "方便": 1}
negative_words = {"糟糕": -1}
negation_words = {"不", "没", "无"}

filtered_words = []
for word, flag in pseg.cut(s):
    if flag.startswith(("a", "d", "c")):
        filtered_words.append((word, flag))

print("形容词、副词和连词提取结果：")
for word, flag in filtered_words:
    print(f"{word}/{flag}")

words = list(jieba.lcut(s))
sentiment_score = 0

for index, word in enumerate(words):
    base_score = 0

    if word in positive_words:
        base_score = positive_words[word]
    elif word in negative_words:
        base_score = negative_words[word]
    elif word == "方便" and index > 0 and words[index - 1] in negation_words:
        base_score = -1

    if base_score != 0:
        multiplier = 1
        if index > 0 and words[index - 1] in degree_dict:
            multiplier = degree_dict[words[index - 1]]
        sentiment_score += base_score * multiplier

print(f"情感分为：{sentiment_score}")
if sentiment_score > 0:
    print("该评论为积极情感。")
elif sentiment_score < 0:
    print("该评论为消极情感。")
else:
    print("该评论为中性情感。")
