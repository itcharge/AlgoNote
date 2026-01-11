# [0527. 单词缩写](https://leetcode.cn/problems/word-abbreviation/)

- 标签：贪心、字典树、数组、字符串、排序
- 难度：困难

## 题目链接

- [0527. 单词缩写 - 力扣](https://leetcode.cn/problems/word-abbreviation/)

## 题目大意

**描述**：

给定一个字符串数组 $words$，该数组由 **互不相同** 的若干字符串组成，需要为每个单词生成最短的唯一缩写。

缩写规则如下：

- 初始缩写由起始字母 + 省略字母的数量 + 结尾字母组成。
- 如果多个单词的缩写相同，则使用更长的前缀代替首字母，直到从单词到缩写唯一。换而言之，最终的缩写必须只能映射到一个单词。
- 如果缩写不比原词短，则保持原词。

**要求**：

返回每个单词的最短唯一缩写列表。

**说明**：

- $1 \le words.length \le 400$。
- $2 \le words[i].length \le 400$。
- $words[i]$ 由小写英文字母组成。
- 所有 $words[i]$ 都是唯一的。

**示例**：

- 示例 1：

```python
输入: words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
输出: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
```

- 示例 2：

```python
输入：words = ["aa","aaa"]
输出：["aa","aaa"]
```

## 解题思路

### 思路 1：分组 + 字典树

每个单词的缩写规则：首字母 + 中间字符数量 + 尾字母。例如 `"like"` 缩写为 `"l2e"`。要求每个缩写唯一，不唯一时需增加前缀长度直到唯一。

**算法步骤**：

1. 将所有单词按 (长度, 首字母, 尾字母) 分组，只有这三个属性相同的单词才可能产生冲突。
2. 对每组单词构建字典树，记录每个前缀路径经过的单词数量。
3. 对于每个单词，在字典树中查找最短的唯一前缀（即路径上 $count = 1$ 的位置）。
4. 生成缩写：如果中间部分长度大于 1，使用 $word[:k] + str(len(word)-k-1) + word[-1]$；否则保持原词。

### 思路 1：代码

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # 路径经过多少单词

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        from collections import defaultdict
        n = len(words)
        res = [''] * n
        
        # 按 (长度, 首字母, 尾字母) 分组
        groups = defaultdict(list)
        for i, word in enumerate(words):
            key = (len(word), word[0], word[-1])
            groups[key].append((word, i))
        
        # 处理每组
        for group in groups.values():
            # 构造字典树
            root = TrieNode()
            for word, _ in group:
                node = root
                for c in word:
                    node = node.children.setdefault(c, TrieNode())
                    node.count += 1
            
            # 查询每个单词的唯一前缀
            for word, idx in group:
                node = root
                prefix_len = 0
                for c in word:
                    node = node.children[c]
                    prefix_len += 1
                    if node.count == 1:
                        break
                
                # 生成缩写
                if len(word) - prefix_len - 1 > 1:
                    res[idx] = word[:prefix_len] + str(len(word) - prefix_len - 1) + word[-1]
                else:
                    res[idx] = word
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times L)$，其中 $n$ 是单词数量，$L$ 是单词的平均长度。需要构建字典树和查询前缀。
- **空间复杂度**：$O(n \times L)$，字典树节点和分组的空间开销。
