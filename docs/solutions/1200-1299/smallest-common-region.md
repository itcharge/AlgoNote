# [1257. 最小公共区域](https://leetcode.cn/problems/smallest-common-region/)

- 标签：树、哈希表、深度优先搜索
- 难度：中等

## 题目链接

- [1257. 最小公共区域 - 力扣](https://leetcode.cn/problems/smallest-common-region/)

## 题目大意

**描述**：给定一些区域列表 $regions$，其中 $regions[i]$ 的第一个元素表示该区域的根区域，后面是它的子区域。所有区域构成一棵树（每个节点（区域）可能包含多个子区域）。

再给定两个区域 $region1$ 和 $region2$。

**要求**：返回 $region1$ 和 $region2$ 的最近公共祖先（LCA，即最小的公共区域）。

**说明**：

- $1 \le regions.length \le 10^{4}$。
- $2 \le regions[i].length \le 50$。
- 所有区域名称都是字符串。

**示例**：

- 示例 1：

```python
输入：regions = [["Earth","North America","South America"],
                ["North America","United States","Canada"],
                ["United States","New York","Boston"],
                ["Canada","Ontario","Quebec"],
                ["South America","Brazil"]],
      region1 = "Quebec",
      region2 = "New York"
输出："North America"
解释：Quebec 属于 Canada → North America，New York 属于 United States → North America，公共区域为 North America。
```

## 解题思路

### 思路 1：哈希表建图 + 路径比较

#### 1. 核心思想

题目给出的区域关系是一棵树，但每个节点可以有多个子节点，且没有环。我们需要找两个节点的最近公共祖先。

关键步骤：
1. 用哈希表记录每个子区域到父区域的映射（$parent$）。
2. 从 $region1$ 开始，沿着父指针向上，收集它到根节点路径上的所有区域。
3. 从 $region2$ 开始，沿着父指针向上，第一个出现在 $region1$ 路径集合中的区域就是最近公共祖先。

#### 2. 建图、遍历、标记、收集

- **建图**：遍历 $regions$，对每组的根和子节点，建立子→父映射。
- **遍历**：向上回溯路径。
- **标记**：将 $region1$ 路径上的节点存入集合。
- **收集**：$region2$ 回溯时第一个匹配的节点即为答案。

#### 3. 具体步骤

**第 1 步**：构建 $parent$ 字典，键为子区域，值为父区域。

**第 2 步**：从 $region1$ 开始，不断向上找父节点，将路径上的所有节点加入 $path\_set$（包括自身）。

**第 3 步**：从 $region2$ 开始，不断向上找父节点，遇到的第一个在 $path\_set$ 中的节点即为结果。

#### 4. 结合示例走一遍

$regions$ 构建的树：

```
Earth
├── North America
│   ├── United States
│   │   ├── New York
│   │   └── Boston
│   └── Canada
│       ├── Ontario
│       └── Quebec
└── South America
    └── Brazil
```

$region1 = \text{"Quebec"}, region2 = \text{"New York"}$

$region1$ 路径：$\text{Quebec} \to \text{Canada} \to \text{North America} \to \text{Earth}$  
$path\_set = \{\text{Quebec}, \text{Canada}, \text{North America}, \text{Earth}\}$

$region2$ 回溯：$\text{New York} \to \text{United States} \to \text{North America}$ → $\text{North America} \in path\_set$，返回。

### 思路 1：代码

```python
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # 建立子区域到父区域的映射
        parent = {}
        for reg in regions:
            root = reg[0]
            for child in reg[1:]:
                parent[child] = root

        # 收集 region1 的路径
        path_set = set()
        node = region1
        while node:
            path_set.add(node)
            node = parent.get(node)

        # 查找 region2 的路径中第一个在 path_set 中的节点
        node = region2
        while node not in path_set:
            node = parent.get(node)
        return node
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是区域总数。建图需要 $O(n)$，两个回溯路径需要 $O(d)$，$d$ 是树的深度。
- **空间复杂度**：$O(n)$，存储父映射和路径集合。
