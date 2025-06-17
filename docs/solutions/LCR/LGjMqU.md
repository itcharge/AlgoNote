# [LCR 026. 重排链表](https://leetcode.cn/problems/LGjMqU/)

- 标签：栈、递归、链表、双指针
- 难度：中等

## 题目链接

- [LCR 026. 重排链表 - 力扣](https://leetcode.cn/problems/LGjMqU/)

## 题目大意

给定一个单链表 `L` 的头节点 `head`，单链表 `L` 表示为：$L_0$ -> $L_1$ -> $L_2$ -> ... -> $L_{n-1}$ -> $L_n$。

要求：将单链表 `L` 重新排列为：$L_0$ -> $L_n$ -> $L_1$ -> $L_{n-1}$ -> $L_2$ -> $L_{n-2}$ -> $L_3$ -> $L_{n-3}$ -> ...。

注意：需要将实际节点进行交换。

## 解题思路

链表不能像数组那样直接进行随机访问。所以我们可以先将链表转为线性表。然后直接按照提要要求的排列顺序访问对应数据元素，重新建立链表。

## 代码

```python
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        vec = []
        node = head
        while node:
            vec.append(node)
            node = node.next

        left, right = 0, len(vec) - 1
        while left < right:
            vec[left].next = vec[right]
            left += 1
            if left == right:
                break
            vec[right].next = vec[left]
            right -= 1
        vec[left].next = None
```

