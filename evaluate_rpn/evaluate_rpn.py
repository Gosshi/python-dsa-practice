# 問題: 逆ポーランド記法（RPN）の計算
# 問題文
# 逆ポーランド記法（RPN: Reverse Polish Notation）は、演算子がオペランドの後に記述される表記法です。
# この形式で記述された式を計算するプログラムを実装してください。
#
# 例：
#
# 式 "3 4 +" は、通常の表記では 3 + 4 に対応し、結果は 7 となります。
# 式 "5 1 2 + 4 * + 3 -" は、通常の表記では 5 + ((1 + 2) * 4) - 3 に対応し、結果は 14 となります。
from data_structure.stack import Stack


def evaluate_rpn(expression: str) -> int:
    """
    逆ポーランド記法の式を計算する関数。

    Args:
    expression (str): 空白で区切られた逆ポーランド記法の式

    Returns:
    int: 式の計算結果
    """

    stack = Stack()
    operators = ["*", "+", "-", "/"]

    # for token in expression.split(): がbetter
    for s in expression:
        if s == " ":
            continue
        if s not in operators:
            stack.push(s)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if s == "*":
                stack.push(b*a)
            elif s == "+":
                stack.push(b+a)
            elif s == "-":
                stack.push(b-a)
            elif s == "/":
                stack.push(b//a)
    result = stack.pop()
    return result


if __name__ == "__main__":
    print(evaluate_rpn("3 4 +"))               # 出力: 7
    print(evaluate_rpn("5 1 2 + 4 * + 3 -"))  # 出力: 14
    print(evaluate_rpn("2 3 1 * + 9 -"))      # 出力: -4
