# [0876. 链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)

- 标签：链表、双指针
- 难度：简单

## 题目链接

- [0876. 链表的中间结点 - 力扣](https://leetcode.cn/problems/middle-of-the-linked-list/)

## 题目大意

**描述**：给定一个单链表的头节点 `head`。

**要求**：返回链表的中间节点。如果有两个中间节点，则返回第二个中间节点。

**说明**：

- 给定链表的结点数介于 `1` 和 `100` 之间。

**示例**：

- 示例 1：

```python
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
解释：返回的结点值为 3 。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
```

- 示例 2：

```python
输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
解释：由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
```

## 解题思路

### 思路 1：单指针

先遍历一遍链表，统计一下节点个数为 `n`，再遍历到 `n / 2` 的位置，返回中间节点。

### 思路 1：代码

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        k = 0
        curr = head
        while k < n // 2:
            k += 1
            curr = curr.next
        return curr
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

### 思路 2：快慢指针

使用步长不一致的快慢指针进行一次遍历找到链表的中间节点。具体做法如下：

1. 使用两个指针 `slow`、`fast`。`slow`、`fast` 都指向链表的头节点。
2. 在循环体中将快、慢指针同时向右移动。其中慢指针每次移动 `1` 步，即 `slow = slow.next`。快指针每次移动 `2` 步，即 `fast = fast.next.next`。
3. 等到快指针移动到链表尾部（即 `fast == Node`）时跳出循环体，此时 `slow` 指向链表中间位置。
4. 返回 `slow` 指针。

### 思路 2：代码

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。