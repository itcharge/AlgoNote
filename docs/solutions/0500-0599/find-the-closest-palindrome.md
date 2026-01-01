# [0564. 寻找最近的回文数](https://leetcode.cn/problems/find-the-closest-palindrome/)

- 标签：数学、字符串
- 难度：困难

## 题目链接

- [0564. 寻找最近的回文数 - 力扣](https://leetcode.cn/problems/find-the-closest-palindrome/)

## 题目大意

**描述**：

给定一个表示整数的字符串 $n$。

**要求**：

返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。

**说明**：

- 「最近的」定义为两个整数差的绝对值最小。
- $1 \le n.length \le 18$。
- $n$ 只由数字组成。
- $n$ 不含前导 $0$。
- $n$ 代表在 $[1, 10^{18} - 1]$ 范围内的整数。

**示例**：

- 示例 1：

```python
输入: n = "123"
输出: "121"
```

- 示例 2：

```python
输入: n = "1"
输出: "0"
解释: 0 和 2 是最近的回文，但我们返回最小的，也就是 0。
```

## 解题思路

### 思路 1：枚举候选回文数

对于给定的数字 $n$，最近的回文数只可能是以下几种情况之一：
1. $999...999$（$n$ 的位数减 $1$）。
2. $100...001$（$n$ 的位数加 $1$）。
3. 将 $n$ 的前半部分镜像到后半部分。
4. 将 $n$ 的前半部分加 $1$ 后镜像到后半部分。
5. 将 $n$ 的前半部分减 $1$ 后镜像到后半部分。

生成这些候选数，然后选择与 $n$ 差值最小的（排除 $n$ 本身），如果差值相同则选择较小的。

### 思路 1：代码

```python
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()
        
        # 情况 1: 999...999 (length - 1 位)
        candidates.add(str(10**(length - 1) - 1))
        
        # 情况 2: 100...001 (length + 1 位)
        candidates.add(str(10**length + 1))
        
        # 情况 3, 4, 5: 基于前半部分的镜像
        prefix_length = (length + 1) // 2
        prefix = int(n[:prefix_length])
        
        for delta in [-1, 0, 1]:
            new_prefix = str(prefix + delta)
            if length % 2 == 0:
                # 偶数长度
                palin = new_prefix + new_prefix[::-1]
            else:
                # 奇数长度
                palin = new_prefix + new_prefix[-2::-1]
            candidates.add(palin)
        
        # 移除 n 本身
        candidates.discard(n)
        
        # 找到最近的回文数
        num = int(n)
        result = min(candidates, key=lambda x: (abs(int(x) - num), int(x)))
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(L)$，其中 $L$ 是字符串 $n$ 的长度，需要生成和比较常数个候选数。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
