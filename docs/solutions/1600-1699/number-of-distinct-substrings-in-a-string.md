# [1698. 字符串的不同子字符串个数](https://leetcode.cn/problems/number-of-distinct-substrings-in-a-string/)

- 标签：字典树、字符串、后缀数组、哈希函数、滚动哈希
- 难度：中等

## 题目链接

- [1698. 字符串的不同子字符串个数 - 力扣](https://leetcode.cn/problems/number-of-distinct-substrings-in-a-string/)

## 题目大意

给定一个字符串 `s`。

要求：返回 `s` 的不同子字符串的个数。

注意：字符串的「子字符串」是由原字符串删除开头若干个字符（可能是 0 个）并删除结尾若干个字符（可能是 0 个）形成的字符串。

## 解题思路

构建一颗字典树。分别将原字符串删除开头若干个字符的子字符串依次插入到字典树中。

每次插入过程中碰到字典树中没有的字符节点时，说明此时插入的字符串可作为新的子字符串。

我们可以通过统计插入过程中新建字符节点的次数的方式来获取不同子字符串的个数。

## 代码

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False


    def insert(self, word: str) -> int:
        """
        Inserts a word into the trie.
        """
        cur = self
        cnt = 0
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
                cnt += 1
            cur = cur.children[ch]
        cur.isEnd = True
        return cnt


class Solution:
    def countDistinct(self, s: str) -> int:
        trie_tree = Trie()
        cnt = 0
        for i in range(len(s)):
            cnt += trie_tree.insert(s[i:])
        return cnt
```

