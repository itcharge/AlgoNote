# [1483. 树节点的第 K 个祖先](https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/)

- 标签：树、深度优先搜索、广度优先搜索、设计、二分查找、动态规划
- 难度：困难

## 题目链接

- [1483. 树节点的第 K 个祖先 - 力扣](https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/)

## 题目大意

**描述**：给定一棵 $n$ 个节点的树（节点编号 $0 \sim n-1$），给定 $parent$ 数组，$parent[i]$ 表示节点 $i$ 的父节点（根节点的 $parent$ 为 $-1$）。

实现 `TreeAncestor` 类，支持：
- `TreeAncestor(n, parent)` 初始化。
- `getKthAncestor(node, k)` 返回第 $k$ 个祖先节点。如果不存在，返回 $-1$。

**说明**：
- $1 \le k \le n \le 5 \times 10^4$。
- 最多调用 $5 \times 10^4$ 次。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/06/14/1528_ex1.png)

```python
输入：
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

输出：
[null,1,0,-1]

解释：
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
```

- 示例 2：

```python
输入：
输出：
```

## 解题思路

### 思路 1：树上倍增

#### 1. 核心思想

预处理每个节点的 $2^j$ 级祖先。$up[node][j]$ 表示节点 $node$ 的第 $2^j$ 个祖先。

- $up[node][0] = parent[node]$（直接父节点）。
- $up[node][j] = up[up[node][j-1]][j-1]$（先跳 $2^{j-1}$ 步，再跳 $2^{j-1}$ 步）。

查询 $k$ 级祖先：将 $k$ 的二进制分解，对应跳 $2^j$ 步。

#### 2. 具体步骤

**初始化**：
- $LOG = \lceil \log_2 n \rceil + 1$（$n \le 5 \times 10^4$，取 $16$ 或 $17$）。
- $up = [[-1] * LOG for \_ in range(n)]$。
- 设置 $up[node][0] = parent[node]$。
- 递推填充 $up[node][j]$。

**$getKthAncestor(node, k)$**：
- 遍历 $j = 0 \to LOG-1$：
  - 如果 $k$ 的第 $j$ 位是 $1$：$node = up[node][j]$。
  - 如果 $node == -1$：返回 $-1$。
- 返回 $node$。

#### 3. 举例说明

以 $n=7, parent=[-1,0,0,1,1,2,2]$ 为例：

```
       0
     /   \
    1     2
   / \   / \
  3   4 5   6
```

$up$ 表初始化：
- $up[0][0] = -1$
- $up[1][0] = 0, up[2][0] = 0$
- $up[3][0] = 1, up[4][0] = 1, up[5][0] = 2, up[6][0] = 2$

递推 $up[3][1] = up[up[3][0]][0] = up[1][0] = 0$

查询 `getKthAncestor(5, 3)`：
- $k=3=二进制 011$，遍历 $j=0,1$
- $j=0$，$k$ 第 $0$ 位为 $1$：$5 \to up[5][0] = 2$
- $j=1$，$k$ 第 $1$ 位为 $1$：$2 \to up[2][1] = up[up[2][0]][0] = up[0][0] = -1$

返回 $-1$（节点 $5$ 只有 $2$ 级祖先，即 $0$，没有 $3$ 级祖先）。

### 思路 1：代码

```python
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        LOG = (n).bit_length()  # 2^LOG >= n
        self.up = [[-1] * LOG for _ in range(n)]

        for v in range(n):
            self.up[v][0] = parent[v]

        for j in range(1, LOG):
            for v in range(n):
                if self.up[v][j - 1] != -1:
                    self.up[v][j] = self.up[self.up[v][j - 1]][j - 1]

        self.LOG = LOG

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.LOG):
            if k & (1 << j):
                node = self.up[node][j]
                if node == -1:
                    return -1
        return node
```

### 思路 1：复杂度分析

- **时间复杂度**：初始化 $O(n \log n)$，单次查询 $O(\log n)$。
- **空间复杂度**：$O(n \log n)$。
