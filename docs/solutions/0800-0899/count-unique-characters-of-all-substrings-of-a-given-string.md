# [0828. 统计子串中的唯一字符](https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/)

- 标签：哈希表、字符串、动态规划
- 难度：困难

## 题目链接

- [0828. 统计子串中的唯一字符 - 力扣](https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/)

## 题目大意

**描述**：

我们定义了一个函数 `countUniqueChars(s)` 来统计字符串 $s$ 中的唯一字符，并返回唯一字符的个数。

例如：`s = "LEETCODE"`，则其中 `"L"`, `"T"`, `"C"`, "O","D" 都是唯一字符，因为它们只出现一次，所以 `countUniqueChars(s) = 5`。

给定一个字符串 $s$。

**要求**：

返回 `countUniqueChars(t)` 的总和，其中 $t$ 是 $s$ 的子字符串。输入用例保证返回值为 32 位整数。

**说明**：

- 注意：某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 $s$ 的所有子字符串中的唯一字符）。
- $1 \le s.length \le 10^{5}$。
- $s$ 只包含大写英文字符。

**示例**：

- 示例 1：

```python
输入: s = "ABC"
输出: 10
解释: 所有可能的子串为："A","B","C","AB","BC" 和 "ABC"。
     其中，每一个子串都由独特字符构成。
     所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
```

- 示例 2：

```python
输入: s = "ABA"
输出: 8
解释: 除了 countUniqueChars("ABA") = 1 之外，其余与示例 1 相同。
```

## 解题思路

### 思路 1：贡献法

这道题如果暴力枚举所有子串会超时。我们需要换个角度思考：计算每个字符作为唯一字符对答案的贡献。

关键观察：

- 对于字符串中的某个字符 $s[i]$，它在哪些子串中是唯一字符？
- 答案是：子串的左边界在 $s[i]$ 左侧最近的相同字符之后，右边界在 $s[i]$ 右侧最近的相同字符之前。

算法步骤：

1. 对于每个字符，记录它在字符串中所有出现的位置。
2. 对于每个位置 $i$ 的字符 $s[i]$：
   - 找到它左侧最近的相同字符位置 $left$（如果没有，则为 $-1$）。
   - 找到它右侧最近的相同字符位置 $right$（如果没有，则为 $n$）。
   - 该字符作为唯一字符的贡献为：$(i - left) \times (right - i)$。
3. 累加所有字符的贡献。

### 思路 1：代码

```python
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        from collections import defaultdict
        
        n = len(s)
        # 记录每个字符出现的所有位置
        pos = defaultdict(list)
        
        for i, ch in enumerate(s):
            pos[ch].append(i)
        
        result = 0
        
        # 遍历每个字符
        for ch, indices in pos.items():
            # 在位置列表前后添加哨兵
            indices = [-1] + indices + [n]
            
            # 计算每个位置的贡献
            for i in range(1, len(indices) - 1):
                left = indices[i - 1]  # 左侧最近的相同字符位置
                mid = indices[i]       # 当前位置
                right = indices[i + 1] # 右侧最近的相同字符位置
                
                # 当前字符作为唯一字符的贡献
                result += (mid - left) * (right - mid)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串的长度。需要遍历字符串两次。
- **空间复杂度**：$O(n)$，需要存储每个字符的位置列表。
