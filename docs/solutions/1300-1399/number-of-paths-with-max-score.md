# [1301. 最大得分的路径数目](https://leetcode.cn/problems/number-of-paths-with-max-score/)

- 标签：数组、动态规划、矩阵
- 难度：困难

## 题目链接

- [1301. 最大得分的路径数目 - 力扣](https://leetcode.cn/problems/number-of-paths-with-max-score/)

## 题目大意

**描述**：给定一个 $n \times n$ 的字符矩阵 $board$。起点为右下角的 `'S'`，终点为左上角的 `'E'`。每次移动可以向左、上、左上（三个方向）移动一格。路径上会经过数字字符（'0' ~ '9'），其数值累加到得分中。`'X'` 表示障碍物，不可经过。

**要求**：返回从 `'S'` 到 `'E'` 的最大得分以及得到该得分的路径数目。结果对 $10^9 + 7$ 取模。如果无法到达，返回 $[0, 0]$。

**说明**：
- $2 \le n \le 100$。
- 保证有且只有一个 `'S'` 和一个 `'E'`。

**示例**：

- 示例 1：

```python
输入：board = ["E23","2X2","12S"]
输出：[7,1]
```

- 示例 2：

```python
输入：board = ["E12","1X1","21S"]
输出：[4,2]
```


## 解题思路

### 思路 1：动态规划

#### 1. 阶段划分

从右下角 `'S'` 走到左上角 `'E'`，移动方向为左、上、左上。因此可以按**从右下到左上**的顺序逐行逐列处理。

#### 2. 定义状态

定义两个 DP 数组，维度均为 $(n+1) \times (n+1)$（加一圈边界方便处理）：
- $score[i][j]$：从 `'S'` 到 $(i,j)$ 的最大得分
- $count[i][j]$：从 `'S'` 到 $(i,j)$ 达到最大得分的路径数目

为方便起见，在矩阵的右侧和下方各加一行/列 $0$ 作为哨兵。

#### 3. 状态转移方程

对于位置 $(i, j)$（$1$ 索引），可以从三个方向转移：
- 从左边 $(i, j-1)$ 来
- 从上边 $(i-1, j)$ 来
- 从左上 $(i-1, j-1)$ 来

先计算三个方向中的最大得分 $best$：

$$best = \max(score[i-1][j], \; score[i][j-1], \; score[i-1][j-1])$$

然后从达到 $best$ 的方向累加路径数：

$$count[i][j] = \sum_{\substack{dir \in \{(i-1,j),(i,j-1),(i-1,j-1)\} \\ score[dir] == best}} count[dir]$$

最后加上当前位置的数字得分：

$$score[i][j] = best + val(i,j)$$

其中 $val(i,j)$ 是 $(i,j)$ 处的数字值（如果是 `'S'` 或 `'E'` 则为 $0$）。

#### 4. 初始条件

$score[n][n] = 0$（起点 `'S'` 处得分为 $0$）。
$count[n][n] = 1$（起点处有一条路径）。

#### 5. 最终结果

$res = [score[1][1], \; count[1][1] \% MOD]$，其中 $MOD = 10^9 + 7$。

如果 $score[1][1] == 0$ 且 $count[1][1] == 0$（不可达），返回 $[0, 0]$。

#### 6. 举例说明

以 $board = ["E23","2X2","12S"]$ 为例：

```
E 2 3
2 X 2
1 2 S
```

从右下角 `'S'` 出发逆推：

- $(3,3)$：`'S'`，$score=0, count=1$
- $(3,2)$：`'2'`，从 $(3,3)$ 左移来，$score=2, count=1$
- $(3,1)$：`'1'`，从 $(3,2)$ 左移来，$score=2+1=3, count=1$
- $(2,3)$：`'2'`，从 $(3,3)$ 上移来，$score=2, count=1$
- $(2,2)$：`'X'`，障碍物，跳过
- $(2,1)$：`'2'`，从 $(3,1)$ 上移来，$score=3+2=5, count=1$
- 依此类推直到左上角...

### 思路 1：代码

```python
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        # 加两圈边界（1-indexed），方便处理 i+1/j+1 不越界
        score = [[0] * (n + 2) for _ in range(n + 2)]
        count = [[0] * (n + 2) for _ in range(n + 2)]

        # 起点：右下角 S
        count[n][n] = 1

        # 从右下角向左上角遍历
        for i in range(n, 0, -1):
            for j in range(n, 0, -1):
                if i == n and j == n:
                    continue  # 起点已初始化
                ch = board[i - 1][j - 1]
                if ch == 'X':
                    continue  # 障碍物

                # 三个方向的最大得分
                best = max(score[i + 1][j], score[i][j + 1], score[i + 1][j + 1])
                # 累加达到 best 的路径数
                ways = 0
                if score[i + 1][j] == best:
                    ways = (ways + count[i + 1][j]) % MOD
                if score[i][j + 1] == best:
                    ways = (ways + count[i][j + 1]) % MOD
                if score[i + 1][j + 1] == best:
                    ways = (ways + count[i + 1][j + 1]) % MOD

                score[i][j] = best
                count[i][j] = ways

                # 加上当前位置的数字得分
                if ch != 'E':
                    score[i][j] += int(ch)

        if count[1][1] == 0:
            return [0, 0]
        return [score[1][1], count[1][1] % MOD]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，需要遍历整个矩阵。
- **空间复杂度**：$O(n^2)$，使用两个 $(n+1) \times (n+1)$ 的 DP 数组。

---

### 思路 2：空间优化

注意到状态转移只依赖右方、下方、右下方的值，可以只用一维数组滚动优化，但为了代码可读性通常保留二维写法。
