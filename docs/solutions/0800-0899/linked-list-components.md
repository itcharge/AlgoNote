# [0817. 链表组件](https://leetcode.cn/problems/linked-list-components/)

- 标签：数组、哈希表、链表
- 难度：中等

## 题目链接

- [0817. 链表组件 - 力扣](https://leetcode.cn/problems/linked-list-components/)

## 题目大意

**描述**：

给定链表头结点 $head$，该链表上的每个结点都有一个「唯一的整型值」。同时给定列表 $nums$，该列表是上述链表中整型值的一个子集。

**要求**：

返回列表 $nums$ 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 $nums$ 中）构成的集合。

**说明**：

- 链表中节点数为n。
- $1 \le n \le 10^{4}$。
- $0 \le Node.val \lt n$。
- Node.val 中所有值 不同。
- $1 \le nums.length \le n$。
- $0 \le nums[i] \lt n$。
- $nums$ 中所有值「不同」。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom1.jpg)

```python
输入: head = [0,1,2,3], nums = [0,1,3]
输出: 2
解释: 链表中,0 和 1 是相连接的，且 nums 中不包含 2，所以 [0, 1] 是 nums 的一个组件，同理 [3] 也是一个组件，故返回 2。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom2.jpg)

```python
输入: head = [0,1,2,3,4], nums = [0,3,1,4]
输出: 2
解释: 链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。
```

## 解题思路

### 思路 1：哈希表 + 链表遍历

这道题要求统计链表中组件的数量。组件是链表中连续的、值都在 $nums$ 中的节点序列。

算法步骤：

1. 将 $nums$ 转换为哈希集合，方便快速查找。
2. 遍历链表，统计组件数量：
   - 如果当前节点的值在 $nums$ 中，且前一个节点的值不在 $nums$ 中（或当前是第一个节点），则组件数加 $1$。
   - 换句话说，每次遇到一个新组件的开始时，计数器加 $1$。

### 思路 1：代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # 将 nums 转换为哈希集合
        num_set = set(nums)
        
        count = 0
        in_component = False  # 标记当前是否在组件中
        
        # 遍历链表
        curr = head
        while curr:
            if curr.val in num_set:
                # 如果当前节点在 nums 中
                if not in_component:
                    # 如果之前不在组件中，说明这是一个新组件的开始
                    count += 1
                    in_component = True
            else:
                # 如果当前节点不在 nums 中，标记不在组件中
                in_component = False
            
            curr = curr.next
        
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 是链表的长度，$m$ 是数组 $nums$ 的长度。需要遍历链表和构建哈希集合。
- **空间复杂度**：$O(m)$，需要使用哈希集合存储 $nums$ 中的元素。
