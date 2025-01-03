# 問題: マージソート
# 問題文:
# 整数の配列 arr が与えられます。この配列をマージソートを使用して昇順にソートしてください。
#
# 制約:
# 配列の長さは 1 以上 100 以下です。
# 各要素は整数で、範囲は -1000 から 1000 です。

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # 両方の配列を比較して小さい方を追加
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 残った要素をすべて追加
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    arr = [-10, -5, 0, 4, 7, 10, 15]
    print(merge_sort(arr))
