## 1. 线段树的常见题型

### 1.1 RMQ 问题

> **RMQ 问题**：Range Maximum / Minimum Query 的缩写，指的是对于长度为 $n$ 的数组序列 $nums$，回答若干个询问问题 `RMQ(nums, q_left, q_right)`，要求返回数组序列 $nums$ 在区间 $[q\underline{\hspace{0.5em}}left, q\underline{\hspace{0.5em}}right]$ 中的最大（最小）值。也就是求区间最大（最小）值问题。

假设查询次数为 $q$，则使用朴素算法解决 RMQ 问题的时间复杂度为 $O(q \times n)$。而使用线段树解决 RMQ 问题的时间复杂度为 $O(q \times n) \sim Q(q \times \log_2n)$ 之间。

### 1.2 单点更新，区间查询问题

> **单点更新，区间查询问题**：
>
> 1. 修改某一个元素的值。
> 2. 查询区间为 $[q\underline{\hspace{0.5em}}left, q\underline{\hspace{0.5em}}right]$ 的区间值。

这类问题直接使用「3.1 线段树的单点更新」和「3.2 线段树的区间查询」即可解决。

### 1.3 区间更新，区间查询问题

> **区间更新，区间查询问题**：
>
> 1. 修改某一个区间的值。
> 2. 查询区间为 $[q\underline{\hspace{0.5em}}left, q\underline{\hspace{0.5em}}right]$ 的区间值。

这类问题直接使用「3.3 线段树的区间更新」和「3.2 线段树的区间查询」即可解决。

### 1.4 区间合并问题

> **区间合并，区间查询问题**：
>
> 1. 修改某一个区间的值。
> 2. 查询区间为 $[q\underline{\hspace{0.5em}}left, q\underline{\hspace{0.5em}}right]$ 中满足条件的连续最长区间值。

这类问题需要在「3.3 线段树的区间更新」和「3.2 线段树的区间查询」的基础上增加变动，在进行向上更新时需要对左右子节点的区间进行合并。

### 1.5 扫描线问题

> **扫描线问题**：虚拟扫描线或扫描面来解决欧几里德空间中的各种问题，一般被用来解决图形面积，周长等问题。
>
> 主要思想为：想象一条线（通常是一条垂直线）在平面上扫过或移动，在某些点停止。几何操作仅限于几何对象，无论何时停止，它们都与扫描线相交或紧邻扫描线，并且一旦线穿过所有对象，就可以获得完整的解。

这类问题通常坐标跨度很大，需要先对每条扫描线的坐标进行离散化处理，将 $y$ 坐标映射到 $0, 1, 2, ...$ 中。然后将每条竖线的端点作为区间范围，使用线段树存储每条竖线的信息（$x$ 坐标、是左竖线还是右竖线等），然后再进行区间合并，并统计相关信息。

## 2. 线段树的拓展

### 2.1 动态开点线段树

在有些情况下，线段树需要维护的区间很大（例如 $[1, 10^9]$），在实际中用到的节点却很少。

如果使用之前数组形式实现线段树，则需要 $4 \times n$ 大小的空间，空间消耗有点过大了。

这时候我们就可以使用动态开点的思想来构建线段树。

动态开点线段树的算法思想如下：

- 开始时只建立一个根节点，代表整个区间。
- 当需要访问线段树的某棵子树（某个子区间）时，再建立代表这个子区间的节点。

动态开点线段树实现代码如下：

```python
# 线段树的节点类
class TreeNode:
    def __init__(self, left=-1, right=-1, val=0):
        self.left = left                            # 区间左边界
        self.right = right                          # 区间右边界
        self.mid = left + (right - left) // 2
        self.leftNode = None                        # 区间左节点
        self.rightNode = None                       # 区间右节点
        self.val = val                              # 节点值（区间值）
        self.lazy_tag = None                        # 区间问题的延迟更新标记
        
        
# 线段树类
class SegmentTree:
    def __init__(self, function):
        self.tree = TreeNode(0, int(1e9))
        self.function = function                    # function 是一个函数，左右区间的聚合方法
            
    # 向上更新 node 节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果
    def __pushup(self, node):
        leftNode = node.leftNode
        rightNode = node.rightNode
        if leftNode and rightNode:
            node.val = self.function(leftNode.val, rightNode.val)
            
    # 单点更新，将 nums[i] 更改为 val
    def update_point(self, i, val):
        self.__update_point(i, val, self.tree)
        
    # 单点更新，将 nums[i] 更改为 val。node 节点的区间为 [node.left, node.right]
    def __update_point(self, i, val, node):
        if node.left == node.right:
            node.val = val                          # 叶子节点，节点值修改为 val
            return
        
        if i <= node.mid:                           # 在左子树中更新节点值
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            self.__update_point(i, val, node.leftNode)
        else:                                       # 在右子树中更新节点值
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            self.__update_point(i, val, node.rightNode)
        self.__pushup(node)                         # 向上更新节点的区间值
        
    # 区间查询，查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, self.tree)
    
    # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def __query_interval(self, q_left, q_right, node):
        if node.left >= q_left and node.right <= q_right:   # 节点所在区间被 [q_left, q_right] 所覆盖
            return node.val                         # 直接返回节点值
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return 0
                                  
        self.__pushdown(node)                       # 向下更新节点所在区间的左右子节点的值和懒惰标记
        
        res_left = 0                                # 左子树查询结果
        res_right = 0                               # 右子树查询结果
        if q_left <= node.mid:                      # 在左子树中查询
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            res_left = self.__query_interval(q_left, q_right, node.leftNode)
        if q_right > node.mid:                      # 在右子树中查询
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            res_right = self.__query_interval(q_left, q_right, node.rightNode)
        return self.function(res_left, res_right)   # 返回左右子树元素值的聚合计算结果
    
    # 区间更新，将区间为 [q_left, q_right] 上的元素值修改为 val
    def update_interval(self, q_left, q_right, val):
        self.__update_interval(q_left, q_right, val, self.tree)
        
    # 区间更新
    def __update_interval(self, q_left, q_right, val, node):
        if node.left >= q_left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            if node.lazy_tag:
                node.lazy_tag += val                # 将当前节点的延迟标记增加 val
            else:
                node.lazy_tag = val                 # 将当前节点的延迟标记增加 val
            interval_size = (node.right - node.left + 1)    # 当前节点所在区间大小
            node.val += val * interval_size         # 当前节点所在区间每个元素值增加 val
            return
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return 0
    
        self.__pushdown(node)                       # 向下更新节点所在区间的左右子节点的值和懒惰标记
    
        if q_left <= node.mid:                      # 在左子树中更新区间值
            if not node.leftNode:
                node.leftNode = TreeNode(node.left, node.mid)
            self.__update_interval(q_left, q_right, val, node.leftNode)
        if q_right > node.mid:                      # 在右子树中更新区间值
            if not node.rightNode:
                node.rightNode = TreeNode(node.mid + 1, node.right)
            self.__update_interval(q_left, q_right, val, node.rightNode)
            
        self.__pushup(node)
    
    # 向下更新 node 节点所在区间的左右子节点的值和懒惰标记
    def __pushdown(self, node):
        lazy_tag = node.lazy_tag
        if not node.lazy_tag:
            return
        
        if not node.leftNode:
            node.leftNode = TreeNode(node.left, node.mid)
        if not node.rightNode:
            node.rightNode = TreeNode(node.mid + 1, node.right)
            
        if node.leftNode.lazy_tag:
            node.leftNode.lazy_tag += lazy_tag      # 更新左子节点懒惰标记
        else:
            node.leftNode.lazy_tag = lazy_tag       # 更新左子节点懒惰标记
        left_size = (node.leftNode.right - node.leftNode.left + 1)
        node.leftNode.val += lazy_tag * left_size   # 左子节点每个元素值增加 lazy_tag
        
        if node.rightNode.lazy_tag:
            node.rightNode.lazy_tag += lazy_tag     # 更新右子节点懒惰标记
        else:
            node.rightNode.lazy_tag = lazy_tag      # 更新右子节点懒惰标记
        right_size = (node.rightNode.right - node.rightNode.left + 1)
        node.rightNode.val += lazy_tag * right_size # 右子节点每个元素值增加 lazy_tag
        
        node.lazy_tag = None                        # 更新当前节点的懒惰标记
```

## 参考资料

- 【书籍】ACM-ICPC 程序设计系列 - 算法设计与实现 - 陈宇 吴昊 主编
- 【书籍】算法训练营 陈小玉 著
- 【博文】[史上最详细的线段树教程 - 知乎](https://zhuanlan.zhihu.com/p/34150142)
- 【博文】[线段树 Segment Tree 实战 - halfrost](https://halfrost.com/segment_tree/)
- 【博文】[线段树 - OI Wiki](https://oi-wiki.org/ds/seg/)
- 【博文】[线段树的 python 实现 - 年糕的博客 - CSDN博客](https://blog.csdn.net/qq_33935895/article/details/102806357)
- 【博文】[线段树 从入门到进阶 - Dijkstra·Liu - 博客园](https://www.cnblogs.com/dijkstra2003/p/9676729.html)

