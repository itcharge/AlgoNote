# [0857. 雇佣 K 名工人的最低成本](https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/)

- 标签：贪心、数组、排序、堆（优先队列）
- 难度：困难

## 题目链接

- [0857. 雇佣 K 名工人的最低成本 - 力扣](https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/)

## 题目大意

**描述**：

有 $n$ 名工人。 给定两个数组 $quality$ 和 $wage$ ，其中，$quality[i]$ 表示第 $i$ 名工人的工作质量，其最低期望工资为 $wage[i]$。

现在我们想雇佣 $k$ 名工人组成一个 工资组。在雇佣 一组 $k$ 名工人时，我们必须按照下述规则向他们支付工资：

1. 对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。
2. 工资组中的每名工人至少应当得到他们的最低期望工资。

给定整数 $k$。

**要求**：

返回「组成满足上述条件的付费群体所需的最小金额」。与实际答案误差相差在 $10^{-5}$ 以内的答案将被接受。

**说明**：

- $n == quality.length == wage.length$。
- $1 \le k \le n \le 10^{4}$。
- $1 \le quality[i], wage[i] \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入： quality = [10,20,5], wage = [70,50,30], k = 2
输出： 105.00000
解释： 我们向 0 号工人支付 70，向 2 号工人支付 35。
```

- 示例 2：

```python
输入： quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
输出： 30.66667
解释： 我们向 0 号工人支付 4，向 2 号和 3 号分别支付 13.33333。
```

## 解题思路

### 思路 1:贪心 + 堆

关键观察:如果我们选定了某个工人作为"基准",其工资恰好等于最低期望工资,那么其他工人的工资由他们的工作质量比例决定。

设基准工人的工资期望比为 $r = \frac{wage}{quality}$,那么所有工人的工资期望比都不能超过 $r$,否则无法满足最低工资要求。

算法步骤:

1. 计算每个工人的工资期望比 $ratio[i] = \frac{wage[i]}{quality[i]}$
2. 按照 $ratio$ 从小到大排序
3. 枚举每个工人作为工资期望比最大的工人(基准)
4. 对于当前基准,选择前面 $k-1$ 个工作质量最小的工人,使用大顶堆维护
5. 计算总成本:$ratio \times \sum quality$

### 思路 1:代码

```python
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        import heapq
        
        n = len(quality)
        # 计算每个工人的工资期望比,并按比例排序
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])
        
        min_cost = float('inf')
        quality_sum = 0  # 当前选中的工人的工作质量之和
        max_heap = []  # 大顶堆,存储工作质量(取负数实现大顶堆)
        
        for ratio, q in workers:
            # 将当前工人加入堆
            heapq.heappush(max_heap, -q)
            quality_sum += q
            
            # 如果堆中元素超过 k 个,移除工作质量最大的
            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)  # 注意是负数,所以用加法
            
            # 如果堆中恰好有 k 个工人,计算成本
            if len(max_heap) == k:
                min_cost = min(min_cost, ratio * quality_sum)
        
        return min_cost
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(n \log n)$,其中 $n$ 是工人数量。排序需要 $O(n \log n)$,每个工人最多入堆出堆一次,堆操作需要 $O(n \log k)$。
- **空间复杂度**:$O(n)$,需要存储排序后的工人信息和堆。
