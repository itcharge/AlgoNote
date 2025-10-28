# [0493. 翻转对](https://leetcode.cn/problems/reverse-pairs/)

- 标签：树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
- 难度：困难

## 题目链接

- [0493. 翻转对 - 力扣](https://leetcode.cn/problems/reverse-pairs/)

## 题目大意

**描述**：

给定一个数组 $nums$，如果 $i < j$ 且 $nums[i] > 2 \times nums[j]$ 我们就将 $(i, j)$ 称作一个重要翻转对。

**要求**：

返回给定数组中的重要翻转对的数量。

**说明**：

- 给定数组的长度不会超过 $50000$。
- 输入数组中的所有数字都在 32 位整数的表示范围内。

**示例**：

- 示例 1：

```python
输入: [1,3,2,3,1]
输出: 2
```

- 示例 2：

```python
输入: [2,4,3,5,1]
输出: 3
```

## 解题思路

### 思路 1：归并排序 + 分治思想

**核心思想**：翻转对问题可以转化为在归并排序过程中统计满足 $nums[i] > 2 \times nums[j]$ 且 $i < j$ 的 $(i, j)$ 对的数量。

**算法步骤**：

1. **分解**：将数组分成左右两部分，分别统计左右两部分内部的翻转对数量。
2. **合并前统计**：在合并左右两部分之前，统计跨越中点的翻转对数量（即 $i$ 在左半部分，$j$ 在右半部分）。
3. **合并**：按照归并排序的方式合并左右两部分，并返回总的翻转对数量。

**统计跨越中点的翻转对**：

- 对于左半部分的每个元素 $nums[i]$，在右半部分中找到所有满足 $nums[i] > 2 \times nums[j]$ 的元素 $nums[j]$。
- 由于两部分都是有序的，可以使用双指针技术高效统计。

**注意**：在统计翻转对和合并的过程中，左右两部分的相对顺序会影响统计结果，需要分别处理。

### 思路 1：代码

```python
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 用于统计翻转对数量
        self.count = 0
        
        # 归并排序函数
        def merge_sort(nums, left, right):
            if left >= right:
                return
            
            # 计算中点
            mid = (left + right) // 2
            
            # 递归处理左右两部分
            merge_sort(nums, left, mid)
            merge_sort(nums, mid + 1, right)
            
            # 统计跨越中点的翻转对
            i = left
            j = mid + 1
            # 对于左半部分的每个元素，统计右半部分中满足条件的元素
            while i <= mid:
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                # 右半部分中满足 nums[i] > 2 * nums[j] 的元素个数
                self.count += (j - mid - 1)
                i += 1
            
            # 合并左右两部分（使用临时数组）
            temp = []
            i = left
            j = mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            # 添加剩余元素
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
            
            # 将排序后的结果写回原数组
            for k in range(len(temp)):
                nums[left + k] = temp[k]
        
        # 执行归并排序
        merge_sort(nums, 0, len(nums) - 1)
        
        return self.count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$。其中 $n$ 是数组 $nums$ 的长度。归并排序的时间复杂度为 $O(n \log n)$，在每次合并过程中统计翻转对需要 $O(n)$ 时间，因此总的时间复杂度为 $O(n \log n)$。
- **空间复杂度**：$O(n)$。归并排序需要使用额外的临时数组来存储中间结果，递归调用栈的深度为 $O(\log n)$，因此总的空间复杂度为 $O(n)$。
