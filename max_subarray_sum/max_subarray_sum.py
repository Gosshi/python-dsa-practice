# 問題文
# 整数の配列が与えられたとき、その中で部分配列の最大和を求めてください。
import sys


def max_subarray_sum(arr):
    # とりあえず先頭1件を最大値とする
    max_value = arr[0]

    for i in range(len(arr)):
        for j in range(len(arr) + 1):
            # if i + j > len(arr)+1 は実際には不要です。
            # スライスの範囲外アクセスはPythonでは空リストを返すため、問題にはなりません。
            if i + j > len(arr) + 1:
                continue
            subarray_sum = sum(arr[i:i + j])
            if subarray_sum > max_value:
                max_value = subarray_sum
    return max_value


def max_subarray_sum_with_kadane(arr):
    # とりあえず先頭1件を最大値とする
    max_value = arr[0]
    current_sum = 0

    for i in range(len(arr)):
        current_sum = max(current_sum + arr[i], arr[i])
        max_value = max(max_value, current_sum)
    return max_value


if __name__ == "__main__":
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray_sum([1]))
    print(max_subarray_sum([5, 4, -1, 7, 8]))
    print(max_subarray_sum([0, -1, 2, -1, 3, -2, 4]))

    print(max_subarray_sum_with_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray_sum_with_kadane([1]))
    print(max_subarray_sum_with_kadane([5, 4, -1, 7, 8]))
    print(max_subarray_sum_with_kadane([0, -1, 2, -1, 3, -2, 4]))
