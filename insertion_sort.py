# 問題: 挿入ソートの実装
# 問題文
# 整数リストを入力として受け取り、挿入ソートアルゴリズムを用いてリストを昇順にソートする関数を実装してください。

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """
    挿入ソートを実装する関数。

    Args:
    arr (list[int]): 整数のリスト

    Returns:
    list[int]: 昇順にソートされたリスト
    """
    # 外側のループ：未ソート部分の先頭を選ぶ
    for i in range(1, len(arr)):
        tmp = arr[i]
        k = i - 1

        # ソート済み部分を逆方向に走査しながらシフト
        # 先頭はソート済みとして良い。ソート済み部分が左から広がっていくイメージ
        while k >= 0 and arr[k] > tmp:
            arr[k + 1] = arr[k]  # 要素を右にシフト
            k = k - 1

        # 空いた位置に key を挿入
        arr[k + 1] = tmp
    return arr


if __name__ == "__main__":
    print(insertion_sort([5, 2, 9, 1, 5, 6]))
    print(insertion_sort([3, 2, 1]))
    print(insertion_sort([1, 2, 3, 4]))
