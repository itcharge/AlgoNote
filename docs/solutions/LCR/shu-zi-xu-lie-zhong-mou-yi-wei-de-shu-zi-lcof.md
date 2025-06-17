# [LCR 163. 找到第 k 位数字](https://leetcode.cn/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)

- 标签：数学、二分查找
- 难度：中等

## 题目链接

- [LCR 163. 找到第 k 位数字 - 力扣](https://leetcode.cn/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)

## 题目大意

数字以 `0123456789101112131415…` 的格式序列化到一个字符序列中。在这个序列中，第 `5` 位（从下标 `0` 开始计数）是 `5`，第 `13` 位是 `1`，第 `19` 位是 `4`，等等。

要求：返回任意第 `n` 位对应的数字。

## 解题思路

根据题意中的字符串，找数学规律：

- `123456789`：是 `9` 个 `1` 位数字。
- `10111213...9899`：是 `90` 个 `2` 位数字。
- `100...999`：是 `900` 个 `3` 位数字。
- `1000...9999` 是 `9000` 个 `4` 位数字。

- 我们可以先找到对应的数字对应的位数 `digits`。
- 然后找到该位数 `digits` 的起始数字 `start`。
- 再计算出 `n` 所在的数字 `number`。`number` 等于从起始数字 `start` 开始的第 $\lfloor(n - 1) / digits\rfloor$ 个数字。即 `number = start + (n - 1) // digits`。
- 然后确定 `n` 对应的是数字 `number` 中的哪一位。即 `idx = (n - 1) % digits`。
- 最后返回结果。

## 代码

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        start = 1
        base = 9
        while n > base:
            n -= base
            digits += 1
            start *= 10
            base = start * digits * 9

        number = start + (n - 1) // digits
        idx = (n - 1) % digits
        return int(str(number)[idx])
```

## 参考资料

- 【题解】[面试题44. 数字序列中某一位的数字（迭代 + 求整 / 求余，清晰图解） - 数字序列中某一位的数字 - 力扣](https://leetcode.cn/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/mian-shi-ti-44-shu-zi-xu-lie-zhong-mou-yi-wei-de-6/)
