# [0826. 安排工作以达到最大收益](https://leetcode.cn/problems/most-profit-assigning-work/)

- 标签：贪心、数组、双指针、二分查找、排序
- 难度：中等

## 题目链接

- [0826. 安排工作以达到最大收益 - 力扣](https://leetcode.cn/problems/most-profit-assigning-work/)

## 题目大意

**描述**：

你有 $n$ 个工作和 $m$ 个工人。给定三个数组：$difficulty$, $profit$ 和 $worker$，其中:

- $difficulty[i]$ 表示第 $i$ 个工作的难度，$profit[i]$ 表示第 $i$ 个工作的收益。
- $worker[i]$ 是第 $i$ 个工人的能力，即该工人只能完成难度小于等于 $worker[i]$ 的工作。

每个工人「最多」只能安排「一个」工作，但是一个工作可以「完成多次」。

- 举个例子，如果 3 个工人都尝试完成一份报酬为 1 的同样工作，那么总收益为 $3$。如果一个工人不能完成任何工作，他的收益为 0。

**要求**：

返回「在把工人分配到工作岗位后，我们所能获得的最大利润」。

**说明**：

- $n == difficulty.length$。
- $n == profit.length$。
- $m == worker.length$。
- $1 \le n, m \le 10^{4}$。
- $1 \le difficulty[i], profit[i], worker[i] \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
输出: 100 
解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。
```

- 示例 2：

```python
输入: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
输出: 0
```

## 解题思路

### 思路 1：贪心 + 排序 + 双指针

这道题要求安排工人完成工作以达到最大收益。每个工人只能完成一个工作，且工作难度不能超过工人能力。

贪心策略：

- 对于每个工人，选择他能完成的工作中收益最大的。

算法步骤：

1. 将工作按难度排序，同时记录对应的收益。
2. 预处理：对于每个难度，记录到该难度为止的最大收益（因为难度更高的工作收益不一定更高）。
3. 将工人按能力排序。
4. 使用双指针遍历工人和工作：
   - 对于每个工人，找到他能完成的所有工作中收益最大的。
   - 累加收益。

### 思路 1：代码

```python
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 将工作按难度排序
        jobs = sorted(zip(difficulty, profit))
        
        # 预处理：记录到每个难度为止的最大收益
        max_profit = 0
        for i in range(len(jobs)):
            max_profit = max(max_profit, jobs[i][1])
            jobs[i] = (jobs[i][0], max_profit)
        
        # 将工人按能力排序
        worker.sort()
        
        total_profit = 0
        job_idx = 0
        
        # 遍历每个工人
        for ability in worker:
            # 找到该工人能完成的所有工作中收益最大的
            while job_idx < len(jobs) and jobs[job_idx][0] <= ability:
                job_idx += 1
            
            # 如果该工人能完成至少一个工作
            if job_idx > 0:
                total_profit += jobs[job_idx - 1][1]
        
        return total_profit
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n + m \log m)$，其中 $n$ 是工作数量，$m$ 是工人数量。需要对工作和工人排序。
- **空间复杂度**：$O(n)$，需要存储排序后的工作列表。
