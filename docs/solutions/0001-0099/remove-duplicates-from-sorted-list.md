# [0083. 删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/)

- 标签：链表
- 难度：简单

## 题目链接

- [0083. 删除排序链表中的重复元素 - 力扣](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/)

## 题目大意

**描述**：给定一个已排序的链表的头 $head$。

**要求**：删除所有重复的元素，使每个元素只出现一次。返回已排序的链表。

**说明**：

- 链表中节点数目在范围 $[0, 300]$ 内。
- $-100 \le Node.val \le 100$。
- 题目数据保证链表已经按升序排列。

**示例**：

- 示例 1：

```python
输入：head = [1,1,2,3,3]
输出：[1,2,3]
```

## 解题思路

### 思路 1：遍历

- 使用指针 $curr$ 遍历链表，先将 $head$ 保存到 $curr$ 指针。
- 判断当前元素的值和当前元素下一个节点元素值是否相等。
- 如果相等，则让当前指针指向当前指针下两个节点。
- 否则，让 $curr$ 继续向后遍历。
- 遍历完之后返回头节点 $head$。

### 思路 1：遍历代码

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 为链表长度。
- **空间复杂度**：$O(1)$。