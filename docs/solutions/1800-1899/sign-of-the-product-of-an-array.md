# [1822. 数组元素积的符号](https://leetcode.cn/problems/sign-of-the-product-of-an-array/)

- 标签：数组、数学
- 难度：简单

## 题目链接

- [1822. 数组元素积的符号 - 力扣](https://leetcode.cn/problems/sign-of-the-product-of-an-array/)

## 题目大意

**描述**：已知函数 `signFunc(x)` 会根据 `x` 的正负返回特定值：

- 如果 `x` 是正数，返回 `1`。
- 如果 `x` 是负数，返回 `-1`。
- 如果 `x` 等于 `0`，返回 `0`。

现在给定一个整数数组 `nums`。令 `product` 为数组 `nums` 中所有元素值的乘积。

**要求**：返回 `signFun(product)` 的值。

**说明**：

- $1 \le nums.length \le 1000$。
- $-100 \le nums[i] \le 100$。

**示例**：

- 示例 1：

```python
输入 nums = [-1,-2,-3,-4,3,2,1]
输出 1
解释 数组中所有值的乘积是 144，且 signFunc(144) = 1
```

## 解题思路

### 思路 1：

题目要求的是数组所有值乘积的正负性，但是我们没必要将所有数乘起来再判断正负性。只需要统计出数组中负数的个数，再加以判断即可。

- 使用变量 `minus_count` 记录数组中负数个数。
- 然后遍历数组 `nums`，对于当前元素 `num`：
  - 如果为 `0`，则最终乘积肯定为 `0`，直接返回 `0`。
  - 如果小于 `0`，负数个数加 `1`。
- 最终统计出数组中负数的个数为 `minus_count`。
- 如果 `minus_count` 是 `2` 的倍数，则说明最终乘积为正数，返回 `1`。
- 如果 `minus_count` 不是 `2` 的倍数，则说明最终乘积为负数，返回 `-1`。

## 代码

### 思路 1 代码：

```python
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        minus_count = 0
        for num in nums:
            if num < 0:
                minus_count += 1
            elif num == 0:
                return 0

        if minus_count % 2 == 0:
            return 1
        else:
            return -1
```

