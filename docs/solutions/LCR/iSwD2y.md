# [LCR 065. 单词的压缩编码](https://leetcode.cn/problems/iSwD2y/)

- 标签：字典树、数组、哈希表、字符串
- 难度：中等

## 题目链接

- [LCR 065. 单词的压缩编码 - 力扣](https://leetcode.cn/problems/iSwD2y/)

## 题目大意

给定一个单词数组 `words`。要求对 `words` 进行编码成一个助记字符串，用来帮助记忆。`words` 中拥有相同字符后缀的单词可以合并成一个单词，比如`time` 和 `me` 可以合并成 `time`。同时每个不能再合并的单词末尾以 `#` 为结束符，将所有合并后的单词排列起来就是一个助记字符串。

要求：返回对 `words` 进行编码的最小助记字符串 `s` 的长度。

## 解题思路

构建一个字典树。然后对字符串长度进行从小到大排序。

再依次将去重后的所有单词插入到字典树中。如果出现比当前单词更长的单词，则将短单词的结尾置为 `False`，意为替换掉短单词。

然后再依次在字典树中查询所有单词，「单词长度 + 1」就是当前不能在合并的单词，累加起来就是答案。

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
            cur.isEnd = False
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
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie_tree = Trie()
        words = list(set(words))
        words.sort(key=lambda i: len(i))

        ans = 0
        for word in words:
            trie_tree.insert(word[::-1])

        for word in words:
            if trie_tree.search(word[::-1]):
                ans += len(word) + 1

        return ans
```

