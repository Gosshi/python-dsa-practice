## 1. 線形探索 (Linear Search)

### **問題**
配列内の指定された要素を探し、そのインデックスを返す。見つからない場合は `-1` を返す。

### **アルゴリズム**
1. 配列を左から右に順番に探索。
2. 要素が見つかったら、その位置を返す。

### **計算量**
- **最悪ケース**: \( O(n) \)  
  配列全体を調べる必要がある。
- **最良ケース**: \( O(1) \)  
  最初の位置にターゲットがある場合。

---

## 2. 二分探索 (Binary Search)

### **問題**
ソート済みの配列内で指定された要素を探し、そのインデックスを返す。見つからない場合は `-1` を返す。

### **アルゴリズム**
1. 配列の中央の要素を比較。
2. ターゲットが中央より小さい場合は左側、そうでない場合は右側を再帰的または反復的に探索。

### **計算量**
- **最悪ケース**: \( O(\log n) \)  
  配列のサイズを半分に分割するため。
- **最良ケース**: \( O(1) \)  
  中央にターゲットがある場合。

---