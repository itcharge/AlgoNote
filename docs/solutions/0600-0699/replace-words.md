# [0648. 单词替换](https://leetcode.cn/problems/replace-words/)

- 标签：字典树、数组、哈希表、字符串
- 难度：中等

## 题目链接

- [0648. 单词替换 - 力扣](https://leetcode.cn/problems/replace-words/)

## 题目大意

**描述**：给定一个由许多词根组成的字典列表 `dictionary`，以及一个句子字符串 `sentence`。

**要求**：将句子中有词根的单词用词根替换掉。如果单词有很多词根，则用最短的词根替换掉他。最后输出替换之后的句子。

**说明**：

- $1 \le dictionary.length \le 1000$。
- $1 \le dictionary[i].length \le 100$。
- `dictionary[i]` 仅由小写字母组成。
- $1 \le sentence.length \le 10^6$。
- `sentence` 仅由小写字母和空格组成。
- `sentence` 中单词的总量在范围 $[1, 1000]$ 内。
- `sentence` 中每个单词的长度在范围 $[1, 1000]$ 内。
- `sentence` 中单词之间由一个空格隔开。
- `sentence` 没有前导或尾随空格。

**示例**：

- 示例 1：

```python
输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
```

- 示例 2：

```python
输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"
```

## 解题思路

### 思路 1：字典树

1. 构造一棵字典树。
2. 将所有的词根存入到前缀树（字典树）中。
3. 然后在树上查找每个单词的最短词根。

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

### 思路 1：复杂度分析

- **时间复杂度**：$O(|dictionary| + |sentence|)$。其中 $|dictionary|$ 是字符串数组 `dictionary` 中的字符总数，$|sentence|$ 是字符串 `sentence` 的字符总数。
- **空间复杂度**：$O(|dictionary| + |sentence|)$。