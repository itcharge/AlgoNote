# [0839. 相似字符串组](https://leetcode.cn/problems/similar-string-groups/)

- 标签：深度优先搜索、广度优先搜索、并查集、数组、哈希表、字符串
- 难度：困难

## 题目链接

- [0839. 相似字符串组 - 力扣](https://leetcode.cn/problems/similar-string-groups/)

## 题目大意

**描述**：

如果交换字符串 $X$ 中的两个不同位置的字母，使得它和字符串 $Y$ 相等，那么称 $X$ 和 $Y$ 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。

例如，`"tars"` 和 `"rats"` 是相似的 (交换 0 与 2 的位置)； `"rats"` 和 `"arts"` 也是相似的，但是 `"star"` 不与 `"tars"`，`"rats"`，或 `"arts"` 相似。

总之，它们通过相似性形成了两个关联组：`{"tars", "rats", "arts"}` 和 `{"star"}`。注意，`"tars"` 和 `"arts"` 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。

给你一个字符串列表 $strs$。列表中的每个字符串都是 $strs$ 中其它所有字符串的一个字母异位词。

**要求**：

计算 $strs$ 中有多少个相似字符串组。

**说明**：

- $1 \le strs.length \le 300$。
- $1 \le strs[i].length \le 300$。
- $strs[i]$ 只包含小写字母。
- $strs$ 中的所有单词都具有相同的长度，且是彼此的字母异位词。

**示例**：

- 示例 1：

```python
输入：strs = ["tars","rats","arts","star"]
输出：2
```

- 示例 2：

```python
输入：strs = ["omv","ovm"]
输出：1
```

## 解题思路

### 思路 1:并查集

判断两个字符串是否相似:只需检查它们有多少个位置的字符不同。如果不同位置的个数为 0 或 2,则相似。

使用并查集来维护相似字符串组:

1. 初始化并查集,每个字符串自成一组
2. 遍历所有字符串对,如果两个字符串相似,将它们合并到同一组
3. 最后统计并查集中有多少个不同的根节点

### 思路 1:代码

```python
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        
        # 并查集
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        # 判断两个字符串是否相似
        def is_similar(s1, s2):
            diff_count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff_count += 1
                    if diff_count > 2:
                        return False
            # 相同或恰好两个位置不同
            return diff_count == 0 or diff_count == 2
        
        # 遍历所有字符串对
        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    union(i, j)
        
        # 统计不同的根节点数量
        return len(set(find(i) for i in range(n)))
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(n^2 \times m + n \times \alpha(n))$,其中 $n$ 是字符串数量,$m$ 是字符串长度,$\alpha$ 是并查集的反阿克曼函数。需要检查 $O(n^2)$ 对字符串,每次比较需要 $O(m)$。
- **空间复杂度**:$O(n)$,并查集需要 $O(n)$ 空间。
