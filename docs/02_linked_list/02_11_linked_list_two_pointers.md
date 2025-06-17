## 1. 双指针简介

在数组双指针中我们已经学习过了双指针的概念。这里再来复习一下。

> **双指针（Two Pointers）**：指的是在遍历元素的过程中，不是使用单个指针进行访问，而是使用两个指针进行访问，从而达到相应的目的。如果两个指针方向相反，则称为「对撞时针」。如果两个指针方向相同，则称为「快慢指针」。如果两个指针分别属于不同的数组 / 链表，则称为「分离双指针」。

而在单链表中，因为遍历节点只能顺着 `next` 指针方向进行，所以对于链表而言，一般只会用到「快慢指针」和「分离双指针」。其中链表的「快慢指针」又分为「起点不一致的快慢指针」和「步长不一致的快慢指针」。这几种类型的双指针所解决的问题也各不相同，下面我们一一进行讲解。

## 2. 起点不一致的快慢指针

>**起点不一致的快慢指针**：指的是两个指针从同一侧开始遍历链表，但是两个指针的起点不一样。 快指针 `fast` 比慢指针 `slow` 先走 `n` 步，直到快指针移动到链表尾端时为止。

### 2.1 起点不一致的快慢指针求解步骤

1. 使用两个指针 `slow`、`fast`。`slow`、`fast` 都指向链表的头节点，即：`slow = head`，`fast = head`。
2. 先将快指针向右移动 `n` 步。然后再同时向右移动快、慢指针。
3. 等到快指针移动到链表尾部（即 `fast == None`）时跳出循环体。

### 2.2 起点不一致的快慢指针伪代码模板

```python
slow = head
fast = head

while n:
    fast = fast.next
    n -= 1
while fast:
    fast = fast.next
    slow = slow.next
```

### 2.3 起点不一致的快慢指针适用范围

起点不一致的快慢指针主要用于找到链表中倒数第 k 个节点、删除链表倒数第 N 个节点等。

### 2.4 删除链表的倒数第 N 个结点

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

需要注意的是要删除的节点可能包含了头节点。我们可以考虑在遍历之前，新建一个头节点，让其指向原来的头节点。这样，最终如果删除的是头节点，则删除原头节点即可。返回结果的时候，可以直接返回新建头节点的下一位节点。

##### 思路 1：代码

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        newHead = ListNode(0, head)
        fast = head
        slow = newHead
        while n:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return newHead.next
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

## 3. 步长不一致的快慢指针

> **步长不一致的快慢指针**：指的是两个指针从同一侧开始遍历链表，两个指针的起点一样，但是步长不一致。例如，慢指针 `slow` 每次走 `1` 步，快指针 `fast` 每次走两步。直到快指针移动到链表尾端时为止。

### 3.1 步长不一致的快慢指针求解步骤

1. 使用两个指针 `slow`、`fast`。`slow`、`fast` 都指向链表的头节点。
2. 在循环体中将快、慢指针同时向右移动，但是快、慢指针的移动步长不一致。比如将慢指针每次移动 `1` 步，即 `slow = slow.next`。快指针每次移动 `2` 步，即 `fast = fast.next.next`。
3. 等到快指针移动到链表尾部（即 `fast == None`）时跳出循环体。

### 3.2 步长不一致的快慢指针伪代码模板

```python
fast = head
slow = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### 3.3 步长不一致的快慢指针适用范围

步长不一致的快慢指针适合寻找链表的中点、判断和检测链表是否有环、找到两个链表的交点等问题。

### 3.4 链表的中间结点

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
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

##### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

### 3.5 判断链表中是否含有环

#### 3.5.1 题目链接

- [141. 环形链表 - 力扣（LeetCode）](https://leetcode.cn/problems/linked-list-cycle/)

#### 3.5.2 题目大意

**描述**：给定一个链表的头节点 `head`。

**要求**：判断链表中是否有环。如果有环则返回 `True`，否则返回 `False`。

**说明**：

- 链表中节点的数目范围是 $[0, 10^4]$。
- $-10^5 \le Node.val \le 10^5$。
- `pos` 为 `-1` 或者链表中的一个有效索引。

**示例**：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

```python
输入：head = [3,2,0,-4], pos = 1
输出：True
解释：链表中有一个环，其尾部连接到第二个节点。
```

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

```python
输入：head = [1,2], pos = 0
输出：True
解释：链表中有一个环，其尾部连接到第一个节点。
```

#### 3.5.3 解题思路

##### 思路 1：哈希表

最简单的思路是遍历所有节点，每次遍历节点之前，使用哈希表判断该节点是否被访问过。如果访问过就说明存在环，如果没访问过则将该节点添加到哈希表中，继续遍历判断。

##### 思路 1：代码

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodeset = set()

        while head:
            if head in nodeset:
                return True
            nodeset.add(head)
            head = head.next
        return False
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

##### 思路 2：快慢指针（Floyd 判圈算法）

这种方法类似于在操场跑道跑步。两个人从同一位置同时出发，如果跑道有环（环形跑道），那么快的一方总能追上慢的一方。

基于上边的想法，Floyd 用两个指针，一个慢指针（龟）每次前进一步，快指针（兔）指针每次前进两步（两步或多步效果是等价的）。如果两个指针在链表头节点以外的某一节点相遇（即相等）了，那么说明链表有环，否则，如果（快指针）到达了某个没有后继指针的节点时，那么说明没环。

##### 思路 2：代码

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
```

##### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。   

## 4. 分离双指针

> **分离双指针**：两个指针分别属于不同的链表，两个指针分别在两个链表中移动。

### 4.1 分离双指针求解步骤

1. 使用两个指针 `left_1`、`left_2`。`left_1` 指向第一个链表头节点，即：`left_1 = list1`，`left_2` 指向第二个链表头节点，即：`left_2 = list2`。
2. 当满足一定条件时，两个指针同时右移，即 `left_1 = left_1.next`、`left_2 = left_2.next`。
3. 当满足另外一定条件时，将 `left_1` 指针右移，即 `left_1 = left_1.next`。
4. 当满足其他一定条件时，将 `left_2` 指针右移，即 `left_2 = left_2.next`。
5. 当其中一个链表遍历完时或者满足其他特殊条件时跳出循环体。

### 4.2 分离双指针伪代码模板

```python
left_1 = list1
left_2 = list2

while left_1 and left_2:
    if 一定条件 1:
        left_1 = left_1.next
        left_2 = left_2.next
    elif 一定条件 2:
        left_1 = left_1.next
    elif 一定条件 3:
        left_2 = left_2.next
```

### 4.3 分离双指针适用范围

分离双指针一般用于有序链表合并等问题。

### 4.4 合并两个有序链表

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
        dummy_head = ListNode(-1)

        curr = dummy_head
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 is not None else list2

        return dummy_head.next
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

