# [0514. 自由之路](https://leetcode.cn/problems/freedom-trail/)

- 标签：深度优先搜索、广度优先搜索、字符串、动态规划
- 难度：困难

## 题目链接

- [0514. 自由之路 - 力扣](https://leetcode.cn/problems/freedom-trail/)

## 题目大意

**描述**：

电子游戏「辐射4」中，任务「通向自由」要求玩家到达名为 `Freedom Trail Ring` 的金属表盘，并使用表盘拼写特定关键词才能开门。

给定一个字符串 $ring$ ，表示刻在外环上的编码；给定另一个字符串 $key$，表示需要拼写的关键词。

**要求**：

算出能够拼写关键词中所有字符的最少步数。

最初，$ring$ 的第一个字符与 12:00 方向对齐。您需要顺时针或逆时针旋转 $ring$ 以使 $key$ 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 $key$ 中的所有字符。

旋转 $ring$ 拼出 $key$ 字符 $key[i]$ 的阶段中：

1. 您可以将 $ring$ 顺时针或逆时针旋转 一个位置 ，计为 1 步。旋转的最终目的是将字符串 $ring$ 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 $key[i]$。
2. 如果字符 $key[i]$ 已经对齐到 12:00 方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 $key$ 的下一个字符（下一阶段），直至完成所有拼写。

**说明**：

- $1 \le ring.length, key.length \le 10^{3}$。
- $ring$ 和 $key$ 只包含小写英文字母。
- 保证字符串 $key$ 一定可以由字符串 $ring$ 旋转拼出。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2018/10/22/ring.jpg)

```python
输入: ring = "godding", key = "gd"
输出: 4
解释:
 对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。 
 对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
 当然, 我们还需要1步进行拼写。
 因此最终的输出是 4。
```

- 示例 2：

```python
输入: ring = "godding", key = "godding"
输出: 13
```

## 解题思路

### 思路 1：动态规划

定义 $dp[i][j]$ 表示拼写完 $key$ 的前 $i$ 个字符，且 $ring$ 的第 $j$ 个字符对齐到 12:00 方向时的最少步数。

状态转移：

- 对于 $key[i]$，需要找到 $ring$ 中所有等于 $key[i]$ 的位置
- 对于每个这样的位置 $k$，可以从上一个状态 $dp[i-1][j]$ 转移过来
- 转移代价 = 旋转步数 + 按下按钮的 1 步
- 旋转步数 = $\min(|k - j|, len(ring) - |k - j|)$（顺时针或逆时针的最小值）

初始状态：$dp[0][j] = \min(j, len(ring) - j) + 1$（从位置 0 旋转到位置 $j$ 并按下按钮）

### 思路 1：代码

```python
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        
        n, m = len(ring), len(key)
        
        # 记录每个字符在 ring 中的所有位置
        pos = defaultdict(list)
        for i, ch in enumerate(ring):
            pos[ch].append(i)
        
        # dp[i][j] 表示拼写完 key 的前 i 个字符，ring 的第 j 个字符对齐时的最少步数
        dp = [[float('inf')] * n for _ in range(m + 1)]
        dp[0][0] = 0
        
        for i in range(m):
            # 对于 key[i]，找到 ring 中所有等于 key[i] 的位置
            for k in pos[key[i]]:
                # 从上一个状态转移
                for j in range(n):
                    if dp[i][j] != float('inf'):
                        # 计算从位置 j 旋转到位置 k 的最少步数
                        dist = min(abs(k - j), n - abs(k - j))
                        dp[i + 1][k] = min(dp[i + 1][k], dp[i][j] + dist + 1)
        
        # 返回拼写完所有字符的最少步数
        return min(dp[m])
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n^2)$，其中 $m$ 是 $key$ 的长度，$n$ 是 $ring$ 的长度。
- **空间复杂度**：$O(m \times n)$，需要存储 DP 数组。
