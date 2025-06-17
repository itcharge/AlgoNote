# [1646. 获取生成数组中的最大值](https://leetcode.cn/problems/get-maximum-in-generated-array/)

- 标签：数组、动态规划、模拟
- 难度：简单

## 题目链接

- [1646. 获取生成数组中的最大值 - 力扣](https://leetcode.cn/problems/get-maximum-in-generated-array/)

## 题目大意

**描述**：给定一个整数 $n$，按照下述规则生成一个长度为 $n + 1$ 的数组 $nums$：

- $nums[0] = 0$。
- $nums[1] = 1$。
- 当 $2 \le 2 \times i \le n$ 时，$nums[2 \times i] = nums[i]$。
- 当 $2 \le 2 \times i + 1 \le n$ 时，$nums[2 \times i + 1] = nums[i] + nums[i + 1]$。

**要求**：返回生成数组 $nums$ 中的最大值。

**说明**：

- $0 \le n \le 100$。

**示例**：

- 示例 1：

```python
输入：n = 7
输出：3
解释：根据规则：
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
因此，nums = [0,1,1,2,1,3,2,3]，最大值 3
```

- 示例 2：

```python
输入：n = 2
输出：1
解释：根据规则，nums[0]、nums[1] 和 nums[2] 之中的最大值是 1
```

## 解题思路

### 思路 1：模拟

1. 按照题目要求，定义一个长度为 $n + 1$ 的数组 $nums$。
2. 按照规则模拟生成对应的 $nums$ 数组元素。
3. 求出数组 $nums$ 中最大值，并作为答案返回。

### 思路 1：代码

```python
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
            
        nums = [0 for _ in range(n + 1)]
        nums[1] = 1

        for i in range(n):
            if 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]

        ans = max(nums)
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
