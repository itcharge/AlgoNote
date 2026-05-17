# [1290. 二进制链表转整数](https://leetcode.cn/problems/convert-binary-number-in-a-linked-list-to-integer/)

- 标签：链表、数学
- 难度：简单

## 题目链接

- [1290. 二进制链表转整数 - 力扣](https://leetcode.cn/problems/convert-binary-number-in-a-linked-list-to-integer/)

## 题目大意

**描述**：给你一个单链表的引用结点 $head$。链表中每个结点的值不是 $0$ 就是 $1$。已知此链表是一个整数数字的二进制表示形式，最高位在链表的头部。

**要求**：返回该链表所表示数字的十进制值。

**说明**：

- 链表不为空。
- 链表的结点总数不超过 $30$。
- 每个结点的值不是 $0$ 就是 $1$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/15/graph-1.png)

```python
输入：head = [1,0,1]
输出：5
解释：二进制数 (101) 转化为十进制数 (5)
```

- 示例 2：

```python
输入：head = [0]
输出：0
```

## 解题思路

### 思路 1：遍历模拟

###### 1. 核心思想

二进制数转十进制最直观的方法就是「按权展开」。比如二进制数 $101$：$1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 5$。

但对于链表结构，我们是从最高位开始依次访问每一位的。一种更自然的计算方式是使用**秦九韶算法（Horner's method）**：

从最高位开始，每读入一个新的二进制位，将当前结果左移一位（乘以 $2$）再加上新位。用递推式表示为：

$$ans = ans \times 2 + bit$$

比如 $101$ 的计算过程：
- $ans = 0$
- 读 $1$：$ans = 0 \times 2 + 1 = 1$
- 读 $0$：$ans = 1 \times 2 + 0 = 2$
- 读 $1$：$ans = 2 \times 2 + 1 = 5$

这样就不需要知道链表的长度，也不需要预先计算每一位的幂次。

###### 2. 具体步骤

**第 1 步：初始化结果变量**

$ans = 0$。

**第 2 步：遍历链表**

从头结点开始，逐个访问链表的每个结点：
- 将 $ans$ 左移一位（乘以 $2$），为新的二进制位腾出最低位位置。
- 加上当前结点的值 $head.val$。

**第 3 步：移动到下一个结点**

$head = head.next$，继续处理直到链表末尾。

**第 4 步：返回结果**

遍历结束后 $ans$ 中存储的就是最终的十进制值。

**结合示例 1 走一遍：**

链表 $[1, 0, 1]$：
- $head.val = 1$：$ans = 0 \times 2 + 1 = 1$
- $head.val = 0$：$ans = 1 \times 2 + 0 = 2$
- $head.val = 1$：$ans = 2 \times 2 + 1 = 5$

返回 $5$。

### 思路 1：代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # 初始化结果变量
        ans = 0
        # 遍历链表，逐步计算十进制值
        while head:
            # 左移一位（乘 2）再加当前位
            ans = ans * 2 + head.val
            head = head.next
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是链表的长度。只需要从头到尾遍历一次链表，每个结点执行一次乘法和加法。
- **空间复杂度**：$O(1)$，只使用了一个整型变量 $ans$ 来存储结果，不随输入规模变化。
