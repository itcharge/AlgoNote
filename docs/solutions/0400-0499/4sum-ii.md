# [0454. 四数相加 II](https://leetcode.cn/problems/4sum-ii/)

- 标签：数组、哈希表
- 难度：中等

## 题目链接

- [0454. 四数相加 II - 力扣](https://leetcode.cn/problems/4sum-ii/)

## 题目大意

**描述**：给定四个整数数组 $nums1$、$nums2$、$nums3$、$nums4$。

**要求**：计算有多少不同的 $(i, j, k, l)$ 满足以下条件。

1. $0 \le i, j, k, l < n$。
2. $nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0$。

**说明**：

- $n == nums1.length$。
- $n == nums2.length$。
- $n == nums3.length$。
- $n == nums4.length$。
- $1 \le n \le 200$。
- $-2^{28} \le nums1[i], nums2[i], nums3[i], nums4[i] \le 2^{28}$。

**示例**：

- 示例 1：

```python
输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
输出：2
解释：
两个元组如下：
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
```

- 示例 2：

```python
输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
输出：1
```

## 解题思路

### 思路 1：哈希表

直接暴力搜索的时间复杂度是 $O(n^4)$。我们可以降低一下复杂度。

将四个数组分为两组。$nums1$ 和 $nums2$ 分为一组，$nums3$ 和 $nums4$ 分为一组。

已知 $nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0$，可以得到 $nums1[i] + nums2[j] = -(nums3[k] + nums4[l])$

建立一个哈希表。两重循环遍历数组 $nums1$、$nums2$，先将 $nums[i] + nums[j]$ 的和个数记录到哈希表中，然后再用两重循环遍历数组 $nums3$、$nums4$。如果 $-(nums3[k] + nums4[l])$ 的结果出现在哈希表中，则将结果数累加到答案中。最终输出累加之后的答案。

### 思路 1：代码

```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums_dict = dict()
        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2
                if sum in nums_dict:
                    nums_dict[sum] += 1
                else:
                    nums_dict[sum] = 1
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                sum = num3 + num4
                if -sum in nums_dict:
                    count += nums_dict[-sum]

        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 为数组的元素个数。
- **空间复杂度**：$O(n^2)$。

