# [0992. K 个不同整数的子数组](https://leetcode.cn/problems/subarrays-with-k-different-integers/)

- 标签：数组、哈希表、计数、滑动窗口
- 难度：困难

## 题目链接

- [0992. K 个不同整数的子数组 - 力扣](https://leetcode.cn/problems/subarrays-with-k-different-integers/)

## 题目大意

给定一个正整数数组 `nums`，再给定一个整数 `k`。如果 `nums` 的某个子数组中不同整数的个数恰好为 `k`，则称 `nums` 的这个连续、不一定不同的子数组为「好子数组」。

- 例如，`[1, 2, 3, 1, 2]` 中有 3 个不同的整数：`1`，`2` 以及 `3`。

要求：返回 `nums` 中好子数组的数目。

## 解题思路

这道题转换一下思路会更简单。

恰好包含 `k` 个不同整数的连续子数组数量 = 包含小于等于 `k` 个不同整数的连续子数组数量 - 包含小于等于 `k - 1` 个不同整数的连续子数组数量

可以专门写一个方法计算包含小于等于 `k` 个不同整数的连续子数组数量。

计算包含小于等于 `k` 个不同整数的连续子数组数量的方法具体步骤如下：

用滑动窗口 `windows` 来记录不同的整数个数，`windows` 为哈希表类型。

设定两个指针：`left`、`right`，分别指向滑动窗口的左右边界，保证窗口内不超过 `k` 个不同整数。

- 一开始，`left`、`right` 都指向 `0`。
- 将最右侧整数 `nums[right]` 加入当前窗口 `windows` 中，记录该整数个数。
- 如果该窗口中该整数的个数多于 `k` 个，即 `len(windows) > k`，则不断右移 `left`，缩小滑动窗口长度，并更新窗口中对应整数的个数，直到 `len(windows) <= k`。
- 维护更新包含小于等于 `k` 个不同整数的连续子数组数量。每次累加数量为 `right - left + 1`，表示以 `nums[right]` 为结尾的小于等于 `k` 个不同整数的连续子数组数量。
- 然后右移 `right`，直到 `right >= len(nums)` 结束。
- 返回包含小于等于 `k` 个不同整数的连续子数组数量。

## 代码

```python
class Solution:
    def subarraysMostKDistinct(self, nums, k):
        windows = dict()
        left, right = 0, 0
        ans = 0
        while right < len(nums):
            if nums[right] in windows:
                windows[nums[right]] += 1
            else:
                windows[nums[right]] = 1
            while len(windows) > k:
                windows[nums[left]] -= 1
                if windows[nums[left]] == 0:
                    del windows[nums[left]]
                left += 1
            ans += right - left + 1
            right += 1
        return ans

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysMostKDistinct(nums, k) - self.subarraysMostKDistinct(nums, k - 1)
```

