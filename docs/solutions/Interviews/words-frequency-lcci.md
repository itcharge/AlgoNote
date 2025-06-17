# [面试题 16.02. 单词频率](https://leetcode.cn/problems/words-frequency-lcci/)

- 标签：设计、字典树、数组、哈希表、字符串
- 难度：中等

## 题目链接

- [面试题 16.02. 单词频率 - 力扣](https://leetcode.cn/problems/words-frequency-lcci/)

## 题目大意

要求：设计一个方法，找出任意指定单词在一本书中的出现频率。

支持如下操作：

- `WordsFrequency(book)` 构造函数，参数为字符串数组构成的一本书。
- `get(word)` 查询指定单词在书中出现的频率。

## 解题思路

使用字典树统计单词频率。

构造函数时，构建一个字典树，并将所有单词存入字典树中，同时在字典树中记录并维护单词频率。

查询时，调用字典树查询方法，查询单词频率。

## 代码

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False
        self.count = 0


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
        cur.count += 1


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        if cur and cur.isEnd:
            return cur.count
        return 0

class WordsFrequency:

    def __init__(self, book: List[str]):
        self.tire_tree = Trie()
        for word in book:
            self.tire_tree.insert(word)


    def get(self, word: str) -> int:
        return self.tire_tree.search(word)
```

