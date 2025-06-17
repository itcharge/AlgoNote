# [0336. 回文对](https://leetcode.cn/problems/palindrome-pairs/)

- 标签：字典树、数组、哈希表、字符串
- 难度：困难

## 题目链接

- [0336. 回文对 - 力扣](https://leetcode.cn/problems/palindrome-pairs/)

## 题目大意

给定一组互不相同的单词列表 `words`。

要求：找出所有不同的索引对 `(i, j)`，使得列表中的两个单词 `words[i] + words[j]` ，可拼接成回文串。

## 解题思路

如果字符串 `words[i] + words[j]` 能构成一个回文串，把 `words[i]` 分成 `words_left[i]` 和 `words_right[i]` 两部分。即 `words[i] + words[j] = words_left[i] + words_right[i] + words[j]`。则：

- `words_right[i]` 本身是回文串，`words_left[i]` 和 `words[j]` 互为逆序。

同理，如果 `words[j] + word[i]` 能构成一个回文串，把 `word[i]` 分成 `words_left[i]` 和 `words_right[i]` 两部分。即 `words[j] + word[i] = words[j] + words_left[i] + words_right[i]`。则：

- `words_left[i]` 本身是回文串，`words[j]` 和 `words_right[i]` 互为逆序。

从上面的表述可以得知，`words[j]` 可以通过拆分 `words[i]` 之后逆序得出。

我们使用两重循环遍历。一重循环遍历单词列表 `words` 中的每一个单词 `words[i]`，二重循环遍历每个单词的拆分位置 `j`。然后将每一个单词 `words[i]` 拆分成 `words[i][0:j+1]` 和 `words[i][j+1:]`。然后分别判断 `words[i][0:j+1]` 的逆序和 `words[i][j+1:]` 的逆序是否在单词列表中，如果在单词列表中，则将「`words[i]` 和 `words[i][0:j+1]` 对应的索引」或者 「`words[i]` 和 `words[i][j+1:]` 对应的索引」插入到答案数组中。

至于判断 `words[i][0:j+1]` 的逆序和 `words[i][j+1:]` 的逆序是否在单词列表中，以及获取 `words[i][0:j+1]` 的逆序和 `words[i][j+1:]` 的逆序所对应单词的索引下标可以通过构建字典树的方式获取。

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

    def search(self, word: str) -> int:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return -1
            cur = cur.children[ch]

        if cur is not None and cur.isEnd:
            return cur.index
        return -1

class Solution:
    def isPalindrome(self, word: str) -> bool:
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie_tree = Trie()
        size = len(words)
        for i in range(size):
            word = words[i]
            trie_tree.insert(word, i)

        res = []
        for i in range(size):
            word = words[i]
            for j in range(len(word)):
                if self.isPalindrome(word[:j+1]):
                    temp = word[j+1:][::-1]
                    index = trie_tree.search(temp)
                    if index != i and index != -1:
                        res.append([index, i])
                        if temp == "":
                            res.append([i, index])
                if self.isPalindrome(word[j+1:]):
                    temp = word[:j+1][::-1]
                    index = trie_tree.search(temp)
                    if index != i and index != -1:
                        res.append([i, index])
        return res
```

