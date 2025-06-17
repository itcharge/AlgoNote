# [LCR 171. 训练计划 V](https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)

- 标签：哈希表、链表、双指针
- 难度：简单

## 题目链接

- [LCR 171. 训练计划 V - 力扣](https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)

## 题目大意

给定 A、B 两个链表，判断两个链表是否相交，返回相交的起始点。如果不相交，则返回 None。

比如：链表 A 为 [4, 1, 8, 4, 5]，链表 B 为 [5, 0, 1, 8, 4, 5]。则如下图所示，两个链表相交的起始节点为 8，则输出结果为 8。

![](https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png)

## 解题思路

如果两个链表相交，那么从相交位置开始，到结束，必有一段等长且相同的节点。假设链表 A 的长度为 m、链表 B 的长度为 n，他们的相交序列有 k 个，则相交情况可以如下如所示：

![](https://qcdn.itcharge.cn/images/20210401113538.png)

现在问题是如何找到 m-k 或者 n-k 的位置。

考虑将链表 A 的末尾拼接上链表 B，链表 B 的末尾拼接上链表 A。

然后使用两个指针 pA 、PB，分别从链表 A、链表 B 的头节点开始遍历，如果走到共同的节点，则返回该节点。

否则走到两个链表末尾，返回 None。

![](https://qcdn.itcharge.cn/images/20210401114100.png)

## 代码

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
```

