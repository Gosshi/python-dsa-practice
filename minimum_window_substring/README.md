# 最小ウィンドウ部分文字列問題の詳細解説

---

## **問題文**
文字列 `s` と `t` が与えられます。`s` の中から `t` のすべての文字を含む最小の部分文字列を見つけて返してください。部分文字列が存在しない場合は空文字列を返してください。

---

## **アルゴリズムの解法**

この問題を効率的に解くには、「スライディングウィンドウ」と「辞書」を使用します。

---

### **1. 基本的な考え方**
1. **ウィンドウを広げる**:
   - `tail_index` を右に進めてウィンドウを広げます。
   - 現在のウィンドウ内の文字をカウントします。

2. **条件を満たしたら縮める**:
   - ウィンドウ内の文字が `t` の条件を満たしている場合、`head_index` を右に進めてウィンドウを縮めます。
   - 縮めることで、最小の部分文字列を探索します。

3. **終了条件**:
   - `tail_index` が `s` の末尾に到達したら処理を終了します。

---

### **2. アルゴリズムの実装**
以下のステップで問題を解決します。

#### **ステップ 1: 初期化**
- `target_count`: 文字列 `t` の各文字の出現回数を記録する辞書。
- `window_count`: 現在のウィンドウ内の各文字の出現回数を記録する辞書。
- `head_index`, `tail_index`: ウィンドウの左右端を管理するインデックス。
- `matched`: 条件を満たしている文字数を追跡。
- `result`: 最小ウィンドウの開始位置と終了位置を記録。

#### **ステップ 2: ウィンドウを広げる**
- `tail_index` を右に進め、`window_count` に文字を追加。
- もしその文字が `target_count` の条件を満たした場合、`matched` を更新。

#### **ステップ 3: 条件を満たしたらウィンドウを縮める**
- 条件を満たしている間、`head_index` を右に進めてウィンドウを縮める。
- 縮める際に、現在のウィンドウの長さを記録し、最小値を更新。

#### **ステップ 4: 最小ウィンドウを返す**
- `result` を基に、最小の部分文字列を返す。

---

### **コード**
以下は最終的なコードです。

```python
from collections import Counter

def minimum_window_substring(s, t):
    head_index = 0
    tail_index = 0
    matched = 0
    result = (0, float('inf'))  # 初期値 (開始位置, 最小長さ)
    target_count = Counter(t)
    window_count = Counter()

    while tail_index < len(s):
        # ウィンドウを広げる
        char = s[tail_index]
        window_count[char] += 1
        if char in target_count and window_count[char] == target_count[char]:
            matched += 1

        # 条件を満たしている場合にウィンドウを縮める
        while matched == len(target_count):
            # 最小ウィンドウを更新
            if tail_index - head_index + 1 < result[1] - result[0]:
                result = (head_index, tail_index + 1)

            # ウィンドウの左端を進める
            left_char = s[head_index]
            window_count[left_char] -= 1
            if left_char in target_count and window_count[left_char] < target_count[left_char]:
                matched -= 1
            head_index += 1

        # ウィンドウの右端を進める
        tail_index += 1

    return "" if result[1] == float('inf') else s[result[0]:result[1]]
