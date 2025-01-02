# 問題文:
# ソートされた整数の配列 arr と整数 target が与えられます。配列の中で target に等しい値が存在する場合、そのインデックスを返してください。
# もし存在しない場合は -1 を返してください。
#
# 制約:
# 配列 arr は昇順にソートされています。
# 配列 arr の長さは 1 以上 100 以下です。
# 各要素は整数で、範囲は -1000 から 1000 です。
# target は整数です。

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    # 中央のindex
    middle = (low + high) // 2

    if target < arr[middle]:
        return binary_search(arr, target, low, middle - 1)
    elif target > arr[middle]:
        return binary_search(arr, target, middle + 1, high)
    else:
        return middle


if __name__ == "__main__":
    arr = [-10, -5, 0, 3, 7, 10, 15]
    target = 7
    print(binary_search(arr, target, 0, len(arr) - 1))

# ChatGPT
# def binary_search(arr, target, low, high):
#     if low > high:
#         return -1
#     # 中央のindex
#     middle = (low + high) // 2
#
#     if target < arr[middle]:
#         return binary_search(arr, target, low, middle - 1)
#     elif target > arr[middle]:
#         return binary_search(arr, target, middle + 1, high)
#     else:
#         return middle
#
#
# def binary_search_wrapper(arr, target):
#     if not arr:
#         return -1
#     return binary_search(arr, target, 0, len(arr) - 1)
#
#
# if __name__ == "__main__":
#     # テストケース
#     print(binary_search_wrapper([-10, -5, 0, 3, 7, 10, 15], 7))  # 出力: 4
#     print(binary_search_wrapper([], 7))                         # 出力: -1
#     print(binary_search_wrapper([10], 10))                     # 出力: 0
#     print(binary_search_wrapper([1, 3, 5, 7], 4))              # 出力: -1
