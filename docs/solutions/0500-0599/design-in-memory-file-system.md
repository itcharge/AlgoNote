# [0588. 设计内存文件系统](https://leetcode.cn/problems/design-in-memory-file-system/)

- 标签：设计、字典树、哈希表、字符串、排序
- 难度：困难

## 题目链接

- [0588. 设计内存文件系统 - 力扣](https://leetcode.cn/problems/design-in-memory-file-system/)

## 题目大意

**描述**：

设计一个内存文件系统，模拟以下功能：

**要求**：

实现 FileSystem 类：

- `FileSystem()` 初始化系统对象。
- `List<String> ls(String path)` 如果 $path$ 是文件路径，返回一个列表，包含这个文件的名字；如果 $path$ 是目录路径，返回该目录下所有文件和目录的名字，结果按字典序排列。
- `void mkdir(String path)` 根据给定的 $path$ 创建一个新目录。给定的目录路径不存在，如果路径中的某些目录不存在，则需要创建这些目录。
- `void addContentToFile(String filePath, String content)` 如果 $filePath$ 不存在，创建包含给定内容 $content$ 的文件；如果文件已存在，将给定的内容 $content$ 附加到原始内容之后。
- `String readContentFromFile(String filePath)` 返回 $filePath$ 下文件的内容。

**说明**：

- $1 \le path.length, filePath.length \le 100$。
- $1 \le content.length \le 50$。
- $path$ 和 $filePath$ 都是绝对路径，除非是根目录 `'/'` 自身，其他路径都是以 `'/'` 开头且不以 `'/'` 结束。
- 可以假定所有操作的参数都是有效的，即用户不会获取不存在文件的内容，或者获取不存在文件夹和文件的列表。
- 可以假定所有文件夹名字和文件名字都只包含小写字母，且同一文件夹下不会有相同名字的文件夹或文件。
- 可以假定 `addContentToFile` 中的文件的父目录都存在。
- `ls`、`mkdir`、`addContentToFile` 和 `readContentFromFile` 最多被调用 $300$ 次。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/04/28/filesystem.png)

```python
输入: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
输出:
[null,[],null,null,["a"],"hello"]

解释:
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // 返回 []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // 返回 ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // 返回 "hello"
```

## 解题思路

### 思路 1：字典树（Trie）

使用字典树结构来模拟文件系统。每个节点代表一个目录或文件。

核心设计：

1. 定义节点类 `TrieNode`，包含：
   - $children$：字典，存储子目录和文件。
   - $content$：字符串，存储文件内容（目录为空字符串）。
   - $is\_file$：布尔值，标识是否为文件。

2. 路径解析：将路径按 `'/'` 分割，过滤空字符串。

3. 各操作实现：
   - `ls`：遍历到目标节点，如果是文件返回文件名，如果是目录返回排序后的子节点列表。
   - `mkdir`：沿路径创建不存在的目录节点。
   - `addContentToFile`：沿路径创建节点，最后节点标记为文件并追加内容。
   - `readContentFromFile`：遍历到文件节点，返回内容。

### 思路 1：代码

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # 子目录/文件
        self.content = ""   # 文件内容
        self.is_file = False  # 是否为文件

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        node = self.root
        # 解析路径
        if path != "/":
            parts = path.split("/")
            for part in parts:
                if part:
                    node = node.children[part]
        
        # 如果是文件，返回文件名
        if node.is_file:
            return [path.split("/")[-1]]
        
        # 如果是目录，返回排序后的子节点列表
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        node = self.root
        parts = path.split("/")
        # 沿路径创建目录
        for part in parts:
            if part:
                if part not in node.children:
                    node.children[part] = TrieNode()
                node = node.children[part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        parts = filePath.split("/")
        # 沿路径创建节点
        for part in parts:
            if part:
                if part not in node.children:
                    node.children[part] = TrieNode()
                node = node.children[part]
        
        # 标记为文件并追加内容
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        parts = filePath.split("/")
        # 遍历到文件节点
        for part in parts:
            if part:
                node = node.children[part]
        
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `ls`：$O(m + k \log k)$，其中 $m$ 为路径深度，$k$ 为子节点数量（排序）。
  - `mkdir`：$O(m)$，其中 $m$ 为路径深度。
  - `addContentToFile`：$O(m + |content|)$，其中 $m$ 为路径深度。
  - `readContentFromFile`：$O(m)$，其中 $m$ 为路径深度。
- **空间复杂度**：$O(N)$，其中 $N$ 为所有路径和文件内容的总长度。
