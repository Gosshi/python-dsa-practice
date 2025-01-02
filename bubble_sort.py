# 問題: バブルソートの実装
# 問題文
# 整数リストを入力として受け取り、バブルソートアルゴリズムを用いてリストを昇順にソートする関数を実装してください。

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    バブルソートを実装する関数。

    Args:
    arr (list[int]): 整数のリスト

    Returns:
    list[int]: 昇順にソートされたリスト
    """

    while True:
        if is_sorted(arr):
            break
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


# これでも良いが、swapがあったかどうかでソート済みか判定可能
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1, 5, 6]))
    print(bubble_sort([3, 2, 1]))
    print(bubble_sort([1, 2, 3, 4]))
