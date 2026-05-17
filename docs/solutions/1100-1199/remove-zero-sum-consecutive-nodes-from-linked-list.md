# [1171. 从链表中删去总和值为零的连续节点](https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)

- 标签：哈希表、链表
- 难度：中等

## 题目链接

- [1171. 从链表中删去总和值为零的连续节点 - 力扣](https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)

## 题目大意

**描述**：给定一个链表的头节点 `head`，链表中每个节点都有一个整数值。

**要求**：反复删去链表中由总和值为 $0$ 的连续节点组成的序列，直到不存在这样的序列为止。返回最终结果链表的头节点。

**说明**：

- 链表中可能有 $1$ 到 $10^3$ 个节点。
- 节点的值：$-10^3 \le node.val \le 10^3$。

**示例**：

- 示例 1：

```python
输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。
```

- 示例 2：

```python
输入：head = [1,2,3,-3,4]
输出：[1,2,4]
```

- 示例 3：

```python
输入：head = [1,2,3,-3,-2]
输出：[1]
```

## 解题思路

### 思路 1：前缀和 + 哈希表

**核心观察**：前缀和相等 $\Rightarrow$ 中间这一段的和为 $0$。

**拆解步骤**：

1. **创建哑节点**：在头节点前面加一个哑节点（值为 $0$），方便处理从第一个节点就开始和为 $0$ 的情况。

2. **第一遍遍历——记录每个前缀和最后出现的位置**：
   - 用哈希表存储：前缀和 $\to$ 该前缀和对应的最后一个节点
   - 如果同一个前缀和出现多次，后面的节点会覆盖前面的

3. **第二遍遍历——跳过和为 $0$ 的区间**：
   - 重新计算前缀和
   - 对于当前节点，查表找到相同前缀和最后出现的节点
   - 把当前节点的 `next` 直接指向那个节点的 `next`，这样就跳过了中间和为 $0$ 的部分

4. **返回哑节点的 `next`**。

### 思路 1：代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建哑节点，方便处理头节点被删除的情况
        dummy = ListNode(0)
        dummy.next = head

        # 哈希表：前缀和 -> 该前缀和对应的最后一个节点
        prefix_sum_map = {}
        prefix_sum = 0
        curr = dummy

        # 第一遍遍历：记录每个前缀和最后出现的位置
        while curr:
            prefix_sum += curr.val
            prefix_sum_map[prefix_sum] = curr  # 后出现的覆盖先出现的
            curr = curr.next

        # 第二遍遍历：跳过和为 0 的区间
        prefix_sum = 0
        curr = dummy
        while curr:
            prefix_sum += curr.val
            # 当前节点直接连接到相同前缀和最后出现位置的 next
            # 这样就跳过了中间和为 0 的节点
            curr.next = prefix_sum_map[prefix_sum].next
            curr = curr.next

        return dummy.next
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。用人话说就是：需要遍历链表两次，每次都是线性时间，总时间和节点数成正比。
- **空间复杂度**：$O(n)$。哈希表最多存储 $n$ 个不同的前缀和。
