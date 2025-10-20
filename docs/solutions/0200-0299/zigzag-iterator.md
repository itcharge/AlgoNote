# [0281. 锯齿迭代器](https://leetcode.cn/problems/zigzag-iterator/)

- 标签：设计、队列、数组、迭代器
- 难度：中等

## 题目链接

- [0281. 锯齿迭代器 - 力扣](https://leetcode.cn/problems/zigzag-iterator/)

## 题目大意

**描述**：

给定两个整数向量 $v1$ 和 $v2$。

**要求**：

请你实现一个迭代器，交替返回它们的元素。

实现 `ZigzagIterator` 类：

- `ZigzagIterator(List<int> v1, List<int> v2)` 用两个向量 $v1$ 和 $v2$ 初始化对象。
- `boolean hasNext()` 如果迭代器还有元素返回 $true$，否则返回 $false$。
- `int next()` 返回迭代器的当前元素并将迭代器移动到下一个元素。

**说明**：

- 拓展：假如给你 $k$ 个向量呢？你的代码在这种情况下的扩展性又会如何呢?
- 拓展声明：「锯齿」顺序对于 $k > 2$ 的情况定义可能会有些歧义。所以，假如你觉得「锯齿」这个表述不妥，也可以认为这是一种「循环」。例如：

```python
输入：v1 = [1,2,3], v2 = [4,5,6,7], v3 = [8,9]
输出：[1,4,8,2,5,9,3,6,7]
```

**示例**：

- 示例 1：

```python
输入：v1 = [1,2], v2 = [3,4,5,6]
输出：[1,3,2,4,5,6]
解释：通过重复调用 next 直到 hasNext 返回 false，那么 next 返回的元素的顺序应该是：[1,3,2,4,5,6]。
```

- 示例 2：

```python
输入：v1 = [1], v2 = []
输出：[1]
```

## 解题思路

### 思路 1：队列模拟

使用队列来模拟锯齿迭代的过程。我们可以将两个向量 $v1$ 和 $v2$ 的元素按照锯齿顺序放入队列中，然后依次从队列中取出元素。

具体步骤如下：

1. 初始化时，将两个向量 $v1$ 和 $v2$ 的元素按照锯齿顺序（交替）放入队列 $queue$ 中。
2. 使用指针 $i$ 和 $j$ 分别指向 $v1$ 和 $v2$ 的当前位置。
3. 交替从 $v1$ 和 $v2$ 中取元素，直到其中一个向量遍历完毕。
4. 将剩余向量的所有元素按顺序加入队列。
5. `next()` 方法从队列头部取出元素。
6. `hasNext()` 方法检查队列是否为空。

### 思路 1：代码

```python
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        # 使用队列存储按锯齿顺序排列的元素
        self.queue = []
        # 初始化两个指针
        i, j = 0, 0
        # 交替从 v1 和 v2 中取元素
        while i < len(v1) and j < len(v2):
            self.queue.append(v1[i])
            self.queue.append(v2[j])
            i += 1
            j += 1
        # 将剩余元素加入队列
        while i < len(v1):
            self.queue.append(v1[i])
            i += 1
        while j < len(v2):
            self.queue.append(v2[j])
            j += 1
        # 队列索引
        self.index = 0

    def next(self) -> int:
        # 从队列中取出下一个元素
        result = self.queue[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        # 检查是否还有元素
        return self.index < len(self.queue)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m + n)$，其中 $m$ 和 $n$ 分别是 $v1$ 和 $v2$ 的长度。初始化时需要遍历两个向量的所有元素。
- **空间复杂度**：$O(m + n)$，需要额外的队列空间存储所有元素。
