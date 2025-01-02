# 問題: 選択ソートの実装
# 問題文
# 整数リストを入力として受け取り、選択ソートアルゴリズムを用いてリストを昇順にソートする関数を実装してください。

# アルゴリズムの説明
# 配列を「ソート済み部分」と「未ソート部分」に分けます。
# 未ソート部分の中から最小値を見つけ、ソート済み部分の末尾と交換します。
# この操作を配列の要素が全てソート済みになるまで繰り返します。
import sys

from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """
    選択ソートを実装する関数。

    Args:
    arr (list[int]): 整数のリスト

    Returns:
    list[int]: 昇順にソートされたリスト
    """

    for i in range(len(arr) - 1):
        # 新しいリストを作成するため、時間とメモリの効率が悪い
        min_index, min_num = find_min_index(arr[i:])
        arr[i + min_index] = arr[i]
        arr[i] = min_num

    # ChatGPT answer
    # n = len(arr)
    # for i in range(n - 1):
    #     # 最小値のインデックスを見つける
    #     min_index = i
    #     for j in range(i + 1, n):
    #         if arr[j] < arr[min_index]:
    #             min_index = j
    #
    #     # 最小値を現在の位置と交換
    #     arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def find_min_index(arr):
    min_num = sys.maxsize
    min_index = 0
    for i in range(len(arr)):
        if arr[i] < min_num:
            min_index = i
            min_num = arr[i]
    return min_index, min_num


if __name__ == "__main__":
    print(selection_sort([5, 2, 9, 1, 5, 6]))
    print(selection_sort([3, 2, 1]))
    print(selection_sort([1, 2, 3, 4]))
