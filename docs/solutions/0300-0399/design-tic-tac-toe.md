# [0348. 设计井字棋](https://leetcode.cn/problems/design-tic-tac-toe/)

- 标签：设计、数组、哈希表、矩阵、模拟
- 难度：中等

## 题目链接

- [0348. 设计井字棋 - 力扣](https://leetcode.cn/problems/design-tic-tac-toe/)

## 题目大意

**要求**：

在 $n \times n$ 的棋盘上，实现一个判定井字棋（Tic-Tac-Toe）胜负的神器，判断每一次玩家落子后，是否有胜出的玩家。

在这个井字棋游戏中，会有 $2$ 名玩家，他们将轮流在棋盘上放置自己的棋子。

在实现这个判定器的过程中，你可以假设以下这些规则一定成立：

1. 每一步棋都是在棋盘内的，并且只能被放置在一个空的格子里；
2. 一旦游戏中有一名玩家胜出的话，游戏将不能再继续；
3. 一个玩家如果在同一行、同一列或者同一斜对角线上都放置了自己的棋子，那么他便获得胜利。

**说明**：

- $2 \le n \le 10^{3}$。
- 玩家是 $1$ 或 $2$。
- $0 \le row, col \lt n$。
- 每次调用 `move` 时 $(row, col)$ 都是不同的。
- 最多调用 `move` $n2$ 次。

- 进阶：有没有可能将每一步的 `move()` 操作优化到比 $O(n2)$ 更快吗?

**示例**：

- 示例 1：

```python
给定棋盘边长 n = 3, 玩家 1 的棋子符号是 "X"，玩家 2 的棋子符号是 "O"。

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> 函数返回 0 (此时，暂时没有玩家赢得这场对决)
|X| | |
| | | |    // 玩家 1 在 (0, 0) 落子。
| | | |

toe.move(0, 2, 2); -> 函数返回 0 (暂时没有玩家赢得本场比赛)
|X| |O|
| | | |    // 玩家 2 在 (0, 2) 落子。
| | | |

toe.move(2, 2, 1); -> 函数返回 0 (暂时没有玩家赢得比赛)
|X| |O|
| | | |    // 玩家 1 在 (2, 2) 落子。
| | |X|

toe.move(1, 1, 2); -> 函数返回 0 (暂没有玩家赢得比赛)
|X| |O|
| |O| |    // 玩家 2 在 (1, 1) 落子。
| | |X|

toe.move(2, 0, 1); -> 函数返回 0 (暂无玩家赢得比赛)
|X| |O|
| |O| |    // 玩家 1 在 (2, 0) 落子。
|X| |X|

toe.move(1, 0, 2); -> 函数返回 0 (没有玩家赢得比赛)
|X| |O|
|O|O| |    // 玩家 2 在 (1, 0) 落子.
|X| |X|

toe.move(2, 1, 1); -> 函数返回 1 (此时，玩家 1 赢得了该场比赛)
|X| |O|
|O|O| |    // 玩家 1 在 (2, 1) 落子。
|X|X|X|
```

## 解题思路

### 思路 1：计数法

**核心思想**：使用计数数组来跟踪每个玩家在每行、每列和两条对角线上的棋子数量，避免每次检查整个棋盘。

**算法步骤**：

1. **初始化**：创建 $n \times n$ 的棋盘，以及用于计数的数组：
   - `rows[i]`：第 $i$ 行上每个玩家的棋子数量。
   - `cols[j]`：第 $j$ 列上每个玩家的棋子数量。
   - `diagonal`：主对角线上的棋子数量。
   - `anti_diagonal`：副对角线上的棋子数量。

2. **落子操作**：
   - 在位置 $(row, col)$ 放置玩家 $player$ 的棋子。
   - 更新对应的行、列计数。
   - 如果 $(row, col)$ 在主对角线上（$row = col$），更新 `diagonal`。
   - 如果 $(row, col)$ 在副对角线上（$row + col = n - 1$），更新 `anti_diagonal`。

3. **胜负判断**：
   - 检查当前行、列或对角线是否被当前玩家完全占据。
   - 如果任一计数达到 $n$，则该玩家获胜。

### 思路 1：代码

```python
class TicTacToe:

    def __init__(self, n: int):
        """
        初始化井字棋游戏
        :param n: 棋盘大小 n x n
        """
        self.n = n
        # 初始化棋盘
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        
        # 计数数组：跟踪每个玩家在每行、每列的棋子数量
        # rows[i][player] 表示第 i 行上玩家 player 的棋子数量
        self.rows = [[0, 0] for _ in range(n)]  # 索引 0 和 1 分别对应玩家 1 和 2
        self.cols = [[0, 0] for _ in range(n)]  # 索引 0 和 1 分别对应玩家 1 和 2
        
        # 对角线计数
        self.diagonal = [0, 0]      # 主对角线 (i == j)
        self.anti_diagonal = [0, 0] # 副对角线 (i + j == n - 1)

    def move(self, row: int, col: int, player: int) -> int:
        """
        玩家在指定位置落子
        :param row: 行索引
        :param col: 列索引  
        :param player: 玩家编号 (1 或 2)
        :return: 获胜玩家编号，如果无人获胜返回 0
        """
        # 将玩家编号转换为数组索引 (1 -> 0, 2 -> 1)
        player_idx = player - 1
        
        # 在棋盘上放置棋子
        self.board[row][col] = player
        
        # 更新行计数
        self.rows[row][player_idx] += 1
        
        # 更新列计数
        self.cols[col][player_idx] += 1
        
        # 更新主对角线计数 (row == col)
        if row == col:
            self.diagonal[player_idx] += 1
            
        # 更新副对角线计数 (row + col == n - 1)
        if row + col == self.n - 1:
            self.anti_diagonal[player_idx] += 1
        
        # 检查是否获胜
        # 如果当前行、列或任一对角线被当前玩家完全占据，则获胜
        if (self.rows[row][player_idx] == self.n or
            self.cols[col][player_idx] == self.n or
            self.diagonal[player_idx] == self.n or
            self.anti_diagonal[player_idx] == self.n):
            return player
            
        return 0  # 无人获胜


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。每次 `move` 操作只需要更新计数数组和检查胜负，时间复杂度为常数。
- **空间复杂度**：$O(n)$。需要 $O(n^2)$ 空间存储棋盘，$O(n)$ 空间存储计数数组，总体为 $O(n^2)$。
