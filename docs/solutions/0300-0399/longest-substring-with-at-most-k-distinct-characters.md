# [0340. 至多包含 K 个不同字符的最长子串](https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/)

- 标签：哈希表、字符串、滑动窗口
- 难度：中等

## 题目链接

- [0340. 至多包含 K 个不同字符的最长子串 - 力扣](https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/)

## 题目大意

给定一个字符串 `s`，

要求：返回至多包含 `k` 个不同字符的最长子串 `t` 的长度。

## 解题思路

用滑动窗口 `window_counts` 来记录各个字符个数，`window_counts` 为哈希表类型。用 `ans` 来维护至多包含 `k` 个不同字符的最长子串 `t` 的长度。

设定两个指针：`left`、`right`，分别指向滑动窗口的左右边界，保证窗口中不超过 `k` 种字符。

- 一开始，`left`、`right` 都指向 `0`。
- 将最右侧字符 `s[right]` 加入当前窗口 `window_counts` 中，记录该字符个数，向右移动 `right`。
- 如果该窗口中字符的种数多于 `k` 个，即 `len(window_counts) > k`，则不断右移 `left`，缩小滑动窗口长度，并更新窗口中对应字符的个数，直到 `len(window_counts) <= k`。
- 维护更新至多包含 `k` 个不同字符的最长子串 `t` 的长度。然后继续右移 `right`，直到 `right >= len(nums)` 结束。
- 输出答案 `ans`。

## 代码

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = 0
        window_counts = dict()
        left, right = 0, 0

        while right < len(s):
            if s[right] in window_counts:
                window_counts[s[right]] += 1
            else:
                window_counts[s[right]] = 1

            while(len(window_counts) > k):
                window_counts[s[left]] -= 1
                if window_counts[s[left]] == 0:
                    del window_counts[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
```

