# [0425. 单词方块](https://leetcode.cn/problems/word-squares/)

- 标签：字典树、数组、字符串、回溯
- 难度：困难

## 题目链接

- [0425. 单词方块 - 力扣](https://leetcode.cn/problems/word-squares/)

## 题目大意

给定一个单词集合 `words`（没有重复）。

要求：找出其中所有的单词方块 。

- 单词方块：指从第 `k` 行和第 `k` 列 `(0 ≤ k < max(行数, 列数))` 来看都是相同的字符串。

例如，单词序列 ["ball","area","lead","lady"] 形成了一个单词方块，因为每个单词从水平方向看和从竖直方向看都是相同的。

```
b a l l
a r e a
l e a d
l a d y
```

## 解题思路

根据单词方块的第一个单词，可以推出下一个单词的前缀。

比如第一个单词是 `ball`，那么单词方块的长度是 `4 * 4`，则下一个单词（第二个单词）的前缀为 `a`。这样我们就又找到了一个以 `a` 为前缀且长度为 `4` 的单词，即 `area`，此时就变成了 `[ball, area]`。

那么下一个单词（第三个单词）的前缀为 `le`。这样我们就又找到了一个以 `le` 为前缀且长度为 `4` 的单词，即 `lead`。此时就变成了 `[ball, area, lead]`。

以此类推，就可以得到整个单词方块。

并且我们可以使用字典树（前缀树）来存储单词，并且通过回溯得到所有的解。

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


    def search(self, word: str):
        """
        Returns if the word is in the trie.
        """
        cur = self
        res = []
        for ch in word:
            if ch not in cur.children:
                return res
            cur = cur.children[ch]
        cur.dfs(word, res)
        return res

    def dfs(self, word, res):
        cur = self
        if cur and cur.isEnd:
            res.append(word)
            return
        for ch in cur.children:
            node = cur.children[ch]
            node.dfs(word + ch, res)


class Solution:

    def backtrace(self, index, size, path, res, trie_tree):
        if index == size:
            res.append(path[:])
            return
        next_prefix = ""  # 下一行的前缀
        for i in range(index):
            next_prefix += path[i][index]

        next_words_with_prefix = trie_tree.search(next_prefix)
        for word in next_words_with_prefix:
            path.append(word)
            self.backtrace(index + 1, size, path, res, trie_tree)
            path.pop(-1)


    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie_tree = Trie()
        for word in words:
            trie_tree.insert(word)
        size = len(words[0])
        res = []
        path = []
        for word in words:
            path.append(word)
            self.backtrace(1, size, path, res, trie_tree)
            path.pop(-1)
        return res
```

