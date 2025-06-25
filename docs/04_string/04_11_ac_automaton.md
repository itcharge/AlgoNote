## 1. AC 自动机简介

> **AC 自动机（Aho-Corasick Automaton）**：该算法在 1975 年产生于贝尔实验室，是最著名的多模式匹配算法之一。简单来说，AC 自动机是以 **字典树（Trie）** 的结构为基础，结合 **KMP 算法思想** 建立的。

AC 自动机的构造有 3 个步骤：

1. 构造一棵字典树（Trie），作为 AC 自动机的搜索数据结构。
2. 利用 KMP 算法思想，构造失配指针。使得当前字符失配时可以通过失配指针跳转到具有最长公共前后缀的字符位置上继续匹配。
3. 扫描文本串进行匹配。

## 2. AC 自动机原理

接下来我们以一个例子来说明一下 AC 自动机的原理。

> 描述：给定 5 个单词，分别是 `say`、`she`、`shr`、`he`、`her`，再给定一个文本串 `yasherhs`。
>
> 要求：计算出有多少个单词在文本串中出现过。

### 2.1 构造一棵字典树（Trie）

首先我们需要建立一棵字典树。字典树是一种树形数据结构，用于高效地存储和检索字符串集合。每个节点代表一个字符，从根节点到某个节点的路径上的字符连接起来，就是该节点对应的字符串。

对于给定的 5 个单词，构造的字典树如下：

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

失配指针（fail pointer）是 AC 自动机的核心。当在字典树中匹配失败时，失配指针指向另一个节点，该节点对应的字符串是当前节点对应字符串的最长后缀。

失配指针的构造过程：
1. 根节点的失配指针指向空
2. 对于每个节点，其失配指针指向其父节点的失配指针指向的节点的对应子节点
3. 如果对应子节点不存在，则继续沿着失配指针向上查找

### 2.3 扫描文本串

扫描文本串的过程：
1. 从根节点开始，按照文本串的字符顺序在字典树中移动
2. 如果当前字符匹配成功，继续移动到下一个字符
3. 如果当前字符匹配失败，通过失配指针跳转到另一个节点继续匹配
4. 当到达某个单词的结束节点时，说明找到了一个匹配的单词

## 3. AC 自动机的应用

AC 自动机在以下场景中有着广泛的应用：

1. **多模式字符串匹配**：在文本中查找多个模式串
2. **敏感词过滤**：检测文本中是否包含敏感词
3. **DNA序列分析**：在生物信息学中用于DNA序列的模式匹配
4. **网络入侵检测**：检测网络数据包中的恶意模式
5. **拼写检查**：检查文本中的拼写错误

## 4. AC 自动机的实现

### 4.1 时间复杂度

- 构建字典树：O(Σ|P|)，其中 P 是所有模式串的集合
- 构建失配指针：O(Σ|P|)
- 文本串匹配：O(n + k)，其中 n 是文本串长度，k 是匹配的模式串数量

### 4.2 空间复杂度

- O(Σ|P|)，其中 Σ 是字符集大小

## 5. 代码实现

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # 子节点
        self.fail = None    # 失配指针
        self.is_end = False # 是否是单词结尾
        self.word = ""      # 存储完整的单词

class AC_Automaton:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.word = word
    
    def build_fail_pointers(self):
        queue = []
        # 将根节点的子节点的失配指针指向根节点
        for char, node in self.root.children.items():
            node.fail = self.root
            queue.append(node)
        
        # 广度优先搜索构建失配指针
        while queue:
            current = queue.pop(0)
            for char, child in current.children.items():
                fail = current.fail
                while fail and char not in fail.children:
                    fail = fail.fail
                child.fail = fail.children[char] if fail else self.root
                queue.append(child)
    
    def search(self, text):
        result = []
        current = self.root
        
        for char in text:
            while current is not self.root and char not in current.children:
                current = current.fail
            if char in current.children:
                current = current.children[char]
            
            # 检查当前节点是否是某个单词的结尾
            temp = current
            while temp is not self.root:
                if temp.is_end:
                    result.append(temp.word)
                temp = temp.fail
        
        return result
```

## 6. 总结

AC 自动机是一种高效的多模式匹配算法，它通过结合字典树和 KMP 算法的思想，实现了在文本串中快速查找多个模式串的功能。虽然其实现相对复杂，但在需要多模式匹配的场景下，AC 自动机提供了最优的时间复杂度。