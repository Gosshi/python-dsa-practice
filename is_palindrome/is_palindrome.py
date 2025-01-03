# 問題: 回文判定
# 問題文
# 文字列が回文（前から読んでも後ろから読んでも同じ）かどうかを判定する関数を実装してください。
# アルファベットの大文字と小文字の区別をせず、非アルファベット文字（スペースや記号など）は無視して判定してください。


def is_palindrome(s: str) -> bool:
    """
    文字列が回文かどうかを判定する関数。

    Args:
    s (str): 判定対象の文字列

    Returns:
    bool: 回文の場合は True、それ以外は False
    """
    lower_str = s.lower()

    filtered_lower_str = ""
    for str in lower_str:
        if str.isalnum():
            filtered_lower_str = filtered_lower_str + str

    # joinの方が効率的
    # filtered_lower_str = []
    # for char in lower_str:
    #     if char.isalnum():
    #         filtered_lower_str.append(char)
    # filtered_lower_str = "".join(filtered_lower_str)

    length = len(filtered_lower_str)

    for i in range(length//2):
        if filtered_lower_str[i] != filtered_lower_str[length-i-1]:
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal, Panama"))
    print(is_palindrome("race a car"))
    print(is_palindrome(" "))
