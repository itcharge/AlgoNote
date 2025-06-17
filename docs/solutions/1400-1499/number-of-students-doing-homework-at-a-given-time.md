# [1450. 在既定时间做作业的学生人数](https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/)

- 标签：数组
- 难度：简单

## 题目链接

- [1450. 在既定时间做作业的学生人数 - 力扣](https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/)

## 题目大意

**描述**：给你两个长度相等的整数数组，一个表示开始时间的数组 $startTime$ ，另一个表示结束时间的数组 $endTime$。再给定一个整数 $queryTime$ 作为查询时间。已知第 $i$ 名学生在 $startTime[i]$ 时开始写作业并于 $endTime[i]$ 时完成作业。

**要求**：返回在查询时间 $queryTime$ 时正在做作业的学生人数。即能够使 $queryTime$ 处于区间 $[startTime[i], endTime[i]]$ 的学生人数。

**说明**：

- $startTime.length == endTime.length$。
- $1\le startTime.length \le 100$。
- $1 \le startTime[i] \le endTime[i] \le 1000$。
- $1 \le queryTime \le 1000$。

**示例**：

- 示例 1：

```python
输入：startTime = [4], endTime = [4], queryTime = 4
输出：1
解释：在查询时间只有一名学生在做作业。
```

## 解题思路

### 思路 1：枚举算法

- 维护一个用于统计在查询时间 $queryTime$ 时正在做作业的学生人数的变量 $cnt$。然后遍历所有学生的开始时间和结束时间。
- 如果 $queryTime$ 在区间 $[startTime[i], endTime[i]]$ 之间，即 $startTime[i] <= queryTime <= endTime[i]$，则令 $cnt$ 加 $1$。
- 遍历完输出统计人数 $cnt$。

### 思路 1：枚举算法代码

```python
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        size = len(startTime)
        for i in range(size):
            if startTime[i] <= queryTime <= endTime[i]:
                cnt += 1
        return cnt
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组中的元素个数。
- **空间复杂度**：$O(1)$。

### 思路 2：线段树

- 因为 $1 \le startTime[i] \le endTime[i] \le 1000$，所以我们可以维护一个区间为 $[0, 1000]$ 的线段树，初始化所有区间值都为 $0$。
- 然后遍历所有学生的开始时间和结束时间，并将区间 $[startTime[i], endTime[i]]$ 值加 $1$。
- 在线段树中查询 $queryTime$ 对应的单点区间 $[queryTime, queryTime]$ 的最大值为多少。

### 思路 2：线段树代码

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
    
    # 单点更新实现方法：将 nums[i] 更改为 val，节点的存储下标为 index
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
    
    # 区间更新实现方法
    def __update_interval(self, q_left, q_right, val, index):
        left = self.tree[index].left
        right = self.tree[index].right
        
        if left >= q_left and right <= q_right:     # 节点所在区间被 [q_left, q_right] 所覆盖        
            if self.tree[index].lazy_tag is not None:
                self.tree[index].lazy_tag += val    # 将当前节点的延迟标记增加 val
            else:
                self.tree[index].lazy_tag = val     # 将当前节点的延迟标记增加 val
            interval_size = (right - left + 1)      # 当前节点所在区间大小
            self.tree[index].val += val * interval_size  # 当前节点所在区间每个元素值增加 val
            return
        
        if right < q_left or left > q_right:        # 节点所在区间与 [q_left, q_right] 无关
            return
    
        self.__pushdown(index)                      # 向下更新节点的区间值
    
        mid = left + (right - left) // 2            # 左右节点划分点
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        if q_left <= mid:                           # 在左子树中更新区间值
            self.__update_interval(q_left, q_right, val, left_index)
        if q_right > mid:                           # 在右子树中更新区间值
            self.__update_interval(q_left, q_right, val, right_index)
        
        self.__pushup(index)                        # 向上更新节点的区间值
    
    # 区间查询实现方法：在线段树中搜索区间为 [q_left, q_right] 的区间值
    def __query_interval(self, q_left, q_right, index):
        left = self.tree[index].left
        right = self.tree[index].right
        
        if left >= q_left and right <= q_right:     # 节点所在区间被 [q_left, q_right] 所覆盖
            return self.tree[index].val             # 直接返回节点值
        if right < q_left or left > q_right:        # 节点所在区间与 [q_left, q_right] 无关
            return 0
    
        self.__pushdown(index)
    
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

    # 向下更新实现方法：更新下标为 index 的节点所在区间的左右子节点的值和懒惰标记
    def __pushdown(self, index):
        lazy_tag = self.tree[index].lazy_tag
        if lazy_tag is None: 
            return
        
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        
        if self.tree[left_index].lazy_tag is not None:
            self.tree[left_index].lazy_tag += lazy_tag  # 更新左子节点懒惰标记
        else:
            self.tree[left_index].lazy_tag = lazy_tag
        left_size = (self.tree[left_index].right - self.tree[left_index].left + 1)
        self.tree[left_index].val += lazy_tag * left_size   # 左子节点每个元素值增加 lazy_tag
        
        if self.tree[right_index].lazy_tag is not None:
            self.tree[right_index].lazy_tag += lazy_tag # 更新右子节点懒惰标记
        else:
            self.tree[right_index].lazy_tag = lazy_tag
        right_size = (self.tree[right_index].right - self.tree[right_index].left + 1)
        self.tree[right_index].val += lazy_tag * right_size # 右子节点每个元素值增加 lazy_tag
        
        self.tree[index].lazy_tag = None            # 更新当前节点的懒惰标记


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        nums = [0 for _ in range(1010)]
        self.STree = SegmentTree(nums, lambda x, y: max(x, y))
        size = len(startTime)
        for i in range(size):
            self.STree.update_interval(startTime[i], endTime[i], 1)

        return self.STree.query_interval(queryTime, queryTime)
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n \times \log n)$，其中 $n$ 为数组元素的个数。
- **空间复杂度**：$O(n)$。

### 思路 3：树状数组

- 因为 $1 \le startTime[i] \le endTime[i] \le 1000$，所以我们可以维护一个区间为 $[0, 1000]$ 的树状数组。
- 注意：
  - 树状数组中 $update(self, index, delta):$ 指的是将对应元素 $nums[index] $ 加上 $delta$。
  - $query(self, index):$ 指的是 $index$ 位置之前的元素和，即前缀和。
- 然后遍历所有学生的开始时间和结束时间，将树状数组上 $startTime[i]$ 的值增加 $1$，再将树状数组上$endTime[i]$ 的值减少 $1$。
- 则查询 $queryTime$ 位置的前缀和即为答案。

### 思路 3：树状数组代码

```python
class BinaryIndexTree:

    def __init__(self, n):
        self.size = n
        self.tree = [0 for _ in range(n + 1)]

    def lowbit(self, index):
        return index & (-index)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += self.lowbit(index)

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        bit = BinaryIndexTree(1010)
        size = len(startTime)
        for i in range(size):
            bit.update(startTime[i], 1)
            bit.update(endTime[i] + 1, -1)
        return bit.query(queryTime)
```

### 思路 3：复杂度分析

- **时间复杂度**：$O(n \times \log n)$，其中 $n$ 为数组元素的个数。
- **空间复杂度**：$O(n)$。
