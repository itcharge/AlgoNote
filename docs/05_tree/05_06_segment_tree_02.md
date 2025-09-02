## 1. 线段树常见题型

线段树是一种高效的数据结构，常用于处理区间相关的查询与修改。以下是线段树常见的几类题型及其简要说明：

### 1.1 区间最大 / 最小值查询（RMQ）

> **RMQ（Range Maximum / Minimum Query）问题**：给定长度为 $n$ 的数组 $nums$，多次询问区间 $[q_{left}, q_{right}]$ 内的最大值或最小值。

假设有 $q$ 次查询，朴素算法每次需遍历区间，整体时间复杂度为 $O(q \times n)$；而采用线段树后，每次查询仅需 $O(\log n)$，总复杂度降为 $O(q \times \log n)$，大大提升了效率。

### 1.2 单点更新与区间查询

> **单点更新与区间查询问题**：
>
> 1. 支持对数组中某一元素进行修改（单点更新）。
> 2. 支持查询任意区间 $[q_{left}, q_{right}]$ 的聚合值（如区间和、最大/最小值等）。

这类问题直接使用「5.5 线段树（一）」中的「3.1 单点更新」和「3.2 区间查询」即可解决。

### 1.3 区间更新与区间查询

> **区间更新与区间查询问题**：
>
> 1. 支持对某一连续区间的所有元素进行批量修改（区间更新）。
> 2. 支持查询任意区间 $[q_{left}, q_{right}]$ 的聚合值（如区间和、最大/最小值等）。

此类问题直接使用「5.5 线段树（一）」中的「3.3 区间更新」与「3.2 区间查询」即可解决。

### 1.4 区间合并与区间查询

> **区间合并与区间查询问题**：
>
> 1. 支持对某一连续区间的所有元素进行批量修改（区间更新）。
> 2. 支持查询区间 $[q_{left}, q_{right}]$ 内，满足特定条件的连续最长子区间（如最长连续 1、最长连续递增/递减等）。

这类问题在解决时，需在「5.5 线段树（一）」中「3.3 区间更新」和「3.2 区间查询」的基础上，扩展每个节点维护的信息。例如，节点需额外记录区间内的前缀/后缀/最大连续长度等统计量。在向上合并时，需根据左右子节点的这些信息进行合并计算，从而支持高效的区间合并与查询操作。

### 1.5 扫描线问题

> **扫描线问题**：通过模拟一条虚拟的扫描线（通常为垂直或水平线）在平面上移动，动态处理与其相交的几何对象，从而高效解决如图形面积、周长等几何统计问题。
>
> 核心思想是：让扫描线从一端出发，依次经过所有关键事件点（如矩形的边界），每到一个事件点时，更新与扫描线相交的区间集合，并据此统计所需信息。随着扫描线的推进，所有对象都被处理，最终得到完整解答。

这类问题往往涉及大范围的坐标区间，因此通常需要对坐标进行离散化（如将 $y$ 坐标映射为 $0, 1, 2, \ldots$），以便用线段树等数据结构高效维护区间信息。具体做法是：将每条竖线（或水平线）的端点作为区间边界，利用线段树动态维护区间的覆盖情况（如 $x$ 坐标、左/右边界等），在扫描过程中实时合并区间并统计相关量（如总覆盖长度、重叠次数等）。

## 2. 线段树的拓展

### 2.1 动态开点线段树

在某些场景下，线段树需要维护的区间范围极大（如 $[1, 10^9]$），但实际被访问和修改的节点却非常有限。

如果仍采用传统的数组实现方式，则需要分配 $4 \times n$ 的空间，导致空间浪费严重，效率低下。

为了解决这一问题，可以采用 **动态开点** 的线段树实现思路：

- 初始时仅创建一个根节点，表示整个区间。
- 只有在访问或修改到某个子区间时，才动态地为该区间分配节点。

这种方式极大地节省了空间，仅为实际需要的区间分配内存，适合处理稀疏访问、超大区间的问题。

动态开点线段树的基本实现如下：

```python
# 动态开点线段树节点类
class TreeNode:
    def __init__(self, left=-1, right=-1, val=0):
        self.left = left                            # 区间左边界
        self.right = right                          # 区间右边界
        self.mid = left + (right - left) // 2       # 区间中点
        self.leftNode = None                        # 左子节点
        self.rightNode = None                       # 右子节点
        self.val = val                              # 区间聚合值
        self.lazy_tag = None                        # 懒惰标记（延迟更新）

# 动态开点线段树
class SegmentTree:
    def __init__(self, function):
        self.tree = TreeNode(0, int(1e9))           # 根节点，维护区间 [0, 1e9]
        self.function = function                    # 区间聚合函数（如 sum, max, min）

    def __pushup(self, node):
        """
        向上更新当前节点的区间值，由左右子节点聚合得到
        """
        leftNode = node.leftNode
        rightNode = node.rightNode
        if leftNode and rightNode:
            node.val = self.function(leftNode.val, rightNode.val)
        elif leftNode:
            node.val = leftNode.val
        elif rightNode:
            node.val = rightNode.val
        # 如果左右子节点都不存在，val 保持不变

    def update_point(self, i, val):
        """
        单点更新：将下标 i 的元素修改为 val
        """
        self.__update_point(i, val, self.tree)

    def __update_point(self, i, val, node):
        """
        递归实现单点更新
        """
        if node.left == node.right:
            node.val = val                          # 叶子节点，直接赋值
            node.lazy_tag = None                    # 清除懒惰标记
            return

        self.__pushdown(node)                       # 下推懒惰标记，保证更新正确

        if i <= node.mid:
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            self.__update_point(i, val, node.leftNode)
        else:
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            self.__update_point(i, val, node.rightNode)
        self.__pushup(node)                         # 向上更新

    def query_interval(self, q_left, q_right):
        """
        区间查询：[q_left, q_right] 区间的聚合值
        """
        return self.__query_interval(q_left, q_right, self.tree)

    def __query_interval(self, q_left, q_right, node):
        """
        递归实现区间查询
        """
        if node.left > q_right or node.right < q_left:
            # 当前节点区间与查询区间无交集
            return 0
        if node.left >= q_left and node.right <= q_right:
            # 当前节点区间被查询区间完全覆盖
            return node.val

        self.__pushdown(node)                       # 下推懒惰标记

        res_left = 0
        res_right = 0
        if q_left <= node.mid:
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            res_left = self.__query_interval(q_left, q_right, node.leftNode)
        if q_right > node.mid:
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            res_right = self.__query_interval(q_left, q_right, node.rightNode)
        return self.function(res_left, res_right)   # 返回左右子树元素值的聚合计算结果

    def update_interval(self, q_left, q_right, val):
        """
        区间更新：将 [q_left, q_right] 区间内所有元素增加 val
        """
        self.__update_interval(q_left, q_right, val, self.tree)

    def __update_interval(self, q_left, q_right, val, node):
        """
        递归实现区间更新（区间加法）
        """
        if node.left > q_right or node.right < q_left:
            # 当前节点区间与更新区间无交集
            return

        if node.left >= q_left and node.right <= q_right:
            # 当前节点区间被更新区间完全覆盖
            interval_size = node.right - node.left + 1
            if node.lazy_tag is not None:
                node.lazy_tag += val
            else:
                node.lazy_tag = val
            node.val += val * interval_size
            return

        self.__pushdown(node)                       # 下推懒惰标记

        if q_left <= node.mid:
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            self.__update_interval(q_left, q_right, val, node.leftNode)
        if q_right > node.mid:
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            self.__update_interval(q_left, q_right, val, node.rightNode)

        self.__pushup(node)                         # 向上更新

    def __pushdown(self, node):
        """
        懒惰标记下推：将当前节点的延迟更新传递给左右子节点
        """
        if node.lazy_tag is None:
            return

        # 动态创建左右子节点
        if not node.leftNode:
            node.leftNode = TreeNode(node.left, node.mid)
        if not node.rightNode:
            node.rightNode = TreeNode(node.mid + 1, node.right)

        # 更新左子节点
        left_size = node.leftNode.right - node.leftNode.left + 1
        if node.leftNode.lazy_tag is not None:
            node.leftNode.lazy_tag += node.lazy_tag
        else:
            node.leftNode.lazy_tag = node.lazy_tag
        node.leftNode.val += node.lazy_tag * left_size

        # 更新右子节点
        right_size = node.rightNode.right - node.rightNode.left + 1
        if node.rightNode.lazy_tag is not None:
            node.rightNode.lazy_tag += node.lazy_tag
        else:
            node.rightNode.lazy_tag = node.lazy_tag
        node.rightNode.val += node.lazy_tag * right_size

        node.lazy_tag = None                        # 清除当前节点的懒惰标记
```

## 练习题目

- [线段树题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E7%BA%BF%E6%AE%B5%E6%A0%91%E9%A2%98%E7%9B%AE)

## 参考资料

- 【书籍】ACM-ICPC 程序设计系列 - 算法设计与实现 - 陈宇 吴昊 主编
- 【书籍】算法训练营 陈小玉 著
- 【博文】[史上最详细的线段树教程 - 知乎](https://zhuanlan.zhihu.com/p/34150142)
- 【博文】[线段树 Segment Tree 实战 - halfrost](https://halfrost.com/segment_tree/)
- 【博文】[线段树 - OI Wiki](https://oi-wiki.org/ds/seg/)
- 【博文】[线段树的 python 实现 - 年糕的博客 - CSDN博客](https://blog.csdn.net/qq_33935895/article/details/102806357)
- 【博文】[线段树 从入门到进阶 - Dijkstra·Liu - 博客园](https://www.cnblogs.com/dijkstra2003/p/9676729.html)

