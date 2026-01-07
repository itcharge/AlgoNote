# [0757. 设置交集大小至少为2](https://leetcode.cn/problems/set-intersection-size-at-least-two/)

- 标签：贪心、数组、排序
- 难度：困难

## 题目链接

- [0757. 设置交集大小至少为2 - 力扣](https://leetcode.cn/problems/set-intersection-size-at-least-two/)

## 题目大意

**描述**：

给定一个二维整数数组 $intervals$ ，其中 $intervals[i] = [starti, endi]$ 表示从 $starti$ 到 $endi$ 的所有整数，包括 $starti$ 和 $endi$。

「包含集合」是一个名为 $nums$ 的数组，并满足 $intervals$ 中的每个区间都「至少」有「两个」整数在 $nums$ 中。

- 例如，如果 $intervals = [[1,3], [3,7], [8,9]]$，那么 $[1,2,4,7,8,9]$ 和 $[2,3,4,8,9]$ 都符合「包含集合」的定义。

**要求**：

返回包含集合可能的最小大小。

**说明**：

- $1 \le intervals.length \le 3000$。
- $intervals[i].length == 2$。
- $0 \le starti \lt endi \le 10^{8}$。

**示例**：

- 示例 1：

```python
输入：intervals = [[1,3],[3,7],[8,9]]
输出：5
解释：nums = [2, 3, 4, 8, 9].
可以证明不存在元素数量为 4 的包含集合。
```

- 示例 2：

```python
输入：intervals = [[1,3],[1,4],[2,5],[3,5]]
输出：3
解释：nums = [2, 3, 4].
可以证明不存在元素数量为 2 的包含集合。
```

## 解题思路

### 思路 1：贪心 + 排序

贪心策略：按照区间的右端点排序，优先选择右端点较小的区间。

**实现步骤**：

1. 按照区间的右端点升序排序，如果右端点相同，按左端点降序排序。
2. 维护一个集合 $S$，初始为空。
3. 遍历每个区间 $[start, end]$：
   - 统计 $S$ 中在该区间内的元素个数 $count$。
   - 如果 $count < 2$，需要添加 $2 - count$ 个元素。
   - 贪心地选择尽可能靠右的元素（$end - 1$ 和 $end$），以便覆盖更多后续区间。
4. 返回集合的大小。

### 思路 1：代码

```python
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 按右端点升序排序，右端点相同时按左端点降序排序
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        result = []
        
        for start, end in intervals:
            # 统计 result 中在 [start, end] 范围内的元素个数
            count = sum(1 for x in result if start <= x <= end)
            
            # 需要添加的元素个数
            need = 2 - count
            
            if need <= 0:
                continue
            
            # 贪心地选择尽可能靠右的元素
            if need == 1:
                # 添加 end
                result.append(end)
            else:  # need == 2
                # 添加 end-1 和 end
                result.append(end - 1)
                result.append(end)
        
        return len(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是区间的数量。排序需要 $O(n \log n)$，遍历每个区间需要 $O(n)$，每次统计需要 $O(n)$。
- **空间复杂度**：$O(n)$，存储结果的空间。
