# 問題文
# 文字列 s と t が与えられます。s の中から t のすべての文字を含む最小の部分文字列を見つけて返してください。
# 部分文字列が存在しない場合は空文字列を返してください。
from collections import Counter


def minimum_window_substring(s, t):
    head_index = 0
    tail_index = 0
    matched = 0
    result = (0, float('inf'))  # 初期値
    target_count = Counter(t)
    window_count = Counter()

    while tail_index < len(s):
        char = s[tail_index]
        window_count[char] += 1
        if window_count[char] == target_count[char]:
            matched += 1

        # ウィンドウを縮める
        while matched == len(target_count):
            if tail_index - head_index + 1 < result[1] - result[0]:
                result = (head_index, tail_index + 1)

            char = s[head_index]
            window_count[char] -= 1
            if window_count[char] < target_count[char]:
                matched -= 1
            head_index += 1

        tail_index += 1

    return "" if result[1] == float('inf') else s[result[0]:result[1]]


if __name__ == "__main__":
    print(minimum_window_substring("ADOBECODEBANC", "ABC"))
