# [1365. 有多少小于当前数字的数字](https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/)

- 标签：数组、哈希表、计数排序
- 难度：简单

## 题目链接

- [1365. 有多少小于当前数字的数字 - 力扣](https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/)

## 题目大意

**描述**：给定一个数组 $nums$。

**要求**：返回一个数组 $ans$，其中 $ans[i]$ 是 $nums$ 中比 $nums[i]$ 小的数字的个数。

**说明**：
- $2 \le nums.length \le 500$。
- $0 \le nums[i] \le 100$。

**示例**：

- 示例 1：

```python
输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释： 
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。 
对于 nums[3]=2 存在一个比它小的数字：（1）。 
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
```

- 示例 2：

```python
输入：nums = [6,5,4,8]
输出：[2,1,0,3]
```


## 解题思路

### 思路 1：计数排序

#### 1. 核心思想

值范围只有 $0$ 到 $100$，可以用计数排序。统计每个值出现的次数，然后计算前缀和，$prefix[x-1]$ 就是比 $x$ 小的数的个数。

#### 2. 具体步骤

**第 1 步**：统计频率 $cnt$。

**第 2 步**：计算前缀和 $prefix[x] = \sum_{i=0}^{x} cnt[i]$。

**第 3 步**：对每个 $nums[i]$，$ans[i] = prefix[nums[i] - 1]$（如果 $nums[i] > 0$）。

### 思路 1：代码

```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0] * 101
        for num in nums:
            cnt[num] += 1
        prefix = [0] * 101
        for i in range(1, 101):
            prefix[i] = prefix[i - 1] + cnt[i - 1]
        return [prefix[num] for num in nums]
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(101)$。
