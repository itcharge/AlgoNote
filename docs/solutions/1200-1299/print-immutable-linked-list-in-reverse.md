# [1265. 逆序打印不可变链表](https://leetcode.cn/problems/print-immutable-linked-list-in-reverse/)

- 标签：栈、递归、链表、双指针
- 难度：中等

## 题目链接

- [1265. 逆序打印不可变链表 - 力扣](https://leetcode.cn/problems/print-immutable-linked-list-in-reverse/)

## 题目大意

**描述**：给定一个不可变链表 $ImmutableListNode$，提供 $printValue()$ 方法打印当前节点的值和 $getNext()$ 方法获取下一个节点。不允许修改链表结构，也不允许修改节点的值。

**要求**：逆序打印链表中的所有节点值。

**说明**：

- 链表长度未知。
- 不能修改链表结构，也不能修改节点的值。
- 只能使用 $printValue()$ 和 $getNext()$ 方法。

**示例**：

- 示例 1：

```python
输入：head = [1, 2, 3, 4]
输出：[]  # 实际上是依次打印 4, 3, 2, 1
解释：依次调用 printValue() 输出 4, 3, 2, 1。
```

## 解题思路

### 思路 1：递归

#### 1. 核心思想

链表的逆序输出，最自然的做法就是递归。递归到链表末尾，然后在回溯的过程中打印节点值。利用函数调用栈天然地实现了"后进先出"。

#### 2. 具体步骤

**第 1 步**：定义递归函数 $printLinkedListInReverse(head)$：
- 如果 $head$ 为空，直接返回。
- 递归调用 $printLinkedListInReverse(head.getNext())$。
- 调用 $head.printValue()$。

**第 3 步**：递归终止条件：当前节点为空。

#### 3. 结合示例走一遍

链表 $1 \to 2 \to 3 \to 4$

```
printLinkedListInReverse(1):
  → printLinkedListInReverse(2):
      → printLinkedListInReverse(3):
          → printLinkedListInReverse(4):
              → printLinkedListInReverse(None): 返回
              → printValue(4): 输出 4
          → printValue(3): 输出 3
      → printValue(2): 输出 2
  → printValue(1): 输出 1
```

输出顺序：$4, 3, 2, 1$。

### 思路 1：代码

```python
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head is None:
            return
        # 先递归到末尾
        self.printLinkedListInReverse(head.getNext())
        # 回溯时打印
        head.printValue()
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是链表长度。每个节点被访问一次。
- **空间复杂度**：$O(n)$，递归栈需要 $O(n)$ 空间。如果链表很长，可能导致栈溢出。

### 思路 2：显式栈

#### 1. 核心思想

用栈模拟递归过程：遍历链表将节点依次入栈，然后从栈顶开始弹出并打印。

#### 2. 代码

```python
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        stack = []
        # 遍历入栈
        while head:
            stack.append(head)
            head = head.getNext()
        # 出栈打印
        while stack:
            stack.pop().printValue()
```

#### 3. 复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$，栈空间。

### 思路 3：分块（进阶，$O(\sqrt{n})$ 空间）

#### 1. 核心思想

递归和栈都需要 $O(n)$ 额外空间。如果要求只使用 $O(\sqrt{n})$ 空间，可以分块处理。

将链表分成 $\sqrt{n}$ 大小的块。先遍历链表确定块边界（存下每块的最后一个节点），然后逆序遍历这些块，对每个块内的节点再次逆序打印。

但题目没有空间限制，思路 1 或思路 2 足矣。
