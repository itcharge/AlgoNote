# [1947. 最大兼容性评分和](https://leetcode.cn/problems/maximum-compatibility-score-sum/)

- 标签：位运算、数组、动态规划、回溯、状态压缩
- 难度：中等

## 题目链接

- [1947. 最大兼容性评分和 - 力扣](https://leetcode.cn/problems/maximum-compatibility-score-sum/)

## 题目大意

**描述**：有一份由 $n$ 个问题组成的调查问卷，每个问题的答案只有 $0$ 或 $1$。将这份调查问卷分发给 $m$ 名学生和 $m$ 名老师，学生和老师的编号都是 $0 \sim m - 1$。现在给定一个二维整数数组 $students$ 表示 $m$ 名学生给出的答案，其中 $studuents[i][j]$ 表示第 $i$ 名学生第 $j$ 个问题给出的答案。再给定一个二维整数数组 $mentors$ 表示 $m$ 名老师给出的答案，其中 $mentors[i][j]$ 表示第 $i$ 名导师第 $j$ 个问题给出的答案。

每个学生要和一名导师互相配对。配对的学生和导师之间的兼容性评分等于学生和导师答案相同的次数。

- 例如，学生答案为 $[1, 0, 1]$，而导师答案为 $[0, 0, 1]$，那么他们的兼容性评分为 $2$，因为只有第 $2$ 个和第 $3$ 个答案相同。

**要求**：找出最优的学生与导师的配对方案，以最大程度上提高所有学生和导师的兼容性评分和。然后返回可以得到的最大兼容性评分和。

**说明**：

- $m == students.length == mentors.length$。
- $n == students[i].length == mentors[j].length$。
- $1 \le m, n \le 8$。
- $students[i][k]$ 为 $0$ 或 $1$。
- $mentors[j][k]$ 为 $0$ 或 $1$。

**示例**：

- 示例 1：

```python
输入：students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
输出：8
解释：按下述方式分配学生和导师：
- 学生 0 分配给导师 2 ，兼容性评分为 3。
- 学生 1 分配给导师 0 ，兼容性评分为 2。
- 学生 2 分配给导师 1 ，兼容性评分为 3。
最大兼容性评分和为 3 + 2 + 3 = 8。
```

- 示例 2：

```python
输入：students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]
输出：0
解释：任意学生与导师配对的兼容性评分都是 0。
```

## 解题思路

### 思路 1：状压 DP

因为 $m$、$n$ 的范围都是 $[1, 8]$，所以我们可以使用「状态压缩」的方式来表示学生的分配情况。即使用一个 $m$ 位长度的二进制数 $state$ 来表示每一位老师是否被分配了学生。如果 $state$ 的第 $i$ 位为 $1$，表示第 $i$ 位老师被分配了学生，如果 $state$ 的第 $i$ 位为 $0$，则表示第 $i$ 位老师没有分配到学生。

这样，我们就可以通过动态规划的方式来解决这道题。

###### 1. 划分阶段

按照学生的分配情况进行阶段划分。

###### 2. 定义状态

定义当前学生的分配情况为 $state$，$state$ 中包含 $count(state)$ 个 $1$，表示有 $count(state)$ 个老师被分配了学生。

则可以定义状态 $dp[state]$ 表示为：当前老师被分配学生的状态为 $state$，其中有 $count(state)$ 个老师被分配了学生的情况下，可以得到的最大兼容性评分和。

###### 3. 状态转移方程

对于当前状态 $state$，肯定是从比 $state$ 少选一个老师被分配的状态中递推而来。我们可以枚举少选一个元素的状态，找到可以得到的最大兼容性评分和，赋值给 $dp[state]$。

即状态转移方程为：$dp[state] = max(dp[state], \quad dp[state \oplus (1 \text{ <}\text{< } i)] + score[i][one\underline{\hspace{0.5em}}cnt - 1])$，其中：

1. $state$ 第 $i$ 位一定为 $1$。
2. $state \oplus (1 \text{ <}\text{< } i)$ 为比 $state$ 少选一个元素的状态。
3. $scores[i][one\underline{\hspace{0.5em}}cnt - 1]$ 为第 $i$ 名老师分配到第 $one\underline{\hspace{0.5em}}cnt - 1$ 名学生的兼容性评分。

关于每位老师与每位同学之间的兼容性评分，我们可以事先通过一个 $m \times m \times n$ 的三重循环计算得出，并且存入到 $m \times m$ 大小的二维矩阵 $scores$ 中。

###### 4. 初始条件

- 初始每个老师都没有分配到学生的状态下，可以得到的最兼容性评分和为 $0$，即 $dp[0] = 0$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[state]$ 表示为：当前老师被分配学生的状态为 $state$，其中有 $count(state)$ 个老师被分配了学生的情况下，可以得到的最大兼容性评分和。所以最终结果为 $dp[states - 1]$，其中 $states = 1 \text{ <}\text{< } m$。

### 思路 1：代码

```python
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        scores = [[0 for _ in range(m)] for _ in range(m)]

        for i in range(m):
            for j in range(m):
                for k in range(n):
                    scores[i][j] += (students[i][k] == mentors[j][k])

        states = 1 << m
        dp = [0 for _ in range(states)]

        for state in range(states):
            one_cnt = bin(state).count('1')
            for i in range(m):
                if (state >> i) & 1:
                    dp[state] = max(dp[state], dp[state ^ (1 << i)] + scores[i][one_cnt - 1])
        return dp[states - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m^2 \times n + m \times 2^m)$。
- **空间复杂度**：$O(2^m)$。

