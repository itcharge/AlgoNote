## 1. 数位 DP 简介

### 1.1 数位 DP 简介

> **数位动态规划**：简称为「数位 DP」，是一种与数位相关的一类计数类动态规划问题，即在数位上进行动态规划。这里的数位指的是个位、十位、百位、千位等。

数位 DP 一般用于求解给定区间 $[left, right]$ 中，满足特定条件的数值个数，或者用于求解满足特定条件的第 $k$ 小数。

数位 DP 通常有以下几个特征：

1. 题目会提供一个查询区间（有时也会只提供区间上界）来作为统计限制。
2. 题目中给定区间往往很大（比如 $10^9$），无法采用朴素的方法求解。
3. 题目中给定的给定的限定条件往往与数位有关。
4. 要求统计满足特定条件的数值个数，或者用于求解满足特定条件的第 $k$ 小数。

题目要求一段区间 $[left, right]$ 内满足特定条件的数值个数，如果能找到方法计算出前缀区间 $[0, n]$ 内满足特定条件的数值个数，那么我们就可以利用「前缀和思想」，分别计算出区间 $[0, left - 1]$ 与区间 $[0, right]$ 内满足特定条件的数值个数，然后将两者相减即为所求答案。即：$res[left, right] = res[0, right] - res[0, left - 1]$。

在使用「前缀和思想」思想后，问题转换为计算区间 $[0, n]$ 内满足特定条件的数值个数。

接下来就要用到数位 DP 的基本思想。

> **数位 DP 的基本思想**：将区间数字拆分为数位，然后逐位进行确定。

我们通过将区间上的数字按照数位进行拆分，然后逐位确定每一个数位上的可行方案，从而计算出区间内的可行方案个数。

数位 DP 可以通过「记忆化搜索」的方式实现，也可以通过「迭代递推」的方式实现。因为数位 DP 中需要考虑的参数很多，使用「记忆化搜索」的方式更加方便传入参数，所以这里我们采用「记忆化搜索」的方式来实现。

在使用「记忆化搜索」的时候，需要考虑的参数有：

1. 当前枚举的数位位置（$pos$）。
2. 前一位数位（或前几位数位）的情况，比如前几位的总和（$total$）、某个数字出现次数（$cnt$）、前几位所选数字集合（通常使用「状态压缩」的方式，即用一个二进制整数 $state$ 来表示）等等。
3. 前一位数位（或前几位数位）是否等于上界的前几位数字（$isLimit$），用于限制本次搜索的数位范围。
4. 前一位数位是否填了数字（$isNum$），如果前一位数位填了数字，则当前位可以从 $0$ 开始填写数字；如果前一位没有填写数字，则当前位可以跳过，或者从 $1$ 开始填写数字。
5. 当前位数位所能选择的最小数字（$minX$）和所能选择的最大数字（$maxX$）。

对应代码如下：

```python
class Solution:
    def digitDP(self, n: int) -> int:
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
                # 如果 isNumb 为 False，则可以跳过当前数位
                ans = dfs(pos + 1, state, False, False)
            
            # 如果前一位没有填写数字，则最小可选择数字为 0，否则最少为 1（不能含有前导 0）。
            minX = 0 if isNum else 1
            # 如果受到选择限制，则最大可选择数字为 s[pos]，否则最大可选择数字为 9。
            maxX = int(s[pos]) if isLimit else 9
            
            # 枚举可选择的数字
            for x in range(minX, maxX + 1): 
                # x 不在选择的数字集合中，即之前没有选择过 x
                if (state >> x) & 1 == 0:
                    ans += dfs(pos + 1, state | (1 << x), isLimit and x == maxX, True)
            return ans
    
        return dfs(0, 0, True, False)
```

接下来，我们通过一道简单的例题来具体了解一下数位 DP 以及解题思路。

### 1.2 统计特殊整数

#### 1.2.1 题目大意

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

#### 1.2.2 解题思路

##### 思路 1：动态规划 + 数位 DP

将 $n$ 转换为字符串 $s$，定义递归函数 `def dfs(pos, state, isLimit, isNum):` 表示构造第 $pos$ 位及之后所有数位的合法方案数。接下来按照如下步骤进行递归。

1. 从 `dfs(0, 0, True, False)` 开始递归。 `dfs(0, 0, True, False)` 表示：
	1. 从位置 $0$ 开始构造。
	2. 初始没有使用数字（即前一位所选数字集合为 $0$）。
	3. 开始时受到数字 $n$ 对应最高位数位的约束。
	4. 开始时没有填写数字。
2. 如果遇到  $pos == len(s)$，表示到达数位末尾，此时：
	1. 如果 $isNum == True$，说明当前方案符合要求，则返回方案数 $1$。
	2. 如果 $isNum == False$，说明当前方案不符合要求，则返回方案数 $0$。
3. 如果 $pos \ne len(s)$，则定义方案数 $ans$，令其等于 $0$，即：$ans = 0$。
4. 如果遇到 $isNum == False$，说明之前位数没有填写数字，当前位可以跳过，这种情况下方案数等于 $pos + 1$ 位置上没有受到 $pos$ 位的约束，并且之前没有填写数字时的方案数，即：`ans = dfs(i + 1, state, False, False)`。
5. 如果 $isNum == True$，则当前位必须填写一个数字。此时：
	1. 根据 $isNum$ 和 $isLimit$ 来决定填当前位数位所能选择的最小数字（$minX$）和所能选择的最大数字（$maxX$），
	2. 然后根据 $[minX, maxX]$ 来枚举能够填入的数字 $x$。
	3. 如果之前没有选择 $x$，即 $x$ 不在之前选择的数字集合 $state$ 中，则方案数累加上当前位选择 $x$ 之后的方案数，即：`ans += dfs(pos + 1, state | (1 << x), isLimit and x == maxX, True)`。
		1. `state | (1 << x)` 表示之前选择的数字集合 $state$ 加上 $x$。
		2. `isLimit and x == maxX` 表示 $pos + 1$ 位受到之前位限制和 $pos$ 位限制。
		3. $isNum == True$ 表示 $pos$ 位选择了数字。

##### 思路 1：代码

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
                # 如果 isNumb 为 False，则可以跳过当前数位
                ans = dfs(pos + 1, state, False, False)
            
            # 如果前一位没有填写数字，则最小可选择数字为 0，否则最少为 1（不能含有前导 0）。
            minX = 0 if isNum else 1
            # 如果受到选择限制，则最大可选择数字为 s[pos]，否则最大可选择数字为 9。
            maxX = int(s[pos]) if isLimit else 9
            
            # 枚举可选择的数字
            for x in range(minX, maxX + 1): 
                # x 不在选择的数字集合中，即之前没有选择过 x
                if (state >> x) & 1 == 0:
                    ans += dfs(pos + 1, state | (1 << x), isLimit and x == maxX, True)
            return ans
    
        return dfs(0, 0, True, False)
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n \times 10 \times 2^{10})$，其中 $n$ 为给定整数。
- **空间复杂度**：$O(\log n \times 2^{10})$。

## 2. 数位 DP 的应用

### 2.1 至少有 1 位重复的数字

#### 2.1.1 题目链接

- [1012. 至少有 1 位重复的数字 - 力扣](https://leetcode.cn/problems/numbers-with-repeated-digits/)

#### 2.1.2 题目大意

**描述**：给定一个正整数 $n$。

**要求**：返回在 $[1, n]$ 范围内具有至少 $1$ 位重复数字的正整数的个数。

**说明**：

- $1 \le n \le 10^9$。

**示例**：

- 示例 1：

```python
输入：n = 20
输出：1
解释：具有至少 1 位重复数字的正数（<= 20）只有 11。
```

- 示例 2：

```python
输入：n = 100
输出：10
解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100。
```

#### 2.1.3 解题思路

##### 思路 1：动态规划 + 数位 DP

正向求解在 $[1, n]$ 范围内具有至少 $1$ 位重复数字的正整数的个数不太容易，我们可以反向思考，先求解出在 $[1, n]$ 范围内各位数字都不重复的正整数的个数 $ans$，然后 $n - ans$ 就是题目答案。

将 $n$ 转换为字符串 $s$，定义递归函数 `def dfs(pos, state, isLimit, isNum):` 表示构造第 $pos$ 位及之后所有数位的合法方案数。接下来按照如下步骤进行递归。

1. 从 `dfs(0, 0, True, False)` 开始递归。 `dfs(0, 0, True, False)` 表示：
   1. 从位置 $0$ 开始构造。
   2. 初始没有使用数字（即前一位所选数字集合为 $0$）。
   3. 开始时受到数字 $n$ 对应最高位数位的约束。
   4. 开始时没有填写数字。
2. 如果遇到  $pos == len(s)$，表示到达数位末尾，此时：
   1. 如果 $isNum == True$，说明当前方案符合要求，则返回方案数 $1$。
   2. 如果 $isNum == False$，说明当前方案不符合要求，则返回方案数 $0$。
3. 如果 $pos \ne len(s)$，则定义方案数 $ans$，令其等于 $0$，即：$ans = 0$。
4. 如果遇到 $isNum == False$，说明之前位数没有填写数字，当前位可以跳过，这种情况下方案数等于 $pos + 1$ 位置上没有受到 $pos$ 位的约束，并且之前没有填写数字时的方案数，即：`ans = dfs(i + 1, state, False, False)`。
5. 如果 $isNum == True$，则当前位必须填写一个数字。此时：
   1. 根据 $isNum$ 和 $isLimit$ 来决定填当前位数位所能选择的最小数字（$minX$）和所能选择的最大数字（$maxX$），
   2. 然后根据 $[minX, maxX]$ 来枚举能够填入的数字 $d$。
   3. 如果之前没有选择 $d$，即 $d$ 不在之前选择的数字集合 $state$ 中，则方案数累加上当前位选择 $d$ 之后的方案数，即：`ans += dfs(pos + 1, state | (1 << d), isLimit and d == maxX, True)`。
      1. `state | (1 << d)` 表示之前选择的数字集合 $state$ 加上 $d$。
      2. `isLimit and d == maxX` 表示 $pos + 1$ 位受到之前位限制和 $pos$ 位限制。
      3. $isNum == True$ 表示 $pos$ 位选择了数字。
6. 最后的方案数为 `n - dfs(0, 0, True, False)`，将其返回即可。

##### 思路 1：代码

```python
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
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
    
        return n - dfs(0, 0, True, False)
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n \times 10 \times 2^{10})$。
- **空间复杂度**：$O(\log n \times 2^{10})$。

### 2.2 数字 1 的个数

#### 2.2.1 题目链接

- [233. 数字 1 的个数 - 力扣](https://leetcode.cn/problems/number-of-digit-one/)

#### 2.2.2 题目大意

**描述**：给定一个整数 $n$。

**要求**：计算所有小于等于 $n$ 的非负整数中数字 $1$ 出现的个数。

**说明**：

- $0 \le n \le 10^9$。

**示例**：

- 示例 1：

```python
输入：n = 13
输出：6
```

- 示例 2：

```python
输入：n = 0
输出：0
```

#### 2.2.3 解题思路

##### 思路 1：动态规划 + 数位 DP

将 $n$ 转换为字符串 $s$，定义递归函数 `def dfs(pos, cnt, isLimit):` 表示构造第 $pos$ 位及之后所有数位中数字 $1$ 出现的个数。接下来按照如下步骤进行递归。

1. 从 `dfs(0, 0, True)` 开始递归。 `dfs(0, 0, True)` 表示：
   1. 从位置 $0$ 开始构造。
   2. 初始数字 $1$ 出现的个数为 $0$。
   3. 开始时受到数字 $n$ 对应最高位数位的约束。
2. 如果遇到  $pos == len(s)$，表示到达数位末尾，此时：返回数字 $1$ 出现的个数 $cnt$。
3. 如果 $pos \ne len(s)$，则定义方案数 $ans$，令其等于 $0$，即：$ans = 0$。
4. 如果遇到 $isNum == False$，说明之前位数没有填写数字，当前位可以跳过，这种情况下方案数等于 $pos + 1$ 位置上没有受到 $pos$ 位的约束，并且之前没有填写数字时的方案数，即：`ans = dfs(i + 1, state, False, False)`。
5. 如果 $isNum == True$，则当前位必须填写一个数字。此时：
   1. 因为不需要考虑前导 $0$ 所以当前位数位所能选择的最小数字（$minX$）为 $0$。
   2. 根据 $isLimit$ 来决定填当前位数位所能选择的最大数字（$maxX$）。
   3. 然后根据 $[minX, maxX]$ 来枚举能够填入的数字 $d$。
   4. 方案数累加上当前位选择 $d$ 之后的方案数，即：`ans += dfs(pos + 1, cnt + (d == 1), isLimit and d == maxX)`。
      1. `cnt + (d == 1)` 表示之前数字 $1$ 出现的个数加上当前位为数字 $1$ 的个数。
      2. `isLimit and d == maxX` 表示 $pos + 1$ 位受到之前位 $pos$ 位限制。
6. 最后的方案数为 `dfs(0, 0, True)`，将其返回即可。

##### 思路 1：代码

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        # 将 n 转换为字符串 s
        s = str(n)
        
        @cache
        # pos: 第 pos 个数位
        # cnt: 之前数字 1 出现的个数。
        # isLimit: 表示是否受到选择限制。如果为真，则第 pos 位填入数字最多为 s[pos]；如果为假，则最大可为 9。
        def dfs(pos, cnt, isLimit):
            if pos == len(s):
                return cnt
            
            ans = 0            
            # 不需要考虑前导 0，则最小可选择数字为 0
            minX = 0
            # 如果受到选择限制，则最大可选择数字为 s[pos]，否则最大可选择数字为 9。
            maxX = int(s[pos]) if isLimit else 9
            
            # 枚举可选择的数字
            for d in range(minX, maxX + 1): 
                ans += dfs(pos + 1, cnt + (d == 1), isLimit and d == maxX)
            return ans
    
        return dfs(0, 0, True)
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。
- **空间复杂度**：$O(\log n)$。

## 练习题目

- [0357. 统计各位数字都不同的数字个数](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0300-0399/count-numbers-with-unique-digits.md)
- [0788. 旋转数字](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/rotated-digits.md)
- [2719. 统计整数数目](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/2700-2799/count-of-integers.md)

- [数位 DP 题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E6%95%B0%E4%BD%8D-dp-%E9%A2%98%E7%9B%AE)

## 参考资料

- 【文章】[AcWing 1081. 度的数量【数位DP基本概念+数位DP记忆化搜索】](https://www.acwing.com/solution/content/66855/)
- 【视频】[数位 DP 通用模板【力扣周赛 306】LeetCode - 灵茶山艾府](https://www.bilibili.com/video/BV1rS4y1s721/)