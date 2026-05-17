# [1244. 力扣排行榜](https://leetcode.cn/problems/design-a-leaderboard/)

- 标签：设计、哈希表、排序
- 难度：中等

## 题目链接

- [1244. 力扣排行榜 - 力扣](https://leetcode.cn/problems/design-a-leaderboard/)

## 题目大意

**描述**：需要设计一个 $Leaderboard$ 类，具有如下 $3$ 个函数：
1. `addScore(playerId, score)`：如果参赛者已经在排行榜上，就给他的当前得分增加 $score$ 分；如果不在，就把他添加到榜单上，分数设为 $score$。
2. `top(K)`：返回前 $K$ 名参赛者的得分总和。
3. `reset(playerId)`：将指定参赛者从排行榜中删除（成绩清零）。

**要求**：实现上述类。

**说明**：

- $1 \le playerId, K \le 10^{4}$。
- 题目保证 $K$ 小于或等于当前参赛者的数量。
- $1 \le score \le 10^{3}$。
- 最多进行 $10^{3}$ 次函数调用。

**示例**：

- 示例 1：

```python
输入： 
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
输出：
[null,null,null,null,null,null,73,null,null,null,141]

解释： 
Leaderboard leaderboard = new Leaderboard();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
```

## 解题思路

### 思路 1：哈希表 + 排序

###### 1. 核心思想

最直观的方案：使用一个哈希表（字典）来存储每个参赛者 $playerId$ 对应的当前分数。`addScore` 和 `reset` 都是 $O(1)$ 的哈希表操作。`top(K)` 时取出所有分数进行排序，取前 $K$ 大的值求和。

由于题目限制最多 $10^3$ 次函数调用，即使 `top(K)` 每次都排序，也是完全可以接受的。每次排序最多 $O(N \log N)$，其中 $N \le 10^4$。

###### 2. 具体步骤

**第 1 步：初始化**

创建一个字典 $self.scores$，键为 $playerId$，值为当前分数。

**第 2 步：实现 addScore**

如果 $playerId$ 不存在，$get$ 方法返回 $0$，然后加上 $score$ 存入。

**第 3 步：实现 top(K)**

使用 $sorted()$ 对 $self.scores.values()$ 进行降序排序。取前 $K$ 个元素求和并返回。

**第 4 步：实现 reset**

使用 `del self.scores[playerId]` 从字典中删除该参赛者。

### 思路 1：代码

```python
class Leaderboard:

    def __init__(self):
        # 哈希表存储每个参赛者的当前分数
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        # 累加分数（不存在则从 0 开始）
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        # 取出所有分数，降序排列，取前 K 个求和
        all_scores = sorted(self.scores.values(), reverse=True)
        return sum(all_scores[:K])

    def reset(self, playerId: int) -> None:
        # 从排行榜中删除该参赛者
        del self.scores[playerId]
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `addScore`：$O(1)$，哈希表插入/更新操作的平均时间复杂度为 $O(1)$。
  - `top(K)`：$O(N \log N)$，其中 $N$ 是当前参赛者的人数。每次需要将所有分数取出并排序。
  - `reset`：$O(1)$，哈希表的删除操作。
- **空间复杂度**：$O(N)$，需要存储所有参赛者的 ID 和分数。
