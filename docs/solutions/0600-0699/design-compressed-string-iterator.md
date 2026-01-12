# [0604. 迭代压缩字符串](https://leetcode.cn/problems/design-compressed-string-iterator/)

- 标签：设计、数组、字符串、迭代器
- 难度：简单

## 题目链接

- [0604. 迭代压缩字符串 - 力扣](https://leetcode.cn/problems/design-compressed-string-iterator/)

## 题目大意

**要求**：

设计并实现一个迭代压缩字符串的数据结构。给定的压缩字符串的形式是，每个字母后面紧跟一个正整数，表示该字母在原始未压缩字符串中出现的次数。
设计一个数据结构，它支持如下两种操作： `next` 和 `hasNext`。

- `next()`：如果原始字符串中仍有未压缩字符，则返回下一个字符，否则返回空格。
- `hasNext()`：如果原始字符串中存在未压缩的的字母，则返回 true，否则返回 false。

**说明**：

- $1 \le compressedString.length \le 10^{3}$。
- $compressedString$ 由小写字母、大写字母和数字组成。
- 在 $compressedString$ 中，单个字符的重复次数在 $[1, 10^9]$ 范围内。
- `next` 和 `hasNext` 的操作数最多为 $10^{3}$。

**示例**：

- 示例 1：

```python
输入：
["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
输出：
[null, "L", "e", "e", "t", "C", "o", true, "d", true]

解释：
StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
stringIterator.next(); // 返回 "L"
stringIterator.next(); // 返回 "e"
stringIterator.next(); // 返回 "e"
stringIterator.next(); // 返回 "t"
stringIterator.next(); // 返回 "C"
stringIterator.next(); // 返回 "o"
stringIterator.hasNext(); // 返回 True
stringIterator.next(); // 返回 "d"
stringIterator.hasNext(); // 返回 True
```

- 示例 2：

```python
输入：
输出：
```

## 解题思路

### 思路 1：双指针解析

#### 思路 1：算法描述

这道题目要求设计一个迭代压缩字符串的数据结构。压缩字符串的格式是每个字母后面紧跟一个正整数，表示该字母的重复次数。

我们可以在初始化时解析压缩字符串，将字符和对应的重复次数存储起来，然后使用指针来跟踪当前位置。

具体步骤如下：

1. **初始化**：解析压缩字符串，提取每个字符和对应的重复次数，存储在列表中。维护两个变量：
   - $idx$：当前字符在列表中的索引。
   - $count$：当前字符剩余的重复次数。

2. **next()**：返回下一个字符。
   - 如果 $count > 0$，返回当前字符，并将 $count$ 减 $1$。
   - 如果 $count = 0$，移动到下一个字符（$idx$ 加 $1$），更新 $count$。
   - 如果已经没有字符了，返回空格。

3. **hasNext()**：判断是否还有未压缩的字符。
   - 如果 $idx < len(chars)$ 或 $count > 0$，返回 $True$。
   - 否则返回 $False$。

#### 思路 1：代码

```python
class StringIterator:

    def __init__(self, compressedString: str):
        self.chars = []  # 存储字符和重复次数的列表
        i = 0
        n = len(compressedString)
        
        # 解析压缩字符串
        while i < n:
            char = compressedString[i]
            i += 1
            num_str = ""
            # 提取数字
            while i < n and compressedString[i].isdigit():
                num_str += compressedString[i]
                i += 1
            self.chars.append((char, int(num_str)))
        
        self.idx = 0  # 当前字符在列表中的索引
        self.count = self.chars[0][1] if self.chars else 0  # 当前字符剩余的重复次数

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        
        # 获取当前字符
        char = self.chars[self.idx][0]
        self.count -= 1
        
        # 如果当前字符已经用完，移动到下一个字符
        if self.count == 0 and self.idx + 1 < len(self.chars):
            self.idx += 1
            self.count = self.chars[self.idx][1]
        
        return char

    def hasNext(self) -> bool:
        return self.idx < len(self.chars) and self.count > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

#### 思路 1：复杂度分析

- **时间复杂度**：
  - 初始化：$O(n)$，其中 $n$ 是压缩字符串的长度。
  - next()：$O(1)$。
  - hasNext()：$O(1)$。
- **空间复杂度**：$O(m)$，其中 $m$ 是不同字符的数量。
