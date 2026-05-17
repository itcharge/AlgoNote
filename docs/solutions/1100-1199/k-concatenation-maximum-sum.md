# [1191. K 次串联后最大子数组之和](https://leetcode.cn/problems/k-concatenation-maximum-sum/)

- 标签：数组、动态规划
- 难度：中等

## 题目链接

- [1191. K 次串联后最大子数组之和 - 力扣](https://leetcode.cn/problems/k-concatenation-maximum-sum/)

## 题目大意

**描述**：给定一个整数数组 $arr$ 和一个整数 $k$。把 $arr$ 重复 $k$ 次拼成一个新数组。比如 $arr = [1, 2]$，$k = 3$，新数组就是 $[1,2,1,2,1,2]$。

**要求**：返回新数组中最大的子数组之和。子数组可以为空（和为 $0$）。结果可能很大，需要对 $10^9 + 7$ 取模。

**说明**：

- $1 \le arr.length \le 10^{5}$。
- $1 \le k \le 10^{5}$。
- $-10^{4} \le arr[i] \le 10^{4}$。

**示例**：

```python
输入：arr = [1,-2,1], k = 5
输出：2
```

## 解题思路

### 思路 1：Kadane 算法 + 分类讨论

这道题是经典「最大子数组和」的升级版。核心在于 $k$ 可能非常大（最多 $10^5$），不能真的把数组拼接 $k$ 次再算——那样数组长度会爆炸。

所以需要分类讨论，利用数学规律。

**先了解 Kadane 算法**（最大子数组和算法）：遍历数组时，维护当前累加和 `cur`，如果 `cur` 变成负数了就重置为 0（因为负数和只会拖累后面的数），同时记录遇到过的最大值。

**然后分情况讨论：**

1. **$k = 1$**：就是普通的 Kadane 算法。

2. **$k \ge 2$ 且数组总和 $\le 0$**：总和对整体没有正面贡献，最大子数组最多跨越两个数组（因为加上更多的完整数组只会让和变小或不变）。

3. **$k \ge 2$ 且数组总和 $> 0$**：中间那些完整数组的总和是有利的，可以全部加进来。所以最大和 = 最大后缀和（第一个数组的结尾部分）+ $(k-2) \times 总和$ + 最大前缀和（最后一个数组的开头部分）。

用人话理解：如果整个数组的和是正的，那把它反复拼接就像滚雪球——中间的完整段一直往上加，只会越滚越大。最后最大子数组一定是一个「前半截 + 中间好几整个数组 + 后半截」的结构。

**步骤拆解：**

1. 用 Kadane 算法算单个数组的最大子数组和。
2. 算数组总和、最大前缀和、最大后缀和。
3. 算两个数组拼接时的最大子数组和（把数组复制一遍，跑 Kadane）。
4. 用公式分情况决定最终答案。

### 思路 1：代码

```python
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # Kadane 算法：求一个数组的最大子数组和
        def kadane(nums):
            max_sum = 0  # 空子数组和为 0
            cur_sum = 0
            for num in nums:
                cur_sum = max(0, cur_sum + num)  # 如果变负数就重置为 0
                max_sum = max(max_sum, cur_sum)
            return max_sum
        
        # 情况 1：k = 1，普通 Kadane
        max_single = kadane(arr)
        if k == 1:
            return max_single % MOD
        
        total_sum = sum(arr)  # 数组总和
        
        # 计算最大前缀和（从开头往后的最大累加）
        max_prefix = 0
        cur = 0
        for num in arr:
            cur += num
            max_prefix = max(max_prefix, cur)
        
        # 计算最大后缀和（从结尾往前的最大累加）
        max_suffix = 0
        cur = 0
        for num in reversed(arr):
            cur += num
            max_suffix = max(max_suffix, cur)
        
        # 两个数组拼接时的最大子数组和
        max_double = kadane(arr + arr)
        
        # 情况 2 和 3：根据总和正负决定
        if total_sum > 0:
            # 总和为正，中间的完整数组都可以加进来
            result = max(max_double, max_prefix + max_suffix + (k - 2) * total_sum)
        else:
            # 总和为非正，最多跨越两个数组
            result = max_double
        
        return result % MOD
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。不管 $k$ 有多大，都只遍历原数组几次。
- **空间复杂度**：$O(n)$。计算两个数组拼接时需要临时创建一个 $2n$ 的数组。
