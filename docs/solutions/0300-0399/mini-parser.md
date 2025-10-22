# [0385. 迷你语法分析器](https://leetcode.cn/problems/mini-parser/)

- 标签：栈、深度优先搜索、字符串
- 难度：中等

## 题目链接

- [0385. 迷你语法分析器 - 力扣](https://leetcode.cn/problems/mini-parser/)

## 题目大意

**描述**：

给定一个字符串 $s$ 表示一个整数嵌套列表。

**要求**：

实现一个解析它的语法分析器并返回解析的结果 `NestedInteger`。

**说明**：

- 列表中的每个元素只可能是整数或整数嵌套列表。
- $1 \le s.length \le 5 \times 10^{4}$。
- $s$ 由数字、方括号 `"[]"`、负号 `'-'`、逗号 `','` 组成。
- 用例保证 $s$ 是可解析的 `NestedInteger。`
- 输入中的所有值的范围是 $[-10^{6}, 10^{6}]$。

**示例**：

- 示例 1：

```python
输入：s = "324",
输出：324
解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
```

- 示例 2：

```python
输入：s = "[123,[456,[789]]]",
输出：[123,[456,[789]]]
解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
1. 一个 integer 包含值 123
2. 一个包含两个元素的嵌套列表：
    i.  一个 integer 包含值 456
    ii. 一个包含一个元素的嵌套列表
         a. 一个 integer 包含值 789
```

## 解题思路

### 思路 1：栈

这道题的核心思想是：**使用栈来模拟嵌套结构的解析过程**。

解题步骤：

1. **初始化栈**：创建一个栈 $stack$ 来存储当前正在构建的 `NestedInteger` 对象。
2. **遍历字符串**：逐个字符处理字符串 $s$：
   - 遇到 `'['`：创建新的 `NestedInteger` 对象并压入栈中。
   - 遇到 `']'`：弹出栈顶元素，如果栈不为空，将其添加到新的栈顶元素中。
   - 遇到数字或负号：解析完整的数字，创建 `NestedInteger` 对象并添加到当前栈顶元素中。
   - 遇到逗号：跳过，继续处理下一个字符。
3. **返回结果**：栈中最终剩余的元素就是解析结果。

**关键点**：

- 栈用于维护当前嵌套层级，每遇到 `'['` 就进入新的嵌套层级。
- 每遇到 `']'` 就退出当前嵌套层级，将当前层级的结果添加到上一层级。
- 数字解析需要处理负号和多位数字的情况。
- 如果输入是单个数字（没有方括号），直接返回该数字对应的 `NestedInteger`。

**算法正确性**：

设字符串 $s$ 的长度为 $n$，算法通过栈正确维护了嵌套结构：
- 每个 `'['` 对应一个入栈操作，创建新的嵌套层级。
- 每个 `']'` 对应一个出栈操作，完成当前层级的构建。
- 数字解析保证了每个数字都被正确识别和转换。

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
    def deserialize(self, s: str) -> NestedInteger:
        # 如果字符串不以'['开头，说明是单个数字
        if s[0] != '[':
            return NestedInteger(int(s))
        
        # 使用栈来维护嵌套结构
        stack = []
        i = 0
        
        while i < len(s):
            if s[i] == '[':
                # 遇到'['，创建新的NestedInteger并压入栈
                stack.append(NestedInteger())
                i += 1
            elif s[i] == ']':
                # 遇到']'，弹出栈顶元素
                if len(stack) > 1:
                    # 如果栈中还有元素，将当前元素添加到上一层级
                    current = stack.pop()
                    stack[-1].add(current)
                i += 1
            elif s[i] == ',':
                # 遇到逗号，跳过
                i += 1
            else:
                # 遇到数字，解析完整的数字
                start = i
                # 处理负号
                if s[i] == '-':
                    i += 1
                # 解析数字部分
                while i < len(s) and s[i].isdigit():
                    i += 1
                # 创建数字对应的NestedInteger并添加到当前栈顶
                num = int(s[start:i])
                stack[-1].add(NestedInteger(num))
        
        # 返回栈中唯一的元素
        return stack[0]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串 $s$ 的长度。需要遍历字符串中的每个字符一次。
- **空间复杂度**：$O(d)$，其中 $d$ 是嵌套的最大深度。栈的空间复杂度取决于嵌套层级数。
