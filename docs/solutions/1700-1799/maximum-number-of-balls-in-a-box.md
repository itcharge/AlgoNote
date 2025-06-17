# [1742. 盒子中小球的最大数量](https://leetcode.cn/problems/maximum-number-of-balls-in-a-box/)

- 标签：哈希表、数学、计数
- 难度：简单

## 题目链接

- [1742. 盒子中小球的最大数量 - 力扣](https://leetcode.cn/problems/maximum-number-of-balls-in-a-box/)

## 题目大意

**描述**：给定两个整数 $lowLimit$ 和 $highLimt$，代表 $n$ 个小球的编号（包括 $lowLimit$ 和 $highLimit$，即 $n == highLimit = lowLimit + 1$）。另外有无限个盒子。

现在的工作是将每个小球放入盒子中，其中盒子的编号应当等于小球编号上每位数字的和。例如，编号 $321$ 的小球应当放入编号 $3 + 2 + 1 = 6$ 的盒子，而编号 $10$ 的小球应当放入编号 $1 + 0 = 1$ 的盒子。

**要求**：返回放有最多小球的盒子中的小球数量。如果有多个盒子都满足放有最多小球，只需返回其中任一盒子的小球数量。

**说明**：

- $1 \le lowLimit \le highLimit \le 10^5$。

**示例**：

- 示例 1：

```python
输入：lowLimit = 1, highLimit = 10
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
小球数量：2 1 1 1 1 1 1 1 1 0  0  ...
编号 1 的盒子放有最多小球，小球数量为 2。
```

- 示例 2：

```python
输入：lowLimit = 5, highLimit = 15
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
小球数量：1 1 1 1 2 2 1 1 1 0  0  ...
编号 5 和 6 的盒子放有最多小球，每个盒子中的小球数量都是 2。
```

## 解题思路

### 思路 1：动态规划 + 数位 DP

将 $lowLimit$、$highLimit$ 转为字符串 $s1$、$s2$，并将 $s1$ 补上前导 $0$，令其与 $s2$ 长度一致。定义递归函数 `def dfs(pos, remainTotal, isMaxLimit, isMinLimit):` 表示构造第 $pos$ 位及之后剩余数位和为 $remainTotal$ 的合法方案数。

因为数据范围为 $[1, 10^5]$，对应数位和范围为 $[1, 45]$。因此我们可以枚举所有的数位和，并递归调用 `dfs(i, remainTotal, isMaxLimit, isMinLimit)`，求出不同数位和对应的方案数，并求出最大方案数。

接下来按照如下步骤进行递归。

1. 从 `dfs(0, i, True, True)` 开始递归。 `dfs(0, i, True, True)` 表示：
	1. 从位置 $0$ 开始构造。
	2. 剩余数位和为 $i$。
	3. 开始时当前数位最大值受到最高位数位的约束。
	4. 开始时当前数位最小值受到最高位数位的约束。

2. 如果剩余数位和小于 $0$，说明当前方案不符合要求，则返回方案数 $0$。

3. 如果遇到  $pos == len(s)$，表示到达数位末尾，此时：
	1. 如果剩余数位和 $remainTotal$ 等于 $0$，说明当前方案符合要求，则返回方案数 $1$。
	2. 如果剩余数位和 $remainTotal$ 不等于 $0$，说明当前方案不符合要求，则返回方案数 $0$。

4. 如果 $pos \ne len(s)$，则定义方案数 $ans$，令其等于 $0$，即：`ans = 0`。
5. 如果遇到 $isNum == False$，说明之前位数没有填写数字，当前位可以跳过，这种情况下方案数等于 $pos + 1$ 位置上没有受到 $pos$ 位的约束，并且之前没有填写数字时的方案数，即：`ans = dfs(i + 1, state, False, False)`。
6. 根据 $isMaxLimit$ 和 $isMinLimit$ 来决定填当前位数位所能选择的最小数字（$minX$）和所能选择的最大数字（$maxX$）。

7. 然后根据 $[minX, maxX]$ 来枚举能够填入的数字 $d$。
8. 方案数累加上当前位选择 $d$ 之后的方案数，即：`ans += dfs(pos + 1, remainTotal - d, isMaxLimit and d == maxX, isMinLimit and d == minX)`。
	1. `remainTotal - d` 表示当前剩余数位和减去 $d$。
	2. `isMaxLimit and d == maxX` 表示 $pos + 1$ 位最大值受到之前 $pos$ 位限制。
	3. `isMinLimit and d == maxX` 表示 $pos + 1$ 位最小值受到之前 $pos$ 位限制。
9. 最后返回所有 `dfs(0, i, True, True)` 中最大的方案数即可。

### 思路 1：代码

```python
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        s1, s2 = str(lowLimit), str(highLimit)

        m, n = len(s1), len(s2)
        if m < n:
            s1 = '0' * (n - m) + s1
        
        @cache
        # pos: 第 pos 个数位
        # remainTotal: 表示剩余数位和
        # isMaxLimit: 表示是否受到上限选择限制。如果为真，则第 pos 位填入数字最多为 s2[pos]；如果为假，则最大可为 9。
        # isMinLimit: 表示是否受到下限选择限制。如果为真，则第 pos 位填入数字最小为 s1[pos]；如果为假，则最小可为 0。
        def dfs(pos, remainTotal, isMaxLimit, isMinLimit):
            if remainTotal < 0:
                return 0
            if pos == n:
                # remainTotal 为 0，则表示当前方案符合要求
                return int(remainTotal == 0)
            
            ans = 0
            # 如果前一位没有填写数字，或受到选择限制，则最小可选择数字为 s1[pos]，否则最少为 0（可以含有前导 0）。
            minX = int(s1[pos]) if isMinLimit else 0
            # 如果受到选择限制，则最大可选择数字为 s[pos]，否则最大可选择数字为 9。
            maxX = int(s2[pos]) if isMaxLimit else 9
            
            # 枚举可选择的数字
            for d in range(minX, maxX + 1): 
                ans += dfs(pos + 1, remainTotal - d, isMaxLimit and d == maxX, isMinLimit and d == minX)
            return ans

        ans = 0
        for i in range(46):
            ans = max(ans, dfs(0, i, True, True))
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n \times 45)$。
- **空间复杂度**：$O(\log n)$。
