# [0502. IPO](https://leetcode.cn/problems/ipo/)

- 标签：贪心、数组、排序、堆（优先队列）
- 难度：困难

## 题目链接

- [0502. IPO - 力扣](https://leetcode.cn/problems/ipo/)

## 题目大意

**描述**：

假设 力扣（LeetCode）即将开始 IPO。为了以更高的价格将股票卖给风险投资公司，力扣希望在 IPO 之前开展一些项目以增加其资本。由于资源有限，它只能在 IPO 之前完成最多 $k$ 个不同的项目。帮助力扣设计完成最多 $k$ 个不同项目后得到最大总资本的方式。

给定 $n$ 个项目。对于每个项目 $i$，它都有一个纯利润 $profits[i]$，和启动该项目需要的最小资本 $capital[i]$。

最初，你的资本为 $w$。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。

**要求**：

总而言之，从给定项目中选择 最多 $k$ 个不同项目的列表，以「最大化最终资本」，并输出最终可获得的最多资本。

答案保证在 32 位有符号整数范围内。

**说明**：

- $1 \le k \le 10^{5}$。
- $0 \le w \le 10^{9}$。
- $n == profits.length$。
- $n == capital.length$。
- $1 \le n \le 10^{5}$。
- $0 \le profits[i] \le 10^{4}$。
- $0 \le capital[i] \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
输出：4
解释：
由于你的初始资本为 0，你仅可以从 0 号项目开始。
在完成后，你将获得 1 的利润，你的总资本将变为 1。
此时你可以选择开始 1 号或 2 号项目。
由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。
```

- 示例 2：

```python
输入：k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
输出：6
```

## 解题思路

### 思路 1：贪心 + 堆（优先队列）

这道题的核心是在有限资本下，选择利润最大的项目。使用贪心策略：每次选择当前资本能启动的项目中利润最大的。

核心思路：

1. 将所有项目按启动资本从小到大排序。
2. 使用最大堆存储当前资本能启动的所有项目的利润。
3. 重复 $k$ 次：
   - 将所有启动资本不超过当前资本 $w$ 的项目的利润加入最大堆。
   - 从最大堆中取出利润最大的项目，将利润加到当前资本 $w$ 上。
   - 如果堆为空，说明没有可启动的项目，提前结束。

### 思路 1：代码

```python
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # 将项目按启动资本排序
        projects = sorted(zip(capital, profits))
        
        # 最大堆（Python 的 heapq 是最小堆，所以存负值）
        max_heap = []
        idx = 0
        
        # 最多完成 k 个项目
        for _ in range(k):
            # 将所有当前资本能启动的项目加入堆
            while idx < n and projects[idx][0] <= w:
                # 存入负利润（实现最大堆）
                heapq.heappush(max_heap, -projects[idx][1])
                idx += 1
            
            # 如果没有可启动的项目，提前结束
            if not max_heap:
                break
            
            # 选择利润最大的项目
            w += -heapq.heappop(max_heap)
        
        return w
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n + k \log n)$，其中 $n$ 为项目数量。排序需要 $O(n \log n)$，每次堆操作需要 $O(\log n)$，最多进行 $k$ 次。
- **空间复杂度**：$O(n)$，排序和堆的空间开销。
