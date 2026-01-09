# [0943. 最短超级串](https://leetcode.cn/problems/find-the-shortest-superstring/)

- 标签：位运算、数组、字符串、动态规划、状态压缩
- 难度：困难

## 题目链接

- [0943. 最短超级串 - 力扣](https://leetcode.cn/problems/find-the-shortest-superstring/)

## 题目大意

**描述**：

给定一个字符串数组 $words$。

我们可以假设 $words$ 中没有字符串是 $words$ 中另一个字符串的子字符串。

**要求**：

找到以 $words$ 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中「任意一个」即可。

**说明**：

- $1 \le words.length \le 12$。
- $1 \le words[i].length \le 20$。
- $words[i]$ 由小写英文字母组成。
- $words$ 中的所有字符串互不相同。

**示例**：

- 示例 1：

```python
输入：words = ["alex","loves","leetcode"]
输出："alexlovesleetcode"
解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。
```

- 示例 2：

```python
输入：words = ["catg","ctaagt","gcta","ttca","atgcatc"]
输出："gctaagttcatgcatc"
```

## 解题思路

### 思路 1：状态压缩动态规划

#### 思路

这道题要求找到包含所有字符串的最短超级串。这是一个 NP 难问题，但由于字符串数量最多只有 $12$ 个，我们可以使用状态压缩动态规划。

核心思想：

1. **预处理**：计算任意两个字符串的重叠长度 $overlap[i][j]$，表示将字符串 $j$ 接在字符串 $i$ 后面时可以节省的长度。
2. **状态压缩 DP**：
   - 定义 $dp[mask][i]$ 表示已经使用了 $mask$ 中的字符串，且最后一个字符串是 $i$ 时的最短长度。
   - 状态转移：$dp[mask | (1 << j)][j] = \min(dp[mask | (1 << j)][j], dp[mask][i] + len(words[j]) - overlap[i][j])$
3. **路径重建**：记录转移路径，最后重建最短超级串。

#### 代码

```python
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        
        # 计算重叠长度
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    # 计算 words[j] 接在 words[i] 后面的重叠长度
                    max_overlap = min(len(words[i]), len(words[j]))
                    for k in range(max_overlap, 0, -1):
                        if words[i][-k:] == words[j][:k]:
                            overlap[i][j] = k
                            break
        
        # 状态压缩 DP
        # dp[mask][i] 表示使用了 mask 中的字符串，最后一个是 i 时的最短长度
        INF = float('inf')
        dp = [[INF] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        
        # 初始化：只使用一个字符串
        for i in range(n):
            dp[1 << i][i] = len(words[i])
        
        # 状态转移
        for mask in range(1, 1 << n):
            for i in range(n):
                if not (mask & (1 << i)) or dp[mask][i] == INF:
                    continue
                for j in range(n):
                    if mask & (1 << j):
                        continue
                    new_mask = mask | (1 << j)
                    new_len = dp[mask][i] + len(words[j]) - overlap[i][j]
                    if new_len < dp[new_mask][j]:
                        dp[new_mask][j] = new_len
                        parent[new_mask][j] = i
        
        # 找到最短长度和对应的最后一个字符串
        full_mask = (1 << n) - 1
        min_len = INF
        last = -1
        for i in range(n):
            if dp[full_mask][i] < min_len:
                min_len = dp[full_mask][i]
                last = i
        
        # 重建路径
        path = []
        mask = full_mask
        while last != -1:
            path.append(last)
            new_last = parent[mask][last]
            mask ^= (1 << last)
            last = new_last
        path.reverse()
        
        # 构建结果
        result = words[path[0]]
        for i in range(1, len(path)):
            prev = path[i - 1]
            curr = path[i]
            result += words[curr][overlap[prev][curr]:]
        
        return result
```

#### 复杂度分析

- **时间复杂度**：$O(n^2 \times 2^n + n^2 \times L)$，其中 $n$ 是字符串数量，$L$ 是字符串的平均长度。预处理重叠需要 $O(n^2 \times L)$，DP 需要 $O(n^2 \times 2^n)$。
- **空间复杂度**：$O(n \times 2^n)$，需要存储 DP 数组和路径信息。
