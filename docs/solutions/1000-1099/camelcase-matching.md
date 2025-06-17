# [1023. 驼峰式匹配](https://leetcode.cn/problems/camelcase-matching/)

- 标签：字典树、双指针、字符串、字符串匹配
- 难度：中等

## 题目链接

- [1023. 驼峰式匹配 - 力扣](https://leetcode.cn/problems/camelcase-matching/)

## 题目大意

**描述**：给定待查询列表 `queries`，和模式串 `pattern`。如果我们可以将小写字母（0 个或多个）插入模式串 `pattern` 中间（任意位置）得到待查询项 `queries[i]`，那么待查询项与给定模式串匹配。如果匹配，则对应答案为 `True`，否则为 `False`。

**要求**：将匹配结果存入由布尔值组成的答案列表中，并返回。

**说明**：

- $1 \le queries.length \le 100$。
- $1 \le queries[i].length \le 100$。
- $1 \le pattern.length \le 100$。
- 所有字符串都仅由大写和小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
```

- 示例 2：

```python
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
输出：[true,false,true,false,false]
解释：
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".
```

## 解题思路

### 思路 1：字典树

构建一棵字典树，将 `pattern` 存入字典树中。

1. 对于 `queries[i]` 中的每个字符串。逐个字符与 `pattern` 进行匹配。
   1. 如果遇见小写字母，直接跳过。
   2. 如果遇见大写字母，但是不能匹配，返回 `False`。
   3. 如果遇见大写字母，且可以匹配，继续查找。
   4. 如果到达末尾仍然匹配，则返回 `True`。
2. 最后将所有结果存入答案数组中返回。

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
            if ord(ch) > 96:
                if ch not in cur.children:
                    continue
            else:
                if ch not in cur.children:
                    return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie_tree = Trie()
        trie_tree.insert(pattern)
        res = []
        for query in queries:
            res.append(trie_tree.search(query))
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times |T| + |pattern|)$。其中 $n$ 是待查询项的数目，$|T|$  是最长的待查询项的字符串长度，$|pattern|$ 是字符串 `pattern` 的长度。
- **空间复杂度**：$O(|pattern|)$。

