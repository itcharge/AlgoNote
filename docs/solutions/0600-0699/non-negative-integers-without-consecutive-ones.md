# [0600. 不含连续1的非负整数](https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/)

- 标签：动态规划
- 难度：困难

## 题目链接

- [0600. 不含连续1的非负整数 - 力扣](https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/)

## 题目大意

**描述**：给定一个正整数 $n$。

**要求**：统计在 $[0, n]$ 范围的非负整数中，有多少个整数的二进制表示中不存在连续的 $1$。

**说明**：

- $1 \le n \le 10^9$。

**示例**：

- 示例 1：

```python
输入: n = 5
输出: 5
解释: 
下面列出范围在 [0, 5] 的非负整数与其对应的二进制表示：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数 3 违反规则（有两个连续的 1 ），其他 5 个满足规则。
```

- 示例 2：

```python
输入: n = 1
输出: 2
```

## 解题思路

### 思路 1：动态规划 + 数位 DP

将 $n$ 转换为字符串 $s$，定义递归函数 `def dfs(pos, pre, isLimit):` 表示构造第 $pos$ 位及之后所有数位的合法方案数。其中：

1. $pos$ 表示当前枚举的数位位置。
2. $pre$ 表示前一位是否为 $1$，用于过滤连续 $1$ 的不合法方案。
3. $isLimit$ 表示前一位数位是否等于上界，用于限制本次搜索的数位范围。

接下来按照如下步骤进行递归。

1. 从 `dfs(0, False, True)` 开始递归。 `dfs(0, False, True)` 表示：
   1. 从位置 $0$ 开始构造。
   2. 开始时前一位不为 $1$。
   3. 开始时受到数字 $n$ 对应最高位数位的约束。
2. 如果遇到  $pos == len(s)$，表示到达数位末尾，当前为合法方案，此时：直接返回方案数 $1$。
3. 如果 $pos \ne len(s)$，则定义方案数 $ans$，令其等于 $0$，即：`ans = 0`。
4. 因为不需要考虑前导 $0$，所以当前所能选择的最小数字 $minX$ 为 $0$。
5. 根据 $isLimit$ 来决定填当前位数位所能选择的最大数字（$maxX$）。
6. 然后根据 $[minX, maxX]$ 来枚举能够填入的数字 $d$。
7. 如果前一位为 $1$ 并且当前为 $d$ 也为 $1$，则说明当前方案出现了连续的 $1$，则跳过。
8. 方案数累加上当前位选择 $d$ 之后的方案数，即：`ans += dfs(pos + 1, d == 1, isLimit and d == maxX)`。
   1. `d == 1` 表示下一位 $pos - 1$ 的前一位 $pos$ 是否为 $1$。
   2. `isLimit and d == maxX` 表示 $pos + 1$ 位受到之前位限制和 $pos$ 位限制。
9. 最后的方案数为 `dfs(0, False, True)`，将其返回即可。

### 思路 1：代码

```python
class Solution:
    def findIntegers(self, n: int) -> int:
        # 将 n 的二进制转换为字符串 s
        s = str(bin(n))[2:]
        
        @cache
        # pos: 第 pos 个数位
        # pre: 第 pos - 1 位是否为 1
        # isLimit: 表示是否受到选择限制。如果为真，则第 pos 位填入数字最多为 s[pos]；如果为假，则最大可为 9。
        def dfs(pos, pre, isLimit):
            if pos == len(s):
                return 1
            
            ans = 0
            # 不需要考虑前导 0，则最小可选择数字为 0
            minX = 0
            # 如果受到选择限制，则最大可选择数字为 s[pos]，否则最大可选择数字为 1。
            maxX = int(s[pos]) if isLimit else 1
            
            # 枚举可选择的数字
            for d in range(minX, maxX + 1): 
                if pre and d == 1:
                    continue
                ans += dfs(pos + 1, d == 1, isLimit and d == maxX)

            return ans
    
        return dfs(0, False, True)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。
- **空间复杂度**：$O(\log n)$。
