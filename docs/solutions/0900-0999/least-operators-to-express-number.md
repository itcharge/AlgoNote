# [0964. 表示数字的最少运算符](https://leetcode.cn/problems/least-operators-to-express-number/)

- 标签：记忆化搜索、数学、动态规划
- 难度：困难

## 题目链接

- [0964. 表示数字的最少运算符 - 力扣](https://leetcode.cn/problems/least-operators-to-express-number/)

## 题目大意

**描述**：

给定一个正整数 $x$，我们将会写出一个形如 $x (op1) x (op2) x (op3) x ...$ 的表达式，其中每个运算符 $op1, op2, …$ 可以是加、减、乘、除（`+`，`-`，`*`，或是 `/`）之一。例如，对于 $x = 3$，我们可以写出表达式 $3 * 3 / 3 + 3 - 3$，该式的值为 3。

在写这样的表达式时，我们需要遵守下面的惯例：

- 除运算符（`/`）返回有理数。
- 任何地方都没有括号。
- 我们使用通常的操作顺序：乘法和除法发生在加法和减法之前。
- 不允许使用一元否定运算符（`-`）。例如，$x - x$ 是一个有效的表达式，因为它只使用减法，但是 $-x + x$ 不是，因为它使用了否定运算符。

我们希望编写一个能使表达式等于给定的目标值 $target$ 且运算符最少的表达式。

**要求**：

返回所用运算符的最少数量。

**说明**：

- $2 \le x \le 10^{3}$。
- $1 \le target \le 2 * 10^{8}$。

**示例**：

- 示例 1：

```python
输入：x = 3, target = 19
输出：5
解释：3 * 3 + 3 * 3 + 3 / 3 。表达式包含 5 个运算符。
```

- 示例 2：

```python
输入：x = 5, target = 501
输出：8
解释：5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5 。表达式包含 8 个运算符。
```

## 解题思路

### 思路 1：记忆化搜索 + 动态规划

#### 思路

这道题要求用最少的运算符表示目标数字 $target$。我们可以将 $target$ 看作 $x$ 进制数，每一位可以是 $0$ 到 $x$（允许进位）。

**关键观察**：
- $x^0 = 1$ 需要 $x / x$，即 $2$ 个运算符（一个除号一个乘号，但连接时算作 $2$ 个代价）。
- $x^1 = x$ 不需要运算符（直接使用 $x$，但连接时需要 $1$ 个加号/减号）。
- $x^i$ 需要 $i$ 个运算符（$i - 1$ 个乘号 + $1$ 个加号/减号用于连接）。

**状态定义**：
- 定义 $dp(i, target)$ 表示用 $x^i$ 及更高次幂表示 $target$ 的最少运算符数。
- 对于每个位置 $i$，计算 $target$ 除以 $x$ 的商 $q$ 和余数 $r$：
  - **方案 1**：使用 $r$ 个 $x^i$，然后递归处理 $q$。
  - **方案 2**：使用 $(x - r)$ 个 $-x^i$（相当于凑到下一个 $x^{i+1}$），然后递归处理 $q + 1$。

**代价计算**：
- 预先计算 $cost[i]$，表示使用一个 $x^i$ 需要的运算符数：
  - $cost[0] = 2$（$x / x$ 需要 $2$ 个运算符）
  - $cost[i] = i$（$i \ge 1$ 时，$x^i$ 需要 $i$ 个运算符）

#### 代码

```python
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache
        
        # cost[i] 表示使用一个 x^i 需要的运算符数
        # cost[0] = 2 (x/x)，cost[i] = i (i >= 1)
        cost = [2] + list(range(1, 40))
        
        @lru_cache(None)
        def dp(i, targ):
            """用 x^i 及更高次幂表示 targ 的最少运算符数"""
            # 基本情况
            if targ == 0:
                return 0
            if targ == 1:
                return cost[i]
            if i >= 39:  # 防止溢出
                return float('inf')
            
            # 计算 targ 除以 x 的商和余数
            quotient, remainder = divmod(targ, x)
            
            # 方案 1：使用 remainder 个 x^i，然后处理 quotient
            # 每个 x^i 需要 cost[i] 个运算符
            ans1 = remainder * cost[i] + dp(i + 1, quotient)
            
            # 方案 2：使用 (x - remainder) 个 -x^i，然后处理 quotient + 1
            # 相当于凑到下一个 x^(i+1)
            ans2 = (x - remainder) * cost[i] + dp(i + 1, quotient + 1)
            
            return min(ans1, ans2)
        
        # 从 x^0 开始，最后减 1 是因为最外层不需要加号
        return dp(0, target) - 1
```

#### 复杂度分析

- **时间复杂度**：$O(\log_x target \times \log target)$，递归深度最多为 $O(\log_x target)$，每个状态最多被计算一次。
- **空间复杂度**：$O(\log_x target \times \log target)$，记忆化搜索的缓存空间。
