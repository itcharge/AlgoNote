# [0251. 展开二维向量](https://leetcode.cn/problems/flatten-2d-vector/)

- 标签：设计、数组、双指针、迭代器
- 难度：中等

## 题目链接

- [0251. 展开二维向量 - 力扣](https://leetcode.cn/problems/flatten-2d-vector/)

## 题目大意

**要求**：

设计并实现一个能够展开二维向量的迭代器。该迭代器需要支持 `next` 和 `hasNext` 两种操作。
实现 $Vector2D$ 类：

- `Vector2D(int[][] vec)` 使用二维向量 $vec$ 初始化对象。
- `next()` 从二维向量返回下一个元素并将指针移动到下一个位置。你可以假设对 `next` 的所有调用都是合法的。
* `hasNext()` 当向量中还有元素返回 $true$，否则返回 $false$。

**说明**：

- $0 \le vec.length \le 200$。
- $0 \le vec[i].length \le 500$。
- $-500 \le vec[i][j] \le 500$。
- 最多调用 `next` 和 `hasNext` $10^{5}$ 次。

- 进阶：尝试在代码中仅使用 C++ 提供的迭代器 或 Java 提供的迭代器。

**示例**：

- 示例 1：

```python
输入：
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
输出：
[null, 1, 2, 3, true, true, 4, false]

解释：
Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
vector2D.next();    // return 1
vector2D.next();    // return 2
vector2D.next();    // return 3
vector2D.hasNext(); // return True
vector2D.hasNext(); // return True
vector2D.next();    // return 4
vector2D.hasNext(); // return False
```

## 解题思路

### 思路 1：双指针

使用两个指针 $i$ 和 $j$ 来跟踪当前在二维向量中的位置。其中 $i$ 表示当前在第几个一维数组，$j$ 表示在当前一维数组中的位置。

核心思想是维护指针始终指向下一个有效元素，通过预定位机制确保访问安全：

- **初始化**：$i = 0$，$j = 0$，然后调用 `_findNext()` 将指针定位到第一个有效元素。
- **`_findNext()` 方法**：跳过所有空的一维数组，将指针移动到下一个有效位置。当 $j$ 超出当前一维数组长度时，移动到下一个一维数组并重置 $j = 0$。
- **`next()` 方法**：返回当前有效元素 $vec[i][j]$，然后 $j$ 自增，再调用 `_findNext()` 预定位到下一个有效元素。
- **`hasNext()` 方法**：简单检查 $i$ 是否小于向量长度，因为指针已经预定位到有效位置。

### 思路 1：代码

```python
class Vector2D:
    def __init__(self, vec: List[List[int]]):
        # 初始化二维向量和指针
        self.vec = vec
        self.i = 0  # 当前一维数组的索引
        self.j = 0  # 当前一维数组中的索引
        # 初始化时找到第一个有效位置
        self._findNext()

    def _findNext(self):
        # 跳过空的一维数组，找到下一个有效元素
        while self.i < len(self.vec):
            if self.j < len(self.vec[self.i]):
                # 当前一维数组还有元素
                return
            else:
                # 当前一维数组已遍历完，移动到下一个一维数组
                self.i += 1
                self.j = 0

    def next(self) -> int:
        # 获取当前元素
        result = self.vec[self.i][self.j]
        # 移动指针到下一个位置
        self.j += 1
        # 找到下一个有效位置
        self._findNext()
        return result

    def hasNext(self) -> bool:
        # 检查是否还有下一个元素
        return self.i < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$ 对于 `next()` 和 `hasNext()` 操作。虽然 `hasNext()` 可能需要跳过空数组，但每个元素最多被访问一次，总体时间复杂度为 $O(n)$，其中 $n$ 是总元素个数。
- **空间复杂度**：$O(1)$。只使用了常数个额外变量来存储指针位置。
