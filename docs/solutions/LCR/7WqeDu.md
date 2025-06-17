# [LCR 057. 存在重复元素 III](https://leetcode.cn/problems/7WqeDu/)

- 标签：数组、桶排序、有序集合、排序、滑动窗口
- 难度：中等

## 题目链接

- [LCR 057. 存在重复元素 III - 力扣](https://leetcode.cn/problems/7WqeDu/)

## 题目大意

给定一个整数数组 `nums`，以及两个整数 `k`、`t`。判断数组中是否存在两个不同下标的 `i` 和 `j`，其对应元素满足 `abs(nums[i] - nums[j]) <= t`，同时满足 `abs(i - j) <= k`。如果满足条件则返回 `True`，不满足条件返回 `False`。

## 解题思路

对于第 `i` 个元素 `nums[i]`，需要查找的区间为 `[i - t, i + t]`。可以利用桶排序的思想。

桶的大小设置为 `t + 1`。我们将元素按照大小依次放入不同的桶中。

遍历数组 `nums` 中的元素，对于元素 `nums[i]` ：

- 如果 `nums[i]` 放入桶之前桶里已经有元素了，那么这两个元素必然满足 `abs(nums[i] - nums[j]) <= t`，
- 如果之前桶里没有元素，那么就将 `nums[i]` 放入对应桶中。
- 然后再判断左右桶的左右两侧桶中是否有元素满足 `abs(nums[i] - nums[j]) <= t`。
- 然后将 `nums[i - k]` 之前的桶清空，因为这些桶中的元素与 `nums[i]` 已经不满足 `abs(i - j) <= k` 了。

最后上述满足条件的情况就返回 `True`，最终遍历完仍不满足条件就返回 `False`。

## 代码

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket_dict = dict()
        for i in range(len(nums)):
            # 将 nums[i] 划分到大小为 t + 1 的不同桶中
            num = nums[i] // (t + 1)

            # 桶中已经有元素了
            if num in bucket_dict:
                return True

            # 把 nums[i] 放入桶中
            bucket_dict[num] = nums[i]

            # 判断左侧桶是否满足条件
            if (num - 1) in bucket_dict and abs(bucket_dict[num - 1] - nums[i]) <= t:
                return True
            # 判断右侧桶是否满足条件
            if (num + 1) in bucket_dict and abs(bucket_dict[num + 1] - nums[i]) <= t:
                return True
            # 将 i-k 之前的旧桶清除，因为之前的桶已经不满足条件了
            if i >= k:
                bucket_dict.pop(nums[i - k] // (t + 1))

        return False
```

