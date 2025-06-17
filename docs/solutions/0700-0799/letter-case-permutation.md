# [0784. 字母大小写全排列](https://leetcode.cn/problems/letter-case-permutation/)

- 标签：位运算、字符串、回溯
- 难度：中等

## 题目链接

- [0784. 字母大小写全排列 - 力扣](https://leetcode.cn/problems/letter-case-permutation/)

## 题目大意

**描述**：给定一个字符串 $s$，通过将字符串 $s$ 中的每个字母转变大小写，我们可以获得一个新的字符串。

**要求**：返回所有可能得到的字符串集合。

**说明**：

- 答案可以以任意顺序返回输出。
- $1 \le s.length \le 12$。
- $s$ 由小写英文字母、大写英文字母和数字组成。

**示例**：

- 示例 1：

```python
输入：s = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]
```

- 示例 2：

```python
输入: s = "3z4"
输出: ["3z4","3Z4"]
```

## 解题思路

### 思路 1：回溯算法

- $i$ 代表当前要处理的字符在字符串 $s$ 中的下标，$path$ 表示当前路径，$ans$ 表示答案数组。
- 如果处理到 $i == len(s)$ 时，将当前路径存入答案数组中返回，否则进行递归处理。
  - 不修改当前字符，直接递归处理第 $i + 1$ 个字符。
  - 如果当前字符是小写字符，则变为大写字符之后，递归处理第 $i + 1$ 个字符。
  - 如果当前字符是大写字符，则变为小写字符之后，递归处理第 $i + 1$ 个字符。

### 思路 1：代码

```python
class Solution:
    def dfs(self, s, path, i, ans):
        if i == len(s):
            ans.append(path)
            return

        self.dfs(s, path + s[i], i + 1, ans)
        if ord('a') <= ord(s[i]) <= ord('z'):
            self.dfs(s, path + s[i].upper(), i + 1, ans)
        elif ord('A') <= ord(s[i]) <= ord('Z'):
            self.dfs(s, path + s[i].lower(), i + 1, ans)

    def letterCasePermutation(self, s: str) -> List[str]:
        ans, path = [], ""
        self.dfs(s, path, 0, ans)
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$n \times 2^n$，其中 $n$ 为字符串的长度。
- **空间复杂度**：$O(1)$，除返回值外不需要额外的空间。

