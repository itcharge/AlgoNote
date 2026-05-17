# [1284. 转化为全零矩阵的最少反转次数](https://leetcode.cn/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

- 标签：位运算、广度优先搜索、数组、哈希表、矩阵
- 难度：困难

## 题目链接

- [1284. 转化为全零矩阵的最少反转次数 - 力扣](https://leetcode.cn/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

## 题目大意

**描述**：给定一个 $m \times n$ 的二进制矩阵 $mat$（只包含 $0$ 和 $1$）。每一步操作可以选择一个格子 $(i, j)$，反转该格子以及该格子的上、下、左、右四个方向相邻格子（如果存在）。

**要求**：返回将矩阵变为全 $0$ 矩阵所需的最少操作次数。如果无法变为全 $0$ 矩阵，返回 $-1$。

**说明**：

- $1 \le m \le 3$。
- $1 \le n \le 3$。
- $mat[i][j] \in \{0, 1\}$。

## 题目链接

- [1284. 转化为全零矩阵的最少反转次数 - 力扣](https://leetcode.cn/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

## 解题思路

### 思路 1：BFS + 状态压缩

#### 1. 核心思想

矩阵最大为 $3 \times 3 = 9$ 个格子，每个格子有 $0$ 或 $1$ 两种状态，总状态数为 $2^9 = 512$ 种。状态空间非常小，完全可以用 BFS 搜索从初始状态到全 $0$ 状态的最短路径。

**状态压缩**：将 $m \times n$ 的矩阵压缩成一个整数。把每个格子看作二进制的一位，矩阵的第 $(i, j)$ 个格子对应整数的第 $(i \times n + j)$ 位。$1$ 对应位为 $1$，$0$ 对应位为 $0$。

这样，状态表示、合法性检查、操作模拟都可以用位运算高效完成。

#### 2. 建图、遍历、标记、收集

- **建图**：每个状态是一个 $mn$ 位的整数。每个状态可以通过对某个格子（及其上下左右邻格）进行反转操作，转移到新状态。
- **遍历**：BFS 逐层搜索，从初始状态开始。
- **标记**：用 $visited$ 集合记录已访问的状态，避免重复搜索。
- **收集**：当状态变为 $0$ 时，返回当前步数。

#### 3. 具体步骤

**第 1 步**：将初始矩阵压缩为整数 $start$：
- 遍历矩阵，如果 $mat[i][j] == 1$，则将 $start$ 的第 $(i \times n + j)$ 位置为 $1$。

**第 2 步**：BFS 搜索：
- 队列中存储 $(state, steps)$。
- $state = 0$ 时直接返回 $0$。
- 对于当前状态 $state$，尝试对每个格子 $(i, j)$ 进行反转：
  - 计算反转后的新状态 $next\_state$：将 $(i, j)$ 及其上下左右邻格的对应位取反。
  - 取反操作用**异或**实现：构造一个掩码 $mask$，要反转的位为 $1$，其余位为 $0$，$next\_state = state \oplus mask$。
  - 如果 $next\_state$ 未访问过，入队并标记。

**第 3 步**：队列为空时返回 $-1$。

#### 4. 结合示例走一遍

以 $1 \times 2$ 矩阵 $[[1, 0]]$ 为例：

初始状态：二进制 `01`（假设第 $0$ 位是 $(0,0)$，第 $1$ 位是 $(0,1)$），十进制 $1$。

```
第 0 层: state=1 (二进制 01)
  反转 (0,0): 影响 (0,0) 和 (0,1) → 掩码 11 (3) → state⊕3=2 (二进制 10)
  反转 (0,1): 影响 (0,0) 和 (0,1) → 掩码 11 (3) → state⊕3=2 (二进制 10)

第 1 层: state=2 (二进制 10)
  反转 (0,0): 影响 (0,0) 和 (0,1) → 掩码 11 (3) → state⊕3=1 (二进制 01) 已访问
  反转 (0,1): 影响 (0,0) 和 (0,1) → 掩码 11 (3) → state⊕3=1 (二进制 01) 已访问
  
队列为空，返回 -1。
```

这个例子说明 $[[1,0]]$ 无法变为全 $0$。

换个例子：$[[0,1],[1,0]]$（$2 \times 2$）：

初始状态：二进制 `0110`（位 $0$=0, 位 $1$=1, 位 $2$=1, 位 $3$=0），十进制 $6$。

反转 $(0,1)$（影响 $(0,0),(0,1),(1,1)$）：
- 掩码：位 $0$（$(0,0)$）、位 $1$（$(0,1)$）、位 $3$（$(1,1)$）→ `1011` (11)
- $6 \oplus 11 = 13$（二进制 `1101`，即 $[[1,0],[0,1]]$）

继续 BFS 直到状态变为 $0$。

### 思路 1：代码

```python
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # 状态压缩：将矩阵转为整数
        start = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    start |= 1 << (i * n + j)

        # 如果已经是全零
        if start == 0:
            return 0

        # 四个方向（上、下、左、右）
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total = m * n

        # 预处理每个位置的反转掩码
        masks = []
        for i in range(m):
            for j in range(n):
                mask = 1 << (i * n + j)  # 自己
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        mask |= 1 << (ni * n + nj)
                masks.append(mask)

        # BFS
        q = deque([(start, 0)])
        visited = set([start])

        while q:
            state, steps = q.popleft()
            for mask in masks:
                next_state = state ^ mask
                if next_state == 0:
                    return steps + 1
                if next_state not in visited:
                    visited.add(next_state)
                    q.append((next_state, steps + 1))

        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(2^{mn} \times mn)$，总状态数 $2^{mn}$ 最多 $2^9 = 512$，每个状态扩展 $mn$ 次（最多 $9$ 次），实际运行非常快。
- **空间复杂度**：$O(2^{mn})$，需要存储所有已访问状态。

### 思路 2：DFS 枚举所有操作组合

由于状态空间极小，还可以直接枚举所有可能的操作组合（每个格子可以选或不选，共 $2^{mn}$ 种可能），检查是否能使矩阵变为全 $0$，取操作次数最少的一种。这和思路 1 本质相同，BFS 的优势在于它找到的就是最短路径，不需要全部枚举完再取最小值。
