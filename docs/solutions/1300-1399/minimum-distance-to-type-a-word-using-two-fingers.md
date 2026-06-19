# [1320. 二指输入的的最小距离](https://leetcode.cn/problems/minimum-distance-to-type-a-word-using-two-fingers/)

- 标签：字符串、动态规划
- 难度：困难

## 题目链接

- [1320. 二指输入的的最小距离 - 力扣](https://leetcode.cn/problems/minimum-distance-to-type-a-word-using-two-fingers/)

## 题目大意

**描述**：给定一个字符串 $word$，用两个手指在 $6 \times 5$ 的字母键盘上输入。手指可以从任意位置开始。

**要求**：返回输入 $word$ 所需的最小移动距离之和。从一个键 $(x1,y1)$ 到另一个键 $(x2,y2)$ 的距离为 $|x1-x2| + |y1-y2|$。

**示例**：

- 示例 1：

```python
输入：word = "CAKE"
输出：3
解释： 
使用两根手指输入 "CAKE" 的最佳方案之一是： 
手指 1 在字母 'C' 上 -> 移动距离 = 0 
手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'C' 到字母 'A' 的距离 = 2 
手指 2 在字母 'K' 上 -> 移动距离 = 0 
手指 2 在字母 'E' 上 -> 移动距离 = 从字母 'K' 到字母 'E' 的距离  = 1 
总距离 = 3
```

- 示例 2：

```python
输入：word = "HAPPY"
输出：6
解释： 
使用两根手指输入 "HAPPY" 的最佳方案之一是：
手指 1 在字母 'H' 上 -> 移动距离 = 0
手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'H' 到字母 'A' 的距离 = 2
手指 2 在字母 'P' 上 -> 移动距离 = 0
手指 2 在字母 'P' 上 -> 移动距离 = 从字母 'P' 到字母 'P' 的距离 = 0
手指 1 在字母 'Y' 上 -> 移动距离 = 从字母 'A' 到字母 'Y' 的距离 = 4
总距离 = 6
```


## 解题思路

### 思路 1：动态规划

#### 1. 核心思想

定义 $dp[i][j]$ 表示打完前 $i$ 个字符后，一个手指在 $word[i-1]$ 上，另一个手指在键 $j$ 上的最小总距离。

初始：第一个字符用一根手指打，另一根手指在任意位置（距离为 $0$）。

转移：对于下一个字符 $c$：
- 用当前正在打字的手指：移动距离 $dist(word[i-1], c)$。
- 用空闲的手指：移动距离 $dist(j, c)$，空闲手指变成 $word[i-1]$。

#### 2. 具体步骤

**第 1 步**：将字符映射到键盘坐标。

**第 2 步**：DP 滚动数组优化空间。

### 思路 1：代码

```python
class Solution:
    def minimumDistance(self, word: str) -> int:
        def pos(ch):
            idx = ord(ch) - ord('A')
            return (idx // 6, idx % 6)

        def dist(a, b):
            x1, y1 = pos(a)
            x2, y2 = pos(b)
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)
        INF = 10**9
        # dp[other] 表示一个手指在当前位置，另一个在 other 键
        # 空闲手指可以从任意键开始（代价为 0）
        dp = {chr(ord('A') + i): 0 for i in range(26)}

        for i in range(1, n):
            new_dp = {}
            cur = word[i]
            prev = word[i - 1]
            for other, d in dp.items():
                # 用当前打字的手指
                key1 = other
                new_dp[key1] = min(new_dp.get(key1, INF), d + dist(prev, cur))
                # 用空闲的手指
                key2 = prev
                new_dp[key2] = min(new_dp.get(key2, INF), d + dist(other, cur))
            dp = new_dp

        return min(dp.values())
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n \times 26)$。
- **空间复杂度**：$O(26)$。
