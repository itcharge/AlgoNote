# [0473. 火柴拼正方形](https://leetcode.cn/problems/matchsticks-to-square/)

- 标签：位运算、数组、动态规划、回溯、状态压缩
- 难度：中等

## 题目链接

- [0473. 火柴拼正方形 - 力扣](https://leetcode.cn/problems/matchsticks-to-square/)

## 题目大意

**描述**：给定一个表示火柴长度的数组 $matchsticks$，其中 $matchsticks[i]$ 表示第 $i$ 根火柴的长度。

**要求**：找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以将火柴连接起来，并且每根火柴都要用到。如果能拼成正方形，则返回 `True`，否则返回 `False`。

**说明**：

- $1 \le matchsticks.length \le 15$。
- $1 \le matchsticks[i] \le 10^8$。

**示例**：

- 示例 1：

```python
输入: matchsticks = [1,1,2,2,2]
输出: True
解释: 能拼成一个边长为 2 的正方形，每边两根火柴。
```

- 示例 2：

```python
输入: matchsticks = [3,3,3,3,4]
输出: False
解释: 不能用所有火柴拼成一个正方形。
```

## 解题思路

### 思路 1：回溯算法

1. 先排除数组为空和火柴总长度不是 $4$ 的倍数的情况，直接返回 `False`。
2. 然后将火柴按照从大到小排序。用数组 $sums$ 记录四个边长分组情况。
3. 将火柴分为 $4$ 组，把每一根火柴依次向 $4$ 条边上放。
4. 直到放置最后一根，判断能否构成正方形，若能构成正方形，则返回 `True`，否则返回 `False`。

### 思路 1：代码

```python
class Solution:
    def dfs(self, index, sums, matchsticks, size, side_len):
        if index == size:
            return True

        for i in range(4):
            # 如果两条边的情况相等，只需要计算一次，没必要多次重复计算
            if i > 0 and sums[i] == sums[i - 1]:
                continue
            sums[i] += matchsticks[index]
            if sums[i] <= side_len and self.dfs(index + 1, sums, matchsticks, size, side_len):
                return True
            sums[i] -= matchsticks[index]
                
        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        size = len(matchsticks)
        sum_len = sum(matchsticks)
        if sum_len % 4 != 0:
            return False

        side_len = sum_len // 4
        matchsticks.sort(reverse=True)

        sums = [0 for _ in range(4)]
        return self.dfs(0, sums, matchsticks, size, side_len)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(4^n)$。$n$ 是火柴的数目。
- **空间复杂度**：$O(n)$。递归栈的空间复杂度为 $O(n)$。

