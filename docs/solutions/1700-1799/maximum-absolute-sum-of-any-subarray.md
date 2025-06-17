# [1749. 任意子数组和的绝对值的最大值](https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/)

- 标签：数组、动态规划
- 难度：中等

## 题目链接

- [1749. 任意子数组和的绝对值的最大值 - 力扣](https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/)

## 题目大意

**描述**：给定一个整数数组 $nums$。

**要求**：找出 $nums$ 中「和的绝对值」最大的任意子数组（可能为空），并返回最大值。

**说明**：

- **子数组 $[nums_l, nums_{l+1}, ..., nums_{r-1}, nums_{r}]$ 的和的绝对值**：$abs(nums_l + nums_{l+1} + ... + nums_{r-1} + nums_{r})$。
- $abs(x)$ 定义如下：
  - 如果 $x$ 是负整数，那么 $abs(x) = -x$。
  - 如果 $x$ 是非负整数，那么 $abs(x) = x$。

- $1 \le nums.length \le 10^5$。
- $-10^4 \le nums[i] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：nums = [1,-3,2,3,-4]
输出：5
解释：子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5。
```

- 示例 2：

```python
输入：nums = [2,-5,1,-4,3,-2]
输出：8
解释：子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8。
```

## 解题思路

### 思路 1：动态规划

子数组和的绝对值的最大值，可能来自于「连续子数组的最大和」，也可能来自于「连续子数组的最小和」。

而求解「连续子数组的最大和」，我们可以参考「[0053. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)」的做法，使用一个变量 $mmax$ 来表示以第 $i$ 个数结尾的连续子数组的最大和。使用另一个变量 $mmin$ 来表示以第 $i$ 个数结尾的连续子数组的最小和。然后取两者绝对值的最大值为答案 $ans$。

具体步骤如下：

1. 遍历数组 $nums$，对于当前元素 $nums[i]$：
   1. 如果 $mmax < 0$，则「第 $i - 1$ 个数结尾的连续子数组的最大和」+「第 $i$  个数的值」<「第 $i$ 个数的值」，所以 $mmax$ 应取「第 $i$ 个数的值」，即：$mmax = nums[i]$。
   2. 如果 $mmax \ge 0$ ，则「第 $i - 1$ 个数结尾的连续子数组的最大和」 +「第 $i$  个数的值」 >= 第 $i$ 个数的值，所以 $mmax$ 应取「第 $i - 1$ 个数结尾的连续子数组的最大和」 +「第 $i$  个数的值」，即：$mmax = mmax + nums[i]$。
   3. 如果 $mmin > 0$，则「第 $i - 1$ 个数结尾的连续子数组的最大和」+「第 $i$  个数的值」>「第 $i$ 个数的值」，所以 $mmax$ 应取「第 $i$ 个数的值」，即：$mmax = nums[i]$。
   4. 如果 $mmin \le 0$ ，则「第 $i - 1$ 个数结尾的连续子数组的最大和」 +「第 $i$  个数的值」 <= 第 $i$ 个数的值，所以 $mmax$ 应取「第 $i - 1$ 个数结尾的连续子数组的最大和」 +「第 $i$  个数的值」，即：$mmin = mmin + nums[i]$。
   5. 维护答案 $ans$，将 $mmax$ 和 $mmin$ 绝对值的最大值与 $ans$ 进行比较，并更新 $ans$。
2. 遍历完返回答案 $ans$。

### 思路 1：代码

```python
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0
        mmax, mmin = 0, 0
        for num in nums:
            mmax = max(mmax, 0) + num
            mmin = min(mmin, 0) + num
            ans = max(ans, mmax, -mmin)

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

