# [0561. 数组拆分](https://leetcode.cn/problems/array-partition/)

- 标签：贪心、数组、计数排序、排序
- 难度：简单

## 题目链接

- [0561. 数组拆分 - 力扣](https://leetcode.cn/problems/array-partition/)

## 题目大意

**描述**：给定一个长度为 $2 \times n$ 的整数数组 $nums$。

**要求**：将数组中的数拆分成 $n$ 对，每对数求最小值，求 $n$ 对数最小值的最大总和是多少。

**说明**：

- $1 \le n \le 10^4$。
- $nums.length == 2 * n$。
- $-10^4 \le nums[i] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：nums = [1,4,3,2]
输出：4
解释：所有可能的分法（忽略元素顺序）为：
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
所以最大总和为 4
```
- 示例 2：

```python
输入：nums = [6,2,6,5,1,2]
输出：9
解释：最优的分法为 (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9
```

## 解题思路

### 思路 1：计数排序

因为 $nums[i]$ 的范围为 $[-10^4, 10^4]$，范围不是很大，所以我们可以使用计数排序算法先将数组 $nums$ 进行排序。

要想每对数最小值的总和最大，就得使每对数的最小值尽可能大。只有让较大的数与较大的数一起组合，较小的数与较小的数一起结合，才能才能使总和最大。所以，排序完之后将相邻两个元素的最小值进行相加，即得到结果。

###  思路 1：代码

```python
class Solution:
    def countingSort(self, nums: [int]) -> [int]:
        # 计算待排序数组中最大值元素 nums_max 和最小值元素 nums_min
        nums_min, nums_max = min(nums), max(nums)
        # 定义计数数组 counts，大小为 最大值元素 - 最小值元素 + 1
        size = nums_max - nums_min + 1
        counts = [0 for _ in range(size)]
        
        # 统计值为 num 的元素出现的次数
        for num in nums:
            counts[num - nums_min] += 1
        
        # 生成累积计数数组
        for i in range(1, size):
            counts[i] += counts[i - 1]

        # 反向填充目标数组
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            # 根据累积计数数组，将 num 放在数组对应位置
            res[counts[num - nums_min] - 1] = num
            # 将 num 的对应放置位置减 1，从而得到下个元素 num 的放置位置
            counts[nums[i] - nums_min] -= 1

        return res

    def arrayPairSum(self, nums: List[int]) -> int:
        nums = self.countingSort(nums)
        return sum(nums[::2])
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + k)$，其中 $k$ 代表数组 $nums$ 的值域。
- **空间复杂度**：$O(k)$。

### 思路 2：排序

要想每对数最小值的总和最大，就得使每对数的最小值尽可能大。只有让较大的数与较大的数一起组合，较小的数与较小的数一起结合，才能才能使总和最大。

1. 对 $nums$ 进行排序。
2. 将相邻两个元素的最小值进行相加，即得到结果。

### 思路 1：代码

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$。
- **空间复杂度**：$O(1)$。

