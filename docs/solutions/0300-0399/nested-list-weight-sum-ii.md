# [0364. 嵌套列表加权和 II](https://leetcode.cn/problems/nested-list-weight-sum-ii/)

- 标签：栈、深度优先搜索、广度优先搜索
- 难度：中等

## 题目链接

- [0364. 嵌套列表加权和 II - 力扣](https://leetcode.cn/problems/nested-list-weight-sum-ii/)

## 题目大意

**描述**：

给定一个整数嵌套列表 $nestedList$，每一个元素要么是一个整数，要么是一个列表（这个列表中的每个元素也同样是整数或列表）。

- 整数的「深度」取决于它位于多少个列表内部。例如，嵌套列表 $[1,[2,2],[[3],2],1]$ 的每个整数的值都等于它的深度。令 $maxDepth$ 是任意整数的「最大深度」。
- 整数的「权重」为 $maxDepth$ - (整数的深度) $+ 1$。

**要求**：

将 $nestedList$ 列表中每个整数先乘权重再求和，返回该加权和。

**说明**：

- $1 \le nestedList.length \le 50$。
- 嵌套列表中整数的值在范围 $[-10^{3}, 10^{3}]$。
- 任意整数的最大「深度」小于等于 $50$。
- 没有空列表。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/03/27/nestedlistweightsumiiex1.png)

```python
输入：nestedList = [[1,1],2,[1,1]]
输出：8
解释：4 个 1 在深度为 1 的位置， 一个 2 在深度为 2 的位置。
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/03/27/nestedlistweightsumiiex2.png)

```python
输入：nestedList = [1,[4,[6]]]
输出：17
解释：一个 1 在深度为 3 的位置， 一个 4 在深度为 2 的位置，一个 6 在深度为 1 的位置。 
1*3 + 4*2 + 6*1 = 17
```

## 解题思路

### 思路 1：两次遍历

1. **第一次遍历**：计算最大深度 $maxDepth$。使用深度优先搜索遍历整个嵌套列表，记录每个整数的深度，并更新最大深度。

2. **第二次遍历**：计算加权和。再次遍历嵌套列表，对于每个整数，其权重为 $maxDepth - depth + 1$，其中 $depth$ 是该整数的深度。将所有整数的值乘以其权重后求和。

具体步骤：

- 定义递归函数 `getMaxDepth(nestedList, depth)` 用于计算最大深度。
- 定义递归函数 `calculateSum(nestedList, depth, maxDepth)` 用于计算加权和。
- 对每个 `NestedInteger` 元素：
  - 如果是整数，则在计算最大深度时进行比较和更新；在计算加权和时累加当前值乘以权重。
  - 如果是列表，则递归地处理其内部元素。


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
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # 第一次遍历：计算最大深度
        max_depth = self.getMaxDepth(nestedList, 1)
        
        # 第二次遍历：计算加权和
        return self.calculateSum(nestedList, 1, max_depth)
    
    def getMaxDepth(self, nestedList: List[NestedInteger], depth: int) -> int:
        """计算嵌套列表的最大深度"""
        max_depth = depth
        
        for item in nestedList:
            if item.isInteger():
                # 如果是整数，更新最大深度
                max_depth = max(max_depth, depth)
            else:
                # 如果是列表，递归计算子列表的最大深度
                max_depth = max(max_depth, self.getMaxDepth(item.getList(), depth + 1))
        
        return max_depth
    
    def calculateSum(self, nestedList: List[NestedInteger], depth: int, max_depth: int) -> int:
        """计算加权和"""
        total_sum = 0
        
        for item in nestedList:
            if item.isInteger():
                # 如果是整数，计算其加权贡献
                # 权重 = max_depth - depth + 1
                weight = max_depth - depth + 1
                total_sum += item.getInteger() * weight
            else:
                # 如果是列表，递归计算子列表的加权和
                total_sum += self.calculateSum(item.getList(), depth + 1, max_depth)
        
        return total_sum
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是嵌套列表中所有整数的总数。需要遍历两次嵌套列表，每次遍历的时间复杂度都是 $O(n)$。
- **空间复杂度**：$O(d)$，其中 $d$ 是嵌套列表的最大深度。递归调用栈的深度最多为 $d$。
