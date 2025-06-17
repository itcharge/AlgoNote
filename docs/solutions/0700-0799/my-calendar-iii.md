# [0732. 我的日程安排表 III](https://leetcode.cn/problems/my-calendar-iii/)

- 标签：设计、线段树、二分查找、有序集合
- 难度：困难

## 题目链接

- [0732. 我的日程安排表 III - 力扣](https://leetcode.cn/problems/my-calendar-iii/)

## 题目大意

**要求**：实现一个 `MyCalendarThree` 类来存放你的日程安排，你可以一直添加新的日程安排。

日程可以用一对整数 $start$ 和 $end$ 表示，这里的时间是半开区间，即 $[start, end)$，实数 $x$ 的范围为 $start \le x < end$。

`MyCalendarThree` 类：

- `MyCalendarThree()` 初始化对象。
- `int book(int start, int end)` 返回一个整数 `k`，表示日历中存在的 `k` 次预订的最大值。

**说明**：

- `k` 次预定：当 `k` 个日程安排有一些时间上的交叉时（例如 `k` 个日程安排都在同一时间内），就会产生 `k` 次预订。
- $0 \le start < end \le 10^9$
- 每个测试用例，调用 `book` 函数最多不超过 `400` 次。

**示例**：

- 示例 1：

```python
输入
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
输出
[null, 1, 1, 2, 3, 3, 3]

解释
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(50, 60); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(10, 40); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
myCalendarThree.book(5, 15); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
myCalendarThree.book(5, 10); // 返回 3
myCalendarThree.book(25, 55); // 返回 3
```

## 解题思路

### 思路 1：线段树

这道题可以使用线段树来做。

因为区间的范围是 $[0, 10^9]$，普通数组构成的线段树不满足要求。需要用到动态开点线段树。

- 构建一棵线段树。每个线段树的节点类存储当前区间中保存的日程区间个数。

- 在 `book` 方法中，在线段树中更新 `[start, end - 1]` 的交叉日程区间个数，即令其区间值整体加 `1`。

- 然后从线段树中查询区间 $[0, 10^9]$ 上保存的交叉日程区间个数，并返回。


### 思路 1：代码

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
            
    # 单点更新，将 nums[i] 更改为 val
    def update_point(self, i, val):
        self.__update_point(i, val, self.tree)
    
    # 区间更新，将区间为 [q_left, q_right] 上的元素值修改为 val
    def update_interval(self, q_left, q_right, val):
        self.__update_interval(q_left, q_right, val, self.tree)
        
    # 区间查询，查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, self.tree)
    
    # 获取 nums 数组接口：返回 nums 数组
    def get_nums(self, length):
        nums = [0 for _ in range(length)]
        for i in range(length):
            nums[i] = self.query_interval(i, i)
        return nums
    
    
    # 以下为内部实现方法
    
    # 单点更新，将 nums[i] 更改为 val。node 节点的区间为 [node.left, node.right]
    def __update_point(self, i, val, node):
        if node.left == node.right:
            node.val = val                          # 叶子节点，节点值修改为 val
            return
        
        if i <= node.mid:                           # 在左子树中更新节点值
            self.__update_point(i, val, node.leftNode)
        else:                                       # 在右子树中更新节点值
            self.__update_point(i, val, node.rightNode)
        self.__pushup(node)                         # 向上更新节点的区间值
    
    # 区间更新
    def __update_interval(self, q_left, q_right, val, node):
        if node.left >= q_left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            if node.lazy_tag is not None:
                node.lazy_tag += val                # 将当前节点的延迟标记增加 val
            else:
                node.lazy_tag = val                 # 将当前节点的延迟标记增加 val
            node.val += val                         # 当前节点所在区间增加 val
            return
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return 0
    
        self.__pushdown(node)                       # 向下更新节点所在区间的左右子节点的值和懒惰标记
    
        if q_left <= node.mid:                      # 在左子树中更新区间值
            self.__update_interval(q_left, q_right, val, node.leftNode)
        if q_right > node.mid:                      # 在右子树中更新区间值
            self.__update_interval(q_left, q_right, val, node.rightNode)
            
        self.__pushup(node)
    
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
            res_left = self.__query_interval(q_left, q_right, node.leftNode)
        if q_right > node.mid:                      # 在右子树中查询
            res_right = self.__query_interval(q_left, q_right, node.rightNode)
        return self.function(res_left, res_right)   # 返回左右子树元素值的聚合计算结果

    # 向上更新 node 节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果
    def __pushup(self, node):
        if node.leftNode and node.rightNode:
            node.val = self.function(node.leftNode.val, node.rightNode.val)
    
    # 向下更新 node 节点所在区间的左右子节点的值和懒惰标记
    def __pushdown(self, node):
        if node.leftNode is None:
            node.leftNode = SegTreeNode(node.left, node.mid)
        if node.rightNode is None:
            node.rightNode = SegTreeNode(node.mid + 1, node.right)
            
        lazy_tag = node.lazy_tag
        if node.lazy_tag is None:
            return
            
        if node.leftNode.lazy_tag is not None:
            node.leftNode.lazy_tag += lazy_tag      # 更新左子节点懒惰标记
        else:
            node.leftNode.lazy_tag = lazy_tag       # 更新左子节点懒惰标记
        node.leftNode.val += lazy_tag               # 左子节点区间增加 lazy_tag
        
        if node.rightNode.lazy_tag is not None:
            node.rightNode.lazy_tag += lazy_tag     # 更新右子节点懒惰标记
        else:
            node.rightNode.lazy_tag = lazy_tag      # 更新右子节点懒惰标记
        node.rightNode.val += lazy_tag              # 右子节点区间增加 lazy_tag
        
        node.lazy_tag = None                        # 更新当前节点的懒惰标记


class MyCalendarThree:

    def __init__(self):
        self.STree = SegmentTree(lambda x, y: max(x, y))


    def book(self, start: int, end: int) -> int:
        self.STree.update_interval(start, end - 1, 1)
        return self.STree.query_interval(0, int(1e9))



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
```
