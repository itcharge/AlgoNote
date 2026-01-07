# [0871. 最低加油次数](https://leetcode.cn/problems/minimum-number-of-refueling-stops/)

- 标签：贪心、数组、动态规划、堆（优先队列）
- 难度：困难

## 题目链接

- [0871. 最低加油次数 - 力扣](https://leetcode.cn/problems/minimum-number-of-refueling-stops/)

## 题目大意

**描述**：

汽车从起点出发驶向目的地，该目的地位于出发位置东面 $target$ 英里处。

沿途有加油站，用数组 $stations$ 表示。其中 $stations[i] = [position_i, fuel_i] 表示第 $i$ 个加油站位于出发位置东面 $position_i$ 英里处，并且有 $fuel_i$ 升汽油。

假设汽车油箱的容量是无限的，其中最初有 $startFuel$ 升燃料。它每行驶 1 英里就会用掉 1 升汽油。当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。

**要求**：

为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1。

**说明**：

- 注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。
- $1 \le target, startFuel \le 10^{9}$。
- $0 \le stations.length \le 500$。
- $1 \le position_i \lt position_i+1 \lt target$。
- $1 \le fuel_i \lt 10^{9}$。

**示例**：

- 示例 1：

```python
输入：target = 1, startFuel = 1, stations = []
输出：0
解释：可以在不加油的情况下到达目的地。
```

- 示例 2：

```python
输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
输出：2
解释：
出发时有 10 升燃料。
开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后开车抵达目的地。
沿途在两个加油站停靠，所以返回 2 。
```

## 解题思路

### 思路 1：贪心 + 堆（优先队列）

这道题要求计算到达目的地所需的最低加油次数。

贪心策略：

- 尽可能少加油，每次加油时选择之前经过的加油站中油量最多的。
- 使用最大堆记录经过的加油站的油量。

算法步骤：

1. 初始化当前位置 $pos = 0$，当前油量 $fuel = startFuel$，加油次数 $count = 0$。
2. 使用最大堆存储经过的加油站的油量。
3. 遍历加油站：
   - 如果当前油量不足以到达下一个加油站，从堆中取出最大油量加油，直到能到达或堆为空。
   - 如果堆为空仍无法到达，返回 $-1$。
   - 将当前加油站的油量加入堆。
4. 检查是否能到达目的地，如果不能，继续加油。
5. 返回加油次数。

### 思路 1：代码

```python
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        import heapq
        
        # 最大堆（Python 的 heapq 是最小堆，所以存储负值）
        max_heap = []
        fuel = startFuel
        count = 0
        prev = 0
        
        # 遍历所有加油站
        for position, gas in stations:
            # 尝试到达当前加油站
            fuel -= (position - prev)
            
            # 如果油量不足，从之前经过的加油站中选择油量最多的加油
            while fuel < 0 and max_heap:
                fuel += -heapq.heappop(max_heap)
                count += 1
            
            # 如果仍然无法到达，返回 -1
            if fuel < 0:
                return -1
            
            # 将当前加油站的油量加入堆
            heapq.heappush(max_heap, -gas)
            prev = position
        
        # 尝试到达目的地
        fuel -= (target - prev)
        while fuel < 0 and max_heap:
            fuel += -heapq.heappop(max_heap)
            count += 1
        
        # 如果仍然无法到达，返回 -1
        if fuel < 0:
            return -1
        
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是加油站的数量。每个加油站最多入堆和出堆一次。
- **空间复杂度**：$O(n)$，需要使用堆存储加油站的油量。
