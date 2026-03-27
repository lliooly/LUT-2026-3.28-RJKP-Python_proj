numbers = [str(num) for num in range(1, 101) if num % 3 == 0 and num % 5 != 0]
print("1~100之间能被3整除但不能被5整除的数有：")
print(" ".join(numbers))
