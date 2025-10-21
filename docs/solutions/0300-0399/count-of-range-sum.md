# [0327. 区间和的个数](https://leetcode.cn/problems/count-of-range-sum/)

- 标签：树状数组、线段树、数组、二分查找、分治、有序集合、归并排序
- 难度：困难

## 题目链接

- [0327. 区间和的个数 - 力扣](https://leetcode.cn/problems/count-of-range-sum/)

## 题目大意

**描述**：

给定一个整数数组 $nums$ 以及两个整数 $lower$ 和 $upper$。

**要求**：

求数组中，值位于范围 $[lower, upper]$（包含 $lower$ 和 $upper$）之内的「区间和的个数」。

**说明**：

- 区间和 $S(i, j)$：表示在 $nums$ 中，位置从 $i$ 到 $j$ 的元素之和，包含 $i$ 和 $j$ ($i \le j$)。
- $1 \le nums.length \le 10^{5}$。
- $-2^{31} \le nums[i] \le 2^{31} - 1$。
- $-10^{5} \le lower \le upper \le 10^{5}$。
- 题目数据保证答案是一个 $32$ 位的整数。

**示例**：

- 示例 1：

```python
输入：nums = [-2,5,-1], lower = -2, upper = 2
输出：3
解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
```

- 示例 2：

```python
输入：nums = [0], lower = 0, upper = 0
输出：1
```

## 解题思路

### 思路 1：前缀和 + 归并排序

这道题要求统计区间和 $S(i, j) = \sum_{k=i}^{j} nums[k]$ 在 $[lower, upper]$ 范围内的个数。

我们可以使用前缀和的思想：设 $prefix[i] = \sum_{k=0}^{i} nums[k]$，则区间和 $S(i, j) = prefix[j] - prefix[i-1]$。

对于每个位置 $j$，我们需要找到满足条件的 $i$，使得：$lower \leq prefix[j] - prefix[i-1] \leq upper$

即：$prefix[j] - upper \leq prefix[i-1] \leq prefix[j] - lower$

这可以转化为：对于每个 $prefix[j]$，统计在 $prefix[0]$ 到 $prefix[j-1]$ 中有多少个值在区间 $[prefix[j] - upper, prefix[j] - lower]$ 内。

使用归并排序的思想：

1. 将数组分为左右两部分
2. 递归处理左右两部分，得到左右两部分的答案
3. 处理跨越中点的区间：对于右半部分的每个 $prefix[j]$，在左半部分中统计满足条件的 $prefix[i]$
4. 合并左右两部分并排序

### 思路 1：代码

```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # 计算前缀和数组
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        def merge_sort_count(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            # 递归处理左右两部分
            count = merge_sort_count(left, mid) + merge_sort_count(mid + 1, right)
            
            # 处理跨越中点的区间
            i = j = mid + 1
            for k in range(left, mid + 1):
                # 找到左边界：prefix[j] >= prefix[k] + lower
                while i <= right and prefix[i] < prefix[k] + lower:
                    i += 1
                # 找到右边界：prefix[j] <= prefix[k] + upper
                while j <= right and prefix[j] <= prefix[k] + upper:
                    j += 1
                # 统计满足条件的区间数量
                count += j - i
            
            # 合并排序
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if prefix[i] <= prefix[j]:
                    temp.append(prefix[i])
                    i += 1
                else:
                    temp.append(prefix[j])
                    j += 1
            
            # 添加剩余元素
            while i <= mid:
                temp.append(prefix[i])
                i += 1
            while j <= right:
                temp.append(prefix[j])
                j += 1
            
            # 更新原数组
            for i in range(len(temp)):
                prefix[left + i] = temp[i]
            
            return count
        
        return merge_sort_count(0, len(prefix) - 1)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是数组长度。归并排序的时间复杂度为 $O(n \log n)$，每次合并时处理跨越中点的区间需要 $O(n)$ 时间。
- **空间复杂度**：$O(n)$，需要额外的空间存储前缀和数组和归并排序的临时数组。

### 思路 2：树状数组

同样使用前缀和的思想，但这次我们使用树状数组来优化查询。

对于每个前缀和 $prefix[j]$，我们需要统计在 $prefix[0]$ 到 $prefix[j-1]$ 中有多少个值在区间 $[prefix[j] - upper, prefix[j] - lower]$ 内。

使用树状数组的步骤：

1. 计算所有可能的前缀和值，包括 $prefix[j] - upper$ 和 $prefix[j] - lower$
2. 对这些值进行离散化处理
3. 从左到右遍历前缀和数组，对于每个 $prefix[j]$：
   - 查询区间 $[prefix[j] - upper, prefix[j] - lower]$ 内的元素个数
   - 将 $prefix[j]$ 插入到树状数组中

### 思路 2：代码

```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # 计算前缀和数组
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        # 收集所有需要离散化的值
        values = set()
        for p in prefix:
            values.add(p)
            values.add(p - lower)
            values.add(p - upper)
        
        # 离散化
        sorted_values = sorted(values)
        value_to_idx = {v: i + 1 for i, v in enumerate(sorted_values)}
        
        # 树状数组类
        class BIT:
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (n + 1)
            
            def update(self, idx, delta):
                while idx <= self.n:
                    self.tree[idx] += delta
                    idx += idx & (-idx)
            
            def query(self, idx):
                res = 0
                while idx > 0:
                    res += self.tree[idx]
                    idx -= idx & (-idx)
                return res
            
            def range_query(self, left, right):
                return self.query(right) - self.query(left - 1)
        
        # 初始化树状数组
        bit = BIT(len(sorted_values))
        count = 0
        
        # 从左到右处理前缀和
        for p in prefix:
            # 查询区间 [p - upper, p - lower] 内的元素个数
            left_idx = value_to_idx[p - upper]
            right_idx = value_to_idx[p - lower]
            count += bit.range_query(left_idx, right_idx)
            
            # 将当前前缀和插入树状数组
            bit.update(value_to_idx[p], 1)
        
        return count
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是数组长度。离散化需要 $O(n \log n)$ 时间，树状数组的每次更新和查询操作都是 $O(\log n)$，总共需要 $O(n \log n)$ 时间。
- **空间复杂度**：$O(n)$，需要存储离散化后的值和树状数组。
