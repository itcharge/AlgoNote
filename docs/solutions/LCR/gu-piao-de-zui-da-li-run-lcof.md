# [LCR 188. 买卖芯片的最佳时机](https://leetcode.cn/problems/gu-piao-de-zui-da-li-run-lcof/)

- 标签：数组、动态规划
- 难度：中等

## 题目链接

- [LCR 188. 买卖芯片的最佳时机 - 力扣](https://leetcode.cn/problems/gu-piao-de-zui-da-li-run-lcof/)

## 题目大意

给定一个数组 `nums`，`nums[i]` 表示一支给定股票第 `i` 天的价格。选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。求能获取的最大利润。

## 解题思路

最简单的思路当然是两重循环暴力枚举，寻找不同天数下的最大利润。

但更好的做法是进行一次遍历。设置两个变量 `minprice`（用来记录买入的最小值）、`maxprofit`（用来记录可获取的最大利润）。

进行一次遍历，遇到当前价格比 `minprice` 还要小的，就更新 `minprice`。如果单签价格大于或者等于 `minprice`，则判断一下以当前价格卖出的话能卖多少，如果比 `maxprofit` 还要大，就更新 `maxprofit`。

## 代码

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 10010
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > maxprofit:
                maxprofit = price - minprice
        return maxprofit
```

