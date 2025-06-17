# [面试题 17.17. 多次搜索](https://leetcode.cn/problems/multi-search-lcci/)

- 标签：字典树、数组、哈希表、字符串、字符串匹配、滑动窗口
- 难度：中等

## 题目链接

- [面试题 17.17. 多次搜索 - 力扣](https://leetcode.cn/problems/multi-search-lcci/)

## 题目大意

给定一个较长字符串 `big` 和一个包含较短字符串的数组 `smalls`。

要求：设计一个方法，根据 `smalls` 中的每一个较短字符串，对 `big` 进行搜索。输出 `smalls` 中的字符串在 `big` 里出现的所有位置 `positions`，其中 `positions[i]` 为 `smalls[i]` 出现的所有位置。

## 解题思路

构建字典树，将 `smalls` 中所有字符串存入字典树中，并在字典树中记录下插入字符串的顺序下标。

然后一重循环遍历 `big`，表示从第 `i` 位置开始的字符串 `big[i:]`。然后在字符串前缀中搜索对应的单词，将所有符合要求的单词插入顺序位置存入列表中，返回列表。

对于列表中每个单词插入下标顺序 `index` 和 `big[i:]` 来说， `i` 就是 `smalls` 中第 `index` 个字符串所对应在 `big` 中的开始位置，将其存入答案数组并返回即可。

## 代码

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False
        self.index = -1


    def insert(self, word: str, index: int) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True
        cur.index = index


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
                res.append(cur.index)
        return res

class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        trie_tree = Trie()
        for i in range(len(smalls)):
            word = smalls[i]
            trie_tree.insert(word, i)

        res = [[] for _ in range(len(smalls))]

        for i in range(len(big)):
            for index in trie_tree.search(big[i:]):
                res[index].append(i)
        return res
```

