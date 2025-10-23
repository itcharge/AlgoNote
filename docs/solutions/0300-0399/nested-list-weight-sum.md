# [0339. 嵌套列表加权和](https://leetcode.cn/problems/nested-list-weight-sum/)

- 标签：深度优先搜索、广度优先搜索
- 难度：中等

## 题目链接

- [0339. 嵌套列表加权和 - 力扣](https://leetcode.cn/problems/nested-list-weight-sum/)

## 题目大意

**描述**：

给定一个嵌套的整数列表 $nestedList$，每个元素要么是整数，要么是列表。同时，列表中元素同样也可以是整数或者是另一个列表。

- 整数的「深度」是其在列表内部的嵌套层数。例如，嵌套列表 $[1,[2,2],[[3],2],1]$ 中每个整数的值就是其深度。

**要求**：

请返回该列表按深度加权后所有整数的总和。

**说明**：

- $1 \le nestedList.length \le 50$。
- 嵌套列表中整数的值在范围 $[-10^{3}, 10^{3}]$ 内。
- 任何整数的最大深度都小于或等于 $50$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/01/14/nestedlistweightsumex1.png)

```python
输入：nestedList = [[1,1],2,[1,1]]
输出：10 
解释：因为列表中有四个深度为 2 的 1 ，和一个深度为 1 的 2。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/01/14/nestedlistweightsumex2.png)

```python
输入：nestedList = [1,[4,[6]]]
输出：27 
解释：一个深度为 1 的 1，一个深度为 2 的 4，一个深度为 3 的 6。所以，1 + 4*2 + 6*3 = 27。
```

## 解题思路

### 思路 1：深度优先搜索

使用深度优先搜索（DFS）递归遍历嵌套列表，在遍历过程中记录当前深度 $depth$，对于每个整数，将其值乘以深度后累加到总和中。

具体步骤：

1. **递归函数设计**：定义递归函数 `dfs(nestedList, depth)`，其中 $nestedList$ 是当前要处理的嵌套列表，$depth$ 是当前深度。

2. **遍历过程**：
   - 对于每个 `NestedInteger` 元素：
     - 如果是整数，则将其值乘以当前深度 $depth$ 后累加到总和中。
     - 如果是列表，则递归调用 `dfs(item.getList(), depth + 1)`，深度加 $1$。

3. **初始调用**：从深度 $1$ 开始调用 `dfs(nestedList, 1)`。

### 思路 1：代码

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nested_list, depth):
            """深度优先搜索计算加权和"""
            total_sum = 0
            
            for item in nested_list:
                if item.isInteger():
                    # 如果是整数，将其值乘以当前深度后累加
                    total_sum += item.getInteger() * depth
                else:
                    # 如果是列表，递归处理子列表，深度加 1
                    total_sum += dfs(item.getList(), depth + 1)
            
            return total_sum
        
        # 从深度 1 开始递归计算
        return dfs(nestedList, 1)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是嵌套列表中所有整数的总数。需要遍历每个元素一次。
- **空间复杂度**：$O(d)$，其中 $d$ 是嵌套列表的最大深度。递归调用栈的深度最多为 $d$。
