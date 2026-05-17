# [1272. 删除区间](https://leetcode.cn/problems/remove-interval/)

- 标签：数组
- 难度：中等

## 题目链接

- [1272. 删除区间 - 力扣](https://leetcode.cn/problems/remove-interval/)

## 题目大意

**描述**：给定一个**不重叠**的区间列表 $intervals$（按区间起始端点从小到大排序）和一个要删除的区间 $toBeRemoved$。

**要求**：删除 $intervals$ 中所有与 $toBeRemoved$ 重叠的部分，返回剩余的区间（按起始端点升序排列）。

**说明**：

- $1 \le intervals.length \le 10^{4}$。
- $0 \le intervals[i][0] < intervals[i][1] \le 10^{6}$。
- $0 \le toBeRemoved[0] < toBeRemoved[1] \le 10^{6}$。

**示例**：

- 示例 1：

```python
输入：intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
输出：[[0,1],[6,7]]
解释：删除 [1,6] 后，[0,2] 剩下 [0,1]，[3,4] 被完全删除，[5,7] 剩下 [6,7]。
```

- 示例 2：

```python
输入：intervals = [[0,5]], toBeRemoved = [2,3]
输出：[[0,2],[3,5]]
```

## 解题思路

### 思路 1：分类讨论

#### 1. 核心思想

遍历每个区间 $[l, r]$，删除区间为 $[d_l, d_r]$。根据当前区间和删除区间的位置关系，可以分为几种情况：

1. **完全不重叠**：$r \le d_l$ 或 $l \ge d_r$，保留整个区间。
2. **完全被覆盖**：$l \ge d_l$ 且 $r \le d_r$，整个区间被删除。
3. **左边部分重叠**：$l < d_l$ 且 $r > d_l$ 且 $r \le d_r$，保留 $[l, d_l]$。
4. **右边部分重叠**：$l \ge d_l$ 且 $l < d_r$ 且 $r > d_r$，保留 $[d_r, r]$。
5. **删除区间在内部**：$l < d_l$ 且 $r > d_r$，保留 $[l, d_l]$ 和 $[d_r, r]$（被切成两段）。

但上述 5 种情况可以合并为更简洁的逻辑：

对于每个区间 $[l, r]$：
- 如果 $l < d_l$：保留 $[l, \min(r, d_l)]$（左半部分）。
- 如果 $r > d_r$：保留 $[\max(l, d_r), r]$（右半部分）。
- 其余部分被删除。

#### 2. 具体步骤

**第 1 步**：初始化结果列表 $ans = []$。

**第 2 步**：遍历每个区间 $[l, r]$：
- 如果 $l < toBeRemoved[0]$：保留左半部分 $[l, \min(r, toBeRemoved[0])]$。
- 如果 $r > toBeRemoved[1]$：保留右半部分 $[\max(l, toBeRemoved[1]), r]$。

**第 3 步**：返回 $ans$。

#### 3. 结合示例走一遍

$intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]$

- $[0,2]$：$l=0 < 1$ → 保留 $[0, \min(2,1)] = [0,1]$。$r=2 \le 6$ → 不保留右半。
- $[3,4]$：$l=3 \ge 1$ → 不保留左半。$r=4 \le 6$ → 不保留右半。全部删除。
- $[5,7]$：$l=5 \ge 1$ → 不保留左半。$r=7 > 6$ → 保留 $[\max(5,6), 7] = [6,7]$。

结果 $[[0,1],[6,7]]$。

### 思路 1：代码

```python
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        dl, dr = toBeRemoved
        ans = []
        for l, r in intervals:
            # 保留左半部分（不与删除区间重叠的部分）
            if l < dl:
                ans.append([l, min(r, dl)])
            # 保留右半部分（不与删除区间重叠的部分）
            if r > dr:
                ans.append([max(l, dr), r])
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是区间数量。只需一次遍历。
- **空间复杂度**：$O(1)$，不考虑存储结果所需的空间。
