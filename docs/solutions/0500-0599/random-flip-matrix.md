# [0519. 随机翻转矩阵](https://leetcode.cn/problems/random-flip-matrix/)

- 标签：水塘抽样、哈希表、数学、随机化
- 难度：中等

## 题目链接

- [0519. 随机翻转矩阵 - 力扣](https://leetcode.cn/problems/random-flip-matrix/)

## 题目大意

**描述**：

给定一个 $m \times n$ 的二元矩阵 $matrix$，且所有值被初始化为 $0$。

**要求**：

设计一个算法，随机选取一个满足 $matrix[i][j] == 0$ 的下标 $(i, j)$，并将它的值变为 $1$。所有满足 $matrix[i][j] == 0$ 的下标 $(i, j)$ 被选取的概率应当均等。
尽量最少调用内置的随机函数，并且优化时间和空间复杂度。

实现 Solution 类：

- `Solution(int m, int n)` 使用二元矩阵的大小 $m$ 和 $n$ 初始化该对象。
- `int[] flip()` 返回一个满足 $matrix[i][j] == 0$ 的随机下标 $[i, j]$，并将其对应格子中的值变为 $1$。
- `void reset()` 将矩阵中所有的值重置为 $0$。

**说明**：

- $1 \le m, n \le 10^{4}$。
- 每次调用 `flip` 时，矩阵中至少存在一个值为 $0$ 的格子。
- 最多调用 $10^{3}$ 次 `flip` 和 `reset` 方法。

**示例**：

- 示例 1：

```python
输入
["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]
输出
[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

解释
Solution solution = new Solution(3, 1);
solution.flip();  // 返回 [1, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
solution.flip();  // 返回 [2, 0]，因为 [1,0] 已经返回过了，此时返回 [2,0] 和 [0,0] 的概率应当相同
solution.flip();  // 返回 [0, 0]，根据前面已经返回过的下标，此时只能返回 [0,0]
solution.reset(); // 所有值都重置为 0 ，并可以再次选择下标返回
solution.flip();  // 返回 [2, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
```

## 解题思路

### 思路 1：哈希表 + 映射交换

这道题要求随机翻转矩阵中的 $0$，且每个 $0$ 被选中的概率相等。关键是避免存储整个矩阵。

核心思路：

1. 将二维矩阵映射为一维数组，位置 $(i, j)$ 对应索引 $i \times n + j$。
2. 维护变量 $total$，表示剩余可翻转的位置数量，初始为 $m \times n$。
3. 使用哈希表 $pos\_map$ 存储被翻转位置的映射关系（类似数组交换）。
4. `flip` 操作：
   - 随机生成 $[0, total-1]$ 范围内的索引 $idx$。
   - 如果 $idx$ 在哈希表中，取映射值；否则取 $idx$ 本身。
   - 将 $idx$ 位置与 $total-1$ 位置交换（通过哈希表记录）。
   - $total$ 减 $1$。
   - 将一维索引转换为二维坐标返回。
5. `reset` 操作：清空哈希表，重置 $total$。

### 思路 1：代码

```python
import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n  # 剩余可翻转位置数量
        self.pos_map = {}   # 位置映射

    def flip(self) -> List[int]:
        # 随机选择一个位置
        idx = random.randint(0, self.total - 1)
        
        # 获取实际位置（如果被映射过则取映射值）
        actual_idx = self.pos_map.get(idx, idx)
        
        # 将当前位置与最后一个位置交换
        # 记录映射关系：idx 位置现在对应 total-1 位置的值
        self.pos_map[idx] = self.pos_map.get(self.total - 1, self.total - 1)
        
        # 减少可用位置数量
        self.total -= 1
        
        # 将一维索引转换为二维坐标
        return [actual_idx // self.n, actual_idx % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.pos_map.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `flip`：$O(1)$，哈希表操作和随机数生成都是常数时间。
  - `reset`：$O(1)$，清空哈希表。
- **空间复杂度**：$O(k)$，其中 $k$ 为调用 `flip` 的次数，哈希表最多存储 $k$ 个映射关系。
