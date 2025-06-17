# [1310. 子数组异或查询](https://leetcode.cn/problems/xor-queries-of-a-subarray/)

- 标签：位运算、数组、前缀和
- 难度：中等

## 题目链接

- [1310. 子数组异或查询 - 力扣](https://leetcode.cn/problems/xor-queries-of-a-subarray/)

## 题目大意

**描述**：给定一个正整数数组 `arr`，再给定一个对应的查询数组 `queries`，其中 `queries[i] = [Li, Ri]`。

**要求**：对于每个查询 `queries[i]`，要求计算从 `Li` 到 `Ri` 的异或值（即 `arr[Li] ^ arr[Li+1] ^ ... ^ arr[Ri]`）作为本次查询的结果。并返回一个包含给定查询 `queries` 所有结果的数组。

**说明**：

- $1 \le arr.length \le 3 * 10^4$。
- $1 \le arr[i] \le 10^9$。
- $1 \le queries.length \le 3 * 10^4$。
- $queries[i].length == 2$。
- $0 \le queries[i][0] \le queries[i][1] < arr.length$。

**示例**：

- 示例 1：

```python
输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
输出：[2,7,14,8] 
解释

数组中元素的二进制表示形式是：
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 

查询的 XOR 值为：
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
```

## 解题思路

### 思路 1：线段树

- 使用数组 `res` 作为答案数组，用于存放每个查询的结果值。
- 根据 `nums` 数组构建一棵线段树。
- 然后遍历查询数组 `queries`。对于每个查询 `queries[i]`，在线段树中查询对应区间的异或值，将其结果存入答案数组 `res` 中。
- 返回答案数组 `res` 即可。

这样构建线段树的时间复杂度为 $O(\log n)$，单次区间查询的时间复杂度为 $O(\log n)$。总体时间复杂度为 $O(k * \log n)$，其中 $k$ 是查询次数。

### 思路 1：线段树代码

```python
# 线段树的节点类
class SegTreeNode:
    def __init__(self, val=0):
        self.left = -1                              # 区间左边界
        self.right = -1                             # 区间右边界
        self.val = val                              # 节点值（区间值）
        self.lazy_tag = None                        # 区间和问题的延迟更新标记
        
        
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
    
    # 区间更新接口：将区间为 [q_left, q_right] 上的所有元素值加上 val
    def update_interval(self, q_left, q_right, val):
        self.__update_interval(q_left, q_right, val, 0)
        
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
    
    
    # 区间查询实现方法：在线段树中搜索区间为 [q_left, q_right] 的区间值
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
    
    # 向上更新实现方法：更新下标为 index 的节点区间值 等于 该节点左右子节点元素值的聚合计算结果
    def __pushup(self, index):
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        self.tree[index].val = self.function(self.tree[left_index].val, self.tree[right_index].val)


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        self.STree = SegmentTree(arr, lambda x, y: (x ^ y))
        res = []
        for query in queries:
            ans = self.STree.query_interval(query[0], query[1])
            res.append(ans)
        return res
```
