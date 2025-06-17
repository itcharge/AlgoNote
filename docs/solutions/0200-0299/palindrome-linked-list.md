# [0234. 回文链表](https://leetcode.cn/problems/palindrome-linked-list/)

- 标签：栈、递归、链表、双指针
- 难度：简单

## 题目链接

- [0234. 回文链表 - 力扣](https://leetcode.cn/problems/palindrome-linked-list/)

## 题目大意

**描述**：给定一个链表的头节点 `head`。

**要求**：判断该链表是否为回文链表。

**说明**：

- 链表中节点数目在范围 $[1, 10^5]$ 内。
- $0 \le Node.val \le 9$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

```python
输入：head = [1,2,2,1]
输出：True
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)

```python
输入：head = [1,2]
输出：False
```

## 解题思路

### 思路 1：利用数组 + 双指针

1. 利用数组，将链表元素依次存入。
2. 然后再使用两个指针，一个指向数组开始位置，一个指向数组结束位置。
3. 依次判断首尾对应元素是否相等，如果都相等，则为回文链表。如果不相等，则不是回文链表。

### 思路 1：代码

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        p1 = head
        while p1 != None:
            nodes.append(p1.val)
            p1 = p1.next
        return nodes == nodes[::-1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

