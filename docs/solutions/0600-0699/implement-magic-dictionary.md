# [0676. 实现一个魔法字典](https://leetcode.cn/problems/implement-magic-dictionary/)

- 标签：设计、字典树、哈希表、字符串
- 难度：中等

## 题目链接

- [0676. 实现一个魔法字典 - 力扣](https://leetcode.cn/problems/implement-magic-dictionary/)

## 题目大意

**要求**：设计一个使用单词表进行初始化的数据结构。单词表中的单词互不相同。如果给出一个单词，要求判定能否将该单词中的一个字母替换成另一个字母，是的所形成的新单词已经在够构建的单词表中。

实现 MagicDictionary 类：

- `MagicDictionary()` 初始化对象。
- `void buildDict(String[] dictionary)` 使用字符串数组 `dictionary` 设定该数据结构，`dictionary` 中的字符串互不相同。
- `bool search(String searchWord)` 给定一个字符串 `searchWord`，判定能否只将字符串中一个字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 `True`；否则，返回 `False`。

**说明**：

- $1 \le dictionary.length \le 100$。
- $1 \le dictionary[i].length \le 100$。
- `dictionary[i]` 仅由小写英文字母组成。
- `dictionary` 中的所有字符串互不相同。
- $1 \le searchWord.length \le 100$。
- `searchWord` 仅由小写英文字母组成。
- `buildDict` 仅在 `search` 之前调用一次。
- 最多调用 $100$ 次 `search`。

**示例**：

- 示例 1：

```python
输入
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
输出
[null, null, false, true, false, false]

解释
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // 返回 False
magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
magicDictionary.search("hell"); // 返回 False
magicDictionary.search("leetcoded"); // 返回 False
```

## 解题思路

### 思路 1：字典树

1. 构造一棵字典树。
2. `buildDict` 方法中将所有单词存入字典树中。
3. `search` 方法中替换 `searchWord` 每一个位置上的字符，然后在字典树中查询。

### 思路 1：代码

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

### 思路 1：复杂度分析

- **时间复杂度**：初始化操作是 $O(1)$。构建操作是 $O(|dictionary|)$，搜索操作是 $O(|searchWord| \times |\sum|)$。其中 $|dictionary|$ 是字符串数组 `dictionary` 中的字符个数，$|searchWord|$ 是查询操作中字符串的长度，$|\sum|$ 是字符集的大小。
- **空间复杂度**：$O(|dicitonary|)$。