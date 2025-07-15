# [面试题 08.12. 八皇后](https://leetcode.cn/problems/eight-queens-lcci/)

- 标签：数组、回溯
- 难度：困难

## 题目链接

- [面试题 08.12. 八皇后 - 力扣](https://leetcode.cn/problems/eight-queens-lcci/)

## 题目大意

- n 皇后问题：将 n 个皇后放置在 `n * n` 的棋盘上，并且使得皇后彼此之间不能攻击。
- 皇后彼此不能相互攻击：指的是任何两个皇后都不能处于同一条横线、纵线或者斜线上。

现在给定一个整数 `n`，返回所有不同的「n 皇后问题」的解决方案。每一种解法包含一个不同的「n 皇后问题」的棋子放置方案，该方案中的 `Q` 和 `.` 分别代表了皇后和空位。

## 解题思路

经典的回溯问题。使用 `chessboard` 来表示棋盘，`Q` 代表皇后，`.` 代表空位，初始都为 `.`。然后使用 `res` 存放最终答案。

先定义棋盘合理情况判断方法，判断同一条横线、纵线或者斜线上是否存在两个以上的皇后。

再定义回溯方法，从第一行开始进行遍历。

- 如果当前行 `row` 等于 `n`，则当前棋盘为一个可行方案，将其拼接加入到 `res` 数组中。
-  遍历 `[0, n]` 列元素，先验证棋盘是否可行，如果可行：
  - 将当前行当前列尝试换为 `Q`。
  - 然后继续递归下一行。
  - 再将当前行回退为 `.`。
- 最终返回 `res` 数组。

## 代码

```python
class Solution:
    res = []
    def backtrack(self, n: int, row: int, chessboard: List[List[str]]):
        if row == n:
            temp_res = []
            for temp in chessboard:
                temp_str = ''.join(temp)
                temp_res.append(temp_str)
            self.res.append(temp_res)
            return
        for col in range(n):
            if self.isValid(n, row, col, chessboard):
                chessboard[row][col] = 'Q'
                self.backtrack(n, row + 1, chessboard)
                chessboard[row][col] = '.'

    def isValid(self, n: int, row: int, col: int, chessboard: List[List[str]]):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res.clear()
        chessboard = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(n, 0, chessboard)
        return self.res
```

