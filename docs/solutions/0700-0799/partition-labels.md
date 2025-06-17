# [0763. 划分字母区间](https://leetcode.cn/problems/partition-labels/)

- 标签：贪心、哈希表、双指针、字符串
- 难度：中等

## 题目链接

- [0763. 划分字母区间 - 力扣](https://leetcode.cn/problems/partition-labels/)

## 题目大意

给定一个由小写字母组成的字符串 `s`。要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。

要求：返回一个表示每个字符串片段的长度的列表。

## 解题思路

因为同一字母最多出现在一个片段中，则同一字母第一次出现的下标位置和最后一次出现的下标位置肯定在同一个片段中。

我们先遍历一遍字符串，用哈希表 letter_map 存储下每一个字母最后一次出现的下标位置。

为了得到尽可能的片段，我们使用贪心的思想：

- 从头开始遍历字符串，遍历同时维护当前片段的开始位置 start 和结束位置 end。
- 对于字符串中的每个字符 `s[i]`，得到当前字母的最后一次出现的下标位置 `letter_map[s[i]]`，则当前片段的结束位置一定不会早于 `letter_map[s[i]]`，所以更新 end 值为 `end = max(end, letter_map[s[i]])`。
- 当访问到 `i == end` 时，当前片段访问结束，当前片段的下标范围为 `[start, end]`，长度为 `end - start + 1`，将其长度加入答案数组，并更新 start 值为 `i + 1`，继续遍历。
- 最终返回答案数组。

## 代码

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_map = dict()
        for i in range(len(s)):
            letter_map[s[i]] = i
        res = []
        start, end = 0, 0
        for i in range(len(s)):
            end = max(end, letter_map[s[i]])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
```

