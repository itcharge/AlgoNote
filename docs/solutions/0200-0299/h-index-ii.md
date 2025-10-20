# [0275. H 指数 II](https://leetcode.cn/problems/h-index-ii/)

- 标签：数组、二分查找
- 难度：中等

## 题目链接

- [0275. H 指数 II - 力扣](https://leetcode.cn/problems/h-index-ii/)

## 题目大意

**描述**：

给定一个整数数组 $citations$ ，其中 $citations[i]$ 表示研究者的第 $i$ 篇论文被引用的次数，$citations$ 已经按照非降序排列。

**要求**：

计算并返回该研究者的 $h$ 指数。

**说明**：

- $h$ 指数的定义：$h$ 代表「高引用次数」（high citations），一名科研人员的 $h$ 指数是指他（她）的（$n$ 篇论文中）至少有 $h$ 篇论文分别被引用了至少 $h$ 次。
- 设计并实现对数时间复杂度的算法解决此问题。
- $n == citations.length$。
- $1 \le n \le 10^{5}$。
- $0 \le citations[i] \le 10^{3}$。
- $citations$ 按升序排列。

**示例**：

- 示例 1：

```python
输入：citations = [0,1,3,5,6]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
     由于研究者有3篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3 。
```

- 示例 2：

```python
输入：citations = [1,2,100]
输出：2
```

## 解题思路

### 思路 1：二分查找

这是一个经典的 H 指数计算问题，由于数组已经按升序排列，我们可以使用二分查找来优化时间复杂度。

核心思想是：

- 由于数组 $citations$ 已经按升序排列，我们可以使用二分查找来找到满足条件的最大 $h$ 值。
- 对于位置 $i$，如果 $citations[i] \geq n - i$，说明从位置 $i$ 开始到数组末尾有 $n - i$ 篇论文，且这些论文的引用次数都大于等于 $n - i$。
- 我们需要找到最小的 $i$ 使得 $citations[i] \geq n - i$，此时 $h$ 指数就是 $n - i$。

具体算法步骤：

1. 初始化二分查找的边界：$left = 0$，$right = n - 1$。
2. 在 $[left, right]$ 区间内进行二分查找：
   - 计算中点 $mid = (left + right) // 2$。
   - 如果 $citations[mid] \geq n - mid$，说明从位置 $mid$ 开始有 $n - mid$ 篇论文满足条件，尝试寻找更小的 $mid$，更新 $right = mid - 1$。
   - 否则，说明从位置 $mid$ 开始不满足条件，需要增大 $mid$，更新 $left = mid + 1$。
3. 最终 $h$ 指数为 $n - left$。

### 思路 1：代码

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        
        # 二分查找满足条件的最小位置
        while left <= right:
            mid = (left + right) // 2
            # 如果 citations[mid] >= n - mid，说明从位置 mid 开始
            # 有 n - mid 篇论文的引用次数都大于等于 n - mid
            if citations[mid] >= n - mid:
                # 尝试寻找更小的 mid
                right = mid - 1
            else:
                # 需要增大 mid
                left = mid + 1
        
        # h 指数就是 n - left
        return n - left
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$，其中 $n$ 是数组长度。使用二分查找，每次将搜索范围缩小一半。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
