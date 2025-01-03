# 問題: 配列の要素を反転する
# 問題文
# 与えられた整数リストの要素を逆順に並べ替える関数を実装してください。
# 組み込み関数やスライス構文を使わず、自分でアルゴリズムを設計して実装してください。
from typing import List


def reverse_array(arr: List[int]) -> List[int]:
    """
    配列の要素を反転する関数。

    Args:
    arr (list[int]): 整数のリスト

    Returns:
    list[int]: 反転されたリスト
    """

    length = len(arr)

    for i in range(length // 2):
        arr[i], arr[length - i - 1] = arr[length - i - 1], arr[i]
    return arr


if __name__ == "__main__":
    print(reverse_array([1, 2, 3, 4, 5]))
    print(reverse_array([3, 2, 1]))
    print(reverse_array([42]))
