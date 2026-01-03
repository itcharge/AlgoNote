# [0728. 自除数](https://leetcode.cn/problems/self-dividing-numbers/)

- 标签：数学
- 难度：简单

## 题目链接

- [0728. 自除数 - 力扣](https://leetcode.cn/problems/self-dividing-numbers/)

## 题目大意

**描述**：

「自除数」是指可以被它包含的每一位数整除的数。

- 例如，$128$ 是一个自除数，因为 $128 \% 1 == 0, 128 \% 2 == 0, 128 \% 8 == 0$。

「自除数」不允许包含 $0$。

给定两个整数 $left$ 和 $right$。

**要求**：

返回一个列表，列表的元素是范围 $[left, right]$（包括两个端点）内所有的自除数。

**说明**：

- $1 \le left \le right \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入：left = 1, right = 22
输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
```

- 示例 2：

```python
输入：left = 47, right = 85
输出：[48,55,66,77]
```

## 解题思路

### 思路 1：模拟

自除数是指可以被它包含的每一位数整除的数。我们可以遍历范围内的每个数字，检查它是否是自除数。

**实现步骤**：

1. 遍历 $[left, right]$ 范围内的每个数字 $num$。
2. 对于每个数字，检查它的每一位数字：
   - 如果某一位是 $0$，则不是自除数。
   - 如果 $num$ 不能被某一位整除，则不是自除数。
3. 如果所有位数字都能整除 $num$，则将其加入结果列表。

### 思路 1：代码

```python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            """判断一个数是否是自除数"""
            temp = num
            while temp > 0:
                digit = temp % 10
                # 如果某一位是 0，或者 num 不能被该位整除
                if digit == 0 or num % digit != 0:
                    return False
                temp //= 10
            return True
        
        result = []
        # 遍历范围内的每个数字
        for num in range(left, right + 1):
            if isSelfDividing(num):
                result.append(num)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O((right - left) \times \log_{10}(right))$，其中 $\log_{10}(right)$ 是数字的位数。
- **空间复杂度**：$O(1)$，不考虑结果数组的空间。
