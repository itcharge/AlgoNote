# [0859. 亲密字符串](https://leetcode.cn/problems/buddy-strings/)

- 标签：哈希表、字符串
- 难度：简单

## 题目链接

- [0859. 亲密字符串 - 力扣](https://leetcode.cn/problems/buddy-strings/)

## 题目大意

**描述**：

给定两个字符串 $s$ 和 $goal$。

**要求**：

只要我们可以通过交换 $s$ 中的两个字母得到与 $goal$ 相等的结果，就返回 true；否则返回 false。

**说明**：

- 交换字母的定义是：取两个下标 $i$ 和 $j$（下标从 0 开始）且满足 $i \ne j$ ，接着交换 $s[i]$ 和 $s[j]$ 处的字符。
   - 例如，在 `"abcd"` 中交换下标 0 和下标 2 的元素可以生成 `"cbad"`。
- $1 \le s.length, goal.length \le 2 \times 10^{4}$。
- $s$ 和 $goal$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "ab", goal = "ba"
输出：true
解释：你可以交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 相等。
```

- 示例 2：

```python
输入：s = "ab", goal = "ab"
输出：false
解释：你只能交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 不相等。
```

## 解题思路

### 思路 1：分情况讨论

这道题要求判断是否可以通过交换 $s$ 中的两个字母得到 $goal$。需要分情况讨论：

1. **长度不同**：如果 $s$ 和 $goal$ 长度不同，直接返回 $False$。

2. **字符串相同**：如果 $s$ 和 $goal$ 完全相同，需要判断 $s$ 中是否有重复字符。如果有重复字符，可以交换这两个相同的字符，返回 $True$；否则返回 $False$。

3. **字符串不同**：找出所有不同的位置，如果不同位置的数量不等于 2，返回 $False$。如果恰好有 2 个不同位置，检查交换后是否能得到 $goal$。

### 思路 1：代码

```python
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # 长度不同，直接返回 False
        if len(s) != len(goal):
            return False
        
        # 如果两个字符串相同
        if s == goal:
            # 检查是否有重复字符，有则可以交换
            return len(set(s)) < len(s)
        
        # 找出所有不同的位置
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        
        # 不同位置必须恰好为 2 个
        if len(diff) != 2:
            return False
        
        # 检查交换后是否能得到 goal
        i, j = diff[0], diff[1]
        return s[i] == goal[j] and s[j] == goal[i]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串的长度。需要遍历字符串一次。
- **空间复杂度**：$O(n)$，使用集合存储字符需要 $O(n)$ 空间。
