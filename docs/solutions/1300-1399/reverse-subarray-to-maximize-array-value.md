# [1330. 翻转子数组得到最大的数组值](https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/)

- 标签：贪心、数组、数学
- 难度：困难

## 题目链接

- [1330. 翻转子数组得到最大的数组值 - 力扣](https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/)

## 题目大意

**描述**：给定一个整数数组 $nums$，数组值定义为 $\sum_{i=1}^{n-1} |nums[i] - nums[i-1]|$。可以选择任意子数组 $nums[l \dots r]$ 进行翻转（即变成 $nums[r], nums[r-1], \dots, nums[l]$），可以翻转 $0$ 次或 $1$ 次。

**要求**：返回翻转后可能得到的最大数组值。

**说明**：
- $1 \le nums.length \le 3 \times 10^4$。
- $-10^5 \le nums[i] \le 10^5$。

**示例**：

- 示例 1：

```python
输入：nums = [2,3,1,5,4]
输出：10
解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。
```

- 示例 2：

```python
输入：nums = [2,4,9,24,2,1,10]
输出：68
```


## 解题思路

### 思路 1：数学推导 + 贪心

#### 1. 核心思想

翻转操作只改变了子数组两端的相邻关系，子数组内部的差值和没有变化（因为绝对值翻转后相同）。因此只需考虑翻转带来的边界变化。

在不翻转的情况下，数组值 = 所有相邻差的绝对值之和。

翻转子数组 $nums[l \dots r]$ 后，只有 $l-1$ 和 $l$ 之间、$r$ 和 $r+1$ 之间的相邻关系发生变化：
- 原贡献：$|nums[l] - nums[l-1]| + |nums[r+1] - nums[r]|$
- 新贡献：$|nums[r] - nums[l-1]| + |nums[r+1] - nums[l]|$

数组值的变化量 = 新贡献 - 原贡献。

目标是最大化这个变化量。

#### 2. 数学简化

对于四个数 $a=nums[l-1], b=nums[l], c=nums[r], d=nums[r+1]$：
- 原贡献：$|b-a| + |d-c|$
- 新贡献：$|c-a| + |d-b|$

变化量 $\Delta = (|c-a| + |d-b|) - (|b-a| + |d-c|)$。

利用绝对值不等式推导，可以证明最大变化量等于 $2 \times \max(0, \min(b,d) - \max(a,c))$ 的某种形式。

更简洁的等价形式：最大增量 = $2 \times \max(0, \min(nums[i-1], nums[i]) - \max(nums[j-1], nums[j]))$ 对于所有 $i, j$。

为了求这个最大值，可以遍历数组，维护 $\min(nums[i-1], nums[i])$ 的最大值和 $\max(nums[i-1], nums[i])$ 的最小值。

#### 3. 具体步骤

**第 1 步**：计算原始数组值 $base$。

**第 2 步**：遍历 $i$ 从 $1$ 到 $n-1$，计算：
- $low = \min(nums[i-1], nums[i])$（每对中较小的数）
- $high = \max(nums[i-1], nums[i])$（每对中较大的数）

**第 3 步**：维护所有 $low$ 的最大值 $max\_low$，以及所有 $high$ 的最小值 $min\_high$。

**第 4 步**：如果 $max\_low > min\_high$，说明存在可以增加数组值的翻转。$gain = 2 \times (max\_low - min\_high)$。

**第 5 步**：最终结果 = $base + gain$。

#### 4. 边界情况

翻转整个数组（$l=0$）或翻转后缀/前缀时，只有一个边界变化，也需要考虑。

更一般化，考虑所有可能的翻转，最终公式为：

$$result = base + \max(0, 2 \times (max\_low - min\_high))$$

同时对两端边界情况（$l=0$ 和 $r=n-1$）取最大值。

#### 5. 举例说明

以 $nums = [2, 3, 1, 5, 4]$ 为例：

原始数组值：$|3-2| + |1-3| + |5-1| + |4-5| = 1 + 2 + 4 + 1 = 8$

相邻对：
- $(2,3)$: low=2, high=3
- $(3,1)$: low=1, high=3
- $(1,5)$: low=1, high=5
- $(5,4)$: low=4, high=5

$max\_low = 4$，$min\_high = 3$
$gain = 2 \times (4 - 3) = 2$

最终结果 = $8 + 2 = 10$。

验证：翻转 $[3, 1, 5]$ 得到 $[2, 5, 1, 3, 4]$，数组值 = 10。

### 思路 1：代码

```python
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # 第 1 步：计算原始数组值
        base = 0
        for i in range(1, n):
            base += abs(nums[i] - nums[i - 1])

        # 第 2 步：寻找最优翻转增量
        max_low = float('-inf')  # 所有 min(nums[i-1], nums[i]) 的最大值
        min_high = float('inf')  # 所有 max(nums[i-1], nums[i]) 的最小值

        for i in range(1, n):
            low = min(nums[i - 1], nums[i])
            high = max(nums[i - 1], nums[i])
            max_low = max(max_low, low)
            min_high = min(min_high, high)

        # 基本增益
        gain = max(0, 2 * (max_low - min_high))

        # 第 3 步：考虑边界翻转的增益
        # 翻转前缀 nums[0..r]：只改变边界 nums[r] 和 nums[r+1]
        for i in range(1, n - 1):
            # 翻转 nums[0..i]
            gain = max(gain, abs(nums[i + 1] - nums[0]) - abs(nums[i + 1] - nums[i]))
            # 翻转 nums[i..n-1]
            gain = max(gain, abs(nums[n - 1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]))

        return base + gain
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，一次遍历计算基础值和边界情况。
- **空间复杂度**：$O(1)$，只使用常数额外空间。

