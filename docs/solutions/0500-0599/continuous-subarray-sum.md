# [0523. 连续的子数组和](https://leetcode.cn/problems/continuous-subarray-sum/)

- 标签：数组、哈希表、数学、前缀和
- 难度：中等

## 题目链接

- [0523. 连续的子数组和 - 力扣](https://leetcode.cn/problems/continuous-subarray-sum/)

## 题目大意

**描述**：

给定一个整数数组 $nums$ 和一个整数 $k$。

**要求**：

如果 $nums$ 有一个「好的子数组」返回 true，否则返回 false：

**说明**：

- 一个「好的子数组」是：
   - 长度至少为 $2$ ，且
   - 子数组元素总和为 $k$ 的倍数。
   - 注意：
      - 子数组是数组中连续的部分。
      - 如果存在一个整数 $n$，令整数 $x$ 符合 $x = n \times k$，则称 $x$ 是 $k$ 的一个倍数。$0$ 始终视为 $k$ 的一个倍数。
- $1 \le nums.length \le 10^{5}$。
- $0 \le nums[i] \le 10^{9}$。
- $0 \le sum(nums[i]) \le 2^{31} - 1$。
- $1 \le k \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
```

- 示例 2：

```python
输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
```

## 解题思路

### 思路 1：前缀和 + 哈希表

这道题要求找到长度至少为 $2$ 的连续子数组，其元素和为 $k$ 的倍数。

核心思路：利用同余定理。如果两个前缀和 $preSum[i]$ 和 $preSum[j]$ 对 $k$ 取模的结果相同，那么区间 $[i+1, j]$ 的元素和就是 $k$ 的倍数。

具体步骤：

1. 使用哈希表 $remainder\_map$ 存储前缀和对 $k$ 取模的余数及其第一次出现的位置。
2. 初始化 $remainder\_map[0] = -1$，表示前缀和为 $0$ 的位置在索引 $-1$（方便处理从索引 $0$ 开始的子数组）。
3. 遍历数组，计算当前前缀和 $preSum$ 对 $k$ 的余数 $remainder$。
4. 如果 $remainder$ 已经在哈希表中，且当前位置与该余数第一次出现位置的距离至少为 $2$，返回 $True$。
5. 如果 $remainder$ 不在哈希表中，将其加入哈希表。

### 思路 1：代码

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 哈希表存储余数及其第一次出现的位置
        remainder_map = {0: -1}
        pre_sum = 0
        
        for i in range(len(nums)):
            # 计算前缀和
            pre_sum += nums[i]
            # 计算余数
            remainder = pre_sum % k
            
            # 如果余数已存在
            if remainder in remainder_map:
                # 检查子数组长度是否至少为 2
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # 记录余数第一次出现的位置
                remainder_map[remainder] = i
        
        return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组长度，只需遍历一次数组。
- **空间复杂度**：$O(min(n, k))$，哈希表最多存储 $k$ 个不同的余数。
