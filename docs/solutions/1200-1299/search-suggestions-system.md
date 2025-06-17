# [1268. 搜索推荐系统](https://leetcode.cn/problems/search-suggestions-system/)

- 标签：字典树、数组、字符串
- 难度：中等

## 题目链接

- [1268. 搜索推荐系统 - 力扣](https://leetcode.cn/problems/search-suggestions-system/)

## 题目大意

给定一个产品数组 `products` 和一个字符串 `searchWord` ，`products`  数组中每个产品都是一个字符串。

要求：设计一个推荐系统，在依次输入单词 `searchWord` 的每一个字母后，推荐 `products` 数组中前缀与 `searchWord` 相同的最多三个产品（如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个）。

- 请你以二维列表的形式，返回在输入 `searchWord` 每个字母后相应的推荐产品的列表。

## 解题思路

先将产品数组按字典序排序。

然后使用字典树结构存储每个产品，并在字典树中维护一个数组，用于表示当前前缀所对应的产品列表（只保存最多 3 个产品）。

在查询的时候，将不同前缀所对应的产品列表加入到答案数组中。

最后输出答案数组。

## 代码

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False
        self.words = list()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
            if len(cur.words) < 3:
                cur.words.append(word)
        cur.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self
        res = []
        flag = False
        for ch in word:
            if flag or ch not in cur.children:
                res.append([])
                flag = True
            else:
                cur = cur.children[ch]
                res.append(cur.words)

        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie_tree = Trie()
        for product in products:
            trie_tree.insert(product)

        return trie_tree.search(searchWord)
```

