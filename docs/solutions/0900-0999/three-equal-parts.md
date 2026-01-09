# [0927. 三等分](https://leetcode.cn/problems/three-equal-parts/)

- 标签：数组、数学
- 难度：困难

## 题目链接

- [0927. 三等分 - 力扣](https://leetcode.cn/problems/three-equal-parts/)

## 题目大意

**描述**：

给定一个由 0 和 1 组成的数组 $arr$ ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。

**要求**：

如果可以做到，请返回任何 $[i, j]$，其中 $i+1 < j$，这样一来：

- $arr[0], arr[1], ..., arr[i]$ 为第一部分；
- $arr[i + 1], arr[i + 2], ..., arr[j - 1]$ 为第二部分；
- $arr[j], arr[j + 1], ..., arr[arr.length - 1]$ 为第三部分。
- 这三个部分所表示的二进制值相等。

如果无法做到，就返回 $[-1, -1]$。

注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，$[1,1,0]$ 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 $[0,1,1]$ 和 $[1,1]$ 表示相同的值。

**说明**：

- $3 \le arr.length \le 3 * 10^{4}$。
- $arr[i]$ 是 0 或 1。

**示例**：

- 示例 1：

```python
输入：arr = [1,0,1,0,1]
输出：[0,3]
```

- 示例 2：

```python
输入：arr = [1,1,0,1,1]
输出：[-1,-1]

示例 3:


输入：arr = [1,1,0,0,1]
输出：[0,2]
```

## 解题思路

### 思路 1：数学 + 双指针

要将数组分成三个表示相同二进制值的部分，首先需要统计 $1$ 的个数。

1. 统计数组中 $1$ 的总个数 $ones$。
2. 如果 $ones$ 不能被 $3$ 整除，返回 $[-1, -1]$。
3. 如果 $ones = 0$，说明全是 $0$，返回 $[0, n - 1]$。
4. 每部分应该有 $ones / 3$ 个 $1$。
5. 找到三部分的起始位置（第一个 $1$ 的位置）。
6. 从最后一部分的第一个 $1$ 开始，向前匹配三部分，确保它们表示相同的二进制值。
7. 最后一部分的尾部 $0$ 决定了前两部分的尾部 $0$ 的数量。

### 思路 1：代码

```python
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ones = sum(arr)
        
        # 如果 1 的个数不能被 3 整除，无法分成三等分
        if ones % 3 != 0:
            return [-1, -1]
        
        # 如果全是 0，任意分割都可以
        if ones == 0:
            return [0, n - 1]
        
        # 每部分应该有 k 个 1
        k = ones // 3
        
        # 找到三部分的第一个 1 的位置
        first = second = third = -1
        count = 0
        for i in range(n):
            if arr[i] == 1:
                count += 1
                if count == 1:
                    first = i
                elif count == k + 1:
                    second = i
                elif count == 2 * k + 1:
                    third = i
                    break
        
        # 从第三部分开始，向前匹配
        while third < n:
            if arr[first] != arr[second] or arr[second] != arr[third]:
                return [-1, -1]
            first += 1
            second += 1
            third += 1
        
        # 返回分割点
        return [first - 1, second]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $arr$ 的长度。
- **空间复杂度**：$O(1)$，只使用了常数级别的额外空间。
