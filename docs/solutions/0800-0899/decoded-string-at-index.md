# [0880. 索引处的解码字符串](https://leetcode.cn/problems/decoded-string-at-index/)

- 标签：栈、字符串
- 难度：中等

## 题目链接

- [0880. 索引处的解码字符串 - 力扣](https://leetcode.cn/problems/decoded-string-at-index/)

## 题目大意

**描述**：

给定一个编码字符串 $s$。请你找出「解码字符串」并将其写入磁带。解码时，从编码字符串中 每次读取一个字符 ，并采取以下步骤：

- 如果所读的字符是字母，则将该字母写在磁带上。
- 如果所读的字符是数字（例如 $d$），则整个当前磁带总共会被重复写 $d-1$ 次。

**要求**：

现在，对于给定的编码字符串 $s$ 和索引 $k$，查找并返回解码字符串中的第 $k$ 个字母。

**说明**：

- $2 \le s.length \le 10^{3}$。
- $s$ 只包含小写字母与数字 2 到 9 。
- $s$ 以字母开头。
- $1 \le k \le 10^{9}$。
- 题目保证 $k$ 小于或等于解码字符串的长度。
- 解码后的字符串保证少于 263 个字母。

**示例**：

- 示例 1：

```python
输入：s = "leet2code3", k = 10
输出："o"
解释：
解码后的字符串为 "leetleetcodeleetleetcodeleetleetcode"。
字符串中的第 10 个字母是 "o"。
```

- 示例 2：

```python
输入：s = "ha22", k = 5
输出："h"
解释：
解码后的字符串为 "hahahaha"。第 5 个字母是 "h"。
```

## 解题思路

### 思路 1：逆向思维

这道题如果直接构建解码字符串会超时（解码后的字符串可能非常长）。我们需要逆向思考：

关键观察：

- 如果当前字符是数字 $d$，解码后的长度会变为原来的 $d$ 倍。
- 如果当前字符是字母，解码后的长度加 1。

算法步骤：

1. 先正向遍历，计算解码后的总长度 $size$。
2. 然后逆向遍历：
   - 如果遇到数字 $d$，说明当前段是前面内容重复 $d$ 次，将 $size$ 除以 $d$，同时 $k$ 对 $size$ 取模（因为是重复的）。
   - 如果遇到字母，$size$ 减 1。如果此时 $k$ 等于 0 或 $k$ 等于 $size$，说明找到了答案。

### 思路 1：代码

```python
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # 计算解码后的总长度
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        
        # 逆向遍历
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            
            # k 对 size 取模
            k %= size
            
            # 如果 k 为 0 且当前是字母，返回该字母
            if k == 0 and c.isalpha():
                return c
            
            # 更新 size
            if c.isdigit():
                size //= int(c)
            else:
                size -= 1
        
        return ""
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串 $s$ 的长度。需要遍历字符串两次。
- **空间复杂度**：$O(1)$，只使用常数额外空间。
