# 問題文
# 2つの整数配列 arr1 と arr2 が与えられます。それらを昇順にマージした結果を返してください。
# 両方の配列はすでに昇順にソートされているものとします。

def merge_two_arrays(arr1, arr2):
    result = []
    i, j = 0, 0
    while True:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

        if i == len(arr1):
            result += arr2[j:]
            break
        elif j == len(arr2):
            result += arr1[i:]

    return result


if __name__ == "__main__":
    print(merge_two_arrays([1, 3, 5], [4, 4, 6]))
