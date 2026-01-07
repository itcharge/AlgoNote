# [0870. 优势洗牌](https://leetcode.cn/problems/advantage-shuffle/)

- 标签：贪心、数组、双指针、排序
- 难度：中等

## 题目链接

- [0870. 优势洗牌 - 力扣](https://leetcode.cn/problems/advantage-shuffle/)

## 题目大意

**描述**：

给定两个长度相等的数组 $nums1$ 和 $nums2$，$nums1$ 相对于 $nums2$ 的优势可以用满足 $nums1[i] > nums2[i]$ 的索引 $i$ 的数目来描述。

**要求**：

返回 $nums1$ 的 任意 排列，使其相对于 $nums2$ 的优势最大化。

**说明**：

- $1 \le nums1.length \le 10^{5}$。
- $nums2.length == nums1.length$。
- $0 \le nums1[i], nums2[i] \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
输出：[2,11,7,15]
```

- 示例 2：

```python
输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
输出：[24,32,8,12]
```

## 解题思路

### 思路 1：贪心 + 双指针（田忌赛马）

这道题本质上是经典的"田忌赛马"问题。目标是最大化 $nums1$ 相对于 $nums2$ 的优势。

贪心策略：
1. 将 $nums1$ 排序。
2. 将 $nums2$ 的元素及其索引一起排序。
3. 使用双指针：
   - 对于 $nums2$ 中的每个元素（从大到小），尝试用 $nums1$ 中最大的能战胜它的元素。
   - 如果 $nums1$ 中最大的元素都无法战胜，则用 $nums1$ 中最小的元素（反正也赢不了，不如浪费最小的）。

具体实现：

1. 对 $nums1$ 排序。
2. 对 $nums2$ 的索引按值从大到小排序。
3. 使用左右指针遍历 $nums1$，对于 $nums2$ 中的每个元素（从大到小）：
   - 如果 $nums1$ 的右指针元素能战胜，使用它，右指针左移。
   - 否则，使用 $nums1$ 的左指针元素（最小的），左指针右移。

### 思路 1：代码

```python
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        
        # 对 nums1 排序
        nums1.sort()
        
        # 对 nums2 的索引按值从大到小排序
        idx2 = sorted(range(n), key=lambda i: nums2[i], reverse=True)
        
        # 结果数组
        result = [0] * n
        
        # 双指针
        left, right = 0, n - 1
        
        # 从大到小遍历 nums2
        for i in idx2:
            # 如果 nums1 的最大值能战胜 nums2[i]，使用它
            if nums1[right] > nums2[i]:
                result[i] = nums1[right]
                right -= 1
            else:
                # 否则用 nums1 的最小值（反正也赢不了）
                result[i] = nums1[left]
                left += 1
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是数组的长度。排序需要 $O(n \log n)$。
- **空间复杂度**：$O(n)$，需要存储排序后的索引和结果数组。
