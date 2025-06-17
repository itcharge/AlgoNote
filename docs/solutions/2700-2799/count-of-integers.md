# [2719. 统计整数数目](https://leetcode.cn/problems/count-of-integers/)

- 标签：数学、字符串、动态规划
- 难度：困难

## 题目链接

- [2719. 统计整数数目 - 力扣](https://leetcode.cn/problems/count-of-integers/)

## 题目大意

**描述**：给定两个数字字符串 $num1$ 和 $num2$，以及两个整数 $max\underline{\hspace{0.5em}}sum$ 和 $min\underline{\hspace{0.5em}}sum$。

**要求**：返回好整数的数目。答案可能很大，请返回答案对 $10^9 + 7$ 取余后的结果。

**说明**：

- **好整数**：如果一个整数 $x$ 满足一下条件，我们称它是一个好整数：
  - $num1 \le x \le num2$。
  - $num\underline{\hspace{0.5em}}sum \le digit\underline{\hspace{0.5em}}sum(x) \le max\underline{\hspace{0.5em}}sum$。

- $digit\underline{\hspace{0.5em}}sum(x)$ 表示 $x$ 各位数字之和。
- $1 \le num1 \le num2 \le 10^{22}$。
- $1 \le min\underline{\hspace{0.5em}}sum \le max\underline{\hspace{0.5em}}sum \le 400$。

**示例**：

- 示例 1：

```python
输入：num1 = "1", num2 = "12", min_num = 1, max_num = 8
输出：11
解释：总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11。
```

- 示例 2：

```python
输入：num1 = "1", num2 = "5", min_num = 1, max_num = 5
输出：5
解释：数位和在 1 到 5 之间的 5 个整数分别为 1,2,3,4 和 5 。所以我们返回 5。
```

## 解题思路

### 思路 1：动态规划 + 数位 DP

将 $num1$ 补上前导 $0$，补到和 $num2$ 长度一致，定义递归函数 `def dfs(pos, total, isMaxLimit, isMinLimit):` 表示构造第 $pos$ 位及之后所有数位的合法方案数。接下来按照如下步骤进行递归。

1. 从 `dfs(0, 0, True, True)` 开始递归。 `dfs(0, 0, True, True)` 表示：
	1. 从位置 $0$ 开始构造。
	2. 初始数位和为 $0$。
	3. 开始时当前数位最大值受到最高位数位的约束。
	4. 开始时当前数位最小值受到最高位数位的约束。
2. 如果 $total > max\underline{\hspace{0.5em}}sum$，说明当前方案不符合要求，则返回方案数 $0$。
3. 如果遇到  $pos == len(s)$，表示到达数位末尾，此时：
	1. 如果 $min\underline{\hspace{0.5em}}sum \le total \le max\underline{\hspace{0.5em}}sum$，说明当前方案符合要求，则返回方案数 $1$。
	2. 如果不满足，则当前方案不符合要求，则返回方案数 $0$。
4. 如果 $pos \ne len(s)$，则定义方案数 $ans$，令其等于 $0$，即：`ans = 0`。
5. 根据 $isMaxLimit$ 和 $isMinLimit$ 来决定填当前位数位所能选择的最小数字（$minX$）和所能选择的最大数字（$maxX$）。
6. 然后根据 $[minX, maxX]$ 来枚举能够填入的数字 $d$。
7. 方案数累加上当前位选择 $d$ 之后的方案数，即：`ans += dfs(pos + 1, total + d, isMaxLimit and d == maxX, isMinLimit and d == minX)`。
	1. `total + d` 表示当前数位和 $total$ 加上 $d$。
	2. `isMaxLimit and d == maxX` 表示 $pos + 1$ 位最大值受到之前 $pos$ 位限制。
	3. `isMinLimit and d == maxX` 表示 $pos + 1$ 位最小值受到之前 $pos$ 位限制。
8. 最后的方案数为 `dfs(0, 0, True, True) % MOD`，将其返回即可。

### 思路 1：代码

```python
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 ** 9 + 7
        # 将 num1 补上前导 0，补到和 num2 长度一致
        m, n = len(num1), len(num2)
        if m < n:
            num1 = '0' * (n - m) + num1
        
        @cache
        # pos: 第 pos 个数位
        # total: 表示数位和
        # isMaxLimit: 表示是否受到上限选择限制。如果为真，则第 pos 位填入数字最多为 s[pos]；如果为假，则最大可为 9。
        # isMaxLimit: 表示是否受到下限选择限制。如果为真，则第 pos 位填入数字最小为 s[pos]；如果为假，则最小可为 0。
        def dfs(pos, total, isMaxLimit, isMinLimit):
            if total > max_sum:
                return 0
            
            if pos == n:
                # 当 min_sum <= total <= max_sum 时，当前方案符合要求
                return int(total >= min_sum)
            
            ans = 0
            # 如果受到选择限制，则最小可选择数字为 num1[pos]，否则最大可选择数字为 0。
            minX = int(num1[pos]) if isMinLimit else 0
            # 如果受到选择限制，则最大可选择数字为 num2[pos]，否则最大可选择数字为 9。
            maxX = int(num2[pos]) if isMaxLimit else 9
            
            # 枚举可选择的数字
            for d in range(minX, maxX + 1): 
                ans += dfs(pos + 1, total + d, isMaxLimit and d == maxX, isMinLimit and d == minX)
            return ans % MOD
    
        return dfs(0, 0, True, True) % MOD
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times 10)$，其中 $n$ 为数组 $nums2$ 的长度。
- **空间复杂度**：$O(n \times max\underline{\hspace{0.5em}}sum)$。

