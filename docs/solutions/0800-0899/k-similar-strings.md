# [0854. 相似度为 K 的字符串](https://leetcode.cn/problems/k-similar-strings/)

- 标签：广度优先搜索、哈希表、字符串
- 难度：困难

## 题目链接

- [0854. 相似度为 K 的字符串 - 力扣](https://leetcode.cn/problems/k-similar-strings/)

## 题目大意

**描述**：

对于某些非负整数 $k$，如果交换 $s1$ 中两个字母的位置恰好 $k$ 次，能够使结果字符串等于 $s2$ ，则认为字符串 $s1$ 和 $s2$ 的 相似度为 $k$ 。

给你两个字母异位词 $s1$ 和 $s2$。

**要求**：

返回 $s1$ 和 $s2$ 的相似度 $k$ 的最小值。

**说明**：

- $1 \le s1.length \le 20$。
- $s2.length == s1.length$。
- $s1$ 和 $s2$ 只包含集合 `{'a', 'b', 'c', 'd', 'e', 'f'}` 中的小写字母。
- $s2$ 是 $s1$ 的一个字母异位词。

**示例**：

- 示例 1：

```python
输入：s1 = "ab", s2 = "ba"
输出：1
```

- 示例 2：

```python
输入：s1 = "abc", s2 = "bca"
输出：2
```

## 解题思路

### 思路 1：BFS（广度优先搜索）

这道题要求计算将字符串 $s1$ 通过最少的交换次数变成 $s2$。这是一个典型的 BFS 最短路径问题。

算法步骤：

1. 使用 BFS 从 $s1$ 开始搜索，每次尝试交换两个字符。
2. 使用哈希集合记录已访问的字符串，避免重复搜索。
3. 优化：只交换能让字符串更接近 $s2$ 的位置，即只交换那些当前位置字符与 $s2$ 不匹配的位置。
4. 当搜索到 $s2$ 时，返回交换次数。

具体优化：

- 对于当前字符串，找到第一个与 $s2$ 不匹配的位置 $i$。
- 尝试将位置 $i$ 与后面所有位置 $j$ 交换，其中 $s[j] == s2[i]$ 且 $s[i] \ne s2[j]$（避免无效交换）。

### 思路 1：代码

```python
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        from collections import deque
        
        if s1 == s2:
            return 0
        
        # BFS
        queue = deque([(s1, 0)])  # (当前字符串, 交换次数)
        visited = {s1}
        
        while queue:
            curr, swaps = queue.popleft()
            
            # 找到第一个与 s2 不匹配的位置
            i = 0
            while i < len(curr) and curr[i] == s2[i]:
                i += 1
            
            # 尝试交换位置 i 与后面的位置
            for j in range(i + 1, len(curr)):
                # 只交换能让位置 i 匹配的字符
                if curr[j] == s2[i]:
                    # 交换位置 i 和 j
                    next_str = list(curr)
                    next_str[i], next_str[j] = next_str[j], next_str[i]
                    next_str = ''.join(next_str)
                    
                    # 如果到达目标字符串
                    if next_str == s2:
                        return swaps + 1
                    
                    # 如果未访问过，加入队列
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append((next_str, swaps + 1))
        
        return -1  # 理论上不会到达这里
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2 \times n!)$，其中 $n$ 是字符串的长度。最坏情况下需要遍历所有可能的字符串排列，但实际上由于剪枝和字符集较小，运行时间会快很多。
- **空间复杂度**：$O(n!)$，需要存储访问过的字符串。
