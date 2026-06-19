# [1318. 或运算的最小翻转次数](https://leetcode.cn/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

- 标签：位运算
- 难度：中等

## 题目链接

- [1318. 或运算的最小翻转次数 - 力扣](https://leetcode.cn/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

## 题目大意

**描述**：给定三个整数 $a$、$b$、$c$。每次可以将 $a$ 或 $b$ 的某一位翻转（$0 \to 1$ 或 $1 \to 0$）。

**要求**：返回使 $a | b == c$ 所需的最小翻转次数。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/11/sample_3_1676.png)

```python
输入：a = 2, b = 6, c = 5
输出：3
解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c
```

- 示例 2：

```python
输入：a = 4, b = 2, c = 7
输出：1
```


## 解题思路

### 思路 1：逐位检查

#### 1. 核心思想

逐位比较 $c$ 和 $a|b$。如果 $c$ 的某位为 $0$，则 $a$ 和 $b$ 的该位都需要为 $0$，翻转次数为 $a$ 和 $b$ 该位的 $1$ 的个数。如果 $c$ 的某位为 $1$，则 $a$ 或 $b$ 至少有一位为 $1$，如果都是 $0$ 则需要翻转 $1$ 次。

#### 2. 代码

```python
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            ca, cb, cc = (a >> i) & 1, (b >> i) & 1, (c >> i) & 1
            if cc == 0:
                ans += ca + cb
            else:
                if ca == 0 and cb == 0:
                    ans += 1
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(1)$。
- **空间复杂度**：$O(1)$。
