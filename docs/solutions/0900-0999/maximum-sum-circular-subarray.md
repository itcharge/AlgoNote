# [0918. 环形子数组的最大和](https://leetcode.cn/problems/maximum-sum-circular-subarray/)

- 标签：队列、数组、分治、动态规划、单调队列
- 难度：中等

## 题目链接

- [0918. 环形子数组的最大和 - 力扣](https://leetcode.cn/problems/maximum-sum-circular-subarray/)

## 题目大意

给定一个环形整数数组 nums，数组 nums 的尾部和头部是相连状态。求环形数组 nums 的非空子数组的最大和（子数组中每个位置元素最多出现一次）。

## 解题思路

构成环形整数数组 nums 的非空子数组的最大和的子数组有两种情况：

- 最大和的子数组为一个子区间：$nums[i] + nums[i+1] + nums[i+2] + ... + num[j]$。
- 最大和的子数组为首尾的两个子区间：$(nums[0] + nums[1] + ... + nums[i]) + (nums[j] + nums[j+1] + ... + num[N-1])$。

第一种情况其实就是无环情况下的整数数组的非空子数组最大和问题，跟「[53. 最大子序和](https://leetcode.cn/problems/maximum-subarray/)」问题是一致的，我们假设求解结果为 `max_num`。

下来来思考第二种情况，第二种情况下，要使首尾两个子区间的和尽可能的大，则中间的子区间的和应该尽可能的小。

使得中间子区间的和尽可能小的问题，可以转变为求解：整数数组 nums 的非空子数组最小和问题。求解思路跟上边是相似的，只不过最大变为了最小。我们假设求解结果为 `min_num`。

而首尾两个区间和尽可能大的结果为数组 nums 的和减去中间最小子数组和，即 `sum(nums) - min_num`。

 最终的结果就是比较 `sum(nums) - min_num` 和 `max_num`的大小，返回较大值即可。

## 代码

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        size = len(nums)

        dp_max, dp_min = nums[0], nums[0]
        max_num, min_num = nums[0], nums[0]
        for i in range(1, size):
            dp_max = max(dp_max + nums[i], nums[i])
            dp_min = min(dp_min + nums[i], nums[i])
            max_num = max(dp_max, max_num)
            min_num = min(dp_min, min_num)
        sum_num = sum(nums)
        if max_num < 0:
            return max_num
        return max(sum_num - min_num, max_num)
```

