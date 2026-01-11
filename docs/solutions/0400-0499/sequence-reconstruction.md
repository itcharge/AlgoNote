# [0444. 序列重建](https://leetcode.cn/problems/sequence-reconstruction/)

- 标签：图、拓扑排序、数组
- 难度：中等

## 题目链接

- [0444. 序列重建 - 力扣](https://leetcode.cn/problems/sequence-reconstruction/)

## 题目大意

**描述**：

给定一个整数数组 $nums$ 和一个整数数组序列 $sequences$，其中，其中 $nums$ 是范围为 $[1, n]$ 的整数的排列，$sequences[i]$ 是 $nums$ 的一个子序列。

**要求**：

判断 $nums$ 是否是唯一的最短超序列。即判断 $nums$ 是否是唯一可以从 $sequences$ 重建出来的序列。

**说明**：

- 最短「超序列」：是「长度最短」的序列，并且所有序列 $sequences[i]$ 都是它的子序列。对于给定的数组 $sequences$，可能存在多个有效的「超序列」。
   - 例如，对于 $sequences = [[1,2],[1,3]]$，有两个最短的「超序列」，$[1,2,3]$ 和 $[1,3,2]$。
   - 而对于 $sequences = [[1,2],[1,3],[1,2,3]]$，唯一可能的最短「超序列」是 $[1,2,3]$。$[1,2,3,4]$ 是可能的超序列，但不是最短的。
- $1 \le nums.length \le 10^4$。
- $1 \le sequences.length \le 10^4$。
- $1 \le sequences[i].length \le 10^4$。
- $1 \le sum(sequences[i].length) \le 10^5$。
- $1 \le nums[i], sequences[i][j] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3], sequences = [[1,2],[1,3]]
输出：false
解释：有两种可能的超序列：[1,2,3]和[1,3,2]。
序列 [1,2] 是[1,2,3]和[1,3,2]的子序列。
序列 [1,3] 是[1,2,3]和[1,3,2]的子序列。
因为 nums 不是唯一最短的超序列，所以返回false。
```

- 示例 2：

```python
输入：nums = [1,2,3], sequences = [[1,2]]
输出：false
解释：最短可能的超序列为 [1,2]。
序列 [1,2] 是它的子序列：[1,2]。
因为 nums 不是最短的超序列，所以返回false。
```

## 解题思路

### 思路 1：拓扑排序

判断是否可以从 $sequences$ 中唯一重建出原始序列 $nums$。

**核心思想**：

- 如果 $nums$ 是唯一的拓扑排序结果，那么在拓扑排序的每一步，入度为 0 的节点必须唯一。
- 同时，$sequences$ 中的所有边必须能构建出 $nums$ 的相邻关系。

**解题步骤**：

1. 根据 $sequences$ 构建图的邻接表和入度数组。
2. 检查 $sequences$ 中的所有数字是否都在 $nums$ 中。
3. 使用拓扑排序（BFS）：
   - 每次只能有一个入度为 0 的节点（保证唯一性）。
   - 拓扑排序的结果必须与 $nums$ 完全一致。
4. 检查 $nums$ 中相邻的元素在图中是否有边连接。

### 思路 1：代码

```python
from collections import defaultdict, deque

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        graph = defaultdict(set)
        indegree = {i: 0 for i in nums}
        
        # 检查 sequences 中的数字是否都在 nums 中
        all_nums = set()
        for seq in sequences:
            for num in seq:
                all_nums.add(num)
                if num not in indegree:
                    return False
        
        # 如果 sequences 中的数字集合与 nums 不一致
        if all_nums != set(nums):
            return False
        
        # 构建图
        for seq in sequences:
            for i in range(len(seq) - 1):
                u, v = seq[i], seq[i + 1]
                if v not in graph[u]:
                    graph[u].add(v)
                    indegree[v] += 1
        
        # 拓扑排序
        queue = deque([num for num in nums if indegree[num] == 0])
        result = []
        
        while queue:
            # 每次必须只有一个入度为 0 的节点（保证唯一性）
            if len(queue) != 1:
                return False
            
            node = queue.popleft()
            result.append(node)
            
            # 更新邻居的入度
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 检查拓扑排序结果是否与 nums 一致
        return result == nums
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 是 $nums$ 的长度，$m$ 是 $sequences$ 中所有元素的总数。
- **空间复杂度**：$O(n + m)$，存储图和入度数组。
