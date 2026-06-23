# [1403. 非递增顺序的最小子序列](https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/)

- 标签：贪心、数组、排序
- 难度：简单

## 题目链接

- [1403. 非递增顺序的最小子序列 - 力扣](https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/)

## 题目大意

**描述**：给定一个数组 $nums$。

**要求**：返回一个「最小子序列」，满足子序列的元素之和严格大于剩余元素之和。如果有多个，返回长度最小的。如果长度相同，返回元素和最大的（等价于子序列字典序最大的，因为按降序排列）。

**说明**：
- $1 \le nums.length \le 500$。
- $1 \le nums[i] \le 100$。

**示例**：

- 示例 1：

```python
输入：nums = [4,3,10,9,8]
输出：[10,9] 
解释：子序列 [10,9] 和 [10,8] 是最小的、满足元素之和大于其他各元素之和的子序列。但是 [10,9] 的元素之和最大。
```

- 示例 2：

```python
输入：nums = [4,4,7,6,7]
输出：[7,7,6] 
解释：子序列 [7,7] 的和为 14 ，不严格大于剩下的其他元素之和（14 = 4 + 4 + 6）。因此，[7,6,7] 是满足题意的最小子序列。注意，元素按非递增顺序返回。
```

## 解题思路

### 思路 1：贪心

#### 1. 核心思想

要满足子序列和 > 剩余和，且子序列尽可能短（元素尽可能大），贪心地选择最大的元素即可。

#### 2. 具体步骤

**第 1 步**：计算总和 $total$。

**第 2 步**：降序排序 $nums$。

**第 3 步**：遍历排序后的数组，依次取最大的元素，累加 $cur\_sum$，直到 $cur\_sum > total - cur\_sum$。

**第 4 步**：返回已取的元素列表。

#### 3. 举例说明

以 $nums = [4,3,10,9,8]$ 为例：

降序排序：$[10,9,8,4,3]$

- 取 $10$，$cur=10, rest=24-10=14$，$10 \le 14$，继续
- 取 $9$，$cur=19, rest=5$，$19 > 5$，停止

结果：$[10, 9]$。

### 思路 1：代码

```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        nums.sort(reverse=True)
        cur = 0
        ans = []
        for x in nums:
            cur += x
            ans.append(x)
            if cur > total - cur:
                break
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，排序。
- **空间复杂度**：$O(1)$（不包含返回值）。
