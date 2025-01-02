# 問題: バランスの取れた括弧列の判定
# 問題文
# 与えられた文字列がバランスの取れた括弧列かどうかを判定する関数を実装してください。括弧には以下の3種類があります：
#
# 丸括弧: (, )
# 中括弧: [, ]
# 波括弧: {, }
# 括弧列がバランスしているとは、以下の条件を満たす場合を指します：
#
# 開始括弧がある場合、対応する終了括弧が存在する。
# 括弧の順序が正しい（例: ({[]}) は正しいが、([)] は正しくない）。
from stack import Stack


def is_balanced(s: str) -> bool:
    """
    バランスの取れた括弧列かどうかを判定する関数。

    Args:
    s (str): 入力文字列

    Returns:
    bool: バランスが取れていれば True、そうでなければ False
    """

    stack = Stack()

    for ss in s:
        if ss in ["{", "(", "["]:
            stack.push(ss)
        elif ss in [")", "}", "]"]:
            if stack.is_empty():  # スタックが空の場合、不正な括弧列
                return False
            popped_str = stack.pop()
            if not((ss == "}" and popped_str == "{")
                   or (ss == "]" and popped_str == "[") or (ss == ")" and popped_str == "(")):
                return False
    return stack.is_empty()


if __name__ == "__main__":
    print(is_balanced("()"))  # 出力: True
    print(is_balanced("([])"))  # 出力: True
    print(is_balanced("{[()]}"))  # 出力: True
    print(is_balanced("([])"))  # 出力: False
    print(is_balanced("("))  # 出力: False
    print(is_balanced("]"))  # 出力: False
