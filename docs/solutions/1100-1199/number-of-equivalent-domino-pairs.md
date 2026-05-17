# [1128. 等价多米诺骨牌对的数量](https://leetcode.cn/problems/number-of-equivalent-domino-pairs/)

- 标签：数组、哈希表、计数
- 难度：简单

## 题目链接

- [1128. 等价多米诺骨牌对的数量 - 力扣](https://leetcode.cn/problems/number-of-equivalent-domino-pairs/)

## 题目大意

**描述**：给定一组多米诺骨牌 $dominoes$，每张骨牌由两个数字组成，比如 $[a, b]$。两张骨牌 $[a, b]$ 和 $[c, d]$ 等价，当且仅当 $(a == c$ 且 $b == d)$ 或者 $(a == d$ 且 $b == c)$——也就是说，一张骨牌旋转 $180$ 度后能和另一张重合。

**要求**：在 $0 \le i < j < dominoes.length$ 的前提下，找出满足 $dominoes[i]$ 和 $dominoes[j]$ 等价的骨牌对 $(i, j)$ 的数量。

**说明**：

- $1 \le dominoes.length \le 4 \times 10^4$。
- $dominoes[i].length == 2$。
- $1 \le dominoes[i][j] \le 9$。

**示例**：

- 示例 1：

```python
输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1
```

- 示例 2：

```python
输入：dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
输出：3
```

## 解题思路

### 思路 1：哈希表计数

**配对数量怎么算？** 如果某种骨牌出现了 $n$ 次，那么从中选 $2$ 张组成一对，共有 $C_n^2 = \frac{n \times (n-1)}{2}$ 种选法。

**拆解步骤**：

1. 用一个哈希表记录每种标准形式骨牌出现的次数。

2. **遍历每张骨牌**：
   - 把骨牌标准化：`(min(a, b), max(a, b))`
   - 如果这种标准形式之前已经出现过，它就能和之前出现的每一张配成一对，累加之前出现的次数到答案中
   - 更新这种标准形式的出现次数 $+1$

3. **返回累加的总数**。

**为什么要边遍历边累加？** 因为这样不用等全部统计完再算组合数，每遇到一张新骨牌，它和前面所有同类型的骨牌都能配对，累加即可。

### 思路 1：代码

```python
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 哈希表：记录每种标准形式的骨牌出现了几次
        count = {}
        ans = 0

        for a, b in dominoes:
            # 标准化：把两个数字按从小到大排列作为 key
            key = (min(a, b), max(a, b))

            # 如果之前出现过相同形式的骨牌，每张都能和当前这张配对
            if key in count:
                ans += count[key]   # 累加配对数
                count[key] += 1     # 出现次数 +1
            else:
                count[key] = 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。用人话说就是：只需要从头到尾遍历一次骨牌数组，每张骨牌处理时间是常数。
- **空间复杂度**：$O(n)$。哈希表最多存储 $n$ 种不同的标准形式，但题目中骨牌数字只有 $1$ 到 $9$，所以实际上最多 $9 \times 8 / 2 + 9 = 45$ 种，可以认为是 $O(1)$。
