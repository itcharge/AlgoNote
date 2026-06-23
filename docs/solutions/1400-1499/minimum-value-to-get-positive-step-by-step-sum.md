# [1413. 逐步求和得到正数的最小值](https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum/)

- 标签：数组、前缀和
- 难度：简单

## 题目链接

- [1413. 逐步求和得到正数的最小值 - 力扣](https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum/)

## 题目大意

**描述**：给定一个整数数组 $nums$。选择起始值 $startValue$，然后对 $nums$ 做逐元素累加，要求累加过程中的每个中间值都 $\ge 1$。

**要求**：返回满足条件的最小正数 $startValue$。

**说明**：
- $1 \le nums.length \le 100$。
- $-100 \le nums[i] \le 100$。

**示例**：

- 示例 1：

```python
输入：nums = [-3,2,-3,4,2]
输出：5
解释：如果你选择 startValue = 4，在第三次累加时，和小于 1 。
                累加求和
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
```

- 示例 2：

```python
输入：nums = [1,2]
输出：1
解释：最小的 startValue 需要是正数。
```

## 解题思路

### 思路 1：前缀和最小值

#### 1. 核心思想

设前缀和数组 $prefix$，$prefix[i] = nums[0] + \dots + nums[i-1]$。累加过程中第 $i$ 步的值为 $startValue + prefix[i]$。

要求 $startValue + prefix[i] \ge 1$ 对所有 $i$ 成立，等价于 $startValue \ge 1 - \min(prefix)$。

因此 $startValue = \max(1, 1 - \min\_prefix)$。

#### 2. 具体步骤

**第 1 步**：遍历计算前缀和，同时记录最小值 $min\_prefix$。

**第 2 步**：返回 $\max(1, 1 - min\_prefix)$。

#### 3. 举例说明

以 $nums = [-3, 2, -3, 4, 2]$ 为例：

$prefix = [0, -3, -1, -4, 0, 2]$
$min\_prefix = -4$

$startValue = \max(1, 1 - (-4)) = 5$

验证：$5-3=2\ge1, 2+2=4\ge1, 4-3=1\ge1, 1+4=5\ge1, 5+2=7\ge1$ ✓

### 思路 1：代码

```python
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix = 0
        for x in nums:
            prefix += x
            min_prefix = min(min_prefix, prefix)
        return max(1, 1 - min_prefix)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。
