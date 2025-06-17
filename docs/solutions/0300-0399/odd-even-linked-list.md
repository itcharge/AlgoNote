# [0328. 奇偶链表](https://leetcode.cn/problems/odd-even-linked-list/)

- 标签：链表
- 难度：中等

## 题目链接

- [0328. 奇偶链表 - 力扣](https://leetcode.cn/problems/odd-even-linked-list/)

## 题目大意

**描述**：给定一个单链表的头节点 `head`。

**要求**：将链表中的奇数位置上的节点排在前面，偶数位置上的节点排在后面，返回新的链表节点。

**说明**：

- 要求空间复杂度为 $O(1)$。
- $n$ 等于链表中的节点数。
- $0 \le n \le 10^4$。
- $-10^6 \le Node.val \le 10^6$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg)

```python
输入: head = [1,2,3,4,5]
输出: [1,3,5,2,4]
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg)

```python
输入: head = [2,1,3,5,6,4,7]
输出: [2,3,6,7,1,5,4]
```

## 解题思路

### 思路 1：拆分后合并

1. 使用两个指针 `odd`、`even` 分别表示奇数节点链表和偶数节点链表。
2. 先将奇数位置上的节点和偶数位置上的节点分成两个链表，再将偶数节点的链表接到奇数链表末尾。
3. 过程中需要使用几个必要指针用于保留必要位置（比如原链表初始位置、偶数链表初始位置、当前遍历节点位置）。

### 思路 1：代码

```python
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head

        evenHead = head.next
        odd, even = head, evenHead
        isOdd = True

        curr = head.next.next

        while curr:
            if isOdd:
                odd.next = curr
                odd = curr
            else:
                even.next = curr
                even = curr
            isOdd = not isOdd
            curr = curr.next
        odd.next = evenHead
        even.next = None
        return head
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

