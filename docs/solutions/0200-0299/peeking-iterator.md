# [0284. 窥视迭代器](https://leetcode.cn/problems/peeking-iterator/)

- 标签：设计、数组、迭代器
- 难度：中等

## 题目链接

- [0284. 窥视迭代器 - 力扣](https://leetcode.cn/problems/peeking-iterator/)

## 题目大意

**要求**：

设计一个迭代器，在集成现有迭代器拥有的 `hasNext` 和 `next` 操作的基础上，还额外支持 `peek` 操作。

实现 `PeekingIterator` 类：
* `PeekingIterator(Iterator<int> nums)` 使用指定整数迭代器 $nums$ 初始化迭代器。
* `int next()` 返回数组中的下一个元素，并将指针移动到下个元素处。
* `bool hasNext()` 如果数组中存在下一个元素，返回 $true$；否则，返回 $false$。
* `int peek()` 返回数组中的下一个元素，但不移动指针。

**说明**：

- 注意：每种语言可能有不同的构造函数和迭代器 `Iterator`，但均支持 `int next()` 和 `boolean hasNext()` 函数。
- $1 \le nums.length \le 10^{3}$。
- $1 \le nums[i] \le 10^{3}$。
- 对 `next` 和 `peek` 的调用均有效。
- `next`、`hasNext` 和 `peek` 最多调用 $10^{3}$ 次。

- 进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？

**示例**：

- 示例 1：

```python
输入：
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
输出：
[null, 1, 2, 2, 3, false]

解释：
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // 返回 1 ，指针移动到下一个元素 [1,2,3]
peekingIterator.peek();    // 返回 2 ，指针未发生移动 [1,2,3]
peekingIterator.next();    // 返回 2 ，指针移动到下一个元素 [1,2,3]
peekingIterator.next();    // 返回 3 ，指针移动到下一个元素 [1,2,3]
peekingIterator.hasNext(); // 返回 False
```

- 示例 2：

```python
输入：
输出：
```

## 解题思路

### 思路 1：缓存下一个元素

使用缓存机制来实现 `peek` 操作。我们维护一个变量 $next\_val$ 来缓存下一个元素，以及一个布尔变量 $has\_next$ 来标记是否还有下一个元素。

具体步骤如下：

1. 在初始化时，调用底层迭代器的 `next()` 方法获取第一个元素，存储在 $next\_val$ 中
2. 如果底层迭代器还有元素，设置 $has\_next = true$，否则设置 $has\_next = false$
3. `peek()` 方法直接返回 $next\_val$，不移动指针
4. `next()` 方法返回 $next\_val$，然后调用底层迭代器获取下一个元素更新 $next\_val$
5. `hasNext()` 方法返回 $has\_next$ 的值

这种方法的时间复杂度为 $O(1)$，空间复杂度为 $O(1)$。

### 思路 1：代码

```python
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        # 保存底层迭代器
        self.iterator = iterator
        # 缓存下一个元素
        self.next_val = None
        # 标记是否还有下一个元素
        self.has_next = False
        
        # 初始化时获取第一个元素
        if self.iterator.hasNext():
            self.next_val = self.iterator.next()
            self.has_next = True

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_val

    def next(self):
        """
        :rtype: int
        """
        # 保存当前要返回的值
        result = self.next_val
        
        # 获取下一个元素
        if self.iterator.hasNext():
            self.next_val = self.iterator.next()
            self.has_next = True
        else:
            self.has_next = False
            self.next_val = None
            
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$，所有操作（`peek`、`next`、`hasNext`）都是常数时间。
- **空间复杂度**：$O(1)$，只使用了常数额外空间来存储缓存的下一个元素和状态标志。
