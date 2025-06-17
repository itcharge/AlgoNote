# [1065. 字符串的索引对](https://leetcode.cn/problems/index-pairs-of-a-string/)

- 标签：字典树、数组、字符串、排序
- 难度：简单

## 题目链接

- [1065. 字符串的索引对 - 力扣](https://leetcode.cn/problems/index-pairs-of-a-string/)

## 题目大意

给定字符串 `text` 和单词列表 `words`。

要求：在 `text` 中找出所有属于单词列表 `words` 中的单词，并返回该单词在 `text` 中的索引对位置 `[i, j]`。将所有索引对存入列表中返回，并且返回的索引对可以交叉。

## 解题思路

构建字典树，将所有单词存入字典树中。

然后一重循环遍历 `text`，表示从第 `i` 位置开始的字符串 `text[i:]`。然后在字符串前缀中搜索对应的单词，将所有符合要求的单词末尾位置存入列表中，返回所有位置列表。对于列表中每个单词末尾位置 `index` 和 `text` 来说，每个 `[i, i + index]` 都构成了单词在 `text` 中的索引对位置，将其存入答案数组并返回即可。

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


    def search(self, text: str) -> list:
        """
        Returns if the word is in the trie.
        """
        cur = self
        res = []
        for i in range(len(text)):
            ch = text[i]
            if ch not in cur.children:
                return res
            cur = cur.children[ch]
            if cur.isEnd:
                res.append(i)

        return res

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie_tree = Trie()
        for word in words:
            trie_tree.insert(word)

        res = []
        for i in range(len(text)):
            for index in trie_tree.search(text[i:]):
                res.append([i, i + index])
        return res
```

