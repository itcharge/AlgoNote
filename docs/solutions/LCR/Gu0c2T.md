# [LCR 089. 打家劫舍](https://leetcode.cn/problems/Gu0c2T/)

- 标签：数组、动态规划
- 难度：中等

## 题目链接

- [LCR 089. 打家劫舍 - 力扣](https://leetcode.cn/problems/Gu0c2T/)

## 题目大意

给定一个数组 `nums`，`num[i]` 代表第 `i` 间房屋存放的金额。相邻的房屋装有防盗系统，假如相邻的两间房屋同时被偷，系统就会报警。假如你是一名专业的小偷。

要求：计算在不触动警报装置的情况下，一夜之内能够偷窃到的最高金额。

## 解题思路

可以用动态规划来解决问题，关键点在于找到状态转移方程。

先考虑最简单的情况。假如只有一间房，则直接偷这间屋子就能偷到最高金额，即 `dp[0] = nums[i]`。假如只有两间房屋，那么就选择金额最大的那间屋进行偷窃，就可以偷到最高金额，即 `dp[1] = max(nums[0], nums[1])`。

如果房屋大于两间，则偷窃第 `i` 间房屋的时候，就有两种状态：

- 偷窃第 `i` 间房屋，那么第 `i - 1` 间房屋就不能偷窃了，偷窃的最高金额为：前 `i - 2` 间房屋的最高总金额 + 第 `i` 间房屋的金额，即 `dp[i] = dp[i-2] + nums[i]`；
- 不偷窃第 `i` 间房屋，那么第 `i - 1` 间房屋可以偷窃，偷窃的最高金额为：前 `i - 1` 间房屋的最高总金额，即 `dp[i] = dp[i-1]`。

然后这两种状态取最大值即可，即 `dp[i] = max(dp[i-2] + nums[i], dp[i-1])`。

总结下就是：

$dp[i] = \begin{cases} \begin{array} {**lr**}  nums[0] & i = 0 \cr max( nums[0], nums[1]) & i = 1 \cr max( dp[i-2] + nums[i], dp[i-1]) & i \ge 2 \end{array} \end{cases}$

## 代码

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0 for _ in range(size)]
        for i in range(size):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i - 1], nums[i])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]
```

