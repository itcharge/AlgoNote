# [0793. 阶乘函数后 K 个零](https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/)

- 标签：数学、二分查找
- 难度：困难

## 题目链接

- [0793. 阶乘函数后 K 个零 - 力扣](https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/)

## 题目大意

**描述**：

$f(x)$ 是 $x!$ 末尾是 $0$ 的数量。回想一下 $x! = 1 \times 2 \times 3 \times ... \times x$，且 $0! = 1$。

- 例如，$f(3) = 0$，因为 $3! = 6$ 的末尾没有 $0$；而 $f(11) = 2$，因为 $11! = 39916800$ 末端有 $2$ 个 $0$。

给定 k。

**要求**：

找出返回能满足 $f(x) = k$ 的非负整数 $x$ 的数量。

**说明**：

- $0 \le k \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：k = 0
输出：5
解释：0!, 1!, 2!, 3!, 和 4! 均符合 k = 0 的条件。
```

- 示例 2：

```python
输入：k = 5
输出：0
解释：没有匹配到这样的 x!，符合 k = 5 的条件。
```

## 解题思路

### 思路 1：二分查找

$n!$ 末尾 $0$ 的个数取决于因子中 $5$ 的个数（因为 $2$ 的个数总是比 $5$ 多）。设 $f(x)$ 表示 $x!$ 末尾 $0$ 的个数，则：

$$f(x) = \lfloor \frac{x}{5} \rfloor + \lfloor \frac{x}{25} \rfloor + \lfloor \frac{x}{125} \rfloor + ...$$

**性质**：

- $f(x)$ 是单调非递减的。
- 对于某个 $k$，要么不存在 $x$ 使得 $f(x) = k$（返回 $0$），要么存在连续的 $5$ 个 $x$ 使得 $f(x) = k$（返回 $5$）。

**原因**：

- 当 $x$ 不是 $5$ 的倍数时，$f(x) = f(x-1)$。
- 当 $x$ 是 $5$ 的倍数但不是 $25$ 的倍数时，$f(x) = f(x-1) + 1$。
- 因此，$f(x)$ 每次增加至少 $1$，且连续 $5$ 个数中至少有一个是 $5$ 的倍数。

### 思路 1：代码

```python
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_zeros(x):
            """计算 x! 末尾 0 的个数"""
            count = 0
            while x > 0:
                x //= 5
                count += x
            return count
        
        def binary_search(k):
            """二分查找最小的 x 使得 f(x) >= k"""
            left, right = 0, 5 * (k + 1)
            while left < right:
                mid = (left + right) // 2
                if count_zeros(mid) < k:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        # 找到最小的 x 使得 f(x) = k
        x = binary_search(k)
        
        # 如果 f(x) = k，则存在 5 个这样的 x
        if count_zeros(x) == k:
            return 5
        else:
            return 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log^2 k)$，二分查找的时间复杂度为 $O(\log k)$，每次计算 $f(x)$ 的时间复杂度为 $O(\log k)$。
- **空间复杂度**：$O(1)$。
