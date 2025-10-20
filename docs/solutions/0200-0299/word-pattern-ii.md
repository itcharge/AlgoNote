# [0291. 单词规律 II](https://leetcode.cn/problems/word-pattern-ii/)

- 标签：哈希表、字符串、回溯
- 难度：中等

## 题目链接

- [0291. 单词规律 II - 力扣](https://leetcode.cn/problems/word-pattern-ii/)

## 题目大意

**描述**：

给定一种规律 $pattern$ 和一个字符串 $s$。

**要求**：

判断 $s$ 是否和 $pattern$ 的规律相匹配。

如果存在单个字符到「非空」字符串的「双射映射」，那么字符串 $s$ 匹配 $pattern$，即：如果 $pattern$ 中的每个字符都被它映射到的字符串替换，那么最终的字符串则为 $s$。「双射」意味着映射双方一一对应，不会存在两个字符映射到同一个字符串，也不会存在一个字符分别映射到两个不同的字符串。

**说明**：

- $1 \le pattern.length, s.length \le 20$。
- $pattern$ 和 $s$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：pattern = "abab", s = "redblueredblue"
输出：true
解释：一种可能的映射如下：
'a' -> "red"
'b' -> "blue"
```

- 示例 2：

```python
输入：pattern = "aaaa", s = "asdasdasdasd"
输出：true
解释：一种可能的映射如下：
'a' -> "asd"
```

## 解题思路

### 思路 1：回溯 + 双射映射

核心在于构造规律字符到字符串子串的双射映射。设规律串为 $pattern$，目标串为 $s$。在回溯过程中维护两张映射表：

- $f: \Sigma_{p} \to (\Sigma_{s})^{+}$：从规律字符到非空子串的映射；
- $g: (\Sigma_{s})^{+} \to \Sigma_{p}$：从非空子串到规律字符的反向映射；

用深度优先搜索 `dfs(i, j)` 表示当前匹配到 $pattern$ 的下标 $i$ 与 $s$ 的下标 $j$：

1. 终止条件：如果 $i = |pattern|$ 且 $j = |s|$，说明恰好匹配成功，返回 True；如果其中一个到达末尾另一个未到达，返回 False。
2. 设当前规律字符为 $c = pattern[i]$。
   - 如果 $c$ 已在 $f$ 中映射到某个子串 $t$，则检查 $s$ 在位置 $j$ 是否以 $t$ 为前缀：即 $s[j: j+|t|] = t$。如果匹配则递归到 $dfs(i+1, j+|t|)$，否则返回 False。
   - 如果 $c$ 尚未建立映射，则需要在 $s$ 的后缀中尝试所有可能的非空切分 $s[j:k]$（其中 $j < k \le |s|$）。如果该子串尚未被其他字符使用（即不在 $g$ 中），则建立双射 $f[c] = s[j:k]$、$g[s[j:k]] = c$，并递归 $dfs(i+1, k)$。如果递归失败，撤销映射继续尝试下一个切分。
3. 简单剪枝：剩余字符至少要占用长度 1，如果 $|s| - j < |pattern| - i$，可直接返回 False。

### 思路 1：代码

```python
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        # 回溯 + 双射映射
        # p2w: 规律字符 -> 具体子串；w2p: 子串 -> 规律字符
        p2w = {}
        w2p = {}

        def dfs(i: int, j: int) -> bool:
            # 如果同时走到末尾，匹配成功
            if i == len(pattern) and j == len(s):
                return True
            # 只有一个到末尾则失败
            if i == len(pattern) or j == len(s):
                return False

            # 剪枝：剩余 pattern 字符至少需要占用剩余 s 的长度
            if len(s) - j < len(pattern) - i:
                return False

            c = pattern[i]
            # 如果已有映射，校验前缀
            if c in p2w:
                t = p2w[c]
                # s 当前前缀不匹配则失败
                if not s.startswith(t, j):
                    return False
                return dfs(i + 1, j + len(t))

            # 否则尝试所有可能的非空切分 s[j:k]
            for k in range(j + 1, len(s) + 1):
                t = s[j:k]
                # 子串已被其他字符占用则跳过，保证双射
                if t in w2p:
                    continue

                # 建立双向映射
                p2w[c] = t
                w2p[t] = c
                if dfs(i + 1, k):
                    return True
                # 回溯撤销
                del p2w[c]
                del w2p[t]

            return False

        return dfs(0, 0)
```

### 思路 1：复杂度分析

- **时间复杂度**：最坏情况下为指数级。每个未映射的规律字符 $c$ 可能尝试 $O(|s|)$ 个切分，整体可上界为 $O(|s|^{|pattern|})$。由于题目规模较小（均不超过 20），回溯可接受。
- **空间复杂度**：$O(|pattern| + |s|)$。主要为递归栈与映射表存储，映射的子串总长度不超过 $|s|$。
