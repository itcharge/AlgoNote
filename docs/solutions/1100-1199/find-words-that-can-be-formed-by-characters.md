# [1160. 拼写单词](https://leetcode.cn/problems/find-words-that-can-be-formed-by-characters/)

- 标签：数组、哈希表、字符串、计数
- 难度：简单

## 题目链接

- [1160. 拼写单词 - 力扣](https://leetcode.cn/problems/find-words-that-can-be-formed-by-characters/)

## 题目大意

**描述**：给定一个字符串数组 $words$ 和一个字符串 $chars$。$chars$ 里有一些字母，每个字母只能用一次。

如果一个单词 $word$ 中的每个字母都能从 $chars$ 中找到（且数量够用），就认为这个单词是「好的」。

**要求**：返回所有「好的」单词的长度之和。

**说明**：

- $1 \le words.length \le 10^{3}$。
- $1 \le words[i].length, chars.length \le 10^{3}$。
- 所有字符都是小写英文字母。

**示例**：

```python
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：可以拼出 "cat"（3）+ "hat"（3）= 6。
```

## 解题思路

### 思路 1：哈希表计数

这道题可以想象成你手上有一把字母（$chars$），现在要看看哪些单词能用这些字母拼出来。每个字母只能用一次，所以如果某个单词里需要 2 个 `'a'`，你手上也必须有至少 2 个 `'a'`。

**步骤拆解：**

1. 先数一数 $chars$ 里每个字母各有多少个，记下来（用哈希表或数组都行）。

2. 遍历每个单词：
   - 也数一数这个单词里每个字母各有多少个。
   - 检查每个字母的需求量是否 $\le$ 手上的库存量。
   - 如果全部满足，就把单词长度加到结果里。

3. 返回结果。

### 思路 1：代码

```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        
        # 统计 chars 中每个字母有多少个
        chars_count = Counter(chars)
        
        result = 0
        
        for word in words:
            # 统计当前单词中每个字母有多少个
            word_count = Counter(word)
            # 检查每个字母的需求量是否不超过库存
            # all() 函数：所有条件都满足才返回 True
            if all(word_count[ch] <= chars_count[ch] for ch in word_count):
                result += len(word)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$。用人话说就是：$chars$ 长 $n$，所有单词总长 $m$，每个字符都只检查一次。
- **空间复杂度**：$O(1)$。因为只有 26 个小写字母，哈希表大小是常数。
