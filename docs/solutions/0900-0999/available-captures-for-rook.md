# [0999. 可以被一步捕获的棋子数](https://leetcode.cn/problems/available-captures-for-rook/)

- 标签：数组、矩阵、模拟
- 难度：简单

## 题目链接

- [0999. 可以被一步捕获的棋子数 - 力扣](https://leetcode.cn/problems/available-captures-for-rook/)

## 题目大意

**描述**：在一个 $8 \times 8$ 的棋盘上，有一个白色的车（Rook），用字符 `'R'` 表示。棋盘上还可能存在空方块，白色的象（Bishop）以及黑色的卒（pawn），分别用字符 `'.'`，`'B'` 和 `'p'` 表示。不难看出，大写字符表示的是白棋，小写字符表示的是黑棋。

**要求**：你现在可以控制车移动一次，请你统计有多少敌方的卒处于你的捕获范围内（即，可以被一步捕获的棋子数）。

**说明**：

- 车按国际象棋中的规则移动。东，西，南，北四个基本方向任选其一，然后一直向选定的方向移动，直到满足下列四个条件之一：
  - 棋手选择主动停下来。
  - 棋子因到达棋盘的边缘而停下。
  - 棋子移动到某一方格来捕获位于该方格上敌方（黑色）的卒，停在该方格内。
  - 车不能进入/越过已经放有其他友方棋子（白色的象）的方格，停在友方棋子前。

- $board.length == board[i].length == 8$
- $board[i][j]$ 可以是 `'R'`，`'.'`，`'B'` 或 `'p'`。
- 只有一个格子上存在 $board[i][j] == 'R'$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_1_improved.PNG)

```python
输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
输出：3
解释：在本例中，车能够捕获所有的卒。
```

- 示例 2：

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_2_improved.PNG) 

```python
输入：[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
输出：0
解释：象阻止了车捕获任何卒。
```

## 解题思路

### 思路 1：模拟

1. 双重循环遍历确定白色车的位置 $(pos\underline{\hspace{0.5em}}i,poss\underline{\hspace{0.5em}}j)$。
2. 让车向上、下、左、右四个方向进行移动，直到超出边界 / 碰到白色象 / 碰到卒为止。使用计数器 $cnt$ 记录捕获的卒的数量。
3. 返回答案 $cnt$。

### 思路 1：代码

```Python
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        pos_i, pos_j = -1, -1
        for i in range(len(board)):
            if pos_i != -1 and pos_j != -1:
                break
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    pos_i, pos_j = i, j
                    break

        cnt = 0
        for direction in directions:
            setp = 0
            while True:
                new_i = pos_i + setp * direction[0]
                new_j = pos_j + setp * direction[1]
                if new_i < 0 or new_i >= 8 or new_j < 0 or new_j >= 8 or board[new_i][new_j] == 'B':
                    break
                if board[new_i][new_j] == 'p':
                    cnt += 1
                    break
                setp += 1
        
        return cnt
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 为棋盘的边长。
- **空间复杂度**：$O(1)$。

