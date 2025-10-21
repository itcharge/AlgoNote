# [0353. 贪吃蛇](https://leetcode.cn/problems/design-snake-game/)

- 标签：设计、队列、数组、哈希表、模拟
- 难度：中等

## 题目链接

- [0353. 贪吃蛇 - 力扣](https://leetcode.cn/problems/design-snake-game/)

## 题目大意

**要求**：

设计一个「贪吃蛇游戏」，该游戏将会在一个「屏幕尺寸 = 宽度 x 高度」的屏幕上运行。如果你不熟悉这个游戏，可以 [点击这里](http://patorjk.com/games/snake/) 在线试玩。

起初时，蛇在左上角的 $(0, 0)$ 位置，身体长度为 $1$ 个单位。

你将会被给出一个数组形式的食物位置序列 $food$ ，其中 $food[i] = (ri, ci)$。当蛇吃到食物时，身子的长度会增加 $1$ 个单位，得分也会 $+1$。

食物不会同时出现，会按列表的顺序逐一显示在屏幕上。比方讲，第一个食物被蛇吃掉后，第二个食物才会出现。

当一个食物在屏幕上出现时，保证不会出现在被蛇身体占据的格子里。

如果蛇越界（与边界相撞）或者头与「移动后」的身体相撞（即，身长为 $4$ 的蛇无法与自己相撞），游戏结束。

实现 `SnakeGame` 类：

- `SnakeGame(int width, int height, int[][] food)` 初始化对象，屏幕大小为 $height \times width$，食物位置序列为 $food$。
- `int move(String direction)` 返回蛇在方向 $direction$ 上移动后的得分。如果游戏结束，返回 $-1$。

**说明**：

- $1 \le width, height \le 10^{4}$。
- $1 \le food.length \le 50$。
- $food[i].length == 2$。
- $0 \le ri \lt height$。
- $0 \le ci \lt width$。
- $direction.length == 1$。
- $direction$ 为 `'U'`, `'D'`, `'L'`, or `'R'`。
- 最多调用 $10^{4}$ 次 `move` 方法。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/01/13/snake.jpg)

```python
输入：
["SnakeGame", "move", "move", "move", "move", "move", "move"]
[[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
输出：
[null, 0, 0, 1, 1, 2, -1]

解释：
SnakeGame snakeGame = new SnakeGame(3, 2, [[1, 2], [0, 1]]);
snakeGame.move("R"); // 返回 0
snakeGame.move("D"); // 返回 0
snakeGame.move("R"); // 返回 1 ，蛇吃掉了第一个食物，同时第二个食物出现在 (0, 1)
snakeGame.move("U"); // 返回 1
snakeGame.move("L"); // 返回 2 ，蛇吃掉了第二个食物，没有出现更多食物
snakeGame.move("U"); // 返回 -1 ，蛇与边界相撞，游戏结束
```

## 解题思路

### 思路 1：队列 + 哈希表

使用双端队列 `deque` 来存储蛇的身体位置，使用集合 `set` 来快速检查碰撞。蛇的头部在队列的末尾，尾部在队列的开头。

具体步骤：

1. **初始化**：
   - 使用双端队列 $snake$ 存储蛇的身体位置，初始位置为 $(0, 0)$。
   - 使用集合 $occupied$ 存储蛇身体占据的位置，用于快速碰撞检测。
   - 记录屏幕尺寸 $width$ 和 $height$。
   - 记录食物列表 $food$ 和当前食物索引 $food\_index$。
   - 记录当前得分 $score$。

2. **move 操作**：
   - 根据方向 $direction$ 计算新的头部位置 $new\_head$。
   - 检查新位置是否越界：$new\_head[0] < 0$ 或 $new\_head[0] \geq height$ 或 $new\_head[1] < 0$ 或 $new\_head[1] \geq width$。
   - 检查新位置是否与蛇身碰撞：$new\_head$ 在 $occupied$ 集合中。
   - 如果碰撞，返回 $-1$。
   - 将新头部加入队列和集合。
   - 检查是否吃到食物：$new\_head$ 等于当前食物位置。
   - 如果吃到食物，得分 $+1$，食物索引 $+1$。
   - 如果没吃到食物，移除尾部位置。
   - 返回当前得分。

### 思路 1：代码

```python
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        # 初始化屏幕尺寸
        self.width = width
        self.height = height
        
        # 初始化食物列表和索引
        self.food = food
        self.food_index = 0
        
        # 初始化蛇的身体（使用双端队列，头部在末尾）
        self.snake = deque([(0, 0)])
        
        # 使用集合存储蛇身体占据的位置，用于快速碰撞检测
        self.occupied = {(0, 0)}
        
        # 初始化得分
        self.score = 0

    def move(self, direction: str) -> int:
        # 获取当前头部位置
        head_row, head_col = self.snake[-1]
        
        # 根据方向计算新的头部位置
        if direction == 'U':
            new_head = (head_row - 1, head_col)
        elif direction == 'D':
            new_head = (head_row + 1, head_col)
        elif direction == 'L':
            new_head = (head_row, head_col - 1)
        else:  # direction == 'R'
            new_head = (head_row, head_col + 1)
        
        # 检查是否越界
        if (new_head[0] < 0 or new_head[0] >= self.height or 
            new_head[1] < 0 or new_head[1] >= self.width):
            return -1
        
        # 检查是否吃到食物
        eating_food = (self.food_index < len(self.food) and 
                      new_head == tuple(self.food[self.food_index]))
        
        if not eating_food:
            # 没吃到食物，先移除尾部
            tail = self.snake.popleft()
            self.occupied.remove(tail)
        
        # 检查是否与蛇身碰撞（在移除尾部后检查）
        if new_head in self.occupied:
            return -1
        
        # 将新头部加入蛇身
        self.snake.append(new_head)
        self.occupied.add(new_head)
        
        if eating_food:
            # 吃到食物，得分 +1，食物索引 +1
            self.score += 1
            self.food_index += 1
        
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `move` 操作：$O(1)$，所有操作都是常数时间。
- **空间复杂度**：$O(n)$，其中 $n$ 是蛇的最大长度。
