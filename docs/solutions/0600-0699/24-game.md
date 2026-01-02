# [0679. 24 点游戏](https://leetcode.cn/problems/24-game/)

- 标签：数组、数学、回溯
- 难度：困难

## 题目链接

- [0679. 24 点游戏 - 力扣](https://leetcode.cn/problems/24-game/)

## 题目大意

**描述**：

给定一个长度为4的整数数组 $cards$。你有 $4$ 张卡片，每张卡片上都包含一个范围在 $[1,9]$ 的数字。您应该使用运算符 `['+', '-', '*', '/']` 和括号 `'('` 和 `')'` 将这些卡片上的数字排列成数学表达式，以获得值 $24$。

你须遵守以下规则:

- 除法运算符 `/` 表示实数除法，而不是整数除法。
- 例如， `"4 / (1 - 2 / 3)= 4 / (1 / 3) = 12"`。
- 每个运算都在两个数字之间。特别是，不能使用 `-` 作为一元运算符。
- 例如，如果 $cards =[1,1,1,1]$，则表达式 `"-1 -1 -1 -1"` 是 不允许 的。
- 你不能把数字串在一起
- 例如，如果 $cards =[1,2,1,2]$，则表达式 `"12 + 12"` 无效。

**要求**：

如果可以得到这样的表达式，其计算结果为 24，则返回 true ，否则返回 false。

**说明**：

- $cards.length == 4$。
- $1 \le cards[i] \le 9$。

**示例**：

- 示例 1：

```python
输入: cards = [4, 1, 8, 7]
输出: true
解释: (8-4) * (7-1) = 24
```

- 示例 2：

```python
输入: cards = [1, 2, 1, 2]
输出: false
```

## 解题思路

### 思路 1：回溯算法

#### 思路 1：算法描述

这道题目要求判断是否可以通过四则运算和括号将四个数字组合成 $24$。

我们可以使用回溯算法来枚举所有可能的运算顺序和运算符组合。每次从数组中选择两个数字进行运算，将运算结果放回数组，然后递归处理剩余的数字，直到数组中只剩下一个数字，判断是否等于 $24$。

具体步骤如下：

1. 如果数组中只剩下一个数字，判断是否等于 $24$（考虑浮点数误差，判断是否在 $24$ 的附近）。
2. 枚举数组中的任意两个数字 $a$ 和 $b$，以及四种运算符 $+$、$-$、$\times$、$\div$。
3. 计算 $a$ 和 $b$ 的运算结果，将结果放回数组，递归处理剩余的数字。
4. 如果找到一种方案使得最终结果为 $24$，返回 $True$。
5. 回溯，尝试其他的数字组合和运算符。

注意：除法运算需要判断除数是否为 $0$。

#### 思路 1：代码

```python
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        TARGET = 24
        EPSILON = 1e-6  # 浮点数误差范围
        
        def backtrack(nums):
            # 如果只剩下一个数字，判断是否等于 24
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON
            
            # 枚举任意两个数字进行运算
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    
                    a, b = nums[i], nums[j]
                    # 剩余的数字
                    remaining = [nums[k] for k in range(n) if k != i and k != j]
                    
                    # 枚举四种运算符
                    # 加法
                    if backtrack(remaining + [a + b]):
                        return True
                    # 减法
                    if backtrack(remaining + [a - b]):
                        return True
                    # 乘法
                    if backtrack(remaining + [a * b]):
                        return True
                    # 除法（需要判断除数是否为 0）
                    if abs(b) > EPSILON and backtrack(remaining + [a / b]):
                        return True
            
            return False
        
        # 将整数转换为浮点数
        return backtrack([float(card) for card in cards])
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。虽然看起来是指数级别的复杂度，但由于数组长度固定为 $4$，所以时间复杂度是常数级别的。
- **空间复杂度**：$O(1)$。递归调用栈的深度最多为 $4$，空间复杂度是常数级别的。
