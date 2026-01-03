# [0726. 原子的数量](https://leetcode.cn/problems/number-of-atoms/)

- 标签：栈、哈希表、字符串、排序
- 难度：困难

## 题目链接

- [0726. 原子的数量 - 力扣](https://leetcode.cn/problems/number-of-atoms/)

## 题目大意

**描述**：

原子总是以一个大写字母开始，接着跟随 $0$ 个或任意个小写字母，表示原子的名字。
如果数量大于 $1$，原子后会跟着数字表示原子的数量。如果数量等于 $1$ 则不会跟数字。
   
- 例如，`"H2O"` 和 `"H2O2"` 是可行的，但 `"H1O2"` 这个表达是不可行的。

两个化学式连在一起可以构成新的化学式。

- 例如 `"H2O2He3Mg4"` 也是化学式。

由括号括起的化学式并佐以数字（可选择性添加）也是化学式。

- 例如 `"(H2O2)"` 和 `"(H2O2)3"` 是化学式。

给定一个字符串化学式 $formula$。

**要求**：

返回「每种原子的数量」，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

**说明**：

- $1 \le formula.length \le 10^{3}$。
- $formula$ 由英文字母、数字、`'('` 和 `')'` 组成。
- $formula$ 总是有效的化学式。

**示例**：

- 示例 1：

```python
输入：formula = "H2O"
输出："H2O"
解释：原子的数量是 {'H': 2, 'O': 1}。
```

- 示例 2：

```python
输入：formula = "Mg(OH)2"
输出："H2MgO2"
解释：原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
```

## 解题思路

### 思路 1：栈 + 哈希表

这道题需要解析化学式并统计每种原子的数量。可以使用栈来处理括号嵌套的情况。

**解题步骤**：

1. 使用栈来存储当前层级的原子计数（哈希表）。
2. 遍历化学式字符串：
   - 遇到 `(`：将当前哈希表压入栈，创建新的哈希表。
   - 遇到 `)`：弹出栈顶哈希表，读取后面的数字，将当前哈希表中的所有原子数量乘以该数字，然后合并到栈顶哈希表。
   - 遇到大写字母：读取完整的原子名称和后面的数字，加入当前哈希表。
3. 最后将所有原子按字典序排序，构建结果字符串。

**实现细节**：

- 使用栈存储嵌套的哈希表。
- 解析原子名称：大写字母开头，后面跟若干小写字母。
- 解析数字：连续的数字字符。

### 思路 1：代码

```python
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from collections import defaultdict
        
        n = len(formula)
        i = 0
        stack = [defaultdict(int)]
        
        while i < n:
            if formula[i] == '(':
                # 遇到左括号，压入新的哈希表
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                # 遇到右括号，读取后面的数字
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i]) if start < i else 1
                
                # 弹出栈顶哈希表，乘以倍数后合并到新的栈顶
                top = stack.pop()
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplier
            else:
                # 读取原子名称
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]
                
                # 读取数字
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if start < i else 1
                
                # 加入当前哈希表
                stack[-1][atom] += count
        
        # 构建结果字符串
        result = []
        for atom in sorted(stack[-1].keys()):
            count = stack[-1][atom]
            result.append(atom)
            if count > 1:
                result.append(str(count))
        
        return ''.join(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + k \log k)$，其中 $n$ 是化学式的长度，$k$ 是不同原子的种类数。需要遍历化学式一次，然后对原子排序。
- **空间复杂度**：$O(n)$。栈的深度最多为括号的嵌套层数，哈希表存储原子计数。
