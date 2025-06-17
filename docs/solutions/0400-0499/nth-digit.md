# [0400. 第 N 位数字](https://leetcode.cn/problems/nth-digit/)

- 标签：数学、二分查找
- 难度：中等

## 题目链接

- [0400. 第 N 位数字 - 力扣](https://leetcode.cn/problems/nth-digit/)

## 题目大意

**描述**：给你一个整数 $n$。

**要求**：在无限的整数序列 $[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]$ 中找出并返回第 $n$ 位上的数字。

**说明**：

- $1 \le n \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：n = 3
输出：3
```

- 示例 2：

```python
输入：n = 11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
```

## 解题思路

### 思路 1：找规律

数字以 $0123456789101112131415…$ 的格式序列化到一个字符序列中。在这个序列中，第 $5$ 位（从下标 $0$ 开始计数）是 $5$，第 $13$ 位是 $1$，第 $19$ 位是 $4$，等等。

根据题意中的字符串，找数学规律：

- $1$ 位数字有 $9$ 个，共 $9$ 位：$123456789$。
- $2$ 位数字有 $90$ 个，共 $2 \times 90$ 位：$10111213...9899$。
- $3$ 位数字有 $900$ 个，共 $3 \times 900$ 位：$100...999$。
- $4$ 位数字有 $9000$ 个，共 $4 \times 9000$ 位： $1000...9999$。
- $……$

则我们可以按照以下步骤解决这道题：

1. 我们可以先找到第 $n$ 位所在整数 $number$ 所对应的位数 $digit$。
2. 同时找到该位数 $digit$ 的起始整数 $start$。
3. 再计算出 $n$ 所在整数 $number$。$number$ 等于从起始数字 $start$ 开始的第 $\lfloor \frac{n - 1}{digit} \rfloor$ 个数字。即 `number = start + (n - 1) // digit`。
4. 然后确定 $n$ 对应的是数字 $number$ 中的哪一位。即 $digit\underline{\hspace{0.5em}}idx = (n - 1) \mod digit$。
5. 最后返回结果。

### 思路 1：代码

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        start = 1
        base = 9
        while n > base:
            n -= base
            digit += 1
            start *= 10
            base = start * digit * 9

        number = start + (n - 1) // digit
        digit_idx = (n - 1) % digit
        return int(str(number)[digit_idx])
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。
- **空间复杂度**：$O(1)$。

### 思路 2：二分查找

假设第 $n$ 位数字所在的整数是 $digit$ 位数，我们可以定义一个方法 $totalDigits(x)$ 用于计算所有位数不超过 $x$ 的整数的所有位数和。

根据题意我们可知，所有位数不超过 $digit - 1$ 的整数的所有位数和一定小于 $n$，并且所有不超过 $digit$ 的整数的所有位数和一定大于等于 $n$。

因为所有位数不超过 $x$ 的整数的所有位数和 $totalDigits(x)$  是关于 $x$ 单调递增的，所以我们可以使用二分查找的方式，确定第 $n$ 位数字所在的整数的位数 $digit$。

$n$ 的最大值为 $2^{31} - 1$，约为 $2 \times 10^9$。而 $9$ 位数字有 $9 \times 10^8$ 个，共 $9 \times 9 \times 10^8 = 8.1 \times 10^9 > 2 \times 10 ^ 9$，所以第 $n$ 位所在整数的位数 $digit$ 最多为 $9$ 位，最小为 $1$ 位。即 $digit$ 的取值范围为 $[1, 9]$。

我们使用二分查找算法得到 $digit$ 之后，还可以计算出不超过 $digit - 1$ 的整数的所有位数和 $pre\underline{\hspace{0.5em}}digits = totalDigits(digit - 1)$，则第 $n$ 位数字所在整数在所有 $digit$ 位数中的下标是 $idx = n - pre\underline{\hspace{0.5em}}digits - 1$。

得到下标 $idx$ 后，可以计算出 $n$ 所在整数 $number$。$number$ 等于从起始数字 $10^{digit - 1}$ 开始的第 $\lfloor \frac{idx}{digit} \rfloor$ 个数字。即 `number = 10 ** (digit - 1) + idx // digit`。

该整数 $number$ 中第 $idx \mod digit$ 即为第 $n$ 位上的数字，将其作为答案返回即可。

### 思路 2：代码

```python
class Solution:
    def totalDigits(self, x):
        digits = 0
        digit, cnt = 1, 9
        while digit <= x:
            digits += digit * cnt
            digit += 1
            cnt *= 10
        return digits

    def findNthDigit(self, n: int) -> int:
        left, right = 1, 9
        while left < right:
            mid = left + (right - left) // 2
            if self.totalDigits(mid) < n:
                left = mid + 1
            else:
                right = mid

        digit = left
        pre_digits = self.totalDigits(digit - 1)
        idx = n - pre_digits - 1
        number = 10 ** (digit - 1) + idx // digit
        digit_idx = idx % digit
    
        return int(str(number)[digit_idx])
```

### 思路 2：复杂度分析

- **时间复杂度**：$\log n \times \log \log n$，位数上限 $D$ 为 $\log n$，二分查找的时间复杂度为 $\log D$，每次执行的时间复杂度为 $D$，总的时间复杂度为 $D \times \log D = O(\log n \times \log \log n)$。
- **空间复杂度**：$O(1)$。

## 参考资料

- 【题解】[400. 第 N 位数字 - 清晰易懂的找规律解法(击败100%, 几乎双百)](https://leetcode.cn/problems/nth-digit/solutions/1129463/geekplayers-leetcode-ac-qing-xi-yi-dong-uasjy/)
- 【题解】[400. 第 N 位数字 - 方法一：二分查找](https://leetcode.cn/problems/nth-digit/solutions/1128000/di-n-wei-shu-zi-by-leetcode-solution-mdl2/)
