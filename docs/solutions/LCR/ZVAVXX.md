# [LCR 009. 乘积小于 K 的子数组](https://leetcode.cn/problems/ZVAVXX/)

- 标签：数组、滑动窗口
- 难度：中等

## 题目链接

- [LCR 009. 乘积小于 K 的子数组 - 力扣](https://leetcode.cn/problems/ZVAVXX/)

## 题目大意

给定一个正整数数组 `nums` 和一个整数 `k`。

要求：找出该数组内乘积小于 `k` 的连续子数组的个数。

## 解题思路

滑动窗口求解。

设定两个指针：`left`、`right`，分别指向滑动窗口的左右边界，保证窗口内所有数的乘积 `product` 都小于 `k`。

- 一开始，`left`、`right` 都指向 `0`。

- 向右移动 `right`，将最右侧元素加入当前子数组乘积 `product` 中。

- 如果 `product >= k` ，则不断右移 `left`，缩小滑动窗口，并更新当前乘积值 `product`  直到 `product < k`。
- 累积答案个数 += 1，继续右移 `right`，直到 `right >= len(nums)` 结束。
- 输出累积答案个数。

## 代码

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        size = len(nums)
        left, right = 0, 0
        count = 0
        product = 1
        while right < size:
            product *= nums[right]
            right += 1
            while product >= k:
                product /= nums[left]
                left += 1
            count += (right - left)
        return count
```

