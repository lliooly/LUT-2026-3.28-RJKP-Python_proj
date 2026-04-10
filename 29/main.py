import sys

try:
    import numpy as np
except ModuleNotFoundError:
    print("请先启用 full 可选依赖，例如：uv sync --extra full")
    sys.exit(0)

A = np.arange(20).reshape(4, 5)
B = np.arange(100, 120).reshape(4, 5)
middle_rows_sum = A[1:3] + B[1:3]

print("数组 A：")
print(A)
print("数组 B：")
print(B)
print("A + B：")
print(A + B)
print("B - A：")
print(B - A)
print("A * B：")
print(A * B)
print("A / B：")
print(A / B)
print("A**2 + B**3：")
print(A**2 + B**3)
print("A 和 B 中间两行对应元素之和：")
print(middle_rows_sum)
print(f"A 的 rank：{A.ndim}")
print(f"A 的 shape：{A.shape}")
print(f"A 的 size：{A.size}")
print(f"A 每个元素占用的字节数：{A.itemsize}")
