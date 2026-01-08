# [0869. 重新排序得到 2 的幂](https://leetcode.cn/problems/reordered-power-of-2/)

- 标签：哈希表、数学、计数、枚举、排序
- 难度：中等

## 题目链接

- [0869. 重新排序得到 2 的幂 - 力扣](https://leetcode.cn/problems/reordered-power-of-2/)

## 题目大意

**描述**：

给定正整数 $n$，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

**要求**：

如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

**说明**：

- $1 \le n \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：n = 1
输出：true
```

- 示例 2：

```python
输入：n = 10
输出：false
```

## 解题思路

### 思路 1:计数 + 枚举

判断一个数能否重新排列成 2 的幂,关键在于判断它的数字组成是否与某个 2 的幂相同。

由于 $1 \le n \le 10^9$,所以 2 的幂最多到 $2^{29} = 536870912$。我们可以:

1. 统计 $n$ 中每个数字出现的次数。
2. 枚举所有在范围内的 2 的幂 $2^i$($i = 0, 1, 2, \ldots, 29$)。
3. 统计每个 2 的幂中各数字出现的次数。
4. 如果某个 2 的幂的数字计数与 $n$ 的数字计数完全相同,返回 `True`。

### 思路 1:代码

```python
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 统计 n 中每个数字出现的次数
        def count_digits(num):
            cnt = [0] * 10
            while num > 0:
                cnt[num % 10] += 1
                num //= 10
            return cnt
        
        n_count = count_digits(n)
        
        # 枚举所有可能的 2 的幂(2^0 到 2^29)
        for i in range(30):
            power = 1 << i  # 2^i
            if count_digits(power) == n_count:
                return True
        
        return False
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(\log n + 30 \times \log C)$,其中 $C = 10^9$。统计 $n$ 的数字需要 $O(\log n)$,枚举 30 个 2 的幂并统计数字需要 $O(30 \times \log C)$。
- **空间复杂度**:$O(1)$,只需要常数大小的数组来存储数字计数。
