# [0575. 分糖果](https://leetcode.cn/problems/distribute-candies/)

- 标签：数组、哈希表
- 难度：简单

## 题目链接

- [0575. 分糖果 - 力扣](https://leetcode.cn/problems/distribute-candies/)

## 题目大意

给定一个偶数长度为 `n` 的数组，其中不同的数字代表不同种类的糖果，每一个数字代表一个糖果。

要求：将这些糖果按种类平均分为一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。

## 解题思路

`n` 个糖果分为两个人，每个人最多只能得到 `n // 2` 个糖果。假设糖果种数为 `m`。则如果糖果种类数大于糖果总数的一半，即 `m > n // 2`，则返回糖果数量的一半就好，也就说糖果总数一半的糖果都可以是不同种类的糖果。妹妹能获得最多 `n // 2` 种糖果。而如果让给种类数小于等于糖果总数的一半，即 `m <= n // 2`，则返回种类数，也就是说妹妹可以最多获得 `m` 种糖果。

综合这两种情况，其最终结果就是 `ans = min(m, n // 2)`。

计算糖果种类可以用 set 集合来做。

## 代码

```python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_set = set(candyType)
        return min(len(candyType) // 2, len(candy_set))
```

