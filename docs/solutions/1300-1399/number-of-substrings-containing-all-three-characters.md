# [1358. 包含所有三种字符的子字符串数目](https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/)

- 标签：哈希表、字符串、滑动窗口
- 难度：中等

## 题目链接

- [1358. 包含所有三种字符的子字符串数目 - 力扣](https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/)

## 题目大意

给你一个字符串 `s` ，`s` 只包含三种字符 `a`, `b` 和 `c`。

请你返回 `a`，`b` 和 `c` 都至少出现过一次的子字符串数目。

## 解题思路

只要找到首个 `a`、`b`、`c` 同时存在的子字符串，则在该子字符串后面追加字符构成的新字符串还是满足题意的。假设该子串末尾字母的位置为 `i`，则以此字符串构建的新字符串有 `len(s) - i`个。所以题目可以转换为找出 `a`、`b`、`c` 同时存在的最短子串，并记录所有满足题意的字符串数量。具体做法如下：

用滑动窗口 `window` 来记录各个字符个数，`window` 为哈希表类型。用 `ans` 来维护 `a`，`b` 和 `c` 都至少出现过一次的子字符串数目。

设定两个指针：`left`、`right`，分别指向滑动窗口的左右边界，保证窗口中不超过 `k` 种字符。

- 一开始，`left`、`right` 都指向 `0`。
- 将最右侧字符 `s[right]` 加入当前窗口 `window_counts` 中，记录该字符个数，向右移动 `right`。
- 如果该窗口中字符的种数大于等于 `3` 种，即 `len(window) >= 3`，则累积答案个数为 `len(s) - right`，并不断右移 `left`，缩小滑动窗口长度，并更新窗口中对应字符的个数，直到 `len(window) < 3`。
- 然后继续右移 `right`，直到 `right >= len(nums)` 结束。
- 输出答案 `ans`。

## 代码

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        window = dict()
        ans = 0
        left, right = 0, 0

        while right < len(s):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            while len(window) >= 3:
                ans += len(s) - right
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            right += 1
        return ans
```

