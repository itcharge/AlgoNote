# [1986. 完成任务的最少工作时间段](https://leetcode.cn/problems/minimum-number-of-work-sessions-to-finish-the-tasks/)

- 标签：位运算、数组、动态规划、回溯、状态压缩
- 难度：中等

## 题目链接

- [1986. 完成任务的最少工作时间段 - 力扣](https://leetcode.cn/problems/minimum-number-of-work-sessions-to-finish-the-tasks/)

## 题目大意

**描述**：给定一个整数数组 $tasks$ 代表需要完成的任务。 其中 $tasks[i]$ 表示第 $i$ 个任务需要花费的时长（单位为小时）。再给定一个整数 $sessionTime$，代表在一个工作时段中，最多可以连续工作的小时数。在连续工作至多 $sessionTime$ 小时后，需要进行休息。

现在需要按照如下条件完成给定任务：

1. 如果你在某一个时间段开始一个任务，你需要在同一个时间段完成它。
2. 完成一个任务后，你可以立马开始一个新的任务。
3. 你可以按任意顺序完成任务。

**要求**：按照上述要求，返回完成所有任务所需要的最少数目的工作时间段。

**说明**：

- $n == tasks.length$。
- $1 \le n \le 14$。
- $1 \le tasks[i] \le 10$。
- $max(tasks[i]) \le sessionTime \le 15$。

**示例**：

- 示例 1：

```python
输入：tasks = [1,2,3], sessionTime = 3
输出：2
解释：你可以在两个工作时间段内完成所有任务。
- 第一个工作时间段：完成第一和第二个任务，花费 1 + 2 = 3 小时。
- 第二个工作时间段：完成第三个任务，花费 3 小时。
```

- 示例 2：

```python
输入：tasks = [3,1,3,1,1], sessionTime = 8
输出：2
解释：你可以在两个工作时间段内完成所有任务。
- 第一个工作时间段：完成除了最后一个任务以外的所有任务，花费 3 + 1 + 3 + 1 = 8 小时。
- 第二个工作时间段，完成最后一个任务，花费 1 小时。
```

## 解题思路

### 思路 1：状压 DP

### 思路 1：代码

```python
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        size = len(tasks)
        states = 1 << size
        
        prefix_sum = [0 for _ in range(states)]
        for state in range(states):
            for i in range(size):
                if (state >> i) & 1:
                    prefix_sum[state] = prefix_sum[state ^ (1 << i)] + tasks[i]
                    break
        
        dp = [float('inf') for _ in range(states)]
        dp[0] = 0
        for state in range(states):
            sub = state
            while sub > 0:
                if prefix_sum[sub] <= sessionTime:
                    dp[state] = min(dp[state], dp[state ^ sub] + 1)
                sub = (sub - 1) & state

        return dp[states - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：
- **空间复杂度**：

