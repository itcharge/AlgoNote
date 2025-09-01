# [1032. 字符流](https://leetcode.cn/problems/stream-of-characters/)

- 标签：设计、字典树、数组、字符串、数据流
- 难度：困难

## 题目链接

- [1032. 字符流 - 力扣](https://leetcode.cn/problems/stream-of-characters/)

## 题目大意

**描述**：设计一个算法：接收一个字符流，并检查这些字符的后缀是否是字符串数组 $words$ 中的一个字符串。

**要求**：

按下述要求实现 StreamChecker 类：

- `StreamChecker(String[] words):` 构造函数，用字符串数组 $words$ 初始化数据结构。
- `boolean query(char letter)：` 从字符流中接收一个新字符，如果字符流中的任一非空后缀能匹配 $words$ 中的某一字符串，返回 $True$；否则，返回 $False$。

**说明**：

- $1 \le words.length \le 2000$。
- $1 <= words[i].length <= 200$。
- $words[i]$ 由小写英文字母组成。
- $letter$ 是一个小写英文字母。
- 最多调用查询 $4 \times 10^4$ 次。

**示例**：

- 示例 1：

```python
输入：
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
输出：
[null, false, false, false, true, false, true, false, false, false, false, false, true]

解释：
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // 返回 False
streamChecker.query("b"); // 返回 False
streamChecker.query("c"); // 返回n False
streamChecker.query("d"); // 返回 True ，因为 'cd' 在 words 中
streamChecker.query("e"); // 返回 False
streamChecker.query("f"); // 返回 True ，因为 'f' 在 words 中
streamChecker.query("g"); // 返回 False
streamChecker.query("h"); // 返回 False
streamChecker.query("i"); // 返回 False
streamChecker.query("j"); // 返回 False
streamChecker.query("k"); // 返回 False
streamChecker.query("l"); // 返回 True ，因为 'kl' 在 words 中
```

## 解题思路

这道题要求设计一个数据结构，能够实时检查字符流中的后缀是否匹配给定的单词集合。由于字符流是动态的，我们需要高效地处理每个新字符的查询。

### 思路 1：字典树 + 字符串反转

**问题分析**：
- 需要检查字符流中的后缀是否匹配单词集合中的任意单词
- 字符流是动态添加的，直接存储所有可能的后缀会非常低效
- 字典树适合前缀匹配，但我们需要后缀匹配

**核心思想**：
将后缀匹配问题转化为前缀匹配问题：将所有单词反转后插入字典树，这样检查后缀就变成了检查前缀。

**算法步骤**：
1. **初始化**：将所有单词反转后插入字典树中
2. **查询处理**：每次接收到新字符时，将其添加到字符流的前面
3. **匹配检查**：在字典树中搜索当前字符流，找到匹配的单词就返回 `True`

**关键优化**：
- 使用反转的单词构建字典树，将后缀匹配转化为前缀匹配
- 在搜索过程中，一旦找到匹配的单词就立即返回，避免不必要的继续搜索

**示例分析**：
- 单词集合：`["cd", "f", "kl"]` → 插入字典树：`["dc", "f", "lk"]`
- 字符流 `"cd"` → 检查 `"dc"` 是否在字典树中 → 匹配成功，返回 `True`


### 思路 1：代码

```python
class Node:                                     # 字符节点
    def __init__(self):                         # 初始化字符节点
        self.children = dict()                  # 初始化子节点
        self.isEnd = False                      # isEnd 用于标记单词结束
        
        
class Trie:                                     # 字典树
    
    # 初始化字典树
    def __init__(self):                         # 初始化字典树
        self.root = Node()                      # 初始化根节点（根节点不保存字符）

    # 向字典树中插入一个单词
    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:                         # 遍历单词中的字符
            if ch not in cur.children:          # 如果当前节点的子节点中，不存在键为 ch 的节点
                cur.children[ch] = Node()       # 建立一个节点，并将其保存到当前节点的子节点
            cur = cur.children[ch]              # 令当前节点指向新建立的节点，继续处理下一个字符
        cur.isEnd = True                        # 单词处理完成时，将当前节点标记为单词结束

    # 查找字典树中是否存在一个单词
    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:                         # 遍历单词中的字符
            if ch not in cur.children:          # 如果当前节点的子节点中，不存在键为 ch 的节点
                return False                    # 直接返回 False
            cur = cur.children[ch]              # 令当前节点指向新建立的节点，然后继续查找下一个字符
            if cur.isEnd:
                return True
        return False

    # 查找字典树中是否存在一个前缀
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:                       # 遍历前缀中的字符
            if ch not in cur.children:          # 如果当前节点的子节点中，不存在键为 ch 的节点
                return False                    # 直接返回 False
            cur = cur.children[ch]              # 令当前节点指向新建立的节点，然后继续查找下一个字符
        return cur is not None                  # 判断当前节点是否为空，不为空则查找成功

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = ""
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream = letter + self.stream
        size = len(letter)

        return self.trie.search(self.stream)



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - 初始化：$O(m \times n)$，其中 $m$ 是单词数量，$n$ 是单词的平均长度。
  - 查询：$O(k)$，其中 $k$ 是当前字符流的长度。最坏情况下，每次查询都需要遍历整个字符流。
- **空间复杂度**：$O(m \times n)$，字典树的空间复杂度，其中 $m$ 是单词数量，$n$ 是单词的平均长度。

### 思路 2：AC 自动机

**问题分析**：
- 需要处理多模式串匹配问题，适合使用 AC 自动机
- 字符流查询频率高，需要优化查询时间复杂度
- 不需要存储完整的字符流历史，只需要维护当前匹配状态

**核心思想**：
使用 AC 自动机（Aho-Corasick Automaton）进行多模式串匹配：
1. 将所有单词构建成AC自动机，利用字典树共享公共前缀
2. 为每个节点设置失配指针，实现匹配失败时的快速跳转
3. 维护当前匹配状态，每次接收新字符时更新状态并检查匹配

**算法步骤**：
1. **构建AC自动机**：将所有单词插入字典树，并构建失配指针
2. **维护匹配状态**：使用变量记录当前在AC自动机中的位置
3. **字符流处理**：每次接收新字符时，沿着AC自动机进行状态转移
4. **匹配检测**：检查当前状态及其失配链上是否有单词结尾

**关键优势**：
- **时间复杂度优秀**：构建 $O(m)$，查询平均 $O(1)$
- **空间效率高**：共享公共前缀，节省存储空间
- **适合流式处理**：不需要存储整个字符流历史

### 思路 2：代码

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

class StreamChecker:
    def __init__(self, words):
        self.ac = AC_Automaton()
        # 将所有单词插入AC自动机
        for word in words:
            self.ac.add_word(word)
        # 构建失配指针
        self.ac.build_fail_pointers()
        # 当前匹配状态
        self.current_node = self.ac.root

    def query(self, letter):
        """
        处理新字符，检查是否匹配到任何单词
        """
        # 如果当前节点没有该字符的子节点，则沿 fail 指针向上跳转
        while self.current_node is not self.ac.root and letter not in self.current_node.children:
            self.current_node = self.current_node.fail
        
        # 如果有该字符的子节点，则转移到该子节点
        if letter in self.current_node.children:
            self.current_node = self.current_node.children[letter]
        # 否则仍然停留在根节点

        # 检查当前节点以及沿 fail 链上的所有节点是否为单词结尾
        temp = self.current_node
        while temp is not self.ac.root:
            if temp.is_end:
                return True  # 找到匹配的单词
            temp = temp.fail
        
        return False  # 没有找到匹配的单词


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
```

### 思路 2：复杂度分析

- **时间复杂度**：
  - 初始化：$O(m)$，其中 $m$ 是所有单词的总长度。构建字典树和失配指针都是线性时间。
  - 查询：$O(1)$ 平均情况，$O(k)$ 最坏情况，其中 $k$ 是单词的最大长度。由于失配指针的存在，大部分情况下可以快速跳转。
- **空间复杂度**：$O(m)$，其中 $m$ 是所有单词的总长度。AC自动机的空间复杂度主要由字典树决定。
