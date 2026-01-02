# [0609. 在系统中查找重复文件](https://leetcode.cn/problems/find-duplicate-file-in-system/)

- 标签：数组、哈希表、字符串
- 难度：中等

## 题目链接

- [0609. 在系统中查找重复文件 - 力扣](https://leetcode.cn/problems/find-duplicate-file-in-system/)

## 题目大意

**描述**：

给定一个目录信息列表 $paths$，包括目录路径，以及该目录中的所有文件及其内容。

一组重复的文件至少包括「两个」具有完全相同内容的文件。

「输入」列表中的单个目录信息字符串的格式如下：
   
- `"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"`

这意味着，在目录 `root/d1/d2/.../dm` 下，有 $n$ 个文件 ($f1.txt, f2.txt ... fn.txt$) 的内容分别是 ($f1\_content$, $f2\_content$ ... $fn\_content$) 。注意：$n \ge 1$ 且 $m \ge 0$ 。如果 $m = 0$，则表示该目录是根目录。


「输出」是由「重复文件路径组」构成的列表。其中每个组由所有具有相同内容文件的文件路径组成。文件路径是具有下列格式的字符串：

- `"directory_path/file_name.txt"`

**要求**：

按路径返回文件系统中的所有重复文件。答案可按任意顺序返回。

**说明**：

- $1 \le paths.length \le 2 \times 10^{4}$。
- $1 \le paths[i].length \le 3000$。
- $1 \le sum(paths[i].length) \le 5 \times 10^{5}$。
- $paths[i]$ 由英文字母、数字、字符 `'/'`、`'.'`、`'('`、`')'` 和 `' '` 组成。
- 你可以假设在同一目录中没有任何文件或目录共享相同的名称。
- 你可以假设每个给定的目录信息代表一个唯一的目录。目录路径和文件信息用单个空格分隔。

- 进阶：
   - 假设您有一个真正的文件系统，您将如何搜索文件？广度搜索还是宽度搜索？
   - 如果文件内容非常大（GB级别），您将如何修改您的解决方案？
   - 如果每次只能读取 1 kb 的文件，您将如何修改解决方案？
   - 修改后的解决方案的时间复杂度是多少？其中最耗时的部分和消耗内存的部分是什么？如何优化？
   - 如何确保您发现的重复文件不是误报？

**示例**：

- 示例 1：

```python
输入：paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
输出：[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
```

- 示例 2：

```python
输入：paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
输出：[["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
```

## 解题思路

### 思路 1：哈希表

这道题目要求找出具有相同内容的文件。使用哈希表，以文件内容为键，文件路径列表为值。

1. 创建哈希表 $content\_map$，键为文件内容，值为文件路径列表。
2. 遍历 $paths$ 中的每个目录信息：
   - 解析目录路径和文件信息。
   - 对于每个文件，提取文件名和内容。
   - 构造完整的文件路径 $directory\_path/file\_name.txt$。
   - 将文件路径添加到对应内容的列表中。
3. 遍历哈希表，将包含多个文件路径的列表加入结果。
4. 返回结果。

### 思路 1：代码

```python
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        content_map = defaultdict(list)
        
        for path in paths:
            parts = path.split()
            directory = parts[0]
            
            # 遍历该目录下的所有文件
            for i in range(1, len(parts)):
                file_info = parts[i]
                # 找到文件名和内容的分隔位置
                idx = file_info.index('(')
                file_name = file_info[:idx]
                content = file_info[idx + 1:-1]  # 去掉括号
                
                # 构造完整路径
                full_path = directory + '/' + file_name
                content_map[content].append(full_path)
        
        # 筛选出有重复内容的文件组
        result = []
        for paths_list in content_map.values():
            if len(paths_list) > 1:
                result.append(paths_list)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是目录信息的数量，$m$ 是每个目录中文件的平均数量。需要遍历所有文件。
- **空间复杂度**：$O(n \times m)$，需要使用哈希表存储所有文件的路径和内容。
