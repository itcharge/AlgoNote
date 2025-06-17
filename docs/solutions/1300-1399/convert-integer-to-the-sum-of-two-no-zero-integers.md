# [1317. 将整数转换为两个无零整数的和](https://leetcode.cn/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

- 标签：数学
- 难度：简单

## 题目链接

- [1317. 将整数转换为两个无零整数的和 - 力扣](https://leetcode.cn/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

## 题目大意

**描述**：给定一个整数 $n$。

**要求**：返回一个由两个整数组成的列表 $[A, B]$，满足：

- $A$ 和 $B$ 都是无零整数。
- $A + B = n$。

**说明**：

- **无零整数**：十进制表示中不含任何 $0$ 的正整数。
- 题目数据保证至少一个有效的解决方案。
- 如果存在多个有效解决方案，可以返回其中任意一个。
- $2 \le n \le 10^4$。

**示例**：

- 示例 1：

```python
输入：n = 2
输出：[1,1]
解释：A = 1, B = 1. A + B = n 并且 A 和 B 的十进制表示形式都不包含任何 0。
```

- 示例 2：

```python
输入：n = 11
输出：[2,9]
```

## 解题思路

### 思路 1：枚举

1. 由于给定的 $n$ 范围为 $[1, 10000]$，比较小，我们可以直接在 $[1, n)$ 的范围内枚举 $A$，并通过 $n - A$ 得到 $B$。
2. 在判断 $A$ 和 $B$ 中是否都不包含 $0$。如果都不包含 $0$，则返回 $[A, B]$。

### 思路 1：代码

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for A in range(1, n):
            B = n - A
            if '0' not in str(A) and '0' not in str(B):
                return [A, B]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$。
- **空间复杂度**：$O(1)$。

