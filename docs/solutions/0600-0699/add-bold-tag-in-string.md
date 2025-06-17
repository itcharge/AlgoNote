# [0616. 给字符串添加加粗标签](https://leetcode.cn/problems/add-bold-tag-in-string/)

- 标签：字典树、数组、哈希表、字符串、字符串匹配
- 难度：中等

## 题目链接

- [0616. 给字符串添加加粗标签 - 力扣](https://leetcode.cn/problems/add-bold-tag-in-string/)

## 题目大意

给定一个字符串 `s` 和一个字符串列表 `words`。

要求：如果 `s` 的子串在字符串列表 `words` 中出现过，则在该子串前后添加加粗闭合标签 `<b>` 和 `</b>`。如果两个子串有重叠部分，则将它们一起用一对闭合标签包围起来。同理，如果两个子字符串连续被加粗，那么你也需要把它们合起来用一对加粗标签包围。最后返回添加加粗标签后的字符串 `s`。

## 解题思路

构建字典树，将字符串列表 `words` 中所有字符串添加到字典树中。

然后遍历字符串 `s`，从每一个位置开始查询字典树。在第一个符合要求的单词前面添加 `<b>`。在连续符合要求的单词中的最后一个单词后面添加 `</b>`。

最后返回添加加粗标签后的字符串 `s`。

## 代码

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        trie_tree = Trie()
        for word in words:
            trie_tree.insert(word)

        size = len(s)
        bold_left, bold_right = -1, -1
        ans = ""
        for i in range(size):
            cur = trie_tree
            if s[i] in cur.children:
                bold_left = i
                while bold_left < size and s[bold_left] in cur.children:
                    cur = cur.children[s[bold_left]]
                    bold_left += 1
                    if cur.isEnd:
                        if bold_right == -1:
                            ans += "<b>"
                        bold_right = max(bold_left, bold_right)
            if i == bold_right:
                ans += "</b>"
                bold_right = -1
            ans += s[i]
        if bold_right >= 0:
            ans += "</b>"
        return ans
```

