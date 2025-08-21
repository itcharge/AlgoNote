## 1. 双指针简介

双指针是链表问题中非常常用且高效的技巧，通过两个指针的配合移动，能够巧妙地解决许多复杂问题。

> **双指针（Two Pointers）**：指在遍历链表时同时使用两个指针，根据移动方式主要分为以下两类：
> - **快慢指针**：两个指针从同一起点出发，移动速度不同，常用于检测环、寻找中点、定位倒数第 n 个节点等。
>    - **起点不一致**：快指针先行若干步，之后快慢指针同步移动，常用于定位倒数第 n 个节点。
>    - **步长不一致**：快指针每次移动两步，慢指针每次移动一步，常用于判断链表是否有环、寻找中点等。
> - **分离双指针**：两个指针分别在不同链表或不同起点上独立移动，常用于合并两个有序链表、比较链表节点等场景。

双指针法能够有效降低时间复杂度，减少空间消耗，是解决链表相关问题（如查找、删除、合并等）时非常高效且常用的技巧。

## 2. 快慢指针（起点不一致）

> **起点不一致的快慢指针**：快指针先走 n 步，然后两个指针同时移动，快指针到达末尾时，慢指针正好在目标位置。

### 2.1 求解步骤

1. **初始化**：两个指针 $slow$、$fast$ 都指向头节点。
2. **快指针先行**：快指针先移动 n 步。
3. **同步移动**：两个指针同时移动，直到快指针到达末尾（`fast == None`）。
4. **结果**：慢指针正好指向倒数第 n 个节点。

### 2.2 代码模板

```python
def findNthFromEnd(head, n):
    slow = fast = head
    
    # 快指针先走 n 步
    for _ in range(n):
        fast = fast.next
    
    # 两个指针同时移动
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow  # 慢指针指向倒数第 n 个节点
```

### 2.3 适用场景

- 找到链表中倒数第 k 个节点
- 删除链表倒数第 N 个节点
- 其他需要定位倒数位置的问题

### 2.4 经典例题：删除链表的倒数第 N 个结点

#### 2.4.1 题目链接

- [19. 删除链表的倒数第 N 个结点 - 力扣（LeetCode）](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

#### 2.4.2 题目大意

**描述**：给定一个链表的头节点 `head`。

**要求**：删除链表的倒数第 `n` 个节点，并且返回链表的头节点。

**说明**：

- 要求使用一次遍历实现。
- 链表中结点的数目为 `sz`。
- $1 \le sz \le 30$。
- $0 \le Node.val \le 100$。
- $1 \le n \le sz$。

**示例**：

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```python
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]


输入：head = [1], n = 1
输出：[]
```

#### 2.4.3 解题思路

##### 思路 1：快慢指针

常规思路是遍历一遍链表，求出链表长度，再遍历一遍到对应位置，删除该位置上的节点。

如果用一次遍历实现的话，可以使用快慢指针。让快指针先走 `n` 步，然后快慢指针、慢指针再同时走，每次一步，这样等快指针遍历到链表尾部的时候，慢指针就刚好遍历到了倒数第 `n` 个节点位置。将该位置上的节点删除即可。


##### 思路 1：代码

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建虚拟头节点，简化边界情况处理
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        # 快指针先走 n 步
        for _ in range(n):
            fast = fast.next
        
        # 两个指针同时移动
        while fast:
            slow = slow.next
            fast = fast.next
        
        # 删除目标节点（slow.next 是要删除的节点）
        slow.next = slow.next.next
        
        return dummy.next
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，只遍历一次
- **空间复杂度**：O(1)，只使用常数额外空间

## 3. 快慢指针（步长不一致）

> **步长不一致的快慢指针**：两个指针从同一起点出发，慢指针每次走 1 步，快指针每次走 2 步。

### 3.1 求解步骤

1. **初始化**：两个指针都指向头节点。
2. **不同步长**：慢指针每次移动 1 步，快指针每次移动 2 步。
3. **终止条件**：快指针到达末尾或无法继续移动。
4. **应用场景**：找中点、检测环、找交点等。

### 3.2 代码模板

```python
def fastSlowPointer(head):
    slow = fast = head
    
    # 快指针每次走 2 步，慢指针每次走 1 步
    while fast and fast.next:
        slow = slow.next      # 慢指针移动 1 步
        fast = fast.next.next # 快指针移动 2 步
    
    return slow  # 慢指针指向中点或环的入口
```

### 3.3 适用场景

- 寻找链表的中点
- 检测链表是否有环
- 找到两个链表的交点
- 其他需要定位中间位置的问题

### 3.4 经典例题：链表的中间结点

#### 3.4.1 题目链接

- [876. 链表的中间结点 - 力扣（LeetCode）](https://leetcode.cn/problems/middle-of-the-linked-list/)

#### 3.4.2 题目大意

**描述**：给定一个单链表的头节点 `head`。

**要求**：返回链表的中间节点。如果有两个中间节点，则返回第二个中间节点。

**说明**：

- 给定链表的结点数介于 `1` 和 `100` 之间。

**示例**：

```python
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
解释：返回的结点值为 3 。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.


输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
解释：由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
```

#### 3.4.3 解题思路

##### 思路 1：单指针

先遍历一遍链表，统计一下节点个数为 `n`，再遍历到 `n / 2` 的位置，返回中间节点。

##### 思路 1：代码

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 第一次遍历：计算链表长度
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        # 第二次遍历：找到中间位置
        curr = head
        for _ in range(count // 2):
            curr = curr.next
        
        return curr
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

##### 思路 2：快慢指针

使用步长不一致的快慢指针进行一次遍历找到链表的中间节点。具体做法如下：

1. 使用两个指针 `slow`、`fast`。`slow`、`fast` 都指向链表的头节点。
2. 在循环体中将快、慢指针同时向右移动。其中慢指针每次移动 `1` 步，即 `slow = slow.next`。快指针每次移动 `2` 步，即 `fast = fast.next.next`。
3. 等到快指针移动到链表尾部（即 `fast == Node`）时跳出循环体，此时 `slow` 指向链表中间位置。
4. 返回 `slow` 指针。

##### 思路 2：代码

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        
        # 快指针每次走 2 步，慢指针每次走 1 步
        # 当快指针到达末尾时，慢指针正好在中点
        while fast and fast.next:
            slow = slow.next      # 慢指针移动 1 步
            fast = fast.next.next # 快指针移动 2 步
        
        return slow
```

##### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

## 4. 分离双指针

> **分离双指针**：两个指针分别在不同的链表中移动，常用于合并、比较等操作。

### 4.1 求解步骤

1. **初始化**：两个指针分别指向两个链表的头节点。
2. **条件移动**：根据具体问题决定何时移动哪个指针。
3. **终止条件**：其中一个链表遍历完毕或满足特定条件。
4. **应用场景**：有序链表合并、链表比较等。

### 4.2 代码模板

```python
def separateTwoPointers(list1, list2):
    p1, p2 = list1, list2
    
    while p1 and p2:
        if condition1:
            # 两个指针同时移动
            p1 = p1.next
            p2 = p2.next
        elif condition2:
            # 只移动第一个指针
            p1 = p1.next
        else:
            # 只移动第二个指针
            p2 = p2.next
    
    return result
```

### 4.3 适用场景

- 合并两个有序链表
- 比较两个链表
- 找到两个链表的交点
- 其他需要同时处理两个链表的问题

### 4.4 经典例题：合并两个有序链表

#### 4.4.1 题目链接

- [21. 合并两个有序链表 - 力扣（LeetCode）](https://leetcode.cn/problems/merge-two-sorted-lists/)

#### 4.4.2 题目大意

**描述**：给定两个升序链表的头节点 `list1` 和 `list2`。

**要求**：将其合并为一个升序链表。

**说明**：

- 两个链表的节点数目范围是 $[0, 50]$。
- $-100 \le Node.val \le 100$。
- `list1` 和 `list2` 均按 **非递减顺序** 排列

**示例**：

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```python
输入：list1 = [1,2,4], list2 = [1,3,4]
输出：[1,1,2,3,4,4]


输入：list1 = [], list2 = []
输出：[]
```

#### 4.4.3 解题思路

##### 思路 1：归并排序

利用归并排序的思想，具体步骤如下：

1. 使用哑节点 `dummy_head` 构造一个头节点，并使用 `curr` 指向 `dummy_head` 用于遍历。
2. 然后判断 `list1` 和 `list2` 头节点的值，将较小的头节点加入到合并后的链表中。并向后移动该链表的头节点指针。
3. 然后重复上一步操作，直到两个链表中出现链表为空的情况。
4. 将剩余链表链接到合并后的链表中。
5. 将哑节点 `dummy_dead` 的下一个链节点 `dummy_head.next` 作为合并后有序链表的头节点返回。

##### 思路 1：代码

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头节点，简化操作
        dummy = ListNode(-1)
        curr = dummy
        
        # 分离双指针：分别遍历两个链表
        while list1 and list2:
            if list1.val <= list2.val:
                # 选择 list1 的当前节点
                curr.next = list1
                list1 = list1.next
            else:
                # 选择 list2 的当前节点
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # 处理剩余节点
        curr.next = list1 if list1 else list2
        
        return dummy.next
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

## 练习题目

- [0141. 环形链表](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/linked-list-cycle.md)
- [0142. 环形链表 II](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/linked-list-cycle-ii.md)
- [0019. 删除链表的倒数第 N 个结点](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/remove-nth-node-from-end-of-list.md)

- [链表双指针题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E9%93%BE%E8%A1%A8%E5%8F%8C%E6%8C%87%E9%92%88%E9%A2%98%E7%9B%AE)