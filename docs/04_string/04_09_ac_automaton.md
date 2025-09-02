## 1. AC 自动机简介

> **AC 自动机（Aho-Corasick Automaton）**：由 Alfred V. Aho 和 Margaret J. Corasick 于 1975 年在贝尔实验室提出，是最著名的多模式匹配算法之一。
>
> - **AC 自动机核心思想**：以 **字典树（Trie）** 为基础，结合 **KMP 算法的失配指针思想**，构建一个能够同时匹配多个模式串的有限状态自动机。当在文本串中匹配失败时，通过失配指针快速跳转到下一个可能匹配的状态，避免重复比较，实现高效的多模式匹配。

### 1.1 多模式匹配的难点

在实际应用中，常常需要在文本中一次性查找多个模式串（如敏感词过滤、病毒检测、DNA 序列分析等）。

传统的单模式匹配算法（如 KMP、Boyer-Moore）需要对每个模式串分别进行匹配，时间复杂度为 $O(n \times m \times k)$，其中 $n$ 为文本长度，$m$ 为模式串平均长度，$k$ 为模式串数量，整体效率较低。

如果只使用字典树（Trie），虽然能够共享前缀，但每次匹配失败都必须回到根节点重新开始，无法实现高效跳转，最坏情况下复杂度也接近 $O(n \times m)$。




### 1.2 AC 自动机高效匹配原理

AC 自动机能够高效解决多模式匹配问题，其核心思想是：将所有模式串构建为一棵字典树（Trie），并为每个节点设置失配指针（fail 指针），结合 KMP 算法的失配机制，实现对文本串的一次扫描即可同时匹配多个模式串。

AC 自动机的主要流程如下：

1. **构建字典树（Trie）**：将所有模式串插入字典树，充分利用公共前缀，节省空间和比较次数。
2. **构建失配指针（fail 指针）**：借鉴 KMP 算法思想，为字典树中每个节点添加失配指针。失配指针指向当前节点对应字符串的最长可用后缀节点，实现匹配失败时的快速跳转，避免重复比较。
3. **一次扫描文本串进行匹配**：只需从头到尾扫描一遍文本串，利用字典树和失配指针的协同作用，即可高效找到所有模式串的出现位置。

AC 自动机的时间复杂度为 $O(n + m + k)$，其中 $n$ 为文本串长度，$m$ 为所有模式串的总长度，$k$ 为匹配到的模式串数量。相比传统的多模式串逐一匹配方法（如 $O(n \times m \times k)$），AC 自动机大幅提升了匹配效率。

## 2. AC 自动机原理

下面用一个简单例子来直观理解 AC 自动机的原理。

> **例子**：给定 5 个模式串：`say`、`she`、`shr`、`he`、`her`，文本串为 `yasherhs`。
>
> **目标**：找出文本中所有出现的模式串及其位置。

### 2.1 构建字典树（Trie）

我们先把所有模式串插入到一棵字典树中。字典树就像一棵「分叉的路」，每个节点代表一个字符，从根到某节点的路径，就是一个字符串。

以这 5 个模式串为例，字典树结构如下：

```
        root
       /    \
      s      h
     / \     |
    a   h    e
   /   / \    \
  y   e   r    r
```

### 2.2 构造失配指针

失配指针（fail 指针）是 AC 自动机的关键。它借鉴 KMP 算法的思想，为每个节点指向其「最长可用后缀」在字典树中的节点，实现失配时的快速跳转。

#### 2.2.1 失配指针的定义

对于字典树中的任意节点，其失配指针指向该节点对应字符串的 **最长真后缀** 在字典树中的节点。

- **真后缀**：字符串的真后缀是指该字符串的后缀，但不等于字符串本身。

#### 2.2.2 构造规则

失配指针的构造遵循以下规则：

1. **根节点**：失配指针为 `null`
2. **根节点的子节点**：失配指针都指向根节点
3. **其他节点**：从父节点的失配指针开始查找，如果找到对应字符的子节点，则指向该子节点；否则继续向上查找，直到找到或到达根节点

#### 2.2.3 构造示例

以模式串 `["say", "she", "shr", "he", "her"]` 为例：

```
        root
       /    \
      s      h
     / \     |
    a   h    e
   /   / \    \
  y   e   r    r
```

**失配指针构造过程**：
- `s` → `root`（根节点子节点指向根节点）
- `h` → `root`（根节点子节点指向根节点）
- `sa` → `root`（根节点没有 `a` 子节点）
- `sh` → `h`（根节点有 `h` 子节点）
- `he` → `e`（根节点有 `e` 子节点）
- `hr` → `root`（根节点没有 `r` 子节点）
- `say` → `root`（根节点没有 `y` 子节点）
- `she` → `he`（`h` 节点有 `e` 子节点）
- `shr` → `root`（`h` 和根节点都没有 `r` 子节点）
- `her` → `root`（`e` 和根节点都没有 `r` 子节点）

#### 2.2.4 失配指针的作用

失配指针的主要作用是：
1. **快速跳转**：匹配失败时，不需要回到根节点重新开始
2. **避免重复比较**：利用已匹配的部分信息，避免重复比较
3. **保证匹配连续性**：确保跳转后当前匹配的字符串仍是某个模式串的前缀

### 2.3 文本串匹配过程

有了字典树和失配指针，我们就可以进行高效的文本串匹配了。

#### 2.3.1 匹配算法流程

1. **初始化**：从根节点开始
2. **字符匹配**：对于文本串中的每个字符：
   - 如果当前节点有对应字符的子节点，移动到该子节点
   - 否则，沿着失配指针向上查找，直到找到匹配的子节点或到达根节点
3. **模式串检测**：每到达一个节点，检查该节点是否为某个模式串的结尾
4. **输出匹配结果**：如果找到匹配的模式串，记录其位置和内容

#### 2.3.2 匹配过程示例

以文本串 `yasherhs` 为例，演示匹配过程：

| 字符 | 当前节点 | 操作 | 当前路径 | 匹配结果 |
|------|----------|------|----------|----------|
| `y` | 根节点 | 无匹配，保持根节点 | - | - |
| `a` | 根节点 | 无匹配，保持根节点 | - | - |
| `s` | 根节点 | 移动到 `s` 节点 | `s` | - |
| `h` | `s` 节点 | 移动到 `sh` 节点 | `sh` | - |
| `e` | `sh` 节点 | 移动到 `she` 节点 | `she` | **找到 `she`** |
| `r` | `she` 节点 | 失配，跳转到根节点 | - | - |
| `h` | 根节点 | 移动到 `h` 节点 | `h` | - |
| `s` | `h` 节点 | 失配，跳转到根节点，再移动到 `s` 节点 | `s` | - |

**最终结果**：在文本串 `yasherhs` 中找到模式串 `she`（位置 2-4）。


## 3. AC 自动机代码实现


```python
class TrieNode:
    def __init__(self):
        self.children = {}      # 子节点，key 为字符，value 为 TrieNode
        self.fail = None        # 失配指针，指向当前节点最长可用后缀的节点
        self.is_end = False     # 是否为某个模式串的结尾
        self.word = ""          # 如果是结尾，存储完整的单词

class AC_Automaton:
    def __init__(self):
        self.root = TrieNode()  # 初始化根节点

    def add_word(self, word):
        """
        向Trie树中插入一个模式串
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # 新建子节点
            node = node.children[char]
        node.is_end = True    # 标记单词结尾
        node.word = word      # 存储完整单词

    def build_fail_pointers(self):
        """
        构建失配指针（fail指针），采用BFS广度优先遍历
        """
        from collections import deque
        queue = deque()
        # 1. 根节点的所有子节点的 fail 指针都指向根节点
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        # 2. 广度优先遍历，依次为每个节点建立 fail 指针
        while queue:
            current = queue.popleft()
            for char, child in current.children.items():
                # 从当前节点的 fail 指针开始，向上寻找有无相同字符的子节点
                fail = current.fail
                while fail and char not in fail.children:
                    fail = fail.fail
                # 如果找到了，child的fail指针指向该节点，否则指向根节点
                child.fail = fail.children[char] if fail and char in fail.children else self.root
                queue.append(child)

    def search(self, text):
        """
        在文本text中查找所有模式串出现的位置
        返回所有匹配到的模式串（可重复）
        """
        result = []
        node = self.root

        for idx, char in enumerate(text):
            # 如果当前节点没有该字符的子节点，则沿fail指针向上跳转
            while node is not self.root and char not in node.children:
                node = node.fail
            # 如果有该字符的子节点，则转移到该子节点
            if char in node.children:
                node = node.children[char]
            # 否则仍然停留在根节点

            # 检查当前节点以及沿fail链上的所有节点是否为单词结尾
            temp = node
            while temp is not self.root:
                if temp.is_end:
                    result.append(temp.word)  # 记录匹配到的模式串
                temp = temp.fail

        return result
```



## 4. AC 自动机算法分析

| 指标         | 复杂度           | 说明                                                         |
| ------------ | ---------------- | ------------------------------------------------------------ |
| 构建字典树   | $O(m)$           | $m$ 为所有模式串的总长度                                     |
| 构建失配指针 | $O(m)$           | 使用 BFS 遍历所有节点，每个节点最多被访问一次                 |
| 文本串匹配   | $O(n + k)$       | $n$ 为文本串长度，$k$ 为匹配到的模式串数量                   |
| **总体时间复杂度** | **$O(n + m + k)$** | 线性时间复杂度，非常高效                                     |
| **空间复杂度**   | $O(m)$           | 包含字典树和失配指针的存储，$m$ 为所有模式串的总长度         |


## 6. 总结

AC 自动机是一种高效的多模式匹配算法，它巧妙地结合了字典树和 KMP 算法的思想，实现了在文本串中快速查找多个模式串的功能。

**核心思想**：
- 使用字典树组织所有模式串，共享公共前缀
- 借鉴 KMP 算法的失配指针思想，实现快速状态跳转
- 通过一次扫描文本串，找到所有匹配的模式串

虽然 AC 自动机的实现相对复杂，但在需要多模式匹配的场景下，它提供了最优的时间复杂度，是处理多模式匹配问题的首选算法。

## 练习题目

- [0208. 实现 Trie (前缀树)](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/implement-trie-prefix-tree.md)
- [0677. 键值映射](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/map-sum-pairs.md)
- [1023. 驼峰式匹配](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1000-1099/camelcase-matching.md)
- [0211. 添加与搜索单词 - 数据结构设计](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/design-add-and-search-words-data-structure.md)
- [0648. 单词替换](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/replace-words.md)
- [0676. 实现一个魔法字典](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/implement-magic-dictionary.md)

- [多模式串匹配题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%A4%9A%E6%A8%A1%E5%BC%8F%E4%B8%B2%E5%8C%B9%E9%85%8D%E9%A2%98%E7%9B%AE)

## 参考资料

- 【书籍】算法训练营 陈小玉 著
- 【书籍】ACM-ICPC 程序设计系列 算法设计与实现 陈宇 吴昊 主编
- 【博文】[AC自动机 - OI Wiki](https://oi-wiki.org/string/ac-automaton/)
- 【博文】[AC自动机算法详解 - 数据结构与算法之美 - 极客时间](https://time.geekbang.org/column/article/72810)
- 【博文】[AC自动机算法详解 - 算法竞赛进阶指南](https://www.acwing.com/blog/content/405/)
- 【博文】[AC自动机算法原理与实现 - 算法笔记](https://www.algorithm-notes.org/string/ac-automaton/)