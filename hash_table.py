# 問題: ハッシュテーブル操作の実装
# 問題文
# ハッシュテーブル（辞書）を使用して、以下の操作を実装してください：
#
# キーと値の追加: 指定したキーと値を追加します。
# キーの削除: 指定したキーを削除します。
# キーの検索: 指定したキーに対応する値を取得します（存在しない場合は None を返します）。
# すべてのキーを取得: 現在のすべてのキーをリストで返します。


# 解説
# キーと値の操作
# 値を取得する: d[key]
# 新しいキーと値を追加する: d[key] = value
# キーを削除する: del d[key]

# 特徴
# 辞書のキーは一意である必要があり、重複するキーを設定すると、後から設定された値で上書きされます
#
# キーはハッシュ可能でなければならない
# ・キーは不変（immutable）である必要があり、文字列、数値、タプルなどが使用できます。
# ・リストや辞書など、変更可能なオブジェクトはキーとして使えません。
#
# 順序が保持される
# ・Python 3.7以降、辞書は挿入順序を保持します。


class HashTable:
    def __init__(self):
        self.table = {}

    def add(self, key, value):
        self.table[key] = value

    def remove(self, key):
        if key in self.table:
            del self.table[key]

    def get(self, key):
        if key in self.table:
            return self.table[key]
        return None

    def keys(self):
        return list(self.table.keys())


if __name__ == "__main__":
    # 初期化
    table = HashTable()

    # キーと値の追加
    table.add("name", "Alice")
    table.add("age", 25)

    # キーの検索
    print(table.get("name"))  # 出力: Alice
    print(table.get("age"))  # 出力: 25
    print(table.get("gender"))  # 出力: None

    # キーの削除
    table.remove("age")
    print(table.get("age"))  # 出力: None

    # すべてのキーを取得
    print(table.keys())  # 出力: ["name"]
