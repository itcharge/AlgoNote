# [0673. 最长递增子序列的个数](https://leetcode.cn/problems/number-of-longest-increasing-subsequence/)

- 标签：树状数组、线段树、数组、动态规划
- 难度：中等

## 题目链接

- [0673. 最长递增子序列的个数 - 力扣](https://leetcode.cn/problems/number-of-longest-increasing-subsequence/)

## 题目大意

**描述**：给定一个未排序的整数数组 `nums`。

**要求**：返回最长递增子序列的个数。

**说明**：

- 子数列必须是严格递增的。
- $1 \le nums.length \le 2000$。
- $-10^6 \le nums[i] \le 10^6$。

**示例**：

- 示例 1：

```python
输入：[1,3,5,4,7]
输出：2
解释：有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
```

## 解题思路

### 思路 1：动态规划

可以先做题目 [0300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)。

动态规划的状态 `dp[i]` 表示为：以第 `i` 个数字结尾的前 `i` 个元素中最长严格递增子序列的长度。

两重循环遍历前 `i` 个数字，对于 $0 \le j \le i$：

- 当 `nums[j] < nums[i]` 时，`nums[i]` 可以接在 `nums[j]` 后面，此时以第 `i` 个数字结尾的最长严格递增子序列长度 + 1，即 `dp[i] = dp[j] + 1`。
- 当 `nums[j] ≥ nums[i]` 时，可以直接跳过。

则状态转移方程为：`dp[i] = max(dp[i], dp[j] + 1)`，`0 ≤ j ≤ i`，`nums[j] < nums[i]`。

最后再遍历一遍 dp 数组，求出最大值即为最长递增子序列的长度。

现在求最长递增子序列的个数。则需要在求解的过程中维护一个 `count` 数组，用来保存以 `nums[i]` 结尾的最长递增子序列的个数。

对于 $0 \le j \le i$：

- 当 `nums[j] < nums[i]`，而且 `dp[j] + 1 > dp[i]` 时，说明第一次找到 `dp[j] + 1`长度且以`nums[i]`结尾的最长递增子序列，则以 `nums[i]` 结尾的最长递增子序列的组合数就等于以 `nums[j]` 结尾的组合数，即 `count[i] = count[j]`。
- 当 `nums[j] < nums[i]`，而且 `dp[j] + 1 == dp[i]` 时，说明以 `nums[i]` 结尾且长度为 `dp[j] + 1` 的递增序列已找到过一次了，则以 `nums[i]` 结尾的最长递增子序列的组合数要加上以 `nums[j]` 结尾的组合数，即 `count[i] += count[j]`。

- 然后根据遍历 dp 数组得到的最长递增子序列的长度 Z，然后再一次遍历 dp 数组，将所有 `dp[i] == max_length` 情况下的组合数 `coun[i]` 累加起来，即为最长递增序列的个数。

### 思路 1：动态规划代码

```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1 for _ in range(size)]
        count = [1 for _ in range(size)]
        for i in range(size):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]

        max_length = max(dp)
        res = 0
        for i in range(size):
            if dp[i] == max_length:
                res += count[i]
        return res
```

### 思路 2：线段树

题目中 `nums` 的长度 为 $[1, 2000]$，值域为 $[-10^6, 10^6]$。

值域范围不是特别大，我们可以直接用线段树保存整个值域区间。但因为数组的长度只有 `2000`，所以算法效率更高的做法是先对数组进行离散化处理。把数组中的元素按照大小依次映射到 `[0, len(nums) - 1]` 这个区间。

1. 构建一棵长度为 `len(nums)` 的线段树，其中每个线段树的节点保存一个二元组。这个二元组 `val = [length, count]` 用来表示：以当前节点为结尾的子序列所能达到的最长递增子序列长度 `length` 和最长递增子序列对应的数量 `count`。
2. 顺序遍历数组 `nums`。对于当前元素 `nums[i]`：
3. 查找 `[0, nums[i - 1]]` 离散化后对应区间节点的二元组，也就是查找以区间 `[0, nums[i - 1]]` 上的点为结尾的子序列所能达到的最长递增子序列长度和其对应的数量，即 `val = [length, count]`。
   - 如果所能达到的最长递增子序列长度为 `0`，则加入 `nums[i]` 之后最长递增子序列长度变为 `1`，且数量也变为 `1`。
   - 如果所能达到的最长递增子序列长度不为 `0`，则加入 `nums[i]` 之后最长递增子序列长度 +1，但数量不变。
4. 根据上述计算的 `val` 值更新 `nums[i]` 对应节点的 `val` 值。 
5. 然后继续向后遍历，重复进行第 `3` ~ `4` 步操作。
6. 最后查询以区间 `[0, nums[len(nums) - 1]]` 上的点为结尾的子序列所能达到的最长递增子序列长度和其对应的数量。返回对应的数量即为答案。

### 思路 2：线段树代码

```python
# 线段树的节点类
class SegTreeNode:
    def __init__(self, val=[0, 1]):
        self.left = -1                              # 区间左边界
        self.right = -1                             # 区间右边界
        self.val = val                              # 节点值（区间值）
        
        
        
# 线段树类
class SegmentTree:
    # 初始化线段树接口
    def __init__(self, size):
        self.size = size
        self.tree = [SegTreeNode() for _ in range(4 * self.size)]  # 维护 SegTreeNode 数组
        if self.size > 0:
            self.__build(0, 0, self.size - 1)
    
    # 单点更新接口：将 nums[i] 更改为 val
    def update_point(self, i, val):
        self.__update_point(i, val, 0)
        
    # 区间查询接口：查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, 0)

        
    # 以下为内部实现方法
    
    # 构建线段树实现方法：节点的存储下标为 index，节点的区间为 [left, right]
    def __build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:                           # 叶子节点，节点值为对应位置的元素值
            self.tree[index].val = [0, 0]
            return
    
        mid = left + (right - left) // 2            # 左右节点划分点
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        self.__build(left_index, left, mid)         # 递归创建左子树
        self.__build(right_index, mid + 1, right)   # 递归创建右子树

        self.tree[index].val = self.merge(self.tree[left_index].val, self.tree[right_index].val)   # 向上更新节点的区间值
    
    # 单点更新实现方法：将 nums[i] 更改为 val，节点的存储下标为 index
    def __update_point(self, i, val, index):
        left = self.tree[index].left
        right = self.tree[index].right
        
        if left == i and right == i:
            self.tree[index].val = self.merge(self.tree[index].val, val)
            return
        
        mid = left + (right - left) // 2            # 左右节点划分点
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        if i <= mid:                                # 在左子树中更新节点值
            self.__update_point(i, val, left_index)
        else:                                       # 在右子树中更新节点值
            self.__update_point(i, val, right_index)
        
        self.tree[index].val = self.merge(self.tree[left_index].val, self.tree[right_index].val)   # 向上更新节点的区间值
    
    
    # 区间查询实现方法：在线段树中搜索区间为 [q_left, q_right] 的区间值
    def __query_interval(self, q_left, q_right, index):
        left = self.tree[index].left
        right = self.tree[index].right
        
        if left >= q_left and right <= q_right:     # 节点所在区间被 [q_left, q_right] 所覆盖
            return self.tree[index].val             # 直接返回节点值
        if right < q_left or left > q_right:        # 节点所在区间与 [q_left, q_right] 无关
            return [0, 0]

        mid = left + (right - left) // 2            # 左右节点划分点
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        res_left = [0, 0]
        res_right = [0, 0]
        if q_left <= mid:                           # 在左子树中查询
            res_left = self.__query_interval(q_left, q_right, left_index)
        if q_right > mid:                           # 在右子树中查询
            res_right = self.__query_interval(q_left, q_right, right_index)
        
        # 返回合并结果
        return self.merge(res_left, res_right)

    # 向上合并实现方法
    def merge(self, val1, val2):
        val = [0, 0]
        if val1[0] == val2[0]:                      # 递增子序列长度一致，则合并后最长递增子序列个数为之前两者之和
            val = [val1[0], val1[1] + val2[1]]
        elif val1[0] < val2[0]:                     # 如果递增子序列长度不一致，则合并后最长递增子序列个数取较长一方的个数
            val = [val2[0], val2[1]]
        else:
            val = [val1[0], val1[1]]
        return val

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        # 离散化处理
        num_dict = dict()
        nums_sort = sorted(nums)
        for i in range(len(nums_sort)):
            num_dict[nums_sort[i]] = i
        
        # 构造线段树
        self.STree = SegmentTree(len(nums_sort))

        for num in nums:
            index = num_dict[num]
            # 查询 [0, nums[index - 1]] 区间上以 nums[index - 1] 结尾的子序列所能达到的最长递增子序列长度和对应数量
            val = self.STree.query_interval(0, index - 1)
            # 如果当前最长递增子序列长度为 0，则加入 num 之后最长递增子序列长度为 1，且数量为 1
            # 如果当前最长递增子序列长度不为 0，则加入 num 之后最长递增子序列长度 +1，但数量不变
            if val[0] == 0:
                val = [1, 1]
            else:
                val = [val[0] + 1, val[1]]
            self.STree.update_point(index, val)
        return self.STree.query_interval(0, len(nums_sort) - 1)[1]
```

