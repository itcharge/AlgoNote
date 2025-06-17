# [0714. 买卖股票的最佳时机含手续费](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

- 标签：贪心、数组、动态规划
- 难度：中等

## 题目链接

- [0714. 买卖股票的最佳时机含手续费 - 力扣](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

## 题目大意

给定一个整数数组 `prices`，其中第 `i` 个元素代表了第 `i` 天的股票价格 ；整数 `fee` 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

最后要求返回获得利润的最大值。

## 解题思路

这道题的解题思路和「[0122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)」类似，同样可以买卖多次。122 题是在跌入谷底的时候买入，在涨到波峰的时候卖出，这道题多了手续费，则在判断波峰波谷的时候还要考虑手续费。贪心策略如下：

- 当股票价格小于当前最低股价时，更新最低股价，不卖出。
- 当股票价格大于最小价格 + 手续费时，累积股票利润（实质上暂未卖出，等到波峰卖出），同时最低股价减去手续费，以免重复计算。

## 代码

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] > min_price + fee:
                res += prices[i] - min_price - fee
                min_price = prices[i] - fee
        return res
```

