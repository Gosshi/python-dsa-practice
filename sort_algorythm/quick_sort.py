# 問題: クイックソート
# 問題文:
# 整数の配列 arr が与えられます。この配列をクイックソートを使用して昇順にソートしてください。
#
# 制約:
# 配列の長さは 1 以上 100 以下です。
# 各要素は整数で、範囲は -1000 から 1000 です。

# 再帰の深さは、配列を 𝑛→𝑛/2→𝑛/4→…→1と分割するため、深さは O(logn)。各再帰レベルで O(n) の比較が必要。
# このため、全体の計算量は O(nlogn)

import random


def quick_sort_center_pivot(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, right, center = [], [], []
    for num in arr:
        if pivot < num:
            left.append(num)
        elif pivot > num:
            right.append(num)
        else:
            center.append(num)

    return quick_sort_center_pivot(left) + center + quick_sort_center_pivot(right)


def quick_sort_random_pivot(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randrange(0, len(arr) - 1)]
    left, right, center = [], [], []
    for num in arr:
        if pivot < num:
            left.append(num)
        elif pivot > num:
            right.append(num)
        else:
            center.append(num)

    return quick_sort_random_pivot(left) + center + quick_sort_random_pivot(right)


if __name__ == "__main__":
    arr = [-10, -5, 0, 4, 7, 10, 15]
    print(quick_sort_center_pivot(arr))
    print(quick_sort_random_pivot(arr))
