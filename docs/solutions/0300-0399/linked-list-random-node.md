# [0382. 链表随机节点](https://leetcode.cn/problems/linked-list-random-node/)

- 标签：水塘抽样、链表、数学、随机化
- 难度：中等

## 题目链接

- [0382. 链表随机节点 - 力扣](https://leetcode.cn/problems/linked-list-random-node/)

## 题目大意

**描述**：

给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点「被选中的概率一样」。

**要求**：

实现 `Solution` 类：
- `Solution(ListNode head)` 使用整数数组初始化对象。
- `int getRandom()` 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。

**说明**：

- 链表中的节点数在范围 $[1, 10^{4}]$ 内。
- $-10^{4} \le Node.val \le 10^{4}$。
- 至多调用 `getRandom` 方法 $10^{4}$ 次。

- 进阶：
   - 如果链表非常大且长度未知，该怎么处理？
   - 你能否在不使用额外空间的情况下解决此问题？

**示例**：

- 示例 1：

```python
示例：

![](https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg)


输入
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
输出
[null, 1, 3, 2, 2, 3]

解释
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // 返回 1
solution.getRandom(); // 返回 3
solution.getRandom(); // 返回 2
solution.getRandom(); // 返回 2
solution.getRandom(); // 返回 3
// getRandom() 方法应随机返回 1、2、3中的一个，每个元素被返回的概率相等。
```

- 示例 2：

```python
输入：
输出：
```

## 解题思路

### 思路 1：水塘抽样算法

这道题的核心思想是：**使用水塘抽样算法，在不知道链表长度的情况下，保证每个节点被选中的概率相等**。

解题步骤：

1. **初始化**：保存链表头节点 $head$，用于后续遍历。

2. **水塘抽样**：
   - 遍历链表，对于第 $i$ 个节点（从 $1$ 开始计数），以 $\frac{1}{i}$ 的概率选择该节点。
   - 使用随机数生成器 $random.randint(0, i-1)$，如果结果为 $0$，则选择当前节点。
   - 这样保证每个节点被选中的概率都是 $\frac{1}{n}$，其中 $n$ 是链表长度。

3. **概率证明**：
   - 第 $1$ 个节点被选中的概率：$P_1 = 1$。
   - 第 $2$ 个节点被选中的概率：$P_2 = \frac{1}{2}$。
   - 第 $3$ 个节点被选中的概率：$P_3 = \frac{1}{3}$。
   - ...
   - 第 $n$ 个节点被选中的概率：$P_n = \frac{1}{n}$。
   - 最终每个节点被选中的概率：$P_i = \frac{1}{i} \times \frac{i}{i+1} \times \frac{i+1}{i+2} \times ... \times \frac{n-1}{n} = \frac{1}{n}$。

**关键点**：

- 水塘抽样算法适用于 **数据流** 或 **未知长度** 的情况。
- 只需要 **一次遍历**，时间复杂度为 $O(n)$。
- 空间复杂度为 $O(1)$，不需要额外存储所有节点。
- 每次调用 `getRandom()` 都需要重新遍历整个链表。

### 思路 1：代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution:
    def __init__(self, head: Optional[ListNode]):
        # 保存链表头节点
        self.head = head

    def getRandom(self) -> int:
        # 水塘抽样算法
        current = self.head
        result = 0
        count = 0
        
        # 遍历链表
        while current:
            count += 1
            # 以 1/count 的概率选择当前节点
            if random.randint(0, count - 1) == 0:
                result = current.val
            current = current.next
        
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是链表的长度。每次调用 `getRandom()` 都需要遍历整个链表。
- **空间复杂度**：$O(1)$，只使用了常数额外空间，没有使用额外的数据结构存储节点。
