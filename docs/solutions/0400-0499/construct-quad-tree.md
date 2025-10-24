# [0427. 建立四叉树](https://leetcode.cn/problems/construct-quad-tree/)

- 标签：树、数组、分治、矩阵
- 难度：中等

## 题目链接

- [0427. 建立四叉树 - 力扣](https://leetcode.cn/problems/construct-quad-tree/)

## 题目大意

**描述**：

给定一个 $n \times n$ 矩阵 $grid$ ，矩阵由若干 $0$ 和 $1$ 组成。

**要求**：

请你用四叉树表示该矩阵 $grid$。

你需要返回能表示矩阵 $grid$ 的四叉树的根结点。

四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：

- $val$：储存叶子结点所代表的区域的值。$1$ 对应 $True$，$0$ 对应 $False$。注意，当 $isLeaf$ 为 $False$ 时，你可以把 $True$ 或者 $False$ 赋值给节点，两种值都会被判题机制 接受 。
- $isLeaf$: 当这个节点是一个叶子结点时为 $True$，如果它有 $4$ 个子节点则为 $False$。

```Java
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
```

我们可以按以下步骤为二维区域构建四叉树：

1. 如果当前网格的值相同（即，全为 0 或者全为 1），将 $isLeaf$ 设为 True ，将 $val$ 设为网格相应的值，并将四个子节点都设为 $Null$ 然后停止。
2. 如果当前网格的值不同，将 $isLeaf$ 设为 False， 将 $val$ 设为任意值，然后如下图所示，将当前网格划分为四个子网格。
3. 使用适当的子网格递归每个子节点。

![](https://assets.leetcode.com/uploads/2020/02/11/new_top.png)

如果你想了解更多关于四叉树的内容，可以参考 [百科](https://baike.baidu.com/item/%E5%9B%9B%E5%8F%89%E6%A0%91)。

四叉树格式：

你不需要阅读本节来解决这个问题。只有当你想了解输出格式时才会这样做。输出为使用层序遍历后四叉树的序列化形式，其中 $null$ 表示路径终止符，其下面不存在节点。

它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 $[isLeaf, val]$。

如果 $isLeaf$ 或者 $val$ 的值为 $True$，则表示它在列表 $[isLeaf, val]$ 中的值为 $1$；如果 $isLeaf$ 或者 $val$ 的值为 $False$ ，则表示值为 $0$。

**说明**：

- $n == grid.length == grid[i].length$。
- $n == 2^x$ 其中 $0 \le x \le 6$。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/02/11/grid1.png)

```python
输入：grid = [[0,1],[1,0]]
输出：[[0,1],[1,0],[1,1],[1,1],[1,0]]
解释：此示例的解释如下：
请注意，在下面四叉树的图示中，0 表示 false，1 表示 True 。
```

![](https://assets.leetcode.com/uploads/2020/02/12/e1tree.png)

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/02/12/e2mat.png)

```python
输入：grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
输出：[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
解释：网格中的所有值都不相同。我们将网格划分为四个子网格。
topLeft，bottomLeft 和 bottomRight 均具有相同的值。
topRight 具有不同的值，因此我们将其再分为 4 个子网格，这样每个子网格都具有相同的值。
解释如下图所示：
```

![](https://assets.leetcode.com/uploads/2020/02/12/e2tree.png)

## 解题思路

### 思路 1：递归分治

1. 四叉树的构建是一个典型的递归分治问题。对于给定的 $n \times n$ 矩阵，我们需要递归地将其划分为四个子区域。
2. 定义递归函数 $constructQuadTree(grid, row, col, size)$，其中 $row$ 和 $col$ 表示当前子矩阵的左上角坐标，$size$ 表示子矩阵的边长。
3. 对于当前子矩阵，首先检查所有元素是否相同：
   - 如果所有元素都相同（全为 $0$ 或全为 $1$），则创建一个叶子节点，$isLeaf = True$，$val$ 为对应的值。
   - 如果元素不相同，则创建一个内部节点，$isLeaf = False$，$val$ 可以设为任意值，然后递归构建四个子节点。
4. 四个子节点的区域划分：
   - 左上角：$(row, col)$ 到 $(row + size/2 - 1, col + size/2 - 1)$
   - 右上角：$(row, col + size/2)$ 到 $(row + size/2 - 1, col + size - 1)$
   - 左下角：$(row + size/2, col)$ 到 $(row + size - 1, col + size/2 - 1)$
   - 右下角：$(row + size/2, col + size/2)$ 到 $(row + size - 1, col + size - 1)$
5. 递归终止条件：当 $size = 1$ 时，直接创建叶子节点。

### 思路 1：代码

```python
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def constructQuadTree(row, col, size):
            # 检查当前子矩阵的所有元素是否相同
            all_same = True
            first_val = grid[row][col]
            
            # 遍历当前子矩阵检查是否所有元素相同
            for i in range(row, row + size):
                for j in range(col, col + size):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break
            
            # 如果所有元素相同，创建叶子节点
            if all_same:
                return Node(first_val == 1, True, None, None, None, None)
            
            # 如果元素不相同，创建内部节点并递归构建子节点
            half_size = size // 2
            
            # 递归构建四个子节点
            topLeft = constructQuadTree(row, col, half_size)
            topRight = constructQuadTree(row, col + half_size, half_size)
            bottomLeft = constructQuadTree(row + half_size, col, half_size)
            bottomRight = constructQuadTree(row + half_size, col + half_size, half_size)
            
            # 创建内部节点，val 可以设为任意值
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        n = len(grid)
        return constructQuadTree(0, 0, n)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2 \log n)$，其中 $n$ 是矩阵的边长。在最坏情况下，每个节点都需要检查其对应子矩阵的所有元素，总共有 $O(\log n)$ 层，每层需要检查 $O(n^2)$ 个元素。
- **空间复杂度**：$O(\log n)$，其中 $n$ 是矩阵的边长。递归调用栈的深度为 $O(\log n)$，因为每次递归都将矩阵大小减半。
