# [0526. 优美的排列](https://leetcode.cn/problems/beautiful-arrangement/)

- 标签：位运算、数组、动态规划、回溯、状态压缩
- 难度：中等

## 题目链接

- [0526. 优美的排列 - 力扣](https://leetcode.cn/problems/beautiful-arrangement/)

## 题目大意

**描述**：给定一个整数 $n$。

**要求**：返回可以构造的「优美的排列」的数量。

**说明**：

- **优美的排列**：假设有 $1 \sim n$ 的 $n$ 个整数。如果用这些整数构造一个数组 $perm$（下标从 $1$ 开始），使得数组第 $i$ 位元素 $perm[i]$ 满足下面两个条件之一，则该数组就是一个「优美的排列」：
  - $perm[i]$ 能够被 $i$ 整除；
  - $i$ 能够被 $perm[i]$ 整除。

- $1 \le n \le 15$。

**示例**：

- 示例 1：

```python
输入：n = 2
输出：2
解释：
第 1 个优美的排列是 [1,2]：
    - perm[1] = 1 能被 i = 1 整除
    - perm[2] = 2 能被 i = 2 整除
第 2 个优美的排列是 [2,1]:
    - perm[1] = 2 能被 i = 1 整除
    - i = 2 能被 perm[2] = 1 整除
```

- 示例 2：

```python
输入：n = 1
输出：1
```

## 解题思路

### 思路 1：回溯算法

这道题可以看做是「[0046. 全排列](https://leetcode.cn/problems/permutations/)」的升级版。

1. 通过回溯算法我们可以将数组的所有排列情况列举出来。
2. 因为只有满足第 $i$ 位元素能被 $i$ 整除，或者满足 $i$ 能整除第 $i$ 位元素的条件下才符合要求，所以我们可以进行剪枝操作，不再考虑不满足要求的情况。
3. 最后回溯完输出方案数。

### 思路 1：代码

```python
class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        visited = set()

        def backtracking(index):
            nonlocal ans
            if index == n + 1:
                ans += 1
                return

            for i in range(1, n + 1):
                if i in visited:
                    continue
                if i % index == 0 or index % i == 0:
                    visited.add(i)
                    backtracking(index + 1)
                    visited.remove(i)

        backtracking(1)
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n!)$，其中 $n$ 为给定整数。
- **空间复杂度**：$O(n)$，递归栈空间大小为 $O(n)$。

### 思路 2：状态压缩 DP

因为 $n$ 最大只有 $15$，所以我们可以考虑使用「状态压缩」。

「状态压缩」指的是使用一个 $n$ 位的二进制数来表示排列中数的选取情况。

举个例子：

1. $n = 4, state = (1001)_2$，表示选择了数字 $1, 4$，剩余数字 $2$ 和 $3$ 未被选择。
2. $n = 6, state = (011010)_2$，表示选择了数字 $2, 4, 5$，剩余数字 $1, 3, 6$ 未被选择。

这样我们就可以使用 $n$ 位的二进制数 $state$ 来表示当前排列中数的选取情况。

如果我们需要检查值为 $k$ 的数字是否被选择时，可以通过判断 $(state \text{ >} \text{> } (k - 1)) \text{ \& } 1$ 是否为 $1$ 来确定。

如果为 $1$，则表示值为 $k$ 的数字被选择了，如果为 $0$，则表示值为 $k$ 的数字没有被选择。

###### 1. 阶段划分

按照排列的数字个数、数字集合的选择情况进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][state]$ 表示为：考虑前 $i$ 个数，且当数字集合的选择情况为 $state$ 时的方案数。

###### 3. 状态转移方程

假设 $dp[i][state]$ 中第 $i$ 个位置所选数字为 $k$，则：$state$ 中第 $k$ 位为 $1$，且 $k \mod i == 0$ 或者 $i \mod k == 0$。

那么 $dp[i][state]$ 肯定是由考虑前 $i - 1$ 个位置，且 $state$ 第 $k$ 位为 $0$ 的状态而来，即：$dp[i - 1][state \& (\neg(1 \text{ <}\text{< } (k - 1)))]$。

所以状态转移方程为：$dp[i][state] = \sum_{k = 1}^n dp[i - 1][state \text{ \& } (\neg(1 \text{ <} \text{< } (k - 1)))]$。

###### 4. 初始条件

- 不考虑任何数（$i = 0, state = 0$）的情况下，方案数为 $1$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i][state]$ 表示为：考虑前 $i$ 个数，且当数字集合的选择情况为 $state$ 时的方案数。所以最终结果为 $dp[i][states -  1]$，其中 $states = 1 \text{ <} \text{< } n$。

### 思路 2：代码

```python
class Solution:
    def countArrangement(self, n: int) -> int:
        states = 1 << n
        dp = [[0 for _ in range(states)] for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):                   # 枚举第 i 个位置
            for state in range(states):             # 枚举所有状态
                one_num = bin(state).count("1")     # 计算当前状态中选择了多少个数字（即统计 1 的个数）
                if one_num != i:                    # 只有 i 与选择数字个数相同时才能计算
                    continue
                for k in range(1, n + 1):           # 枚举第 i 个位置（最后 1 位）上所选的数字
                    if state >> (k - 1) & 1 == 0:   # 只有 state 第 k 个位置上为 1 才表示选了该数字
                        continue
                    if k % i == 0 or i % k == 0:    # 只有满足整除关系才符合要求
                        # dp[i][state] 由前 i - 1 个位置，且 state 第 k 位为 0 的状态而来
                        dp[i][state] += dp[i - 1][state & (~(1 << (k - 1)))]

        return dp[i][states - 1]
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n^2 \times 2^n)$，其中 $n$ 为给定整数。
- **空间复杂度**：$O(n \times 2^n)$。

### 思路 3：状态压缩 DP + 优化

通过二维的「状态压缩 DP」可以看出，当我们在考虑第 $i$ 个位置时，其选择数字个数也应该为 $i$。

而我们可以根据 $state$ 中 $1$ 的个数来判断当前选择的数字个数，这样我们就可以减少用于枚举第 $i$ 个位置的循环，改用统计 $state$ 中 $1$ 的个数来判断前选择的数字个数或者说当前正在考虑的元素位置。

而这样，我们还可以进一步优化状态的定义，将二维的状态优化为一维的状态。具体做法如下：

###### 1. 阶段划分

按照数字集合的选择情况进行阶段划分。

###### 2. 定义状态

定义状态 $dp[state]$ 表示为：当数字集合的选择情况为 $state$ 时的方案数。

###### 3. 状态转移方程

对于状态 $state$，先统计出 $state$ 中选择的数字个数（即统计二进制中 $1$ 的个数）$one\_num$。

则 $dp[state]$ 表示选择了前 $one\_num$ 个数字，且选择情况为 $state$ 时的方案数。

$dp[state]$ 的状态肯定是由前 $one\_num - 1$ 个数字，且 $state$ 第 $k$ 位为 $0$ 的状态而来对应状态转移而来，即：$dp[state \oplus (1 << (k - 1))]$。

所以状态转移方程为：$dp[state] = \sum_{k = 1}^n dp[state \oplus (1 << (k - 1))]$

###### 4. 初始条件

- 不考虑任何数的情况下，方案数为 $1$，即：$dp[0] = 1$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[state]$ 表示为：当数字集合选择状态为 $state$ 时的方案数。所以最终结果为 $dp[states -  1]$，其中 $states = 1 << n$。

### 思路 3：代码

```python
class Solution:
    def countArrangement(self, n: int) -> int:
        states = 1 << n
        dp = [0 for _ in range(states)]
        dp[0] = 1

        for state in range(states):                         # 枚举所有状态
            one_num = bin(state).count("1")                 # 计算当前状态中选择了多少个数字（即统计 1 的个数）
            for k in range(1, n + 1):                       # 枚举最后 1 位上所选的数字
                if state >> (k - 1) & 1 == 0:               # 只有 state 第 k 个位置上为 1 才表示选了该数字
                    continue
                if one_num % k == 0 or k % one_num == 0:    # 只有满足整除关系才符合要求
                    # dp[state] 由前 one_num - 1 个位置，且 state 第 k 位为 0 的状态而来
                    dp[state] += dp[state ^ (1 << (k - 1))]

        return dp[states - 1]
```

### 思路 3：复杂度分析

- **时间复杂度**：$O(n \times 2^n)$，其中 $n$ 为给定整数。
- **空间复杂度**：$O(2^n)$。

## 参考资料

- 【题解】[【宫水三叶】详解两种状态压缩 DP 思路 - 优美的排列](https://leetcode.cn/problems/beautiful-arrangement/solution/gong-shui-san-xie-xiang-jie-liang-chong-vgsia/)
