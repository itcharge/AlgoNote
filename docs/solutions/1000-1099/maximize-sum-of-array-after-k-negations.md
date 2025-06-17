# [1005. K 次取反后最大化的数组和](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/)

- 标签：贪心、数组、排序
- 难度：简单

## 题目链接

- [1005. K 次取反后最大化的数组和 - 力扣](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/)

## 题目大意

给定一个整数数组 nums 和一个整数 k。只能用下面的方法修改数组：

- 将数组上第 i 个位置上的值取相反数，即将 `nums[i]` 变为 `-nums[i]`。

用这种方式进行 K 次修改（可以多次修改同一个位置 i） 后，返回数组可能的最大和。

## 解题思路

- 先将数组按绝对值大小进行排序
- 从绝对值大的数开始遍历数组，如果 nums[i] < 0，并且 k > 0：
  - 则对 nums[i] 取相反数，并将 k 值 -1。
- 如果最后 k 还有余值，则判断奇偶性：
  - 若 k 为奇数，则将数组绝对值最小的数进行取反。
  - 若 k 为偶数，则说明可将某一位数进行偶数次取反，和原数值一致，则不需要进行操作。
- 最后返回数组和。

## 代码

```python
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: abs(x), reverse = True)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
        if k % 2 == 1:
            nums[-1] *= -1
        return sum(nums)
```

