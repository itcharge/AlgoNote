# [0488. 祖玛游戏](https://leetcode.cn/problems/zuma-game/)

- 标签：栈、广度优先搜索、记忆化搜索、字符串、动态规划
- 难度：困难

## 题目链接

- [0488. 祖玛游戏 - 力扣](https://leetcode.cn/problems/zuma-game/)

## 题目大意

**描述**：

你正在参与祖玛游戏的一个变种。

在这个祖玛游戏变体中，桌面上有一排彩球，每个球的颜色可能是：红色 `'R'`、黄色 `'Y'`、蓝色 `'B'`、绿色 `'G'` 或白色 `'W'`。你的手中也有一些彩球。

你的目标是「清空」桌面上所有的球。每一回合：

- 从你手上的彩球中选出「任意一颗」，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
- 接着，如果有出现「三个或者三个以上」且 颜色相同 的球相连的话，就把它们移除掉。
- 如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
- 如果桌面上所有球都被移除，则认为你赢得本场游戏。
- 重复这个过程，直到你赢了游戏或者手中没有更多的球。

给定一个字符串 $board$，表示桌面上最开始的那排球。另给你一个字符串 $hand$，表示手里的彩球。

**要求**：

请你按上述操作步骤移除掉桌上所有球，计算并返回所需的「最少」球数。如果不能移除桌上所有的球，返回 $-1$。

**说明**：

- $1 \le board.length \le 16$。
- $1 \le hand.length \le 5$。
- $board$ 和 $hand$ 由字符 `'R'`、`'Y'`、`'B'`、`'G'` 和 `'W'` 组成。
- 桌面上一开始的球中，不会有三个及三个以上颜色相同且连着的球。

**示例**：

- 示例 1：

```python
输入：board = "WRRBBW", hand = "RB"
输出：-1
解释：无法移除桌面上的所有球。可以得到的最好局面是：
- 插入一个 'R' ，使桌面变为 WRRRBBW 。WRRRBBW -> WBBW
- 插入一个 'B' ，使桌面变为 WBBBW 。WBBBW -> WW
桌面上还剩着球，没有其他球可以插入。
```

- 示例 2：

```python
输入：board = "WWRRBBWW", hand = "WRBRW"
输出：2
解释：要想清空桌面上的球，可以按下述步骤：
- 插入一个 'R' ，使桌面变为 WWRRRBBWW 。WWRRRBBWW -> WWBBWW
- 插入一个 'B' ，使桌面变为 WWBBBWW 。WWBBBWW -> WWWW -> empty
只需从手中出 2 个球就可以清空桌面。
```

## 解题思路

### 思路 1：广度优先搜索

**核心思想**：使用广度优先搜索（BFS）逐层探索所有可能的状态。每次从队列中取出一个状态，使用「智能剪枝」在关键位置插入手中的球，然后递归删除连续的同色球。

**算法步骤**：

1. 初始化：将 $hand$ 进行排序，如 $hand = "WRBYG"$ 排序为 $"BGRWY"$，避免相同颜色不同排列的重复计算。
2. 初始化队列：将初始状态 $(board, sorted\_hand, 0)$ 加入队列。
3. 使用哈希表 $visited$ 记录已访问的状态 $(board, hand)$。
4. 逐层处理队列：
   - 取出当前状态 $(curr\_board, curr\_hand, step)$。
   - 使用 $product$ 尝试在每个位置 $i \in [0, len(curr\_board) + 1]$ 插入手中的每个球 $j \in [0, len(curr\_hand)]$。
   - **剪枝 1**：如果当前球和上一个球颜色相同，跳过（避免重复）。
   - **剪枝 2**：跳过在连续相同颜色球开头之后的位置插入相同颜色（因为开头之前插入效果相同）。
   - **剪枝 3**：只在两种情况下插入球：
     - 插入位置的球颜色与插入颜色相同（形成连续）；
     - 前后颜色相同且与插入颜色不同（形成消除）。
   - 插入后执行递归删除操作，如果桌面为空则返回当前步数。
   - 将新状态加入队列（如果未访问过）。

**关键点**：
- **三重剪枝策略**：通过三个剪枝条件大幅减少无效的插入尝试，提升效率。
- **状态去重**：对 $hand$ 排序并使用 $visited$ 避免重复状态。
- **高效删除**：使用正则表达式 `re.subn` 递归删除连续 $3$ 个及以上同色球。

### 思路 1：代码

```python
from collections import deque
import re

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:        
        # 递归删除连续 3 个及以上同色球
        def remove_balls(s):
            """删除字符串中连续的 3 个及以上相同字符"""
            while True:
                # 查找是否有连续的 3 个及以上相同字符
                n = len(s)
                if n < 3:
                    break
                
                # 记录当前连续相同字符的开始位置
                start = 0
                found = False
                
                for i in range(1, n + 1):
                    # 如果到达末尾或字符不同，检查是否需要删除
                    if i == n or s[i] != s[start]:
                        # 如果连续长度 >= 3，进行删除
                        if i - start >= 3:
                            s = s[:start] + s[i:]
                            found = True
                            break
                        start = i
                
                # 如果没有找到需要删除的连续字符，退出循环
                if not found:
                    break
            
            return s
        
        # 对手中的球进行排序，将相同颜色的球归类在一起
        sorted_hand = ''.join(sorted(hand))
        
        # 初始化 BFS 队列和访问记录
        # 每个状态包含：(当前桌面状态, 手中剩余球, 已使用步数)
        queue = deque()
        queue.append((board, sorted_hand, 0))
        
        # 记录已访问过的状态，避免重复搜索
        seen = {(board, sorted_hand)}
        
        while queue:
            curr_board, curr_hand, steps = queue.popleft()
            
            # 尝试在每一个可能的位置插入每一个球
            for pos in range(len(curr_board) + 1):
                for idx in range(len(curr_hand)):
                    # 获取要插入的球的颜色
                    ball = curr_hand[idx]
                    
                    # 剪枝 1：如果这个球和上一个球颜色相同，跳过
                    # （避免对同一个颜色重复尝试）
                    if idx > 0 and curr_hand[idx] == curr_hand[idx - 1]:
                        continue
                    
                    # 剪枝 2：跳过在连续相同颜色球的开头之后插入相同颜色
                    # 原理：在连续相同颜色块中间插入相同颜色的球，
                    # 效果和在块开头之前插入相同，会产生重复状态
                    if pos > 0 and curr_board[pos - 1] == ball:
                        continue
                    
                    # 剪枝 3：只在有效的情况下插入球
                    # 情况 a：插入位置的颜色与插入球颜色相同（形成连续）
                    # 情况 b：前后颜色相同且与插入球颜色不同（可形成消除）
                    should_insert = False
                    
                    # 检查情况 a
                    if pos < len(curr_board) and curr_board[pos] == ball:
                        should_insert = True
                    
                    # 检查情况 b
                    elif pos > 0 and pos < len(curr_board):
                        if curr_board[pos - 1] == curr_board[pos] and curr_board[pos - 1] != ball:
                            should_insert = True
                    
                    if should_insert:
                        # 在指定位置插入球
                        new_board = curr_board[:pos] + ball + curr_board[pos:]
                        
                        # 删除插入后形成的连续球
                        new_board = remove_balls(new_board)
                        
                        # 更新手中的球（移除已使用的球）
                        new_hand = curr_hand[:idx] + curr_hand[idx + 1:]
                        
                        # 如果桌面已清空，返回步数
                        if not new_board:
                            return steps + 1
                        
                        # 构建新状态
                        new_state = (new_board, new_hand)
                        
                        # 如果这个新状态没有被访问过，加入队列
                        if new_state not in seen:
                            queue.append((new_board, new_hand, steps + 1))
                            seen.add(new_state)
        
        # 无法清空桌面
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m \times 5^m \times 2^n)$。其中 $n$ 是 $board$ 的长度（最多 $16$），$m$ 是 $hand$ 的长度（最多 $5$）。最坏情况下需要遍历所有可能的状态组合，但由于三重剪枝策略和状态去重，搜索空间被大幅缩减，实际运行时间会被控制在合理范围内。
- **空间复杂度**：$O(5^m \times 2^n)$。用于存储 BFS 队列和已访问状态的集合。虽然理论状态数可能达到指数级别，但由于剪枝策略，实际状态数会大大减少，且 $n \le 16$、$m \le 5$ 保证了实际运行的可行性。

## 参考资料

- [0488. 祖玛游戏-官方题解](https://leetcode.cn/problems/zuma-game/solutions/1092466/zu-ma-you-xi-by-leetcode-solution-lrp4/)
