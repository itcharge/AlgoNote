# [LCR 064. 实现一个魔法字典](https://leetcode.cn/problems/US1pGT/)

- 标签：设计、字典树、哈希表、字符串
- 难度：中等

## 题目链接

- [LCR 064. 实现一个魔法字典 - 力扣](https://leetcode.cn/problems/US1pGT/)

## 题目大意

要求：设计一个使用单词表进行初始化的数据结构。单词表中的单词互不相同。如果给出一个单词，要求判定能否将该单词中的一个字母替换成另一个字母，是的所形成的新单词已经在够构建的单词表中。

实现 MagicDictionary 类：

- `MagicDictionary()` 初始化对象。
- `void buildDict(String[] dictionary)` 使用字符串数组 `dictionary` 设定该数据结构，`dictionary` 中的字符串互不相同。
- `bool search(String searchWord)` 给定一个字符串 `searchWord`，判定能否只将字符串中一个字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 `True`；否则，返回 `False`。

## 解题思路

- 初始化使用字典树结构。

- `buildDict` 方法中将所有单词存入字典树中。

- `search` 方法中替换 `searchWord` 每一个位置上的字符，然后在字典树中查询。

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

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_tree = Trie()


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie_tree.insert(word)


    def search(self, searchWord: str) -> bool:
        size = len(searchWord)
        for i in range(size):
            for j in range(26):
                new_ch = chr(ord('a') + j)
                if searchWord[i] != new_ch:
                    new_word = searchWord[:i] + new_ch + searchWord[i + 1:]
                    if self.trie_tree.search(new_word):
                        return True
        return False
```

