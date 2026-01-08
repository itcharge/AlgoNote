# [0805. 数组的均值分割](https://leetcode.cn/problems/split-array-with-same-average/)

- 标签：位运算、数组、数学、动态规划、状态压缩
- 难度：困难

## 题目链接

- [0805. 数组的均值分割 - 力扣](https://leetcode.cn/problems/split-array-with-same-average/)

## 题目大意

**描述**：

给定你一个整数数组 $nums$。

我们要将 $nums$ 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 `average(A) == average(B)`。

**要求**：

如果可以完成则返回 true，否则返回 false。

**说明**：

- 注意：对于数组 $arr$, `average(arr)` 是 $arr$ 的所有元素的和除以 $arr$ 长度。
- $1 \le nums.length \le 30$。
- $0 \le nums[i] \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入: nums = [1,2,3,4,5,6,7,8]
输出: true
解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
```

- 示例 2：

```python
输入: nums = [3,1]
输出: false
```

## 解题思路

### 思路 1:动态规划 + 状态压缩

设数组总和为 $sum$,长度为 $n$。如果能将数组分成两部分 $A$ 和 $B$,使得它们的平均值相等,则:
$$\frac{\sum A}{|A|} = \frac{\sum B}{|B|} = \frac{sum}{n}$$

即:$\sum A \times n = sum \times |A|$

因此,我们需要找到一个子集 $A$,使得 $\sum A = \frac{sum \times |A|}{n}$。

枚举子集大小 $k$(从 1 到 $n/2$),使用动态规划判断是否存在大小为 $k$、和为 $\frac{sum \times k}{n}$ 的子集。

定义 $dp[k]$ 为所有大小为 $k$ 的子集的和的集合。

### 思路 1:代码

```python
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        
        # 特判
        if n == 1:
            return False
        
        # dp[k] 存储所有大小为 k 的子集的和
        dp = [set() for _ in range(n // 2 + 1)]
        dp[0].add(0)
        
        for num in nums:
            # 倒序遍历,避免重复使用
            for k in range(n // 2, 0, -1):
                for s in list(dp[k - 1]):
                    dp[k].add(s + num)
        
        # 检查是否存在满足条件的子集
        for k in range(1, n // 2 + 1):
            # 检查 sum * k 是否能被 n 整除
            if (total * k) % n == 0:
                target = (total * k) // n
                if target in dp[k]:
                    return True
        
        return False
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(n^2 \times sum)$,其中 $n$ 是数组长度,$sum$ 是数组总和。需要枚举所有子集。
- **空间复杂度**:$O(n \times sum)$,需要存储所有可能的子集和。
