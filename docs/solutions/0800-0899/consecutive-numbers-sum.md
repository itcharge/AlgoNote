# [0829. 连续整数求和](https://leetcode.cn/problems/consecutive-numbers-sum/)

- 标签：数学、枚举
- 难度：困难

## 题目链接

- [0829. 连续整数求和 - 力扣](https://leetcode.cn/problems/consecutive-numbers-sum/)

## 题目大意

**描述**：

给定一个正整数 $n$。

**要求**：

返回连续正整数满足所有数字之和为 $n$ 的组数。

**说明**：

- $1 \le n \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入: n = 5
输出: 2
解释: 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
```

- 示例 2：

```python
输入: n = 9
输出: 3
解释: 9 = 4 + 5 = 2 + 3 + 4
```

## 解题思路

### 思路 1：数学 + 枚举

假设有 $k$ 个连续正整数，首项为 $x$，则它们的和为：

$$x + (x+1) + (x+2) + \cdots + (x+k-1) = k \times x + \frac{k \times (k-1)}{2} = n$$

化简得：

$$x = \frac{n - \frac{k \times (k-1)}{2}}{k}$$

要使 $x$ 为正整数，需要满足：

1. $n - \frac{k \times (k-1)}{2} > 0$，即 $k < \sqrt{2n} + 1$。
2. $n - \frac{k \times (k-1)}{2}$ 能被 $k$ 整除。

算法步骤：

1. 枚举 $k$ 从 1 到 $\sqrt{2n}$。
2. 对于每个 $k$，检查是否满足上述两个条件。
3. 如果满足，计数加 1。

### 思路 1：代码

```python
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        
        # 枚举连续整数的个数 k
        # k 的上界为 sqrt(2n)
        k = 1
        while k * (k - 1) // 2 < n:
            # 检查 n - k*(k-1)/2 是否能被 k 整除
            if (n - k * (k - 1) // 2) % k == 0:
                count += 1
            k += 1
        
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\sqrt{n})$，需要枚举 $k$ 从 1 到 $\sqrt{2n}$。
- **空间复杂度**：$O(1)$，只使用常数额外空间。
