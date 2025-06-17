# [2276. 统计区间中的整数数目](https://leetcode.cn/problems/count-integers-in-intervals/)

- 标签：设计、线段树、有序集合
- 难度：困难

## 题目链接

- [2276. 统计区间中的整数数目 - 力扣](https://leetcode.cn/problems/count-integers-in-intervals/)

## 题目大意

**描述**：给定一个区间的空集。

**要求**：设计并实现满足要求的数据结构：

- 新增：添加一个区间到这个区间集合中。
- 统计：计算出现在 至少一个 区间中的整数个数。

实现 CountIntervals 类：

- `CountIntervals()` 使用区间的空集初始化对象
- `void add(int left, int right)` 添加区间 `[left, right]` 到区间集合之中。
- `int count()` 返回出现在 至少一个 区间中的整数个数。

**说明**：

- 区间 `[left, right]` 表示满足 $left \le x \le right$ 的所有整数 `x`。
- $1 \le left \le right \le 10^9$。
- 最多调用 `add` 和 `count` 方法 **总计** $10^5$ 次。
- 调用 `count` 方法至少一次。

**示例**：

- 示例 1：

```python
输入：
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
输出：
[null, null, null, 6, null, 8]

解释：
CountIntervals countIntervals = new CountIntervals(); // 用一个区间空集初始化对象
countIntervals.add(2, 3);  // 将 [2, 3] 添加到区间集合中
countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中
countIntervals.count();    // 返回 6
                           // 整数 2 和 3 出现在区间 [2, 3] 中
                           // 整数 7、8、9、10 出现在区间 [7, 10] 中
countIntervals.add(5, 8);  // 将 [5, 8] 添加到区间集合中
countIntervals.count();    // 返回 8
                           // 整数 2 和 3 出现在区间 [2, 3] 中
                           // 整数 5 和 6 出现在区间 [5, 8] 中
                           // 整数 7 和 8 出现在区间 [5, 8] 和区间 [7, 10] 中
                           // 整数 9 和 10 出现在区间 [7, 10] 中
```

## 解题思路

### 思路 1：动态开点线段树

这道题可以使用线段树来做。

因为区间的范围是 $[1, 10^9]$，普通数组构成的线段树不满足要求。需要用到动态开点线段树。具体做法如下：

- 初始化方法，构建一棵线段树。每个线段树的节点类存储当前区间中保存的元素个数。

- 在 `add` 方法中，将区间 `[left, right]` 上的每个元素值赋值为 `1`，则区间值为 `right - left + 1`。

- 在 `count` 方法中，返回区间 $[0, 10^9]$ 的区间值（即区间内元素个数）。

### 思路 1：动态开点线段树代码

```python
# 线段树的节点类
class SegTreeNode:
    def __init__(self, left=-1, right=-1, val=0, lazy_tag=None, leftNode=None, rightNode=None):
        self.left = left                            # 区间左边界
        self.right = right                          # 区间右边界
        self.mid = left + (right - left) // 2
        self.leftNode = leftNode                    # 区间左节点
        self.rightNode = rightNode                  # 区间右节点
        self.val = val                              # 节点值（区间值）
        self.lazy_tag = lazy_tag                    # 区间问题的延迟更新标记
        
        
# 线段树类
class SegmentTree:
    # 初始化线段树接口
    def __init__(self, function):
        self.tree = SegTreeNode(0, int(1e9))
        self.function = function                    # function 是一个函数，左右区间的聚合方法
    
    # 区间更新接口：将区间为 [q_left, q_right] 上的元素值修改为 val
    def update_interval(self, q_left, q_right, val):
        self.__update_interval(q_left, q_right, val, self.tree)
    
    # 区间查询接口：查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, self.tree)
            
    
    # 以下为内部实现方法
    
    # 区间更新实现方法
    def __update_interval(self, q_left, q_right, val, node):
        if node.left >= q_left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            node.lazy_tag = val                     # 将当前节点的延迟标记标记为 val
            interval_size = (node.right - node.left + 1)    # 当前节点所在区间大小
            node.val = val * interval_size          # 当前节点所在区间每个元素值改为 val
            return
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return
    
        self.__pushdown(node)                       # 向下更新节点所在区间的左右子节点的值和懒惰标记
    
        if q_left <= node.mid:                      # 在左子树中更新区间值
            self.__update_interval(q_left, q_right, val, node.leftNode)
        if q_right > node.mid:                      # 在右子树中更新区间值
            self.__update_interval(q_left, q_right, val, node.rightNode)
            
        self.__pushup(node)
    
    # 区间查询实现方法：在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def __query_interval(self, q_left, q_right, node):
        if node.left >= q_left and node.right <= q_right:   # 节点所在区间被 [q_left, q_right] 所覆盖
            return node.val                         # 直接返回节点值
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return 0
                                  
        self.__pushdown(node)                       # 向下更新节点所在区间的左右子节点的值和懒惰标记
        
        res_left = 0                                # 左子树查询结果
        res_right = 0                               # 右子树查询结果
        if q_left <= node.mid:                      # 在左子树中查询
            res_left = self.__query_interval(q_left, q_right, node.leftNode)
        if q_right > node.mid:                      # 在右子树中查询
            res_right = self.__query_interval(q_left, q_right, node.rightNode)
        return self.function(res_left, res_right)   # 返回左右子树元素值的聚合计算结果
    
    # 向上更新实现方法：更新 node 节点区间值 等于 该节点左右子节点元素值的聚合计算结果
    def __pushup(self, node):
        if node.leftNode and node.rightNode:
            node.val = self.function(node.leftNode.val, node.rightNode.val)
            
    # 向下更新实现方法：更新 node 节点所在区间的左右子节点的值和懒惰标记
    def __pushdown(self, node):
        if node.leftNode is None:
            node.leftNode = SegTreeNode(node.left, node.mid)
        if node.rightNode is None:
            node.rightNode = SegTreeNode(node.mid + 1, node.right)
            
        lazy_tag = node.lazy_tag
        if node.lazy_tag is None:
            return
            
        node.leftNode.lazy_tag = lazy_tag           # 更新左子节点懒惰标记
        left_size = (node.leftNode.right - node.leftNode.left + 1)
        node.leftNode.val = lazy_tag * left_size    # 更新左子节点值
        
        node.rightNode.lazy_tag = lazy_tag          # 更新右子节点懒惰标记
        right_size = (node.rightNode.right - node.rightNode.left + 1)
        node.rightNode.val = lazy_tag * right_size  # 更新右子节点值
        
        node.lazy_tag = None                        # 更新当前节点的懒惰标记
    
    
class CountIntervals:

    def __init__(self):
        self.STree = SegmentTree(lambda x, y: x + y)
        self.left = 10 ** 9
        self.right = 0


    def add(self, left: int, right: int) -> None:
        self.STree.update_interval(left, right, 1) 


    def count(self) -> int:
        return self.STree.query_interval(0, int(1e9))



# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
```

