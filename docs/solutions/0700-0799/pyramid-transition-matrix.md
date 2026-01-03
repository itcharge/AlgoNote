# [0756. 金字塔转换矩阵](https://leetcode.cn/problems/pyramid-transition-matrix/)

- 标签：位运算、深度优先搜索、广度优先搜索、哈希表、字符串
- 难度：中等

## 题目链接

- [0756. 金字塔转换矩阵 - 力扣](https://leetcode.cn/problems/pyramid-transition-matrix/)

## 题目大意

**描述**：

你正在把积木堆成金字塔。每个块都有一个颜色，用一个字母表示。每一行的块比它下面的行 少一个块 ，并且居中。

为了使金字塔美观，只有特定的「三角形图案」是允许的。一个三角形的图案由「两个块」和叠在上面的「单个块」组成。模式是以三个字母字符串的列表形式 $allowed$ 给出的，其中模式的前两个字符分别表示左右底部块，第三个字符表示顶部块。

- 例如，`"ABC"` 表示一个三角形图案，其中一个 `"C"` 块堆叠在一个 `"A"` 块(左)和一个 `"B"` 块(右)之上。请注意，这与 `"BAC"` 不同，`"B"` 在左下角，`"A"` 在右下角。

**要求**：

你从作为单个字符串给出的底部的一排积木 $bottom$ 开始，必须「将其作为金字塔的底部」。

在给定 $bottom$ 和 $allowed$ 的情况下，如果你能一直构建到金字塔顶部，使金字塔中的 每个三角形图案 都是在 $allowed$ 中的，则返回 true，否则返回 false。

**说明**：

- $2 \le bottom.length \le 6$。
- $0 \le allowed.length \le 216$。
- $allowed[i].length == 3$。
- 所有输入字符串中的字母来自集合 `{'A', 'B', 'C', 'D', 'E', 'F'}`。
- $allowed$ 中所有值都是唯一的。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/08/26/pyramid1-grid.jpg)

```python
输入：bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
输出：true
解释：允许的三角形图案显示在右边。
从最底层(第 3 层)开始，我们可以在第 2 层构建“CE”，然后在第 1 层构建“E”。
金字塔中有三种三角形图案，分别是 “BCC”、“CDE” 和 “CEA”。都是允许的。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/08/26/pyramid2-grid.jpg)

```python
输入：bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
输出：false
解释：允许的三角形图案显示在右边。
从最底层(即第 4 层)开始，创造第 3 层有多种方法，但如果尝试所有可能性，你便会在创造第 1 层前陷入困境。
```

## 解题思路

### 思路 1：DFS + 哈希表

使用深度优先搜索（DFS）和哈希表来构建金字塔。

**实现步骤**：

1. 将 $allowed$ 转换为哈希表，键为底部两个字符，值为可能的顶部字符列表。
2. 使用 DFS 递归构建金字塔：
   - 如果当前层只有一个字符，返回 `True`。
   - 否则，尝试所有可能的下一层组合。
3. 对于当前层的每个相邻字符对，查找可能的顶部字符。
4. 递归检查是否能构建到顶部。

### 思路 1：代码

```python
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict
        
        # 构建哈希表：底部两个字符 -> 可能的顶部字符列表
        mapping = defaultdict(list)
        for pattern in allowed:
            mapping[pattern[:2]].append(pattern[2])
        
        def dfs(current):
            """递归构建金字塔"""
            # 如果当前层只有一个字符，成功
            if len(current) == 1:
                return True
            
            # 尝试构建下一层
            return build_next_layer(current, 0, [])
        
        def build_next_layer(current, index, next_layer):
            """构建下一层"""
            # 如果已经构建完下一层，递归检查
            if index == len(current) - 1:
                return dfs(''.join(next_layer))
            
            # 尝试当前位置的所有可能字符
            base = current[index:index+2]
            for char in mapping[base]:
                next_layer.append(char)
                if build_next_layer(current, index + 1, next_layer):
                    return True
                next_layer.pop()
            
            return False
        
        return dfs(bottom)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(A^n)$，其中 $A$ 是字母表大小，$n$ 是 $bottom$ 的长度。最坏情况下需要尝试所有可能的组合。
- **空间复杂度**：$O(n^2)$，递归栈的深度为 $O(n)$，每层需要 $O(n)$ 空间。
