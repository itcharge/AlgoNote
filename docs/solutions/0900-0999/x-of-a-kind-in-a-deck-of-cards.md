# [0914. 卡牌分组](https://leetcode.cn/problems/x-of-a-kind-in-a-deck-of-cards/)

- 标签：数组、哈希表、数学、计数、数论
- 难度：简单

## 题目链接

- [0914. 卡牌分组 - 力扣](https://leetcode.cn/problems/x-of-a-kind-in-a-deck-of-cards/)

## 题目大意

**描述**：

给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 $X$，使我们可以将整副牌按下述规则分成 1 组或更多组：

- 每组都有 $X$ 张牌。
- 组内所有的牌上都写着相同的整数。

**要求**：

仅当你可选的 $X \ge 2$ 时返回 true，否则返回 false。

**说明**：

- $1 \le deck.length \le 10^{4}$。
- $0 \le deck[i] \lt 10^{4}$。

**示例**：

- 示例 1：

```python
输入：deck = [1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
```

- 示例 2：

```python
输入：deck = [1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
```

## 解题思路

### 思路 1：最大公约数

要将卡牌分组，每组有 $X$ 张牌且组内所有牌相同，$X \ge 2$。这等价于找到所有牌的出现次数的最大公约数，且该最大公约数 $\ge 2$。

1. 使用哈希表统计每张牌的出现次数。
2. 计算所有出现次数的最大公约数 $g$。
3. 如果 $g \ge 2$，返回 $True$；否则返回 $False$。

### 思路 1：代码

```python
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from math import gcd
        from functools import reduce
        
        # 统计每张牌的出现次数
        count = collections.Counter(deck)
        
        # 计算所有出现次数的最大公约数
        g = reduce(gcd, count.values())
        
        # 最大公约数至少为 2
        return g >= 2
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + k \log C)$，其中 $n$ 是卡牌数量，$k$ 是不同卡牌的种类数，$C$ 是最大的出现次数。
- **空间复杂度**：$O(k)$，需要存储每张牌的出现次数。
