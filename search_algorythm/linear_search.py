
# 問題: 線形探索
# 問題文:
# 整数の配列 arr と整数 target が与えられます。配列の中で target に等しい値が存在する場合、そのインデックスを返してください。
# もし存在しない場合は -1 を返してください。
#
# 制約:
# 配列 arr の長さは 1 以上 100 以下です。
# 各要素は整数で、範囲は -1000 から 1000 です。
# target は整数です。

def linear_search(arr, target):
    result = -1
    for i in range(len(arr)):
        if arr[i] == target:
            result = i
            break
    return result


# ChatGPT's Answer
# def linear_search(arr, target):
#     for i, value in enumerate(arr):
#         if value == target:
#             return i
#     return -1
