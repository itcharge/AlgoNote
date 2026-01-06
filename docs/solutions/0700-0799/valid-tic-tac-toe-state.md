# [0794. 有效的井字游戏](https://leetcode.cn/problems/valid-tic-tac-toe-state/)

- 标签：数组、矩阵
- 难度：中等

## 题目链接

- [0794. 有效的井字游戏 - 力扣](https://leetcode.cn/problems/valid-tic-tac-toe-state/)

## 题目大意

**描述**：

井字游戏的棋盘是一个 $3 \times 3$ 数组，由字符 `' '`，`'X'` 和 `'O'` 组成。字符 `' '` 代表一个空位。

以下是井字游戏的规则：

- 玩家轮流将字符放入空位 `' '` 中。
- 玩家 1 总是放字符 `'X'`，而玩家 2 总是放字符 `'O'`。
- `'X'` 和 `'O'` 只允许放置在空位中，不允许对已放有字符的位置进行填充。
- 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
- 当所有位置非空时，也算为游戏结束。
- 如果游戏结束，玩家不允许再放置字符。

给定一个字符串数组 $board$ 表示井字游戏的棋盘。

**要求**：

当且仅当在井字游戏过程中，棋盘有可能达到 $board$ 所显示的状态时，才返回 true。

**说明**：

- $board.length == 3$。
- $board[i].length == 3$。
- $board[i][j]$ 为 `'X'`、`'O'` 或 `' '`。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/05/15/tictactoe1-grid.jpg)

```python
输入：board = ["O  ","   ","   "]
输出：false
解释：玩家 1 总是放字符 "X" 。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/05/15/tictactoe2-grid.jpg)

```python
输入：board = ["XOX"," X ","   "]
输出：false
解释：玩家应该轮流放字符。
```

## 解题思路

### 思路 1：模拟

判断井字游戏的状态是否有效，需要检查以下条件：

1. **数量关系**：玩家 1（`X`）先手，所以 `X` 的数量应该等于或比 `O` 多 $1$。
2. **获胜条件**：
   - 如果 `X` 获胜，则 `O` 不能获胜，且 `X` 的数量应该比 `O` 多 $1$（因为 `X` 最后一步获胜）。
   - 如果 `O` 获胜，则 `X` 不能获胜，且 `X` 的数量应该等于 `O` 的数量（因为 `O` 最后一步获胜）。

### 思路 1：代码

```python
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def check_win(player):
            """检查某个玩家是否获胜"""
            # 检查行
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
            # 检查列
            for j in range(3):
                if all(board[i][j] == player for i in range(3)):
                    return True
            # 检查对角线
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2-i] == player for i in range(3)):
                return True
            return False
        
        # 统计 X 和 O 的数量
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)
        
        # X 的数量应该等于或比 O 多 1
        if x_count < o_count or x_count > o_count + 1:
            return False
        
        # 检查获胜情况
        x_win = check_win('X')
        o_win = check_win('O')
        
        # X 和 O 不能同时获胜
        if x_win and o_win:
            return False
        
        # 如果 X 获胜，X 的数量应该比 O 多 1
        if x_win and x_count != o_count + 1:
            return False
        
        # 如果 O 获胜，X 和 O 的数量应该相等
        if o_win and x_count != o_count:
            return False
        
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$，棋盘大小固定为 $3 \times 3$。
- **空间复杂度**：$O(1)$。
