# [1166. 设计文件系统](https://leetcode.cn/problems/design-file-system/)

- 标签：设计、字典树、哈希表、字符串
- 难度：中等

## 题目链接

- [1166. 设计文件系统 - 力扣](https://leetcode.cn/problems/design-file-system/)

## 题目大意

**描述**：需要设计一个简单的文件系统，可以创建路径并关联值。

路径格式：以 `/` 开头，后面跟一个或多个小写英文字母。比如 `"/leetcode"` 和 `"/leetcode/problems"` 都是有效路径。空字符串 `""` 和 `"/"` 不是有效路径。

**要求**：实现 `FileSystem` 类：

- `bool createPath(string path, int value)`：创建一个新路径并关联 `value`。如果路径已存在，或父路径不存在，返回 `false`；创建成功返回 `true`。
- `int get(string path)`：返回路径关联的值，路径不存在返回 `-1`。

**说明**：

- 两个方法的调用次数加起来不超过 $10^{4}$。
- $2 \le path.length \le 10^{3}$。
- $1 \le value \le 10^{9}$。

**示例**：

```python
输入：
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
输出：
[null,true,1]
解释：
创建 "/a" → 成功，然后 get("/a") → 返回 1
```

```python
输入：
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
输出：
[null,true,true,2,false,-1]
解释：
创建 "/leet" → 成功
创建 "/leet/code" → 成功（父路径 "/leet" 已存在）
get("/leet/code") → 返回 2
创建 "/c/d" → 失败（父路径 "/c" 不存在）
get("/c") → 返回 -1（路径不存在）
```

## 解题思路

### 思路 1：哈希表

这个文件系统的设计其实很简单，可以用一个哈希表（可以想象成一本超级电话簿，记着「路径 → 值」的对应关系）来存储所有路径和对应的值。

关键在于 `createPath` 时的两个检查：

1. **路径不能重复创建。** 如果路径已经存在，说明是重复创建，返回 `false`。
2. **父路径必须已经存在。** 文件系统中，不能直接在有父目录之前创建子目录。比如想创建 `"/a/b"`，必须先有 `"/a"`。

父路径的判断方法：找到路径中最后一个 `/` 之前的部分。
- 比如 `"/leet/code"` 的最后一个 `/` 之前是 `"/leet"`，这就是父路径。
- 特别地，像 `"/a"` 这种只有一级的路径，它的父路径是空字符串 `""`，这种情况直接允许创建（因为不需要父路径）。

**步骤拆解：**

1. **`__init__`：** 初始化一个空字典 `self.paths = {}`。

2. **`createPath(path, value)`：**
   - 如果 `path` 已经在字典中 → 返回 `false`。
   - 找出父路径：用 `rsplit('/', 1)` 从右边切一刀，取第一部分。
   - 如果父路径不是空字符串（即有多级），而且父路径不在字典中 → 返回 `false`。
   - 通过检查后，存入字典，返回 `true`。

3. **`get(path)`：**
   - 直接从字典中查，存在返回值，不存在返回 `-1`。

### 思路 1：代码

```python
class FileSystem:

    def __init__(self):
        # 用一个字典存储「路径 → 值」的映射
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        # 规则 1：路径不能重复创建
        if path in self.paths:
            return False
        
        # 找到父路径：去掉最后一个 "/" 及其后面的部分
        # 比如 "/leet/code" → 父路径是 "/leet"
        # "/a" → 父路径是 ""（空字符串）
        parent_path = path.rsplit('/', 1)[0]
        
        # 规则 2：父路径必须已存在（根级别路径除外）
        if parent_path != "" and parent_path not in self.paths:
            return False
        
        # 通过检查，创建路径
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        # 字典查询，存在返回值，不存在返回 -1
        return self.paths.get(path, -1)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `createPath`：$O(|path|)$，用人话说就是操作时间和路径长度成正比，因为要找到父路径。
  - `get`：$O(1)$，字典查询，一查就有。
- **空间复杂度**：$O(n \times |path|)$，其中 $n$ 是创建的路径数量。
