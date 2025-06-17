# [0428. 序列化和反序列化 N 叉树](https://leetcode.cn/problems/serialize-and-deserialize-n-ary-tree/)

- 标签：树、深度优先搜索、广度优先搜索、字符串
- 难度：困难

## 题目链接

- [0428. 序列化和反序列化 N 叉树 - 力扣](https://leetcode.cn/problems/serialize-and-deserialize-n-ary-tree/)

## 题目大意

要求：设计一个序列化和反序列化 N 叉树的算法。序列化 / 反序列化算法的算法实现没有限制。你只需要保证 N 叉树可以被序列化为一个字符串并且该字符串可以被反序列化成原树结构即可。

- 序列化是指将一个数据结构转化为位序列的过程，因此可以将其存储在文件中或内存缓冲区中，以便稍后在相同或不同的计算机环境中恢复结构。
- N 叉树是指每个节点都有不超过 N 个孩子节点的有根树。

## 解题思路

- 序列化：通过深度优先搜索的方式，递归遍历节点，以 `root.val`、`len(root.children)`、`root.children` 的顺序生成序列化结果，并用 `-` 链接，返回结果字符串。
- 反序列化：先将字符串按 `-` 分割成数组。然后按照 `root.val`、`len(root.children)`、`root.children` 的顺序解码，并建立对应节点。最后返回根节点。



## 代码

```python
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return 'None'

        data = str(root.val) + '-' + str(len(root.children))
        for child in root.children:
            data += '-' + self.serialize(child)
        return data
        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        datalist = data.split('-')
        return self.dfs(datalist)

    def dfs(self, datalist):
        val = datalist.pop(0)
        if val == 'None':
            return None
        root = Node(int(val))
        root.children = []

        size = int(datalist.pop(0))
        for _ in range(size):
            root.children.append(self.dfs(datalist))
        return root
```

