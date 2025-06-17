# [0357. 统计各位数字都不同的数字个数](https://leetcode.cn/problems/count-numbers-with-unique-digits/)

- 标签：数学、动态规划、回溯
- 难度：中等

## 题目链接

- [0357. 统计各位数字都不同的数字个数 - 力扣](https://leetcode.cn/problems/count-numbers-with-unique-digits/)

## 题目大意

**描述**：给定一个整数 $n$。

**要求**：统计并返回区间 $[0, 10^n)$ 上各位数字都不相同的数字 $x$ 的个数。

**说明**：

- $0 \le n \le 8$。
- $0 \le x < 10^n$。

**示例**：

- 示例 1：

```python
输入：n = 2
输出：91
解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。
```

- 示例 2：

```python
输入：n = 0
输出：1
```

## 解题思路

### 思路 1：动态规划 + 数位 DP

题目求解区间 $[0, 10^n)$ 范围内各位数字都不相同的数字个数。则我们先将 $10^n - 1$ 转换为字符串 $s$，定义递归函数 `def dfs(pos, state, isLimit, isNum):` 表示构造第 $pos$ 位及之后所有数位的合法方案数。接下来按照如下步骤进行递归。

1. 从 `dfs(0, 0, True, False)` 开始递归。 `dfs(0, 0, True, False)` 表示：
   1. 从位置 $0$ 开始构造。
   2. 初始没有使用数字（即前一位所选数字集合为 $0$）。
   3. 开始时受到数字 $n$ 对应最高位数位的约束。
   4. 开始时没有填写数字。
2. 如果遇到  $pos == len(s)$，表示到达数位末尾，此时：
   1. 如果 $isNum == True$，说明当前方案符合要求，则返回方案数 $1$。
   2. 如果 $isNum == False$，说明当前方案不符合要求，则返回方案数 $0$。
3. 如果 $pos \ne len(s)$，则定义方案数 $ans$，令其等于 $0$，即：`ans = 0`。
4. 如果遇到 $isNum == False$，说明之前位数没有填写数字，当前位可以跳过，这种情况下方案数等于 $pos + 1$ 位置上没有受到 $pos$ 位的约束，并且之前没有填写数字时的方案数，即：`ans = dfs(i + 1, state, False, False)`。
5. 如果 $isNum == True$，则当前位必须填写一个数字。此时：
   1. 根据 $isNum$ 和 $isLimit$ 来决定填当前位数位所能选择的最小数字（$minX$）和所能选择的最大数字（$maxX$），
   2. 然后根据 $[minX, maxX]$ 来枚举能够填入的数字 $d$。
   3. 如果之前没有选择 $d$，即 $d$ 不在之前选择的数字集合 $state$ 中，则方案数累加上当前位选择 $d$ 之后的方案数，即：`ans += dfs(pos + 1, state | (1 << d), isLimit and d == maxX, True)`。
      1. `state | (1 << d)` 表示之前选择的数字集合 $state$ 加上 $d$。
      2. `isLimit and d == maxX` 表示 $pos + 1$ 位受到之前位限制和 $pos$ 位限制。
      3. $isNum == True$ 表示 $pos$ 位选择了数字。
6. 最后的方案数为 `dfs(0, 0, True, False) + 1`，因为之前计算时没有考虑 $0$，所以最后统计方案数时要加 $1$。

### 思路 1：代码

```python
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        s = str(10 ** n - 1)

        @cache
        # pos: 第 pos 个数位
        # state: 之前选过的数字集合。
        # isLimit: 表示是否受到选择限制。如果为真，则第 pos 位填入数字最多为 s[pos]；如果为假，则最大可为 9。
        # isNum: 表示 pos 前面的数位是否填了数字。如果为真，则当前位不可跳过；如果为假，则当前位可跳过。
        def dfs(pos, state, isLimit, isNum):
            if pos == len(s):
                # isNum 为 True，则表示当前方案符合要求
                return int(isNum)
            
            ans = 0
            if not isNum:
                # 如果 isNumb 为 False，则可以跳过当前数位
                ans = dfs(pos + 1, state, False, False)
            
            # 如果前一位没有填写数字，则最小可选择数字为 0，否则最少为 1（不能含有前导 0）。
            minX = 0 if isNum else 1
            # 如果受到选择限制，则最大可选择数字为 s[pos]，否则最大可选择数字为 9。
            maxX = int(s[pos]) if isLimit else 9
            
            # 枚举可选择的数字
            for d in range(minX, maxX + 1): 
                # d 不在选择的数字集合中，即之前没有选择过 d
                if (state >> d) & 1 == 0:
                    ans += dfs(pos + 1, state | (1 << d), isLimit and d == maxX, True)
            return ans
    
        return dfs(0, 0, True, False) + 1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times 10 \times 2^{10})$。
- **空间复杂度**：$O(n \times 2^{10})$。

