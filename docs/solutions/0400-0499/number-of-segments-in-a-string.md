# [0434. 字符串中的单词数](https://leetcode.cn/problems/number-of-segments-in-a-string/)

- 标签：字符串
- 难度：简单

## 题目链接

- [0434. 字符串中的单词数 - 力扣](https://leetcode.cn/problems/number-of-segments-in-a-string/)

## 题目大意

**描述**：

给定字符串 $s$。

**要求**：

统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

**说明**：

- 可以假定字符串里不包括任何不可打印的字符。

**示例**：

- 示例 1：

```python
输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
```

## 解题思路

### 思路 1：遍历计数

思路非常简单，直接遍历统计单词数即可。

对于字符串 $s$ 来说，我们使用两个变量：

- $ans$：用来统计单词个数
- $prev$：用来记录上一个字符是否为空格

然后遍历字符串：

- 如果当前字符不是空格，且上一个字符是空格（或者是第一个字符），则说明遇到了一个新的单词，单词数 $ans$ 加 $1$
- 最后返回 $ans$ 即可。

### 思路 1：代码

```python
class Solution:
    def countSegments(self, s: str) -> int:
        # ans 统计单词数，prev 记录上一个字符是否为空格
        ans = 0
        prev = True
        
        # 遍历字符串
        for ch in s:
            # 如果当前字符不是空格，且上一个字符是空格，则遇到新单词
            if ch != ' ' and prev:
                ans += 1
            # 更新 prev：当前字符是否为空格
            prev = (ch == ' ')
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是字符串 $s$ 的长度。
- **空间复杂度**：$O(1)$。
