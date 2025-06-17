# [LCR 066. 键值映射](https://leetcode.cn/problems/z1R5dt/)

- 标签：设计、字典树、哈希表、字符串
- 难度：中等

## 题目链接

- [LCR 066. 键值映射 - 力扣](https://leetcode.cn/problems/z1R5dt/)

## 题目大意

要求：实现一个 MapSum 类，支持两个方法，`insert` 和 `sum`：

- `MapSum()` 初始化 MapSum 对象。
- `void insert(String key, int val)` 插入 `key-val` 键值对，字符串表示键 `key`，整数表示值 `val`。如果键 `key` 已经存在，那么原来的键值对将被替代成新的键值对。
- `int sum(string prefix)` 返回所有以该前缀 `prefix` 开头的键 `key` 的值的总和。

## 解题思路

可以构造前缀树（字典树）解题。

- 初始化时，构建一棵前缀树（字典树），并增加 `val` 变量。

- 调用插入方法时，用字典树存储 `key`，并在对应字母节点存储对应的 `val`。
- 在调用查询总和方法时，先查找该前缀 `prefix` 对应的前缀树节点，从该节点开始，递归遍历该节点的子节点，并累积子节点的 `val`，进行求和，并返回求和累加结果。

## 代码

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False
        self.value = 0


    def insert(self, word: str, value: int) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True
        cur.value = value


    def search(self, word: str) -> int:
        """
        Returns if the word is in the trie.
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return self.dfs(cur)

    def dfs(self, root) -> int:
        if not root:
            return 0
        res = root.value
        for node in root.children.values():
            res += self.dfs(node)
        return res



class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_tree = Trie()


    def insert(self, key: str, val: int) -> None:
        self.trie_tree.insert(key, val)


    def sum(self, prefix: str) -> int:
        return self.trie_tree.search(prefix)
```

