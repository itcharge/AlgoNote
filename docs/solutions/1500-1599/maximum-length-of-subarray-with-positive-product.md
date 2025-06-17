# [1567. 乘积为正数的最长子数组长度](https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/)

- 标签：贪心、数组、动态规划
- 难度：中等

## 题目链接

- [1567. 乘积为正数的最长子数组长度 - 力扣](https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/)

## 题目大意

给定一个整数数组 `nums`。

要求：求出乘积为正数的最长子数组的长度。

- 子数组：是由原数组中零个或者更多个连续数字组成的数组。

## 解题思路

使用动态规划来做。使用数组 `pos` 表示以下标 `i` 结尾的乘积为正数的最长子数组长度。使用数组 `neg` 表示以下标 `i` 结尾的乘积为负数的最长子数组长度。

- 先初始化 `pos[0]`、`neg[0]`。
  - 如果 `nums[0] == 0`，则 `pos[0] = 0, neg[0] = 0`。
  - 如果 `nums[0] > 0`，则 `pos[0] = 1, neg[0] = 0`。
  - 如果 `nums[0] < 0`，则 `pos[0] = 0, neg[0] = 1`。

- 然后从下标 `1` 开始递推遍历数组 `nums`，对于 `nums[i - 1]` 和 `nums[i]`：

  - 如果 `nums[i - 1] == 0`，显然有 `pos[i] = 0`，`neg[i] = 0`。表示：以`i` 结尾的乘积为正数的最长子数组长度为 `0`，以`i` 结尾的乘积为负数数的最长子数组长度也为 `0`。

  - 如果 `nums[i - 1] > 0`，则 `pos[i] = pos[i - 1] + 1`。而 `neg[i]` 需要进行判断，如果 `neg[i - 1] > 0`，则再乘以当前 `nums[i]` 后仍为负数，此时长度 +1，即 `neg[i] = neg[i - 1] + 1 `。而如果 `neg[i - 1] == 0`，则 `neg[i] = 0`。

  - 如果 `nums[i - 1] < 0`，则 `pos[i]` 需要进行判断，如果 `neg[i - 1] > 0`，再乘以当前 `nums[i]` 后变为正数，此时长度 +1，即 `pos[i] = neg[i - 1] + 1`。而如果 `neg[i - 1] = 0`，则 `pos[i] = 0`。
  - 更新 `ans` 答案为 `pos[i]` 最大值。

- 最后输出答案 `ans`。

## 代码

```python
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        size = len(nums)
        pos = [0 for _ in range(size + 1)]
        neg = [0 for _ in range(size + 1)]

        if nums[0] == 0:
            pos[0], neg[0] = 0, 0
        elif nums[0] > 0:
            pos[0], neg[0] = 1, 0
        else:
            pos[0], neg[0] = 0, 1

        ans = pos[0]
        for i in range(1, size):
            if nums[i] == 0:
                pos[i] = 0
                neg[i] = 0
            elif nums[i] > 0:
                pos[i] = pos[i - 1] + 1
                neg[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = neg[i - 1] + 1 if neg[i - 1] > 0 else 0
                neg[i] = pos[i - 1] + 1
            ans = max(ans, pos[i])
        return ans
```

## 参考资料

- 【题解】[递推就完事了，巨好理解~ - 乘积为正数的最长子数组长度 - 力扣](https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/solution/di-tui-jiu-wan-shi-liao-ju-hao-li-jie-by-time-limi/)
