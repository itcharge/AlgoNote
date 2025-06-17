# [0902. 最大为 N 的数字组合](https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/)

- 标签：数组、数学、字符串、二分查找、动态规划
- 难度：困难

## 题目链接

- [0902. 最大为 N 的数字组合 - 力扣](https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/)

## 题目大意

**描述**：给定一个按非递减序列排列的数字数组 $digits$。我们可以使用任意次数的 $digits[i]$ 来写数字。例如，如果 `digits = ["1", "3", "5"]`，我们可以写数字，如 `"13"`, `"551"`, 和 `"1351315"`。

**要求**：返回可以生成的小于等于给定整数 $n$ 的正整数个数。

**说明**：

- $1 \le digits.length \le 9$。
- $digits[i].length == 1$。
- $digits[i]$ 是从 `'1'` 到 `'9'` 的数。
- $digits$ 中的所有值都不同。
- $digits$ 按非递减顺序排列。
- $1 \le n \le 10^9$。

**示例**：

- 示例 1：

```python
输入：digits = ["1","3","5","7"], n = 100
输出：20
解释：
可写出的 20 个数字是：
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77。
```

- 示例 2：

```python
输入：digits = ["1","4","9"], n = 1000000000
输出：29523
解释：
我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
81 个四位数字，243 个五位数字，729 个六位数字，
2187 个七位数字，6561 个八位数字和 19683 个九位数字。
总共，可以使用D中的数字写出 29523 个整数。
```

## 解题思路

### 思路 1：动态规划 + 数位 DP

数位 DP 模板的应用。因为这道题目中可以使用任意次数的 $digits[i]$，所以不需要用状态压缩的方式来表示数字集合。

这道题的具体步骤如下：

将 $n$ 转换为字符串 $s$，定义递归函数 `def dfs(pos, isLimit, isNum):` 表示构造第 $pos$ 位及之后所有数位的合法方案数。接下来按照如下步骤进行递归。

1. 从 `dfs(0, True, False)` 开始递归。 `dfs(0, True, False)` 表示：
   1. 从位置 $0$ 开始构造。
   2. 开始时受到数字 $n$ 对应最高位数位的约束。
   3. 开始时没有填写数字。
2. 如果遇到  $pos == len(s)$，表示到达数位末尾，此时：
   1. 如果 $isNum == True$，说明当前方案符合要求，则返回方案数 $1$。
   2. 如果 $isNum == False$，说明当前方案不符合要求，则返回方案数 $0$。
3. 如果 $pos \ne len(s)$，则定义方案数 $ans$，令其等于 $0$，即：`ans = 0`。
4. 如果遇到 $isNum == False$，说明之前位数没有填写数字，当前位可以跳过，这种情况下方案数等于 $pos + 1$ 位置上没有受到 $pos$ 位的约束，并且之前没有填写数字时的方案数，即：`ans = dfs(i + 1, False, False)`。
5. 如果 $isNum == True$，则当前位必须填写一个数字。此时：
   1. 根据 $isNum$ 和 $isLimit$ 来决定填当前位数位所能选择的最大数字（$maxX$）。
   2. 然后枚举 $digits$ 数组中所有能够填入的数字 $d$。
   3. 如果 $d$ 超过了所能选择的最大数字 $maxX$ 则直接跳出循环。
   4. 如果 $d$ 是合法数字，则方案数累加上当前位选择 $d$ 之后的方案数，即：`ans += dfs(pos + 1, isLimit and d == maxX, True)`。
      1. `isLimit and d == maxX` 表示 $pos + 1$ 位受到之前位限制和 $pos$ 位限制。
      2. $isNum == True$ 表示 $pos$ 位选择了数字。
6. 最后的方案数为 `dfs(0, True, False)`，将其返回即可。

### 思路 1：代码

```python
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # 将 n 转换为字符串 s
        s = str(n)
        
        @cache
        # pos: 第 pos 个数位
        # isLimit: 表示是否受到选择限制。如果为真，则第 pos 位填入数字最多为 s[pos]；如果为假，则最大可为 9。
        # isNum: 表示 pos 前面的数位是否填了数字。如果为真，则当前位不可跳过；如果为假，则当前位可跳过。
        def dfs(pos, isLimit, isNum):
            if pos == len(s):
                # isNum 为 True，则表示当前方案符合要求
                return int(isNum)
            
            ans = 0
            if not isNum:
                # 如果 isNumb 为 False，则可以跳过当前数位
                ans = dfs(pos + 1, False, False)
            
            # 如果受到选择限制，则最大可选择数字为 s[pos]，否则最大可选择数字为 9。
            maxX = s[pos] if isLimit else '9'
            
            # 枚举可选择的数字
            for d in digits:
                if d > maxX:
                    break
                ans += dfs(pos + 1, isLimit and d == maxX, True)

            return ans
        
        return dfs(0, True, False)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times \log n)$，其中 $m$ 是数组 $digits$ 的长度，$\log n$ 是 $n$ 转为字符串之后的位数长度。
- **空间复杂度**：$O(\log n)$。

