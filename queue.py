# 問題: キューの基本操作を実装
# 問題文
# 以下の基本操作を持つ キュー（Queue） のデータ構造をクラスとして実装してください。
#
# 要素の追加 (enqueue):
#
# キューの末尾に要素を追加します。
# 要素の削除 (dequeue):
#
# キューの先頭から要素を削除して返します。
# キューが空の場合、適切なメッセージまたはエラーを返します。
# 先頭の要素の確認 (peek):
#
# キューの先頭にある要素を確認します（削除しません）。
# キューが空の場合、適切なメッセージまたはエラーを返します。
# キューが空かどうかの確認 (is_empty):
#
# キューが空かどうかを確認して、真偽値を返します。

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    # リストの先頭の要素を削除する場合、後続のすべての要素がシフトされるため、dequeue の計算量は O(n) です。
    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        first_element = self.queue[0]
        del self.queue[0]
        return first_element  # 削除した要素を返す

    # リストをpopすると先頭が消える仕様
    def dequeue_pop(self):
        """キューの先頭の値を削除して返す"""
        if len(self.queue) == 0:
            return "Queue is empty"
        return self.queue.pop(0)  # 先頭の要素を削除して返す

    def peek(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


if __name__ == "__main__":
    queue = Queue()

    # 要素の追加
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # 先頭の要素の確認
    print(queue.peek())  # 出力: 1

    # 要素の削除
    print(queue.dequeue())  # 出力: 1
    print(queue.dequeue())  # 出力: 2

    # 空の確認
    print(queue.is_empty())  # 出力: False

    # 要素の削除（キューが空の場合）
    print(queue.dequeue())  # 出力: 3
    print(queue.is_empty())  # 出力: True

    # 空のキューでの操作
    print(queue.dequeue())  # 出力: "Queue is empty."
    print(queue.peek())  # 出力: "Queue is empty."
