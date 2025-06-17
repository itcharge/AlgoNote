# [0014. 最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/)

- 标签：字典树、字符串
- 难度：简单

## 题目链接

- [0014. 最长公共前缀 - 力扣](https://leetcode.cn/problems/longest-common-prefix/)

## 题目大意

**描述**：给定一个字符串数组 `strs`。

**要求**：返回字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 `""`。

**说明**：

- $1 \le strs.length \le 200$。
- $0 \le strs[i].length \le 200$。
- `strs[i]` 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：strs = ["flower","flow","flight"]
输出："fl"
```

- 示例 2：

```python
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
```

## 解题思路

### 思路 1：纵向遍历

1. 依次遍历所有字符串的每一列，比较相同位置上的字符是否相同。
   1. 如果相同，则继续对下一列进行比较。
   2. 如果不相同，则当前列字母不再属于公共前缀，直接返回当前列之前的部分。
2. 如果遍历结束，说明字符串数组中的所有字符串都相等，则可将字符串数组中的第一个字符串作为公共前缀进行返回。

### 思路 1：代码

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length = len(strs[0])
        count = len(strs)
        for i in range(length):
            c = strs[0][i]
            for j in range(1, count):
                if len(strs[j]) == i or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$，其中 $m$ 是字符串数组中的字符串的平均长度，$n$ 是字符串的数量。
- **空间复杂度**：$O(1)$。