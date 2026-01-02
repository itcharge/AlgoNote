# [0670. 最大交换](https://leetcode.cn/problems/maximum-swap/)

- 标签：贪心、数学
- 难度：中等

## 题目链接

- [0670. 最大交换 - 力扣](https://leetcode.cn/problems/maximum-swap/)

## 题目大意

**描述**：

给定一个非负整数，你至多可以交换一次数字中的任意两位。

**要求**：

返回你能得到的最大值。

**说明**：

- 给定数字的范围是 $[0, 10^8]$。

**示例**：

- 示例 1：

```python
输入: 2736
输出: 7236
解释: 交换数字2和数字7。
```

- 示例 2：

```python
输入: 9973
输出: 9973
解释: 不需要交换。
```

## 解题思路

### 思路 1：贪心

这道题目要求交换一次数字中的任意两位，使得结果最大。贪心策略是：从高位到低位找到第一个可以被更大数字替换的位置。

1. 将数字转换为字符数组，方便操作。
2. 从右到左记录每个位置右侧的最大数字及其最右位置。
3. 从左到右遍历，找到第一个可以被右侧更大数字替换的位置：
   - 如果当前位置的数字小于右侧的最大数字，交换它们。
   - 为了使结果最大，选择最右侧的最大数字进行交换。
4. 返回交换后的数字。

### 思路 1：代码

```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        # 将数字转换为字符数组
        digits = list(str(num))
        n = len(digits)
        
        # 记录每个位置右侧（包括自己）的最大数字的最右位置
        max_idx = [0] * n
        max_idx[n - 1] = n - 1
        
        for i in range(n - 2, -1, -1):
            if digits[i] > digits[max_idx[i + 1]]:
                max_idx[i] = i
            else:
                max_idx[i] = max_idx[i + 1]
        
        # 从左到右找到第一个可以交换的位置
        for i in range(n):
            # 如果当前位置的数字小于右侧的最大数字
            if digits[i] < digits[max_idx[i]]:
                # 交换
                digits[i], digits[max_idx[i]] = digits[max_idx[i]], digits[i]
                break
        
        return int(''.join(digits))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log num)$，其中 $num$ 是输入的数字。需要遍历数字的每一位。
- **空间复杂度**：$O(\log num)$，需要将数字转换为字符数组。
