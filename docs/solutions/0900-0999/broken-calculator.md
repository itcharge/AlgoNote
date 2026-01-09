# [0991. 坏了的计算器](https://leetcode.cn/problems/broken-calculator/)

- 标签：贪心、数学
- 难度：中等

## 题目链接

- [0991. 坏了的计算器 - 力扣](https://leetcode.cn/problems/broken-calculator/)

## 题目大意

**描述**：

在显示着数字 $startValue$ 的坏计算器上，我们可以执行以下两种操作：

- 双倍（Double）：将显示屏上的数字乘 2；
- 递减（Decrement）：将显示屏上的数字减 1。

给定两个整数 $startValue$ 和 $target$。

**要求**：

返回显示数字 $target$ 所需的最小操作数。

**说明**：

- $1 \le startValue, target \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：startValue = 2, target = 3
输出：2
解释：先进行双倍运算，然后再进行递减运算 {2 -> 4 -> 3}.
```

- 示例 2：

```python
输入：startValue = 5, target = 8
输出：2
解释：先递减，再双倍 {5 -> 4 -> 8}.
```

## 解题思路

### 思路 1：逆向贪心

#### 思路

这道题可以进行两种操作：乘 $2$（Double）和减 $1$（Decrement），要求从 $startValue$ 到 $target$ 的最少操作数。

如果正向思考，每一步有两种选择，会导致搜索空间很大。我们可以 **逆向思考**：

- 从 $target$ 出发，逆向操作回到 $startValue$。
- 逆向操作为：除以 $2$（对应正向的乘 $2$）和加 $1$（对应正向的减 $1$）。

贪心策略：

1. 如果 $target \le startValue$，只能一直减 $1$，操作数为 $startValue - target$。
2. 如果 $target$ 是偶数，除以 $2$ 更优（一次操作减少一半）。
3. 如果 $target$ 是奇数，必须先加 $1$ 变成偶数，然后再除以 $2$。

#### 代码

```python
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        
        # 从 target 逆向到 startValue
        while target > startValue:
            if target % 2 == 0:
                # target 是偶数，除以 2
                target //= 2
            else:
                # target 是奇数，加 1
                target += 1
            count += 1
        
        # 如果 target < startValue，需要减 1 操作
        count += startValue - target
        
        return count
```

#### 复杂度分析

- **时间复杂度**：$O(\log target)$，每次除以 $2$ 会使 $target$ 减半，最多需要 $O(\log target)$ 次操作。
- **空间复杂度**：$O(1)$，只使用了常数个额外变量。
