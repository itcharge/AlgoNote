# [0725. 分隔链表](https://leetcode.cn/problems/split-linked-list-in-parts/)

- 标签：链表
- 难度：中等

## 题目链接

- [0725. 分隔链表 - 力扣](https://leetcode.cn/problems/split-linked-list-in-parts/)

## 题目大意

**描述**：

给定一个头结点为 $head$ 的单链表和一个整数 $k$。

**要求**：

请你设计一个算法将链表分隔为 $k$ 个连续的部分。

每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 $1$。这可能会导致有些部分为 null。

这 $k$ 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。

返回一个由上述 $k$ 部分组成的数组。

**说明**：

- 链表中节点的数目在范围 $[0, 10^{3}]$。
- $0 \le Node.val \le 10^{3}$。
- $1 \le k \le 50$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/06/13/split1-lc.jpg)

```python
输入：head = [1,2,3], k = 5
输出：[[1],[2],[3],[],[]]
解释：
第一个元素 output[0] 为 output[0].val = 1 ，output[0].next = null 。
最后一个元素 output[4] 为 null ，但它作为 ListNode 的字符串表示是 [] 。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/06/13/split2-lc.jpg)

```python
输入：head = [1,2,3,4,5,6,7,8,9,10], k = 3
输出：[[1,2,3,4],[5,6,7],[8,9,10]]
解释：
输入被分成了几个连续的部分，并且每部分的长度相差不超过 1 。前面部分的长度大于等于后面部分的长度。
```

## 解题思路

### 思路 1：链表遍历

将链表分隔为 $k$ 个连续的部分，每部分的长度应该尽可能相等。

**实现步骤**：

1. 先遍历链表，计算链表的总长度 $n$。
2. 计算每部分的基本长度：$size = n // k$。
3. 计算有多少部分需要多一个节点：$extra = n \% k$。
4. 前 $extra$ 个部分的长度为 $size + 1$，其余部分的长度为 $size$。
5. 遍历链表，按照计算的长度分隔链表：
   - 对于每一部分，遍历相应数量的节点。
   - 断开当前部分与下一部分的连接。
   - 将当前部分的头节点加入结果数组。

### 思路 1：代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 计算链表长度
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # 计算每部分的长度
        size = length // k  # 每部分的基本长度
        extra = length % k  # 前 extra 个部分需要多一个节点
        
        result = []
        curr = head
        
        # 分隔链表
        for i in range(k):
            # 当前部分的头节点
            part_head = curr
            
            # 当前部分的长度
            part_size = size + (1 if i < extra else 0)
            
            # 遍历当前部分
            for j in range(part_size - 1):
                if curr:
                    curr = curr.next
            
            # 断开连接
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            
            result.append(part_head)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + k)$，其中 $n$ 是链表的长度。需要遍历链表两次。
- **空间复杂度**：$O(1)$，不考虑结果数组的空间。
