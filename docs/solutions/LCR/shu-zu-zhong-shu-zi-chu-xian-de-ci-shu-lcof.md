# [LCR 177. 撞色搭配](https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)

- 标签：位运算、数组
- 难度：中等

## 题目链接

- [LCR 177. 撞色搭配 - 力扣](https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)

## 题目大意

给定一个整型数组 `nums` 。`nums` 里除两个数字之外，其他数字都出现了两次。

要求：找出这两个只出现一次的数字。要求时间复杂度是 $O(n)$，空间复杂度是 $O(1)$。

## 解题思路

- 求解这道题之前，我们先来看看如何求解「一个数组中除了某个元素只出现一次以外，其余每个元素均出现两次。」即「[136. 只出现一次的数字](https://leetcode.cn/problems/single-number/)」问题。我们可以对所有数不断进行异或操作，最终可得到单次出现的元素。

- 如果数组中有两个数字只出现一次，其余每个元素均出现两次。那么经过全部异或运算。我们可以得到只出现一次的两个数字的异或结果。
- 根据异或结果的性质，异或运算中如果某一位上为 `1`，则说明异或的两个数在该位上是不同的。根据这个性质，我们将数字分为两组：一组是和该位为 `0` 的数字，另一组是该位为 `1` 的数字。然后将这两组分别进行异或运算，就可以得到最终要求的两个数字。

## 代码

```python
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        all_xor = 0
        for num in nums:
            all_xor ^= num
        # 获取所有异或中最低位的 1
        mask = 1
        while all_xor & mask == 0:
            mask <<= 1

        a_xor, b_xor = 0, 0
        for num in nums:
            if num & mask == 0:
                a_xor ^= num
            else:
                b_xor ^= num

        return a_xor, b_xor
```

