# [0745. 前缀和后缀搜索](https://leetcode.cn/problems/prefix-and-suffix-search/)

- 标签：设计、字典树、数组、哈希表、字符串
- 难度：困难

## 题目链接

- [0745. 前缀和后缀搜索 - 力扣](https://leetcode.cn/problems/prefix-and-suffix-search/)

## 题目大意

**要求**：

设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。

实现 WordFilter 类：
- `WordFilter(string[] words)`：使用词典中的单词 $words$ 初始化对象。
- `f(string pref, string suff)`：返回词典中具有前缀 $pref$ 和后缀 $suff$ 的单词的下标。如果存在不止一个满足要求的下标，返回其中「最大的下标」。如果不存在这样的单词，返回 $-1$。

**说明**：

- $1 \le words.length \le 10^{4}$。
- $1 \le words[i].length \le 7$。
- $1 \le pref.length, suff.length \le 7$。
- $words[i]$、$pref$ 和 $suff$ 仅由小写英文字母组成。
- 最多对函数 $f$ 执行 $10^{4}$ 次调用。

**示例**：

- 示例 1：

```python
输入
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
输出
[null, 0]
解释
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suffix = "e" 。
```

## 解题思路

### 思路 1：字典树（Trie）

使用字典树存储所有单词，同时为每个节点存储前缀和后缀的组合。

**实现步骤**：

1. 对于每个单词 $word$，将所有可能的 `{suffix}#{word}` 形式插入字典树。
   - 例如，对于单词 `"apple"`，插入 `"e#apple"`, `"le#apple"`, `"ple#apple"`, `"pple#apple"`, `"apple#apple"`, `"#apple"`。
2. 查询时，将 `pref` 和 `suff` 组合成 `{suff}#{pref}`，在字典树中查找。
3. 每个节点存储经过该节点的最大索引。

### 思路 1：代码

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.weight = -1  # 存储最大索引

class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        
        # 对于每个单词，插入所有可能的 {suffix}#{word} 形式
        for index, word in enumerate(words):
            word_len = len(word)
            # 遍历所有后缀（包括空后缀）
            for i in range(word_len + 1):
                suffix = word[i:]
                # 插入 suffix#word
                key = suffix + '#' + word
                node = self.root
                for char in key:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                    node.weight = index  # 更新最大索引

    def f(self, pref: str, suff: str) -> int:
        # 查找 suff#pref
        key = suff + '#' + pref
        node = self.root
        for char in key:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.weight


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - 初始化：$O(n \times L^2)$，其中 $n$ 是单词数量，$L$ 是单词的平均长度。
  - 查询：$O(L)$，$L$ 是前缀和后缀的长度之和。
- **空间复杂度**：$O(n \times L^2)$，字典树的空间。
