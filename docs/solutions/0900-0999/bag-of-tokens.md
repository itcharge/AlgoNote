# [0948. 令牌放置](https://leetcode.cn/problems/bag-of-tokens/)

- 标签：贪心、数组、双指针、排序
- 难度：中等

## 题目链接

- [0948. 令牌放置 - 力扣](https://leetcode.cn/problems/bag-of-tokens/)

## 题目大意

**描述**：

你的初始「能量」为 $power$，初始「分数」为 0，只有一包令牌以整数数组 $tokens$ 给出。其中 $tokens[i]$ 是第 $i$ 个令牌的值（下标从 0 开始）。

你的目标是通过有策略地使用这些令牌以「最大化」总「分数」。在一次行动中，你可以用两种方式中的一种来使用一个 未被使用的 令牌（但不是对同一个令牌使用两种方式）：

- 朝上：如果你当前「至少」有 $tokens[i]$ 点 能量 ，可以使用令牌 $i$，失去 $tokens[i]$ 点「能量」，并得到 1 分。
- 朝下：如果你当前至少有 1 分，可以使用令牌 $i$ ，获得 $tokens[i]$ 点「能量」，并失去 1 分。

**要求**：

在使用「任意」数量的令牌后，返回我们可以得到的最大「分数」。

**说明**：

- $0 \le tokens.length \le 10^{3}$。
- $0 \le tokens[i], power \lt 10^{4}$。

**示例**：

- 示例 1：

```python
输入：tokens = [100], power = 50
输出：0
解释：因为你的初始分数为 0，无法使令牌朝下。你也不能使令牌朝上因为你的能量（50）比 tokens[0] 少（100）。
```

- 示例 2：

```python
输入：tokens = [200,100], power = 150
输出：1
解释：使令牌 1 正面朝上，能量变为 50，分数变为 1 。
不必使用令牌 0，因为你无法使用它来提高分数。可得到的最大分数是 1。
```

## 解题思路

### 思路 1：贪心 + 双指针

#### 思路

这道题要求通过使用令牌来最大化分数。我们有两种操作：

- **朝上**：消耗 $tokens[i]$ 点能量，获得 $1$ 分。
- **朝下**：消耗 $1$ 分，获得 $tokens[i]$ 点能量。

贪心策略：

1. **排序**：将令牌按值从小到大排序。
2. **双指针**：使用左右指针分别指向最小和最大的令牌。
3. **策略**：
   - 优先使用能量较少的令牌朝上（左指针），获得分数。
   - 当能量不足时，如果有分数，可以使用能量较大的令牌朝下（右指针），获得能量。
   - 记录过程中的最大分数。

#### 代码

```python
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  # 排序
        left, right = 0, len(tokens) - 1
        score = 0  # 当前分数
        max_score = 0  # 最大分数
        
        while left <= right:
            if power >= tokens[left]:
                # 能量足够，使用最小的令牌朝上
                power -= tokens[left]
                score += 1
                max_score = max(max_score, score)
                left += 1
            elif score > 0:
                # 能量不足但有分数，使用最大的令牌朝下
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                # 能量不足且没有分数，无法继续
                break
        
        return max_score
```

#### 复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是令牌数量。主要时间消耗在排序上。
- **空间复杂度**：$O(1)$，只使用了常数个额外变量（不考虑排序的空间）。
