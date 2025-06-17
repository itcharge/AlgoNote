# [LCR 167. 招式拆解 I](https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/)

- 标签：哈希表、字符串、滑动窗口
- 难度：中等

## 题目链接

- [LCR 167. 招式拆解 I - 力扣](https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/)

## 题目大意

给定一个字符串 `s`。

要求：找出其中不含有重复字符的最长子串的长度。

## 解题思路

利用集合来存储不重复的字符。用两个指针分别指向最长子串的左右节点。遍历字符串，右指针不断右移，利用集合来判断有没有重复的字符，如果没有，就持续向右扩大右边界。如果出现重复字符，就缩小左侧边界。每次移动终止，都要计算一下当前不含重复字符的子串长度，并判断一下是否需要更新最大长度。

## 代码

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        letterSet = set()
        right = 0
        ans = 0
        for i in range(len(s)):
            if i != 0:
                letterSet.remove(s[i - 1])
            while right < len(s) and s[right] not in letterSet:
                letterSet.add(s[right])
                right += 1
            ans = max(ans, right - i)
        return ans
```

