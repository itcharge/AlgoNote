# [0324. 摆动排序 II](https://leetcode.cn/problems/wiggle-sort-ii/)

- 标签：数组、分治、快速选择、排序
- 难度：中等

## 题目链接

- [0324. 摆动排序 II - 力扣](https://leetcode.cn/problems/wiggle-sort-ii/)

## 题目大意

给你一个整数数组 `nums`。

要求：将它重新排列成 `nums[0] < nums[1] > nums[2] < nums[3] ...` 的顺序。可以假设所有输入数组都可以得到满足题目要求的结果。

注意：

- $1 \le nums.length \le 5 * 10^4$。
- $0 \le nums[i] \le 5000$。

## 解题思路

`num[i]` 的取值在 `[0, 5000]`。所以我们可以用桶排序算法将排序算法的时间复杂度降到 $O(n)$。然后按照下标的奇偶性遍历两次数组，第一次遍历将桶中的元素从末尾到头部依次放到对应奇数位置上。第二次遍历将桶中剩余元素从末尾到头部依次放到对应偶数位置上。

## 代码

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0 for _ in range(5010)]
        for num in nums:
            buckets[num] += 1

        size = len(nums)
        big = size - 2 if (size & 1) == 1 else size - 1
        small = size - 1 if (size & 1) == 1 else size - 2

        index = 5000
        for i in range(1, big + 1, 2):
            while buckets[index] == 0:
                index -= 1
            nums[i] = index
            buckets[index] -= 1
        for i in range(0, small + 1, 2):
            while buckets[index] == 0:
                index -= 1
            nums[i] = index
            buckets[index] -= 1
```

