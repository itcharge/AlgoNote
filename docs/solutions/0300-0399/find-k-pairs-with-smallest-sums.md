# [0373. 查找和最小的 K 对数字](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/)

- 标签：数组、堆（优先队列）
- 难度：中等

## 题目链接

- [0373. 查找和最小的 K 对数字 - 力扣](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/)

## 题目大意

**描述**：

给定两个以「非递减顺序排列」的整数数组 $nums1$ 和 $nums2$, 以及一个整数 $k$。

定义一对值 $(u, v)$，其中第一个元素来自 $nums1$，第二个元素来自 $nums2$。

**要求**：

请找到和最小的 $k$ 个数对 $(u1, v1), (u2, v2)  ...  (uk, vk)$。

**说明**：

- $1 \le nums1.length, nums2.length \le 10^{5}$。
- $-10^{9} \le nums1[i], nums2[i] \le 10^{9}$。
- $nums1$ 和 $nums2$ 均为升序排列。
- $1 \le k \le 10^{4}$。
- $k \le nums1.length \times nums2.length$。

**示例**：

- 示例 1：

```python
输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

- 示例 2：

```python
输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
```

## 解题思路

### 思路 1：优先队列（最小堆）

这道题的核心思想是：**使用优先队列来维护当前和最小的数对候选**。

解题步骤：

1. **初始化优先队列**：将 $nums1$ 中每个元素与 $nums2[0]$ 组成的数对加入优先队列，队列中存储 $(sum, i, j)$ 三元组，其中 $sum = nums1[i] + nums2[j]$。
2. **逐步扩展候选**：每次从队列中取出和最小的数对 $(sum, i, j)$，将其加入结果。
3. **添加新的候选**：如果 $j + 1 < len(nums2)$，则将 $(nums1[i] + nums2[j+1], i, j+1)$ 加入队列。
4. **重复直到找到 $k$ 个数对**。

**关键点**：

- 由于 $nums1$ 和 $nums2$ 都是非递减的，对于固定的 $i$，$nums1[i] + nums2[j]$ 随着 $j$ 增大而增大。
- 优先队列确保我们总是处理当前和最小的数对。
- 每次取出一个数对后，只需要考虑该数对的下一个可能候选（$j+1$）。

**算法正确性**：

设当前队列中最小和为 $sum_{min} = nums1[i] + nums2[j]$，则所有未处理的数对 $(nums1[x], nums2[y])$ 满足：

- 如果 $x < i$，则 $nums1[x] + nums2[y] \ge nums1[x] + nums2[0] \ge nums1[i] + nums2[0] \ge sum_{min}$（因为 $nums1$ 非递减）。
- 如果 $x = i$ 且 $y > j$，则 $nums1[i] + nums2[y] \ge sum_{min}$（因为 $nums2$ 非递减）。
- 如果 $x > i$，则 $nums1[x] + nums2[y] \ge nums1[i+1] + nums2[0] \ge nums1[i] + nums2[0] \ge sum_{min}$。

因此，当前队列中的最小和确实是全局最小和。

### 思路 1：代码

```python
import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        
        # 优先队列，存储(sum, i, j)三元组
        # sum = nums1[i] + nums2[j]
        heap = []
        
        # 初始化：将nums1中每个元素与nums2[0]组成的数对加入队列
        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        result = []
        
        # 从队列中取出k个和最小的数对
        while heap and len(result) < k:
            # 取出当前和最小的数对
            sum_val, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            # 如果nums2中还有下一个元素，添加新的候选
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(k \log k)$，其中 $k$ 是要求的数对个数。最多需要从优先队列中取出 $k$ 个元素，每次取出和插入操作的时间复杂度为 $O(\log k)$。
- **空间复杂度**：$O(k)$，优先队列最多存储 $k$ 个元素。
