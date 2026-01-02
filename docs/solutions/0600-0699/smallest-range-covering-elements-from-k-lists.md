# [0632. 最小区间](https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/)

- 标签：贪心、数组、哈希表、排序、滑动窗口、堆（优先队列）
- 难度：困难

## 题目链接

- [0632. 最小区间 - 力扣](https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/)

## 题目大意

**描述**：

你有 $k$ 个「非递减排列」的整数列表。

**要求**：

找到一个 最小 区间，使得 $k$ 个列表中的每个列表至少有一个数包含在其中。

**说明**：

- 我们定义如果 $b - a < d - c$ 或者在 $b - a == d - c$ 时 $a < c$，则区间 $[a, b]$ 比 $[c, d]$ 小。
- $nums.length == k$。
- $1 \le k \le 3500$。
- $1 \le nums[i].length \le 50$。
- $-10^{5} \le nums[i][j] \le 10^{5}$。
- $nums[i]$ 按非递减顺序排列。

**示例**：

- 示例 1：

```python
输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释： 
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
```

- 示例 2：

```python
输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]
```

## 解题思路

### 思路 1：堆（优先队列）

这道题目要求找到一个最小区间，使得 $k$ 个列表中的每个列表至少有一个数包含在其中。使用最小堆维护当前区间。

1. 初始化最小堆，将每个列表的第一个元素加入堆中，元素格式为 $(value, list\_idx, element\_idx)$。
2. 记录当前堆中的最大值 $max\_val$。
3. 当堆中有 $k$ 个元素时（每个列表都有元素在堆中）：
   - 取出堆顶元素（最小值）$min\_val$。
   - 更新最小区间 $[min\_val, max\_val]$。
   - 如果该元素所在列表还有下一个元素，将下一个元素加入堆，并更新 $max\_val$。
   - 如果该元素所在列表没有下一个元素，结束循环。
4. 返回最小区间。

### 思路 1：代码

```python
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        import heapq
        
        # 初始化堆，加入每个列表的第一个元素
        heap = []
        max_val = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
        
        # 初始化结果区间
        result = [float('-inf'), float('inf')]
        
        while len(heap) == len(nums):
            min_val, list_idx, element_idx = heapq.heappop(heap)
            
            # 更新最小区间
            if max_val - min_val < result[1] - result[0]:
                result = [min_val, max_val]
            
            # 如果当前列表还有下一个元素
            if element_idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][element_idx + 1]
                heapq.heappush(heap, (next_val, list_idx, element_idx + 1))
                max_val = max(max_val, next_val)
            else:
                # 当前列表已经遍历完，无法继续
                break
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times k \times \log k)$，其中 $n$ 是所有列表的平均长度，$k$ 是列表的数量。需要遍历所有元素，每次堆操作的时间复杂度为 $O(\log k)$。
- **空间复杂度**：$O(k)$，堆中最多存储 $k$ 个元素。
