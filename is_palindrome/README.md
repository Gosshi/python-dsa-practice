## 9. 回文判定 (Palindrome Check)

### **問題**
文字列が回文かどうかを判定する。

### **アルゴリズム**
1. 文字列を小文字に変換し、英数字以外の文字を除去。
2. 残った文字列を左右から比較。

### **計算量**
- **最悪ケース**: \( O(n) \)  
  フィルタリングと比較操作がそれぞれ \( O(n) \)。