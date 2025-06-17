# [LCR 186. 文物朝代判断](https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)

- 标签：数组、排序
- 难度：简单

## 题目链接

- [LCR 186. 文物朝代判断 - 力扣](https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)

## 题目大意

给定一个 `5` 位数的数组 `nums` 代表扑克牌中的 `5` 张牌。其中 `2~10` 为数字本身，`A` 用 `1` 表示，`J` 用 `11` 表示，`Q` 用 `12` 表示，`K` 用 `13` 表示，大小王用 `0` 表示，且大小王可以替换任意数字。

要求：判断给定的 `5` 张牌是否是一个顺子，即是否为连续的`5` 个数。

## 解题思路

先不考虑牌中有大小王，如果 `5` 个数是连续的，则这 `5` 个数中最大值最小值的关系为：`最大值 - 最小值 = 4`。如果牌中有大小王可以替换这 `5` 个数中的任意数字，则除大小王之外剩下数的最大值最小值关系为 `最大值 - 最小值 <= 4`。而且剩余数不能有重复数字。于是可以这样进行判断。

遍历 `5` 张牌：

- 如果出现大小王，则跳过。
- 判断 `5` 张牌中是否有重复数，如果有则直接返回 `False`，如果没有则将其加入集合。
- 计算 `5` 张牌的最大值，最小值。

最后判断 `最大值 - 最小值  <= 4` 是否成立。如果成立，返回 `True`，否则返回 `False`。

## 代码

```python
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        max_num, min_num = 0, 14
        repeat = set()
        for num in nums:
            if num == 0:
                continue
            if num in repeat:
                return False
            repeat.add(num)
            max_num = max(max_num, num)
            min_num = min(min_num, num)
        return max_num - min_num <= 4
```

