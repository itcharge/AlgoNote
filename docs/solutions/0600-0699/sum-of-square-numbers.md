# [0633. 平方数之和](https://leetcode.cn/problems/sum-of-square-numbers/)

- 标签：数学、双指针、二分查找
- 难度：中等

## 题目链接

- [0633. 平方数之和 - 力扣](https://leetcode.cn/problems/sum-of-square-numbers/)

## 题目大意

给定一个非负整数 c，判断是否存在两个整数 a 和 b，使得 $a^2 + b^2 = c$，如果存在则返回 True，不存在返回 False。

## 解题思路

最直接的办法就是枚举 a、b 所有可能。这样遍历下来的时间复杂度为 $O(c^2)$。但是没必要进行二重遍历。可以只遍历 a，然后去判断 $\sqrt{c - b^2}$ 是否为整数，并且 a 只需遍历到 $\sqrt{c}$ 即可，时间复杂度为 $O(\sqrt{c})$。

另一种方法是双指针。定义两个指针 left，right 分别指向 0 和 $\sqrt{c}$。判断 $left^2 + right^2$ 与 c 之间的关系。

- 如果 $a^2 + b^2 == c$，则返回 True。
- 如果 $a^2 + b^2 < c$，则将 a 值加一，继续查找。
- 如果 $a^2 + b^2 > c$，则将 b 值减一，继续查找。
- 当 $a == b$ 时，结束查找。如果此时仍没有找到满足 $a^2 + b^2 == c$ 的 a、b 值，则返回 False。

## 代码

```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(c ** 0.5)
        while a <= b:
            sum = a*a + b*b
            if sum == c:
                return True
            elif sum < c:
                a += 1
            else:
                b -= 1
        return False
```

