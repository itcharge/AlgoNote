# [0303. 区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/)

- 标签：设计、数组、前缀和
- 难度：简单

## 题目链接

- [0303. 区域和检索 - 数组不可变 - 力扣](https://leetcode.cn/problems/range-sum-query-immutable/)

## 题目大意

**描述**：给定一个整数数组 `nums`。

**要求**：实现 `NumArray` 类，该类能处理区间为 `[left, right]` 之间的区间求和的多次查询。

`NumArray` 类：

- `NumArray(int[] nums)` 使用数组 `nums` 初始化对象。
- `int sumRange(int i, int j)` 返回数组 `nums` 中索引 `left` 和 `right` 之间的元素的 总和 ，包含 `left` 和 `right` 两点（也就是 `nums[left] + nums[left + 1] + ... + nums[right]`）。

**说明**：

- $1 \le nums.length \le 10^4$。
- $-10^5 \le nums[i] \le 10^5$。
- $0 \le left \le right < nums.length$。
- `sumRange` 方法调用次数不超过 $10^4$ 次。

**示例**：

- 示例 1：

```python
给定    nums = [-2, 0, 3, -5, 2, -1]

求和    sumRange(0, 2) -> 1
求和    sumRange(2, 5) -> -1
求和    sumRange(0, 5) -> -3
```

## 解题思路

### 思路 1：线段树

- 根据 `nums` 数组，构建一棵线段树。每个线段树的节点类存储当前区间的左右边界和该区间的和。

这样构建线段树的时间复杂度为 $O(\log n)$，单次区间查询的时间复杂度为 $O(\log n)$。总体时间复杂度为 $O(\log n)$。

### 思路 1 线段树代码：

```python
# 线段树的节点类
class SegTreeNode:
    def __init__(self, val=0):
        self.left = -1                              # 区间左边界
        self.right = -1                             # 区间右边界
        self.val = val                              # 节点值（区间值）
        
        
# 线段树类
class SegmentTree:
    # 初始化线段树接口
    def __init__(self, nums, function):
        self.size = len(nums)
        self.tree = [SegTreeNode() for _ in range(4 * self.size)]  # 维护 SegTreeNode 数组
        self.nums = nums                            # 原始数据
        self.function = function                    # function 是一个函数，左右区间的聚合方法
        if self.size > 0:
            self.__build(0, 0, self.size - 1)
        
    # 单点更新接口：将 nums[i] 更改为 val
    def update_point(self, i, val):
        self.nums[i] = val
        self.__update_point(i, val, 0)
    
    # 区间查询接口：查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, 0)
    
    # 获取 nums 数组接口：返回 nums 数组
    def get_nums(self):
        for i in range(self.size):
            self.nums[i] = self.query_interval(i, i)
        return self.nums
    
    
    # 以下为内部实现方法
    
    # 构建线段树实现方法：节点的存储下标为 index，节点的区间为 [left, right]
    def __build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:                           # 叶子节点，节点值为对应位置的元素值
            self.tree[index].val = self.nums[left]
            return
    
        mid = left + (right - left) // 2            # 左右节点划分点
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        self.__build(left_index, left, mid)         # 递归创建左子树
        self.__build(right_index, mid + 1, right)   # 递归创建右子树
        self.__pushup(index)                        # 向上更新节点的区间值
    
    
    # 单点更新实现方法：将 nums[i] 更改为 val。节点的存储下标为 index，节点的区间为 [left, right]
    def __update_point(self, i, val, index):
        left = self.tree[index].left
        right = self.tree[index].right
        
        if left == right:
            self.tree[index].val = val              # 叶子节点，节点值修改为 val
            return
        
        mid = left + (right - left) // 2            # 左右节点划分点
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        if i <= mid:                                # 在左子树中更新节点值
            self.__update_point(i, val, left_index)
        else:                                       # 在右子树中更新节点值
            self.__update_point(i, val, right_index)
        
        self.__pushup(index)                        # 向上更新节点的区间值
        
    
    # 区间查询实现方法：在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def __query_interval(self, q_left, q_right, index):
        left = self.tree[index].left
        right = self.tree[index].right
        
        if left >= q_left and right <= q_right:     # 节点所在区间被 [q_left, q_right] 所覆盖
            return self.tree[index].val             # 直接返回节点值
        if right < q_left or left > q_right:        # 节点所在区间与 [q_left, q_right] 无关
            return 0
    
        mid = left + (right - left) // 2            # 左右节点划分点
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        res_left = 0                                # 左子树查询结果
        res_right = 0                               # 右子树查询结果
        if q_left <= mid:                           # 在左子树中查询
            res_left = self.__query_interval(q_left, q_right, left_index)
        if q_right > mid:                           # 在右子树中查询
            res_right = self.__query_interval(q_left, q_right, right_index)
        
        return self.function(res_left, res_right)   # 返回左右子树元素值的聚合计算结果
    
    # 向上更新实现方法：下标为 index 的节点区间值 等于 该节点左右子节点元素值的聚合计算结果
    def __pushup(self, index):
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        self.tree[index].val = self.function(self.tree[left_index].val, self.tree[right_index].val)


class NumArray:

    def __init__(self, nums: List[int]):
        self.STree = SegmentTree(nums, lambda x, y: x + y)


    def sumRange(self, left: int, right: int) -> int:
        return self.STree.query_interval(left, right)
```
