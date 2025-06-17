# [LCR 063. 单词替换](https://leetcode.cn/problems/UhWRSj/)

- 标签：字典树、数组、哈希表、字符串
- 难度：中等

## 题目链接

- [LCR 063. 单词替换 - 力扣](https://leetcode.cn/problems/UhWRSj/)

## 题目大意

给定一个由许多词根组成的字典列表 `dictionary`，以及一个句子字符串 `sentence`。

要求：将句子中有词根的单词用词根替换掉。如果单词有很多词根，则用最短的词根替换掉他。最后输出替换之后的句子。

## 解题思路

将所有的词根存入到前缀树（字典树）中。然后在树上查找每个单词的最短词根。

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


    def search(self, word: str) -> str:
        """
        Returns if the word is in the trie.
        """
        cur = self
        index = 0
        for ch in word:
            if ch not in cur.children:
                return word
            cur = cur.children[ch]
            index += 1
            if cur.isEnd:
                break
        return word[:index]


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie_tree = Trie()
        for word in dictionary:
            trie_tree.insert(word)

        words = sentence.split(" ")
        size = len(words)
        for i in range(size):
            word = words[i]
            words[i] = trie_tree.search(word)
        return ' '.join(words)
```

