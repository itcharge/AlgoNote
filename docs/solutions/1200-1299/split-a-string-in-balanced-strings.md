# [1221. 分割平衡字符串](https://leetcode.cn/problems/split-a-string-in-balanced-strings/)

- 标签：栈、贪心、字符串、计数
- 难度：简单

## 题目链接

- [1221. 分割平衡字符串 - 力扣](https://leetcode.cn/problems/split-a-string-in-balanced-strings/)

## 题目大意

**描述**：给定一个平衡字符串 $s$（由 `'L'` 和 `'R'` 组成），其中 `'L'` 和 `'R'` 的数量相等。

**要求**：将 $s$ 分割成尽可能多的子字符串，且每个子字符串都是平衡的（即 `'L'` 和 `'R'` 的数量相等）。返回最大分割数。

**说明**：

- $2 \le s.length \le 1000$。
- $s$ 只包含 `'L'` 和 `'R'`，且整体是平衡的。

**示例**：

- 示例 1：

```python
输入：s = "RLRRLLRLRL"
输出：4
解释：可以分割为 "RL"、"RRLL"、"RL"、"RL"。
```

- 示例 2：

```python
输入：s = "RLLLLRRRLR"
输出：3
解释：可以分割为 "RL"、"LLLRRR"、"LR"。
```

## 解题思路

### 思路 1：贪心计数

#### 1. 核心思想

从左向右遍历，维护一个计数器 $balance$：遇到 `'L'` 加 $1$，遇到 `'R'` 减 $1$（或反过来）。当 $balance == 0$ 时，说明从上一个平衡点开始到当前位置的字符串是平衡的，可以切分一次。

这种贪心策略是正确的：因为平衡字符串没有嵌套限制，只要 $balance$ 归零就可以切分。每次尽早切分可以得到最多的子串数。

#### 2. 具体步骤

**第 1 步**：初始化 $balance = 0$，$ans = 0$。

**第 2 步**：遍历 $s$ 中的每个字符 $ch$：
- 如果 $ch == \text{'L'}$，$balance += 1$。
- 如果 $ch == \text{'R'}$，$balance -= 1$。
- 如果 $balance == 0$，$ans += 1$。

**第 3 步**：返回 $ans$。

#### 3. 结合示例走一遍

$s = \text{"RLRRLLRLRL"}$

```
ch='R' → balance=-1
ch='L' → balance=0 → ans=1，切分 "RL"
ch='R' → balance=-1
ch='R' → balance=-2
ch='L' → balance=-1
ch='L' → balance=0 → ans=2，切分 "RRLL"
ch='R' → balance=-1
ch='L' → balance=0 → ans=3，切分 "RL"
ch='R' → balance=-1
ch='L' → balance=0 → ans=4，切分 "RL"
```

结果为 $4$。

### 思路 1：代码

```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        ans = 0
        for ch in s:
            if ch == 'L':
                balance += 1
            else:  # 'R'
                balance -= 1
            if balance == 0:
                ans += 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度。一次遍历。
- **空间复杂度**：$O(1)$，只使用常数变量。
