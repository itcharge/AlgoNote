# [0796. 旋转字符串](https://leetcode.cn/problems/rotate-string/)

- 标签：字符串、字符串匹配
- 难度：简单

## 题目链接

- [0796. 旋转字符串 - 力扣](https://leetcode.cn/problems/rotate-string/)

## 题目大意

**描述**：给定两个字符串 `s` 和 `goal`。

**要求**：如果 `s` 在若干次旋转之后，能变为 `goal`，则返回 `True`，否则返回 `False`。

**说明**：

- `s` 的旋转操作：将 `s` 最左侧的字符移动到最右边。
  - 比如：`s = "abcde"`，在旋转一次之后结果就是 `s = "bcdea"`。
- $1 \le s.length, goal.length \le 100$。
- `s` 和 `goal` 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入: s = "abcde", goal = "cdeab"
输出: true
```

- 示例 2：

```python
输入: s = "abcde", goal = "abced"
输出: false
```

## 解题思路

### 思路 1：KMP 算法

其实将两个字符串 `s` 拼接在一起，就包含了所有从 `s` 进行旋转后的字符串。那么我们只需要判断一下 `goal` 是否为 `s + s` 的子串即可。可以用 KMP 算法来做。

1. 先排除掉几种不可能的情况，比如 `s` 为空串的情况，`goal` 为空串的情况，`len(s) != len(goal)` 的情况。
2. 然后使用 KMP 算法计算出 `goal` 在 `s + s` 中的下标位置 `index`（`s + s` 可用取余运算模拟）。
3. 如果 `index == -1`，则说明 `s` 在若干次旋转之后，不能能变为 `goal`，则返回 `False`。
4. 如果 `index != -1`，则说明 `s` 在若干次旋转之后，能变为 `goal`，则返回 `True`。

### 思路 1：代码

```python
class Solution:
    def kmp(self, T: str, p: str) -> int:
        n, m = len(T), len(p)

        next = self.generateNext(p)

        i, j = 0, 0
        while i - j < n:
            while j > 0 and T[i % n] != p[j]:
                j = next[j - 1]
            if T[i % n] == p[j]:
                j += 1
            if j == m:
                return i - m + 1
            i += 1
        return -1

    def generateNext(self, p: str):
        m = len(p)
        next = [0 for _ in range(m)]

        left = 0
        for right in range(1, m):
            while left > 0 and p[left] != p[right]:
                left = next[left - 1]
            if p[left] == p[right]:
                left += 1
            next[right] = left

        return next

    def rotateString(self, s: str, goal: str) -> bool:
        if not s or not goal or len(s) != len(goal):
            return False
        index = self.kmp(s, goal)
        if index == -1:
            return False
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中文本串 $s$ 的长度为 $n$，模式串 $goal$ 的长度为 $m$。
- **空间复杂度**：$O(m)$。
