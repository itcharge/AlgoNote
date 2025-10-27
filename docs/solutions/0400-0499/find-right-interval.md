# [0436. 寻找右区间](https://leetcode.cn/problems/find-right-interval/)

- 标签：数组、二分查找、排序
- 难度：中等

## 题目链接

- [0436. 寻找右区间 - 力扣](https://leetcode.cn/problems/find-right-interval/)

## 题目大意

**描述**：

给定一个区间数组 $intervals$ ，其中 $intervals[i] = [start_i, end_i]$，且每个 $start_i$ 都不同。

区间 $i$ 的「右侧区间」是满足 $start_j \ge end_i$，且 $start_j$ 「最小」的区间 $j$。注意 $i$ 可能等于 $j$。

**要求**：

返回一个由每个区间 $i$ 对应的「右侧区间」下标组成的数组。如果某个区间 $i$ 不存在对应的「右侧区间」，则下标 $i$ 处的值设为 $-1$。

**说明**：

- $1 \le intervals.length \le 2 \times 10^{4}$。
- $intervals[i].length == 2$。
- $-10^{6} \le start_i \le end_i \le 10^{6}$。
- 每个间隔的起点都不相同。

**示例**：

- 示例 1：

```python
输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。
```

- 示例 2：

```python
输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。
```

## 解题思路

### 思路 1：排序 + 二分查找

1. 为每个区间保存原索引，按照区间起点 $start_i$ 进行排序。
2. 对于每个区间 $intervals[i] = [start_i, end_i]$，用二分查找在排序后的数组中找第一个 $start_j \ge end_i$ 的区间。
3. 若找到则返回对应原索引，否则为 $-1$。

### 思路 1：代码

```python
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # 保存每个区间的原索引和起点
        start_pos = [(intervals[i][0], i) for i in range(n)]
        # 按照起点排序
        start_pos.sort()
        
        ans = []
        # 对于每个区间，使用二分查找找右区间
        for start, end in intervals:
            # 二分查找第一个 start_j >= end 的区间
            left, right = 0, n - 1
            res_index = -1
            while left <= right:
                mid = (left + right) // 2
                if start_pos[mid][0] >= end:
                    res_index = start_pos[mid][1]
                    right = mid - 1  # 继续往左找更小的
                else:
                    left = mid + 1
            ans.append(res_index)
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是区间数量。排序 $O(n \log n)$，二分查找 $n$ 次共 $O(n \log n)$。
- **空间复杂度**：$O(n)$，排序需要额外空间。
