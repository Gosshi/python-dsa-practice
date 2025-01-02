# 問題: スタックの基本操作を実装
# 問題文
# 以下の基本操作を持つスタック（後入れ先出し、LIFO）のデータ構造をクラスとして実装してください。
#
# 要素の追加 (push):
#
# スタックの上に要素を追加します。
# 要素の削除 (pop):
#
# スタックの上にある要素を削除し、その要素を返します。
# スタックが空の場合、適切なメッセージまたはエラーを返します。
# 要素の確認 (peek):
#
# スタックの一番上にある要素を確認します（削除しません）。
# スタックが空の場合、適切なメッセージまたはエラーを返します。
# スタックが空かどうかの確認 (is_empty):
#
# スタックが空かどうかを確認して、真偽値を返します。
#
# 制約
# スタックのサイズは可変とします（制限なし）。
# 使用するデータ構造はリストをベースにしてください。


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty."
        return self.stack[-1]

    # pop() はデフォルトで最後の要素を削除するため、明示的にインデックスを指定する必要がありません。
    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty."
        return self.stack.pop(len(self.stack) - 1)

    def pop_scratch(self):
        if len(self.stack) == 0:
            return "Stack is empty."
        # 最後の要素を取得して削除
        last_element = self.stack[len(self.stack) - 1]  # 最後の要素を保存
        del self.stack[len(self.stack) - 1]  # 最後の要素を削除
        return last_element  # 削除した要素を返す

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False


if __name__ == "__main__":
    # 初期化
    stack = Stack()

    # 要素の追加
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # 要素の確認
    print(stack.peek())  # 出力: 3

    # 要素の削除
    print(stack.pop())  # 出力: 3
    print(stack.pop())  # 出力: 2

    # 空の確認
    print(stack.is_empty())  # 出力: False

    # 要素の削除（スタックが空の場合）
    print(stack.pop())  # 出力: 1
    print(stack.is_empty())  # 出力: True

    # 空のスタックでの操作
    print(stack.pop())  # 出力: "Stack is empty."
    print(stack.peek())  # 出力: "Stack is empty."
