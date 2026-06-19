# [1374. 生成每种字符都是奇数个的字符串](https://leetcode.cn/problems/generate-a-string-with-characters-that-have-odd-counts/)

- 标签：字符串
- 难度：简单

## 题目链接

- [1374. 生成每种字符都是奇数个的字符串 - 力扣](https://leetcode.cn/problems/generate-a-string-with-characters-that-have-odd-counts/)

## 题目大意

**描述**：给定一个整数 $n$。

**要求**：返回一个长度为 $n$ 的字符串，其中每种字符的出现次数都是奇数。

**示例**：

- 示例 1：

```python
输入：n = 4
输出："pppz"
解释："pppz" 是一个满足题目要求的字符串，因为 'p' 出现 3 次，且 'z' 出现 1 次。当然，还有很多其他字符串也满足题目要求，比如："ohhh" 和 "love"。
```

- 示例 2：

```python
输入：n = 2
输出："xy"
解释："xy" 是一个满足题目要求的字符串，因为 'x' 和 'y' 各出现 1 次。当然，还有很多其他字符串也满足题目要求，比如："ag" 和 "ur"。
```


## 解题思路

### 思路 1：分类构造

#### 1. 核心思想

如果 $n$ 是奇数，全部用 `'a'`（出现 $n$ 次，奇数）。如果 $n$ 是偶数，放 $n-1$ 个 `'a'` 和 $1$ 个 `'b'`（$a$ 出现 $n-1$ 次，奇数；$b$ 出现 $1$ 次，奇数）。

#### 2. 代码

```python
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a' * n
        return 'a' * (n - 1) + 'b'
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
