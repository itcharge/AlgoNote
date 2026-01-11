# [0471. 编码最短长度的字符串](https://leetcode.cn/problems/encode-string-with-shortest-length/)

- 标签：字符串、动态规划
- 难度：困难

## 题目链接

- [0471. 编码最短长度的字符串 - 力扣](https://leetcode.cn/problems/encode-string-with-shortest-length/)

## 题目大意

**描述**：

给定一个字符串 $s$，需要将其编码为最短的字符串。

编码规则：如果子串重复出现 $k$ 次，可以用 `k[substring]` 表示。例如，`"aaaa"` 可以编码为 `"4[a]"`，`"abcabcabc"` 可以编码为 `"3[abc]"`。

编码可以嵌套，例如 `"abababab"` 可以编码为 `"2[2[ab]]"`。

**要求**：

返回编码后长度最短的字符串。

**说明**：

- $1 \le s.length \le 150$。
- $s$ 只包含小写英文字母。

**示例**：

- 示例 1：

```python
输入：s = "aaa"
输出："aaa"
解释：无法编码得更短。
```

- 示例 2：

```python
输入：s = "aaaaa"
输出："5[a]"
```

- 示例 3：

```python
输入：s = "aaaaaaaaaa"
输出："10[a]"
```

## 解题思路

### 思路 1：区间动态规划

给定一个字符串，需要找到编码后长度最短的字符串。编码规则是：如果子串重复出现，可以用 `k[substring]` 表示。

**核心思路**：

- 使用区间 DP，$dp[i][j]$ 表示子串 $s[i:j+1]$ 的最短编码。
- 对于每个子串，尝试：
  1. 不编码，保持原样。
  2. 检查是否由重复子串组成，如果是则编码为 `k[pattern]`。
  3. 分割成两部分，分别编码。

**解题步骤**：

1. 初始化 $dp[i][j] = s[i:j+1]$（不编码）。
2. 枚举子串长度 $length$ 从 1 到 $n$。
3. 对于每个子串 $s[i:j+1]$：
   - 检查是否由重复模式组成：使用 $(s[i:j+1] + s[i:j+1]).find(s[i:j+1], 1)$ 判断。
   - 如果是重复模式，计算编码后的长度。
   - 尝试分割点 $k$，比较 $dp[i][k] + dp[k+1][j]$ 的长度。
4. 返回 $dp[0][n-1]$。

### 思路 1：代码

```python
class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        # dp[i][j] 表示 s[i:j+1] 的最短编码
        dp = [[""] * n for _ in range(n)]
        
        # 枚举子串长度
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                substr = s[i:j+1]
                
                # 初始化为不编码
                dp[i][j] = substr
                
                # 如果长度小于 5，编码后不会更短
                if length < 5:
                    continue
                
                # 检查是否由重复模式组成
                pos = (substr + substr).find(substr, 1)
                if pos < len(substr):
                    # 重复模式的长度
                    pattern_len = pos
                    repeat_count = len(substr) // pattern_len
                    encoded = str(repeat_count) + "[" + dp[i][i + pattern_len - 1] + "]"
                    if len(encoded) < len(dp[i][j]):
                        dp[i][j] = encoded
                
                # 尝试分割
                for k in range(i, j):
                    if len(dp[i][k]) + len(dp[k+1][j]) < len(dp[i][j]):
                        dp[i][j] = dp[i][k] + dp[k+1][j]
        
        return dp[0][n-1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3)$，其中 $n$ 是字符串长度。需要枚举所有子串和分割点。
- **空间复杂度**：$O(n^2)$，存储 DP 数组。
