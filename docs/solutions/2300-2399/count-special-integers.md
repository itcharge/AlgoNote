# [2376. 统计特殊整数](https://leetcode.cn/problems/count-special-integers/)

- 标签：数学、动态规划
- 难度：困难

## 题目链接

- [2376. 统计特殊整数 - 力扣](https://leetcode.cn/problems/count-special-integers/)

## 题目大意

**描述**：给定一个正整数 $n$。

**要求**：求区间 $[1, n]$ 内的所有整数中，特殊整数的数目。

**说明**：

- **特殊整数**：如果一个正整数的每一个数位都是互不相同的，则称它是特殊整数。
- $1 \le n \le 2 \times 10^9$。

**示例**：

- 示例 1：

```python
输入：n = 20
输出：19
解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。
```

- 示例 2：

```python
输入：n = 5
输出：5
解释：1 到 5 所有整数都是特殊整数。
```

## 解题思路

### 思路 1：动态规划 + 数位 DP

将 $n$ 转换为字符串 $s$，定义递归函数 `def dfs(pos, state, isLimit, isNum):` 表示构造第 $pos$ 位及之后所有数位的合法方案数。接下来按照如下步骤进行递归。

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
            2. `isLimit and d == maxX` 表示 $pos + 1$ 位受到之前 $pos$ 位限制。
            3. $isNum == True$ 表示 $pos$ 位选择了数字。

6. 最后的方案数为 `dfs(0, 0, True, False)`，将其返回即可。

### 思路 1：代码

```python
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # 将 n 转换为字符串 s
        s = str(n)
        
        @cache
        # pos: 第 pos 个数位
        # state: 之前选过的数字集合。
        # isLimit: 表示是否受到选择限制。如果为真，则第 pos 位填入数字最多为 s[pos]；如果为假，则最大可为 9。
        # isNum: 表示 pos 前面的数位是否填了数字。
        # 如果为真，则当前位不可跳过；如果为假，则当前位可跳过。
        def dfs(pos, state, isLimit, isNum):
            if pos == len(s):
                # isNum 为 True，则表示当前方案符合要求
                return int(isNum)
            
            ans = 0
            if not isNum:
                # 如果 isNum 为 False，则可以跳过当前数位
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
    
        return dfs(0, 0, True, False)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n \times 10 \times 2^{10})$，其中 $n$ 为给定整数。
- **空间复杂度**：$O(\log n \times 2^{10})$。
