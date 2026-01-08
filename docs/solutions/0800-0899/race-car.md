# [0818. 赛车](https://leetcode.cn/problems/race-car/)

- 标签：动态规划
- 难度：困难

## 题目链接

- [0818. 赛车 - 力扣](https://leetcode.cn/problems/race-car/)

## 题目大意

**描述**：

你的赛车可以从位置 0 开始，并且速度为 +1，在一条无限长的数轴上行驶。赛车也可以向负方向行驶。赛车可以按照由加速指令 `'A'` 和倒车指令 `'R'` 组成的指令序列自动行驶。

- 当收到指令 `'A'` 时，赛车这样行驶：
- $position += speed$
- $speed *= 2$
- 当收到指令 `'R'` 时，赛车这样行驶：
- 如果速度为正数，那么 $speed = -1$
- 否则 $speed = 1$

当前所处位置不变。

例如，在执行指令 `"AAR"` 后，赛车位置变化为 $0 \rightarrow 1 \rightarrow 3 \rightarrow 3$，速度变化为 $1 \rightarrow 2 \rightarrow 4 \rightarrow -1$。

给定一个目标位置 $target$。

**要求**：

返回能到达目标位置的最短指令序列的长度。

**说明**：

- $1 \le target \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入：target = 3
输出：2
解释：
最短指令序列是 "AA" 。
位置变化 0 --> 1 --> 3 。
```

- 示例 2：

```python
输入：target = 6
输出：5
解释：
最短指令序列是 "AAARA" 。
位置变化 0 --> 1 --> 3 --> 7 --> 7 --> 6 。
```

## 解题思路

### 思路 1:动态规划

定义 $dp[i]$ 表示到达位置 $i$ 所需的最少指令数。

对于位置 $target$,有两种策略:

1. **直接到达或超过**:连续执行 $n$ 次 `A`,可以到达位置 $2^n - 1$。
   - 如果 $2^n - 1 = target$,则 $dp[target] = n$
   - 如果 $2^n - 1 > target$,需要先到达 $2^n - 1$,然后倒车回到 $target$

2. **先前进再倒车**:先执行 $n$ 次 `A` 到达 $2^n - 1$,然后执行 `R` 倒车,再执行 $m$ 次 `A` 后退 $2^m - 1$,最后再执行 `R` 前进,到达剩余距离。
   - 总指令数为:$n + 1 + m + 1 + dp[2^n - 1 - (2^m - 1) - target]$

### 思路 1:代码

```python
class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        
        for i in range(1, target + 1):
            # 找到最小的 n,使得 2^n - 1 >= i
            n = i.bit_length()
            
            # 情况 1:恰好到达
            if (1 << n) - 1 == i:
                dp[i] = n
                continue
            
            # 情况 2:超过后倒车回来
            # 先走 n 步到达 2^n - 1,然后倒车,再走到 i
            dp[i] = n + 1 + dp[(1 << n) - 1 - i]
            
            # 情况 3:先走 n-1 步,然后倒车,再前进
            # 枚举倒车时前进的步数 m
            for m in range(n - 1):
                # 先走 n-1 步到达 2^(n-1) - 1
                # 倒车(R)
                # 前进 m 步到达 2^(n-1) - 1 - (2^m - 1)
                # 再倒车(R)
                # 继续前进到 i
                pos = (1 << (n - 1)) - 1 - ((1 << m) - 1)
                dp[i] = min(dp[i], (n - 1) + 1 + m + 1 + dp[i - pos])
        
        return dp[target]
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(target \log target)$,对于每个位置,需要枚举 $O(\log target)$ 种倒车策略。
- **空间复杂度**:$O(target)$,需要存储 $dp$ 数组。
