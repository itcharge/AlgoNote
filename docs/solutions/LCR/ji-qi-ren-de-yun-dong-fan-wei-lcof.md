# [LCR 130. 衣橱整理](https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

- 标签：深度优先搜索、广度优先搜索、动态规划
- 难度：中等

## 题目链接

- [LCR 130. 衣橱整理 - 力扣](https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

## 题目大意

**描述**：有一个 `m * n` 大小的方格，坐标从 `(0, 0)` 到 `(m - 1, n - 1)`。一个机器人从 `(0, 0)` 处的格子开始移动，每次可以向上、下、左、右移动一格（不能移动到方格外），也不能移动到行坐标和列坐标的数位之和大于 `k` 的格子。现在给定 `3` 个整数 `m`、`n`、`k`。

**要求**：计算并输出该机器人能够达到多少个格子。

**说明**：

- $1 \le n, m \le 100$。
- $0 \le k \le 20$。

**示例**：

- 示例 1：

```python
输入：m = 2, n = 3, k = 1
输出：3
```

- 示例 2：

```python
输入：m = 3, n = 1, k = 0
输出：1
```

## 解题思路

### 思路 1：广度优先搜索

先定义一个计算数位和的方法 `digitsum`，该方法输入一个整数，返回该整数各个数位的总和。

然后我们使用广度优先搜索方法，具体步骤如下：

- 将 `(0, 0)` 加入队列 `queue` 中。
- 当队列不为空时，每次将队首坐标弹出，加入访问集合 `visited` 中。
- 再将满足行列坐标的数位和不大于 `k` 的格子位置加入到队列中，继续弹出队首位置。
- 直到队列为空时停止。输出访问集合的长度。

### 思路 1：代码

```python
import collections

class Solution:
    def digitsum(self, n: int):
        ans = 0
        while n:
            ans += n % 10
            n //= 10
        return ans

    def movingCount(self, m: int, n: int, k: int) -> int:
        queue = collections.deque([(0, 0)])
        visited = set()

        while queue:
            x, y = queue.popleft()
            if (x, y) not in visited and self.digitsum(x) + self.digitsum(y) <= k:
                visited.add((x, y))
                for dx, dy in [(1, 0), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        queue.append((nx, ny))
        return len(visited)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$。其中 $m$ 为方格的行数，$n$ 为方格的列数。
- **空间复杂度**：$O(m \times n)$。

