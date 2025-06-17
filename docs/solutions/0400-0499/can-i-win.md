# [0464. 我能赢吗](https://leetcode.cn/problems/can-i-win/)

- 标签：位运算、记忆化搜索、数学、动态规划、状态压缩、博弈
- 难度：中等

## 题目链接

- [0464. 我能赢吗 - 力扣](https://leetcode.cn/problems/can-i-win/)

## 题目大意

**描述**：给定两个整数，$maxChoosableInteger$ 表示可以选择的最大整数，$desiredTotal$ 表示累计和。现在开始玩一个游戏，两个玩家轮流从 $1 \sim maxChoosableInteger$ 中不重复的抽取一个整数，直到累积整数和大于等于 $desiredTotal$ 时，这个人就赢得比赛。假设两位玩家玩游戏时都表现最佳。

**要求**：判断先出手的玩家是否能够稳赢，如果能稳赢，则返回 `True`，否则返回 `False`。

**说明**：

- $1 \le maxChoosableInteger \le 20$。
- $0 \le desiredTotal \le 300$。

**示例**：

- 示例 1：

```python
输入：maxChoosableInteger = 10, desiredTotal = 11
输出：False
解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
```

- 示例 2：

```python
输入：maxChoosableInteger = 10, desiredTotal = 0
输出：True
```

## 解题思路

### 思路 1：状态压缩 + 记忆化搜索

$maxChoosableInteger$ 的区间范围是 $[1, 20]$，数据量不是很大，我们可以使用状态压缩来判断当前轮次中数字的选取情况。

题目假设两位玩家玩游戏时都表现最佳，则每个人都会尽力去赢，在每轮次中，每个人都会分析此次选择后，对后续轮次的影响，判断自己是必赢还是必输。

1. 如果当前轮次选择某个数之后，自己一定会赢时，才会选择这个数。
2. 如果当前轮次无论选择哪个数，自己一定会输时，那无论选择哪个数其实都已经无所谓了。

这样我们可以定义一个递归函数 `dfs(state, curTotal)`，用于判断处于状态 $state$，并且当前累计和为 $curTotal$ 时，自己是否一定会赢。如果自己一定会赢，返回 `True`，否则返回 `False`。递归函数内容如下：

1. 从 $1 \sim maxChoosableInteger$ 中选择一个之前没有选过的数 $k$。
2. 如果选择的数 $k$ 加上当前的整数和 $curTotal$ 之后大于等于 $desiredTotal$，则自己一定会赢。
3. 如果选择的数 $k$ 之后，对方必输（即递归调用 `dfs(state | (1 << (k - 1)), curTotal + k)`  为 `Flase` 时），则自己一定会赢。
4. 如果无论选择哪个数，自己都赢不了，则自己必输，返回 `False`。

这样，我们从 $state = 0, curTotal = 0$ 开始调用递归方法 `dfs(state, curTotal)`，即可判断先出手的玩家是否能够稳赢。

接下来，我们还需要考虑一些边界条件。

1. 当 $maxChoosableInteger$ 直接大于等于 $desiredTotal$，则先手玩家无论选什么，直接就赢了，这种情况下，我们直接返回 `True`。
2. 当 $1 \sim maxChoosableInteger$ 中所有数加起来都小于 $desiredTotal$，则先手玩家无论怎么选，都无法稳赢，题目要求我们判断先出手的玩家是否能够稳赢，既然先手无法稳赢，我们直接返回 `False`。

### 思路 1：代码

```python
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def dfs(state, curTotal):
            for k in range(1, maxChoosableInteger + 1):             # 从 1 ~ maxChoosableInteger 中选择一个数
                if state >> (k - 1) & 1 != 0:                       # 如果之前选过该数则跳过
                    continue
                if curTotal + k >= desiredTotal:                    # 如果选择了 k，累积整数和大于等于 desiredTotal，则该玩家一定赢
                    return True
                if not dfs(state | (1 << (k - 1)), curTotal + k):   # 如果当前选择了 k 之后，对手一定输，则当前玩家一定赢
                    return True
            return False                                            # 以上都赢不了的话，当前玩家一定输

        # maxChoosableInteger 直接大于等于 desiredTotal，则先手玩家一定赢
        if maxChoosableInteger >= desiredTotal:
            return True
            
        # 1 ~ maxChoosableInteger 所有数加起来都不够 desiredTotal，则先手玩家一定输
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        return dfs(0, 0)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times 2^n)$，其中 $n$ 为 $maxChoosableInteger$。
- **空间复杂度**：$O(2^n)$。
