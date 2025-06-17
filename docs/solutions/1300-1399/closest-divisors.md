# [1362. 最接近的因数](https://leetcode.cn/problems/closest-divisors/)

- 标签：数学
- 难度：中等

## 题目链接

- [1362. 最接近的因数 - 力扣](https://leetcode.cn/problems/closest-divisors/)

## 题目大意

**描述**：给定一个整数 $num$。

**要求**：找出同时满足下面全部要求的两个整数：

- 两数乘积等于 $num + 1$ 或 $num + 2$。
- 以绝对差进行度量，两数大小最接近。

你可以按照任意顺序返回这两个整数。

**说明**：

- $1 \le num \le 10^9$。

**示例**：

- 示例 1：

```python
输入：num = 8
输出：[3,3]
解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 & 3。
```

- 示例 2：

```python
输入：num = 123
输出：[5,25]
```

## 解题思路

### 思路 1：数学

对于整数的任意一个范围在 $[\sqrt{n}, n]$ 的因数而言，一定存在一个范围在 $[1, \sqrt{n}]$ 的因数与其对应。因此，我们在遍历整数因数时，我们只需遍历 $[1, \sqrt{n}]$ 范围内的因数即可。

则这道题的具体解题步骤如下：

1. 对于整数 $num + 1$、从 $\sqrt{num + 1}$ 的位置开始，到 $1$ 为止，以递减的顺序在 $[1, \sqrt{num + 1}]$ 范围内找到最接近的小因数 $a1$，并根据 $num // a1$ 获得另一个因数 $a2$。
2. 用同样的方式，对于整数 $num + 2$、从 $\sqrt{num + 2}$ 的位置开始，到 $1$ 为止，以递减的顺序在 $[1, \sqrt{num + 2}]$ 范围内找到最接近的小因数 $b1$，并根据 $num // b1$ 获得另一个因数 $b2$。
3. 判断 $abs(a1 - a2)$ 与 $abs(b1 - b2)$ 的大小，返回差值绝对值较小的一对因子数作为答案。

### 思路 1：代码

```Python
class Solution:
    def disassemble(self, num):
        for i in range(int(sqrt(num) + 1), 1, -1):
            if num % i == 0:
                return (i, num // i)
        return (1, num)

    def closestDivisors(self, num: int) -> List[int]:
        a1, a2 = self.disassemble(num + 1)
        b1, b2 = self.disassemble(num + 2)
        if abs(a1 - a2) <= abs(b1 - b2):
            return [a1, a2]
        return [b1, b2]
```

### 思路 1：复杂度分析

- **时间复杂度**：$(\sqrt{n})$。
- **空间复杂度**：$O(1)$。

