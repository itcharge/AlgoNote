# [1561. 你可以获得的最大硬币数目](https://leetcode.cn/problems/maximum-number-of-coins-you-can-get/)

- 标签：贪心、数组、数学、博弈、排序
- 难度：中等

## 题目链接

- [1561. 你可以获得的最大硬币数目 - 力扣](https://leetcode.cn/problems/maximum-number-of-coins-you-can-get/)

## 题目大意

有 `3*n` 堆数目不一的硬币，三个人按照下面的规则分硬币：

- 每一轮选出任意 3 堆硬币。
- Alice 拿走硬币数量最多的那一堆。
- 我们自己拿走硬币数量第二多的那一堆。
- Bob 拿走最后一堆。
- 重复这个过程，直到没有更多硬币。

现在给定一个整数数组 `piles`，代表 `3*n` 堆硬币，其中 `piles[i]` 表示第 `i` 堆中硬币的数目。

## 解题思路

每次 `3` 堆，总共取 `n` 次。Bob 每次总是选择最少的一堆，所以最终 Bob 得到 `3*n` 堆中最少的 `n` 堆才能使得另外两个人获得更多。所以先对硬币堆进行排序。Bob 拿走最少的 `n` 堆。我们接着分剩下的 `2*n` 堆。

按照大小顺序，每次都选取硬币数目最多的两堆， Alice 取得较大的一堆，我们取较小的一堆。

然后继续在剩余堆中选取硬币数目最多的两堆，同样 Alice 取得较大的一堆，我们取较小的一堆。

只有这样才能在满足规则的情况下，使我们所获得硬币数最多。

最后统计我们所获取的硬币数，并返回结果。

## 代码

```python
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        for i in range(len(piles) // 3, len(piles), 2):
            ans += piles[i]
        return ans
```

