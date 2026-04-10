for tree_count in range(1, 101):
    crow_count = 3 * tree_count + 5
    if crow_count == 5 * (tree_count - 1):
        print(f"树的数量：{tree_count}")
        print(f"鸦的数量：{crow_count}")
        break
