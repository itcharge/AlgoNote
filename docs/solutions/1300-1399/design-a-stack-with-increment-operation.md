# [1381. 设计一个支持增量操作的栈](https://leetcode.cn/problems/design-a-stack-with-increment-operation/)

- 标签：栈、设计、数组
- 难度：中等

## 题目链接

- [1381. 设计一个支持增量操作的栈 - 力扣](https://leetcode.cn/problems/design-a-stack-with-increment-operation/)

## 题目大意

**要求**：设计一个支持对其元素进行增量操作的栈。

实现自定义栈类 $CustomStack$：

- `CustomStack(int maxSize)`：用 $maxSize$ 初始化对象，$maxSize$ 是栈中最多能容纳的元素数量。
- `void push(int x)`：如果栈还未增长到 $maxSize$，就将 $x$ 添加到栈顶。
- `int pop()`：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 $-1$。
- `void inc(int k, int val)`：栈底的 $k$ 个元素的值都增加 $val$。如果栈中元素总数小于 $k$，则栈中的所有元素都增加 $val$。

**说明**：

- $1 \le maxSize, x, k \le 1000$。
- $0 \le val \le 100$。
- 每种方法 `increment`，`push` 以及 `pop` 分别最多调用 $1000$ 次。

**示例**：

- 示例 1：

```python
输入：
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
输出：
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
解释：
CustomStack stk = new CustomStack(3); // 栈是空的 []
stk.push(1);                          // 栈变为 [1]
stk.push(2);                          // 栈变为 [1, 2]
stk.pop();                            // 返回 2 --> 返回栈顶值 2，栈变为 [1]
stk.push(2);                          // 栈变为 [1, 2]
stk.push(3);                          // 栈变为 [1, 2, 3]
stk.push(4);                          // 栈仍然是 [1, 2, 3]，不能添加其他元素使栈大小变为 4
stk.increment(5, 100);                // 栈变为 [101, 102, 103]
stk.increment(2, 100);                // 栈变为 [201, 202, 103]
stk.pop();                            // 返回 103 --> 返回栈顶值 103，栈变为 [201, 202]
stk.pop();                            // 返回 202 --> 返回栈顶值 202，栈变为 [201]
stk.pop();                            // 返回 201 --> 返回栈顶值 201，栈变为 []
stk.pop();                            // 返回 -1 --> 栈为空，返回 -1
```

## 解题思路

### 思路 1：模拟

1. 初始化：
   1. 使用空数组 $stack$ 用于表示栈。
   2. 使用 $size$ 用于表示当前栈中元素个数，
   3. 使用 $maxSize$ 用于表示栈中允许的最大元素个数。
   4. 使用另一个空数组 $increments$ 用于增量操作。
2. `push(x)` 操作：
   1. 判断当前元素个数与栈中允许的最大元素个数关系。
   2. 如果当前元素个数小于栈中允许的最大元素个数，则：
      1. 将 $x$ 添加到数组 $stack$ 中，即：`self.stack.append(x)`。
      2. 当前元素个数加 $1$，即：`self.size += 1`。
      3. 将 $0$ 添加到增量数组 $increments$  中，即：`self.increments.append(0)`。
3. `increment(k, val)` 操作：
   1. 如果增量数组不为空，则取 $k$ 与元素个数 `self.size` 的较小值，令增量数组对应位置加上 `val`（等 `pop()` 操作时，再计算出准确值）。
4. `pop()` 操作：
   1. 如果当前元素个数为 $0$，则直接返回 $-1$。
   2. 如果当前元素个数大于等于 $2$，则更新弹出元素后的增量数组（保证剩余元素弹出时能够正确计算出），即：`self.increments[-2] += self.increments[-1]`
   3. 令元素个数减 $1$，即：`self.size -= 1`。
   4. 弹出数组 $stack$ 中的栈顶元素和增量数组 $increments$ 中的栈顶元素，令其相加，即为弹出元素值，将其返回。

### 思路 1：代码

```python
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.increments = []
        self.size = 0


    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.stack.append(x)
            self.increments.append(0)
            self.size += 1


    def pop(self) -> int:
        if self.size == 0:
            return -1
        if self.size >= 2:
            self.increments[-2] += self.increments[-1]
        self.size -= 1
        
        val = self.stack.pop() + self.increments.pop()
        return val


    def increment(self, k: int, val: int) -> None:
        if self.increments:
            self.increments[min(k, self.size) - 1] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
```

### 思路 1：复杂度分析

- **时间复杂度**：初始化、`push` 操作、`pop` 操作、`increment` 操作的时间复杂度为 $O(1)$。
- **空间复杂度**：$O(maxSize)$。
