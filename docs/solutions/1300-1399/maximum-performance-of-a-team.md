# [1383. 最大的团队表现值](https://leetcode.cn/problems/maximum-performance-of-a-team/)

- 标签：贪心、数组、排序、堆（优先队列）
- 难度：困难

## 题目链接

- [1383. 最大的团队表现值 - 力扣](https://leetcode.cn/problems/maximum-performance-of-a-team/)

## 题目大意

**描述**：给定两个数组 $speed$ 和 $efficiency$，分别表示每个工程师的速度和效率。需要选择最多 $k$ 个工程师组成团队。

团队表现值定义为：团队中所有工程师的速度之和乘以团队中最小的效率。

**要求**：返回最大可能的团队表现值，对 $10^9+7$ 取模。

**示例**：

- 示例 1：

```python
输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
输出：60
解释：
我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为 performance = (10 + 5) * min(4, 7) = 60 。
```

- 示例 2：

```python
输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
输出：68
解释：
此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance = (2 + 10 + 5) * min(5, 4, 7) = 68 。
```


## 解题思路

### 思路 1：贪心 + 最小堆

#### 1. 核心思想

按效率降序排序。遍历时维护一个大小为 $k$ 的速度堆（存当前最大的 $k$ 个速度）。当前遍历到的工程师效率就是团队的最小效率（因为按效率降序），所以表现值 = 堆中速度之和 × 当前效率。

#### 2. 具体步骤

**第 1 步**：按 $(efficiency, speed)$ 降序排序。

**第 2 步**：用最小堆维护已选工程师的速度，堆大小不超过 $k$。

**第 3 步**：遍历时更新速度总和和最大表现值。

### 思路 1：代码

```python
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        speed_sum = 0
        ans = 0
        for eff, spd in engineers:
            heapq.heappush(heap, spd)
            speed_sum += spd
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
            ans = max(ans, speed_sum * eff)
        return ans % mod
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n \log k)$。
- **空间复杂度**：$O(k)$。
