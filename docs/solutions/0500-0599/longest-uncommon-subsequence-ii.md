# [0522. 最长特殊序列 II](https://leetcode.cn/problems/longest-uncommon-subsequence-ii/)

- 标签：数组、哈希表、双指针、字符串、排序
- 难度：中等

## 题目链接

- [0522. 最长特殊序列 II - 力扣](https://leetcode.cn/problems/longest-uncommon-subsequence-ii/)

## 题目大意

**描述**：

给定字符串列表 $strs$。

**要求**：

返回其中「最长的特殊序列」的长度。如果最长特殊序列不存在，返回 $-1$。

**说明**：

- 「特殊序列」定义如下：该序列为某字符串独有的子序列（即不能是其他字符串的子序列）。
- $s$ 的子序列可以通过删去字符串 $s$ 中的某些字符实现。
   - 例如，`"abc"` 是 `"aebdc"` 的子序列，因为您可以删除 `"aebdc"` 中的下划线字符来得到 `"abc"`。`"aebdc"` 的子序列还包括 `"aebdc"`、`"aeb"` 和 `""` (空字符串)。
- $2 \le strs.length \le 50$。
- $1 \le strs[i].length \le 10$。
- $strs[i]$ 只包含小写英文字母。

**示例**：

- 示例 1：

```python
输入: strs = ["aba","cdc","eae"]
输出: 3
```

- 示例 2：

```python
输入: strs = ["aaa","aaa","aa"]
输出: -1
```

## 解题思路

### 思路 1：暴力枚举 & 判子序列

对所有字符串按长度从大到小枚举，把每个字符串 $s$ 作为候选，检查它是否不是其它任一字符串的子序列。

- 判断子序列用双指针时间 $O(L)$，其中$L$为字符串最长长度。
- 遍历未与自己相等的所有字符串，只要$s$不是其他的子序列，即可返回 $|s|$。

### 思路 1：代码
```python
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # 检查s是不是t的子序列
        def is_subseq(s, t):
            i = 0
            for c in t:
                if i < len(s) and s[i] == c:
                    i += 1
            return i == len(s)
        
        res = -1
        for i, s in enumerate(strs):
            if all(i == j or not is_subseq(s, t) for j, t in enumerate(strs)):
                res = max(res, len(s))
        return res
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n^2 L)$，$n$为字符串数量，$L$为最大长度。
- **空间复杂度**：$O(1)$。
