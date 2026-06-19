# [1328. 破坏回文串](https://leetcode.cn/problems/break-a-palindrome/)

- 标签：贪心、字符串
- 难度：中等

## 题目链接

- [1328. 破坏回文串 - 力扣](https://leetcode.cn/problems/break-a-palindrome/)

## 题目大意

**描述**：给定一个回文字符串 $palindrome$。

**要求**：将其中一个字符改成任意小写字母，使得结果字符串**不是回文串**，且结果字典序最小。如果无法做到，返回空字符串。

**说明**：
- $1 \le palindrome.length \le 1000$。

**示例**：
- 示例 1：
```python
输入：palindrome = "abccba"
输出："aaccba"
```
- 示例 2：
```python
输入：palindrome = "a"
输出：""
```

## 解题思路

### 思路 1：贪心

#### 1. 核心思想

要得到字典序最小的非回文字符串，策略是：
1. 遍历前半段字符，找到第一个不是 `'a'` 的字符，将其改为 `'a'`。
2. 如果前半段全是 `'a'`，说明无法通过修改前半段来减小字典序。此时修改最后一个字符为 `'b'`（这样不会破坏上半段的 `'a'`，且字典序增大最少）。
3. 长度为 $1$ 时无法破坏，直接返回空串。

关键细节：只能修改前半段（即 $i < n//2$），因为修改后半段会在对称位置产生对应修改，可能仍保持回文。

#### 2. 具体步骤

**第 1 步**：如果 $n == 1$，返回 `""`。

**第 2 步**：遍历 $i$ 从 $0$ 到 $n//2 - 1$：
- 如果 $palindrome[i] \ne \text{'a'}$：
  - 将 $palindrome[i]$ 改为 `'a'`，返回结果。

**第 3 步**：如果前半段全是 `'a'`，将最后一个字符改为 `'b'`，返回结果。

### 思路 1：代码

```python
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        s = list(palindrome)
        for i in range(n // 2):
            if s[i] != 'a':
                s[i] = 'a'
                return ''.join(s)
        s[-1] = 'b'
        return ''.join(s)
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$，将字符串转为列表。
