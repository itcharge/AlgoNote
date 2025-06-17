# [0179. 最大数](https://leetcode.cn/problems/largest-number/)

- 标签：贪心、数组、字符串、排序
- 难度：中等

## 题目链接

- [0179. 最大数 - 力扣](https://leetcode.cn/problems/largest-number/)

## 题目大意

**描述**：给定一个非负整数数组 `nums`。

**要求**：重新排列数组中每个数的顺序，使之将数组中所有数字按顺序拼接起来所组成的整数最大。

**说明**：

- $1 \le nums.length \le 100$。
- $0 \le nums[i] \le 10^9$。

**示例**：

- 示例 1：

```python
输入：nums = [10,2]
输出："210"
```

- 示例 2：

```python
输入：nums = [3,30,34,5,9]
输出："9534330"
```

## 解题思路

### 思路 1：排序

本质上是给数组进行排序。假设 `x`、`y` 是数组 `nums` 中的两个元素。如果拼接字符串 `x + y < y + x`，则 `y > x `。`y` 应该排在 `x` 前面。反之，则 `y < x`。

按照上述规则，对原数组进行排序即可。这里我们使用了 `functools.cmp_to_key` 自定义排序函数。

### 思路 1：代码

```python
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        nums_s = list(map(str, nums))
        nums_s.sort(key=functools.cmp_to_key(cmp), reverse=True)
        return str(int(''.join(nums_s)))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$。其中 $n$ 是给定数组 `nums` 的大小。
- **空间复杂度**：$O(n)$。