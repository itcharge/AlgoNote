# [1258. 近义词句子](https://leetcode.cn/problems/synonymous-sentences/)

- 标签：并查集、数组、哈希表、字符串、回溯
- 难度：中等

## 题目链接

- [1258. 近义词句子 - 力扣](https://leetcode.cn/problems/synonymous-sentences/)

## 题目大意

**描述**：给定一个近义词对列表 $synonyms$ 和一个文本 $text$。$synonyms[i] = [s_i, t_i]$ 表示 $s_i$ 和 $t_i$ 是近义词。近义词关系具有传递性（如果 $a$ 和 $b$ 是近义词，$b$ 和 $c$ 是近义词，则 $a$ 和 $c$ 也是近义词）。

**要求**：找出所有可能的句子，即把 $text$ 中的每个单词替换为它的所有近义词（包括它自己）后得到的所有句子。按字典序返回。

**说明**：

- $0 \le synonyms.length \le 10$。
- $1 \le text.length \le 100$。

**示例**：

- 示例 1：

```python
输入：synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], 
     text = "I am happy today but was sad yesterday"
输出：["I am cheerful today but was sad yesterday",
      "I am cheerful today but was sorrow yesterday",
      "I am happy today but was sad yesterday",
      "I am happy today but was sorrow yesterday",
      "I am joy today but was sad yesterday",
      "I am joy today but was sorrow yesterday"]
```

## 解题思路

### 思路 1：并查集 + 回溯

#### 1. 核心思想

第一步：用并查集将所有近义词分组。具有传递性的近义词属于同一个连通分量。

第二步：将 $text$ 按空格拆分成单词列表。对于每个单词，找到它所属的近义词组（包括它自己），用回溯法生成所有可能的组合。

#### 2. 建图、遍历、标记、收集

- **建图**：并查集将近义词合并。
- **遍历**：DFS/回溯遍历每个单词的所有可选近义词。
- **标记**：无特殊标记（近义词组不会变化）。
- **收集**：所有组合成的句子。

#### 3. 具体步骤

**第 1 步**：初始化并查集，包含所有出现的单词。

**第 2 步**：遍历 $synonyms$，对每对近义词执行 $union$ 操作。

**第 3 步**：构建 $group$ 字典，键为并查集的根，值为该组的全部单词（排序）。

**第 4 步**：将 $text$ 拆分为单词列表 $words$。对每个 $words[i]$，如果它在并查集中，它所属的组就是它的全部可选替换。

**第 5 步**：回溯生成所有组合，并将结果按字典序排序。

#### 4. 结合示例走一遍

$synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]$

并查集合并后：
- 组 1：$\text{happy, joy, cheerful}$
- 组 2：$\text{sad, sorrow}$

$text = \text{"I am happy today but was sad yesterday"}$
$words = [\text{"I", "am", "happy", "today", "but", "was", "sad", "yesterday"}]$

每个单词的可选项：
- $\text{"happy"} \to \text{["cheerful", "happy", "joy"]}$
- $\text{"sad"} \to \text{["sad", "sorrow"]}$
- 其他单词 → 只有自己

回溯生成 $3 \times 2 = 6$ 种组合。

### 思路 1：代码

```python
class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        uf = UnionFind()
        # 合并近义词
        for a, b in synonyms:
            uf.union(a, b)

        # 构建同义词组
        group = {}
        for a, b in synonyms:
            root = uf.find(a)
            if root not in group:
                group[root] = set()
            group[root].add(a)
            group[root].add(b)

        # 将每个组排序
        for root in group:
            group[root] = sorted(group[root])

        # 拆分文本
        words = text.split()
        # 确定每个位置的可选项
        options = []
        for w in words:
            root = uf.find(w) if w in uf.parent else None
            if root and root in group:
                options.append(group[root])
            else:
                options.append([w])

        # 回溯生成所有句子
        ans = []
        def backtrack(i, path):
            if i == len(options):
                ans.append(' '.join(path))
                return
            for opt in options[i]:
                path.append(opt)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times k^m)$，其中 $n$ 是单词数量，$k$ 是每组近义词的平均数量，$m$ 是有近义词的单词数量。$synonyms.length \le 10$，因此 $k$ 和 $m$ 都很小，结果数量有限。
- **空间复杂度**：$O(n)$，存储并查集、分组和可选项。
