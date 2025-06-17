# [0642. 设计搜索自动补全系统](https://leetcode.cn/problems/design-search-autocomplete-system/)

- 标签：设计、字典树、字符串、数据流
- 难度：困难

## 题目链接

- [0642. 设计搜索自动补全系统 - 力扣](https://leetcode.cn/problems/design-search-autocomplete-system/)

## 题目大意

要求：设计一个搜索自动补全系统。用户会输入一条语句（最少包含一个字母，以特殊字符 `#` 结尾）。除 `#` 以外用户输入的每个字符，返回历史中热度前三并以当前输入部分为前缀的句子。下面是详细规则：

- 一条句子的热度定义为历史上用户输入这个句子的总次数。
- 返回前三的句子需要按照热度从高到低排序（第一个是最热门的）。如果有多条热度相同的句子，请按照 ASCII 码的顺序输出（ASCII 码越小排名越前）。
- 如果满足条件的句子个数少于 3，将它们全部输出。
- 如果输入了特殊字符，意味着句子结束了，请返回一个空集合。

你的工作是实现以下功能：

- 构造函数： `AutocompleteSystem(String[] sentences, int[] times):` 
  - 输入历史数据。 `sentences` 是之前输入过的所有句子，`times` 是每条句子输入的次数，你的系统需要记录这些历史信息。

- 输入函数（用户输入一条新的句子，下面的函数会提供用户输入的下一个字符）：`List<String> input(char c):` 
  - 其中 `c` 是用户输入的下一个字符。字符只会是小写英文字母（`a` 到 `z` ），空格（` `）和特殊字符（`#`）。输出历史热度前三的具有相同前缀的句子。

## 解题思路

使用字典树来保存输入过的所有句子 `sentences`，并且在字典树中维护每条句子的输入次数 `times`。

构造函数中：

- 将所有句子及对应输入次数插入到字典树中。

输入函数中：

- 使用 `path` 变量保存当前输入句子的前缀。
- 如果遇到 `#`，则将当前句子插入到字典树中。
- 如果遇到其他字符，用 `path` 保存当前字符 `c`。并在字典树中搜索以 `path` 为前缀的节点的所有分支，将每个分支对应的单词 `path` 和它们出现的次数 `times` 存入数组中。然后借助 `heapq` 进行堆排序，根据出现次数和 ASCII 码大小排序，找出 `times` 最多的前三个单词。

## 代码

```python
import heapq

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False
        self.times = 0


    def insert(self, word: str, times=1) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True
        cur.times += times


    def search(self, word: str):
        """
        Returns if the word is in the trie.
        """
        cur = self

        for ch in word:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]

        res = []
        path = [word]
        cur.dfs(res, path)
        return res


    def dfs(self, res, path):
        cur = self
        if cur.isEnd:
            res.append((-cur.times, ''.join(path)))
        for ch in cur.children:
            node = cur.children[ch]
            path.append(ch)
            node.dfs(res, path)
            path.pop()


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.path = ''
        self.exists = True
        self.trie_tree = Trie()
        for i in range(len(sentences)):
            self.trie_tree.insert(sentences[i], times[i])


    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie_tree.insert(self.path, 1)
            self.path = ''
            self.exists = True
            return []
        else:
            self.path += c
            if not self.exists:
                return []
            words = self.trie_tree.search(self.path)
            if words:
                heapq.heapify(words)
                res = []
                while words and len(res) < 3:
                    res.append(heapq.heappop(words)[1])
                return res
            else:
                self.exists = False
                return []
```

