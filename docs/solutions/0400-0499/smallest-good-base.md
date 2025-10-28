# [0483. 最小好进制](https://leetcode.cn/problems/smallest-good-base/)

- 标签：数学、二分查找
- 难度：困难

## 题目链接

- [0483. 最小好进制 - 力扣](https://leetcode.cn/problems/smallest-good-base/)

## 题目大意

**描述**：

以字符串的形式给出 $n$。

**要求**：

以字符串的形式返回 $n$ 的最小「好进制」。


**说明**：

- 好进制：如果 $n$ 的 $k(k \ge 2)$ 进制数的所有数位全为 $1$，则称 $k(k \ge 2)$ 是 $n$ 的一个「好进制」。
- $n$ 的取值范围是 $[3, 10^{18}]$。
- $n$ 没有前导 $0$。

**示例**：

- 示例 1：

```python
输入：n = "13"
输出："3"
解释：13 的 3 进制是 111。
```

- 示例 2：

```python
输入：n = "4681"
输出："8"
解释：4681 的 8 进制是 11111。
```

## 解题思路

### 思路 1：数学 + 二分查找

**核心思想**：如果 $n$ 的 $k$ 进制表示为全 $1$，那么 $n = k^0 + k^1 + k^2 + ... + k^m$，即 $n = \frac{k^{m+1} - 1}{k - 1}$。我们需要找到最小的 $k$ 使得该等式成立。

**算法步骤**：

1. **枚举进制表示的长度** $m$：取值范围为 $[1, \lfloor \log_2 n \rfloor]$（因为 $k \ge 2$，最多有 $\log_2 n$ 位）。
2. **二分查找进制** $k$：对于每个固定的长度 $m$，二分查找满足条件的进制 $k$。
   - 左边界 $left = 2$（进制至少为 $2$）。
   - 右边界 $right = n - 1$（最大进制值）。
   - 在区间 $[left, right]$ 中二分查找 $k$。
3. **验证等式**：判断 $k$ 是否满足 $n = \frac{k^{m+1} - 1}{k - 1}$。
4. **返回最小 $k$**：找到满足条件的 $k$ 后返回。

**注意**：需要考虑边界情况，如 $n = 1$ 的特殊情况。

### 思路 1：代码

```python
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n_num = int(n)
        
        # 枚举进制表示的长度 m（从大到小，找到的第一个即为最小的 k）
        max_len = len(bin(n_num)) - 2  # n 的二进制表示长度
        for m in range(max_len, 0, -1):
            # 二分查找进制 k
            left, right = 2, n_num - 1
            
            while left <= right:
                k = (left + right) // 2
                # 计算 k^0 + k^1 + ... + k^m 的和
                s = 0
                current = 1  # k^0
                for i in range(m + 1):
                    s += current
                    # 检查是否溢出
                    if s > n_num:
                        break
                    if i < m:
                        current *= k
                        # 提前检查是否会溢出
                        if current > n_num:
                            s = n_num + 1  # 标记溢出
                            break
                    
                if s == n_num:
                    return str(k)
                elif s < n_num:
                    left = k + 1
                else:
                    right = k - 1
        
        # 如果没找到，返回 n - 1（此时 k = n - 1 一定满足条件）
        return str(n_num - 1)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log^3 n)$。其中 $n$ 是给定的数字。外层枚举长度 $m$ 的复杂度为 $O(\log n)$，内层二分查找的复杂度为 $O(\log n)$，每次验证计算等比数列和的复杂度为 $O(m) = O(\log n)$，因此总的时间复杂度为 $O(\log^3 n)$。
- **空间复杂度**：$O(1)$。只使用了常数个额外变量。
