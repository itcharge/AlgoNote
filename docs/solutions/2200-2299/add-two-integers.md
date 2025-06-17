# [2235. 两整数相加](https://leetcode.cn/problems/add-two-integers/)

- 标签：数学
- 难度：简单

## 题目链接

- [2235. 两整数相加 - 力扣](https://leetcode.cn/problems/add-two-integers/)

## 题目大意

**描述**：给定两个整数 $num1$ 和 $num2$。

**要求**：返回这两个整数的和。

**说明**：

- $-100 \le num1, num2 \le 100$。

**示例**：

- 示例 1：

```python
示例 1：
输入：num1 = 12, num2 = 5
输出：17
解释：num1 是 12，num2 是 5，它们的和是 12 + 5 = 17，因此返回 17。
```

- 示例 2：

```python
输入：num1 = -10, num2 = 4
输出：-6
解释：num1 + num2 = -6，因此返回 -6。
```

## 解题思路

### 思路 1：直接计算

1. 直接计算整数 $num1$ 与 $num2$ 的和，返回 $num1 + num2$ 即可。

### 思路 1：代码

```python
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。
- **空间复杂度**：$O(1)$。
